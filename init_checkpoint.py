#!/usr/bin/env python3
"""
EINMALIG AUSFÜHREN – setzt last_processed_tournament auf das aktuell
neueste abgeschlossene Turnier (status=30).
"""

import json
import os
import requests

TEAM_ID      = "solo-ultrabullet-league"
RANKING_FILE = "ranking.json"
API_BASE     = "https://lichess.org/api"
TOKEN        = os.environ["LICHESS_TOKEN"]

HEADERS_NDJSON = {"Authorization": f"Bearer {TOKEN}", "Accept": "application/x-ndjson"}


def main():
    with open(RANKING_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    print("Fetching finished tournaments (status=30) …")
    # Filter directly via API: status=30 means finished
    url = f"{API_BASE}/team/{TEAM_ID}/arena?status=30"
    resp = requests.get(url, headers=HEADERS_NDJSON, timeout=30)
    resp.raise_for_status()

    tournaments = []
    for line in resp.text.strip().splitlines():
        line = line.strip()
        if line:
            t = json.loads(line)
            tournaments.append(t)

    print(f"Found {len(tournaments)} finished tournaments.")

    if not tournaments:
        print("❌ No finished tournaments found.")
        return

    # API returns newest first → first one is the latest finished
    latest = tournaments[0]
    tid   = latest["id"]
    tname = latest.get("fullName", tid)
    print(f"✅ Latest finished: {tname} ({tid}) — status={latest.get('status')}")

    data["last_processed_tournament"] = tid

    with open(RANKING_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"💾 Saved. From now on only future tournaments will be processed!")


if __name__ == "__main__":
    main()
