#!/usr/bin/env python3
"""
Solo Leagues – Top 100 Ranking Export
Liest ranking_<key>.json (gleiches Format wie update_ranking.py) und
schreibt fuer jede Liga eine fertige .txt-Datei zum Copy-Paste in die
Lichess-Team-Beschreibung.

Usage:
    python print_rankings.py               # alle Ligen
    python print_rankings.py bullet        # nur eine Liga
"""

import json
import os
import sys

LEAGUES = {
    "ultrabullet": "Solo Ultrabullet League",
    "bullet":      "Solo Bullet League",
    "blitz":       "Solo Blitz League",
    "rapid":       "Solo Rapid League",
}

RANKING_MARKER = "## Ranking:"
OUTPUT_DIR = "rankings_output"
TOP_N = 100


def ranking_file(key):
    return f"ranking_{key}.json"


def build_ranking_section(sorted_players):
    lines = [RANKING_MARKER]
    for i, (u, d) in enumerate(sorted_players[:TOP_N], 1):
        boost = f" ({d['booster']}x boost next arena)" if d.get("booster") else ""
        lines.append(f"{i}. @{u}: {d['points']}{boost}")
    return "\n".join(lines)


def process(key, label):
    path = ranking_file(key)
    if not os.path.exists(path):
        print(f"⏭️  {path} nicht gefunden, übersprungen.")
        return

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    players = data.get("players", {})
    sorted_players = sorted(players.items(), key=lambda x: x[1]["points"], reverse=True)

    text = f"{label}\n\n" + build_ranking_section(sorted_players)

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    out_path = os.path.join(OUTPUT_DIR, f"{key}.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"\n{'='*50}\n🏟️  {label}\n{'='*50}")
    print(text)
    print(f"\n💾 Gespeichert unter: {out_path}")


def main():
    if len(sys.argv) > 1:
        key = sys.argv[1]
        if key not in LEAGUES:
            print(f"❌ Unbekannt: '{key}'. Wähle aus: {', '.join(LEAGUES)}")
            sys.exit(1)
        process(key, LEAGUES[key])
    else:
        for key, label in LEAGUES.items():
            process(key, label)

    print(f"\n✅ Fertig. Alle Dateien liegen im Ordner '{OUTPUT_DIR}/'.")


if __name__ == "__main__":
    main()
