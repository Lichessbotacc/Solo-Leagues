#!/usr/bin/env python3
"""
Solo Leagues – Automatic Ranking Updater
Supports: Ultrabullet, Bullet, Blitz, Rapid

Usage:
    python update_ranking.py               # all leagues
    python update_ranking.py ultrabullet   # one league only
"""

import json
import os
import sys
import time
import requests

LEAGUES = {
    "ultrabullet": {"team_id": "solo-ultrabullet-league", "label": "Solo Ultrabullet League"},
    "bullet":      {"team_id": "solo-bullet-league",      "label": "Solo Bullet League"},
    "blitz":       {"team_id": "solo-blitz-league",       "label": "Solo Blitz League"},
    "rapid":       {"team_id": "solo-rapid-league",       "label": "Solo Rapid League"},
}

API_BASE       = "https://lichess.org/api"
TOKEN          = os.environ["LICHESS_TOKEN"]
HEADERS_NDJSON = {"Authorization": f"Bearer {TOKEN}", "Accept": "application/x-ndjson"}
BOOSTER_LEVELS = [2.0, 1.9, 1.8, 1.7, 1.6, 1.5, 1.4, 1.3, 1.2, 1.1]


def ranking_file(key):
    return f"ranking_{key}.json"

def load(key):
    with open(ranking_file(key), "r", encoding="utf-8") as f:
        return json.load(f)

def save(key, data):
    with open(ranking_file(key), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def get_new_tournaments(team_id, last_processed):
    url = f"{API_BASE}/team/{team_id}/arena?status=30"
    resp = requests.get(url, headers=HEADERS_NDJSON, timeout=30)
    resp.raise_for_status()
    all_finished = [json.loads(l) for l in resp.text.strip().splitlines() if l.strip()]
    new = []
    for t in all_finished:
        if t.get("id") == last_processed:
            break
        new.append(t)
    new.reverse()  # oldest first
    return new

def get_results(tournament_id):
    url = f"{API_BASE}/tournament/{tournament_id}/results"
    resp = requests.get(url, headers=HEADERS_NDJSON, timeout=60, stream=True)
    resp.raise_for_status()
    return [json.loads(l) for l in resp.iter_lines() if l]

def update_description(team_id, label, sorted_players):
    medals = {1: "🥇", 2: "🥈", 3: "🥉"}
    lines = [f"# 🏆 {label} – Overall Ranking", "",
             "Top 100 players by accumulated arena points.",
             "Boosters awarded to top 10 of each arena.", ""]
    for i, (u, d) in enumerate(sorted_players[:100], 1):
        boost = f"  ⚡ {d['booster']}x" if d["booster"] else ""
        lines.append(f"{medals.get(i, f'{i}.')} @{u} — {d['points']} pts{boost}")
    lines += ["", "*Updated automatically after each arena.*"]
    resp = requests.post(
        f"{API_BASE}/team/{team_id}/description",
        headers={"Authorization": f"Bearer {TOKEN}"},
        data={"text": "\n".join(lines)}, timeout=30,
    )
    print("  ✅ Description updated." if resp.status_code == 200
          else f"  ⚠️  Description failed: {resp.status_code}")

def process(key, config):
    print(f"\n{'='*50}\n🏟️  {config['label']}\n{'='*50}")
    data = load(key)
    players = data["players"]
    new = get_new_tournaments(config["team_id"], data.get("last_processed_tournament"))

    if not new:
        print("  No new tournaments.")
        return False

    print(f"  {len(new)} new tournament(s).")
    for t in new:
        tid = t["id"]
        print(f"\n  📋 {t.get('fullName', tid)} ({tid})")
        results = get_results(tid)
        if not results:
            print("  No results, skipping.")
            continue
        results.sort(key=lambda r: r.get("score", 0), reverse=True)

        for entry in results:
            u, score = entry["username"], entry.get("score", 0)
            if u not in players:
                players[u] = {"points": 0, "booster": None}
            b = players[u]["booster"]
            if b:
                score = int(score * b)
                print(f"    {u}: × {b} = {score} pts")
            else:
                print(f"    {u}: +{score} pts")
            players[u]["points"] += score

        for u in players:
            players[u]["booster"] = None
        for i, entry in enumerate(results[:10]):
            u = entry["username"]
            if u in players:
                players[u]["booster"] = BOOSTER_LEVELS[i]
                print(f"    🔥 {BOOSTER_LEVELS[i]}x → {u}")

        data["last_processed_tournament"] = tid
        time.sleep(1)

    sorted_players = sorted(players.items(), key=lambda x: x[1]["points"], reverse=True)
    data["players"] = dict(sorted_players)
    save(key, data)
    print(f"\n  💾 Saved ranking_{key}.json")
    print("  📊 Top 5: " + ", ".join(f"{u}({d['points']})" for u, d in sorted_players[:5]))
    update_description(config["team_id"], config["label"], sorted_players)
    return True


def main():
    if len(sys.argv) > 1:
        key = sys.argv[1]
        if key not in LEAGUES:
            print(f"❌ Unknown: '{key}'. Choose: {', '.join(LEAGUES)}")
            sys.exit(1)
        to_run = {key: LEAGUES[key]}
    else:
        to_run = LEAGUES

    any_changed = any(process(k, c) for k, c in to_run.items())
    print("\n✅ All done!" if any_changed else "\n✅ Nothing to update.")


if __name__ == "__main__":
    main()
