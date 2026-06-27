#!/usr/bin/env python3
"""
Solo Ultrabullet League – Automatic Ranking Updater
Fetches the latest completed team tournament from Lichess,
applies boosters, updates points, and pushes the Top 100 to the team description.
"""

import json
import os
import sys
import time
import requests

# ── Config ────────────────────────────────────────────────────────────────────
TEAM_ID      = "solo-ultrabullet-league"
RANKING_FILE = "ranking.json"
API_BASE     = "https://lichess.org/api"
TOKEN        = os.environ["LICHESS_TOKEN"]   # set as GitHub Secret

HEADERS_JSON   = {"Authorization": f"Bearer {TOKEN}", "Accept": "application/json"}
HEADERS_NDJSON = {"Authorization": f"Bearer {TOKEN}", "Accept": "application/x-ndjson"}

BOOSTER_LEVELS = [2.0, 1.9, 1.8, 1.7, 1.6, 1.5, 1.4, 1.3, 1.2, 1.1]

# ── Helpers ───────────────────────────────────────────────────────────────────

def load_ranking() -> dict:
    with open(RANKING_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_ranking(data: dict) -> None:
    with open(RANKING_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def get_team_tournaments() -> list:
    """Return all tournaments for the team, newest first."""
    url = f"{API_BASE}/team/{TEAM_ID}/arena"
    resp = requests.get(url, headers=HEADERS_NDJSON, timeout=30)
    resp.raise_for_status()
    tournaments = []
    for line in resp.text.strip().splitlines():
        line = line.strip()
        if line:
            tournaments.append(json.loads(line))
    return tournaments


def get_tournament_results(tournament_id: str) -> list:
    """Return full result list for a finished tournament (ndjson stream)."""
    url = f"{API_BASE}/tournament/{tournament_id}/results"
    resp = requests.get(url, headers=HEADERS_NDJSON, timeout=60, stream=True)
    resp.raise_for_status()
    results = []
    for line in resp.iter_lines():
        if line:
            results.append(json.loads(line))
    return results


def update_team_description(description: str) -> None:
    """POST new team description via Lichess API."""
    url = f"{API_BASE}/team/{TEAM_ID}/description"
    resp = requests.post(
        url,
        headers={"Authorization": f"Bearer {TOKEN}"},
        data={"text": description},
        timeout=30,
    )
    if resp.status_code == 200:
        print("✅ Team description updated.")
    else:
        print(f"⚠️  Failed to update description: {resp.status_code} {resp.text}")


def build_description(sorted_players: list) -> str:
    """Build the Top-100 ranking text for the team description."""
    lines = [
        "# 🏆 Solo Ultrabullet League – Overall Ranking",
        "",
        "Top 100 players by accumulated arena points.",
        "Boosters are awarded to the top 10 finishers of each arena.",
        "",
    ]
    medals = {1: "🥇", 2: "🥈", 3: "🥉"}
    for i, (username, data) in enumerate(sorted_players[:100], start=1):
        medal = medals.get(i, f"{i}.")
        booster_str = f"  ⚡ {data['booster']}x" if data["booster"] else ""
        lines.append(f"{medal} @{username} — {data['points']} pts{booster_str}")
    lines.append("")
    lines.append("*Updated automatically after each arena.*")
    return "\n".join(lines)


# ── Main logic ────────────────────────────────────────────────────────────────

def main():
    print(f"Loading ranking from {RANKING_FILE} …")
    ranking_data = load_ranking()
    last_processed = ranking_data.get("last_processed_tournament")
    players = ranking_data["players"]

    print("Fetching team tournaments …")
    tournaments = get_team_tournaments()

    if not tournaments:
        print("No tournaments found. Nothing to do.")
        sys.exit(0)

    # Find tournaments that are finished and not yet processed
    new_tournaments = []
    for t in tournaments:
        tid = t.get("id")
        status = t.get("status", "")
        # Lichess: status "finished" means done; also check it's not the last one we processed
        if status == "finished" and tid != last_processed:
            new_tournaments.append(t)

    if not new_tournaments:
        print("No new finished tournaments since last run. Nothing to do.")
        sys.exit(0)

    # Process tournaments in chronological order (oldest first)
    new_tournaments.sort(key=lambda t: t.get("startsAt", 0))

    for tournament in new_tournaments:
        tid = tournament["id"]
        tname = tournament.get("fullName", tid)
        print(f"\n🏟️  Processing tournament: {tname} ({tid})")

        results = get_tournament_results(tid)
        if not results:
            print("  No results found, skipping.")
            continue

        # Sort by score descending (API usually returns sorted, but let's be safe)
        results.sort(key=lambda r: r.get("score", 0), reverse=True)

        # Apply old boosters and add points
        for entry in results:
            username = entry["username"]
            score = entry.get("score", 0)

            if username not in players:
                players[username] = {"points": 0, "booster": None}

            booster = players[username]["booster"]
            if booster:
                score = int(score * booster)
                print(f"  {username}: {entry['score']} × {booster} = {score} pts")
            else:
                print(f"  {username}: {score} pts")

            players[username]["points"] += score

        # Reset all boosters
        for user in players:
            players[user]["booster"] = None

        # Assign new boosters to top 10 of this tournament
        for i, entry in enumerate(results[:10]):
            username = entry["username"]
            if username in players:
                players[username]["booster"] = BOOSTER_LEVELS[i]
                print(f"  🔥 Booster {BOOSTER_LEVELS[i]}x → {username}")

        # Mark this tournament as processed
        ranking_data["last_processed_tournament"] = tid
        print(f"  ✅ Done with {tname}.")

        # Small delay to be polite to the API
        time.sleep(1)

    # Sort final ranking
    sorted_players = sorted(
        players.items(),
        key=lambda x: x[1]["points"],
        reverse=True,
    )

    # Save updated ranking
    ranking_data["players"] = dict(sorted_players)
    save_ranking(ranking_data)
    print(f"\n💾 Ranking saved to {RANKING_FILE}.")

    # Print Top 20 to log
    print("\n📊 Current Top 20:")
    for i, (username, data) in enumerate(sorted_players[:20], start=1):
        booster_str = f" ({data['booster']}x next)" if data["booster"] else ""
        print(f"  {i}. @{username}: {data['points']}{booster_str}")

    # Update team description
    description = build_description(sorted_players)
    update_team_description(description)


if __name__ == "__main__":
    main()
