import json

# Aktuelle Rangliste als Dict: username -> {'points': int, 'booster': float or None}
current_ranking = {
    "DarkOnCrack": {"points": 308, "booster": 2.0},
    "Kurse-Aura1": {"points": 95, "booster": 1.7},
    "VariantsMain": {"points": 81, "booster": 1.9},
    "Konariq7": {"points": 73, "booster": None},
    "DRUHA12": {"points": 70, "booster": None},
    "Last_Suspect": {"points": 65, "booster": None},
    "Satranc599": {"points": 48, "booster": None},
    "PushAttack14": {"points": 47, "booster": 1.8},
    "This-Is-Agamveer": {"points": 41, "booster": None},
    "Justinsenpai": {"points": 39, "booster": None},
    "BlotterFan": {"points": 35, "booster": None},
    "Janislav2000": {"points": 32, "booster": None},
    "Cold_Sewy12": {"points": 29, "booster": 1.6},
    "POPOIPOIPOI": {"points": 27, "booster": None},
    "Abd_el_wahab": {"points": 26, "booster": None},
    "VTacademy": {"points": 25, "booster": 1.5},
    "koreshok73": {"points": 23, "booster": None},
    "kubak5": {"points": 20, "booster": None},
    "tharindujayasuriya": {"points": 19, "booster": 1.4},
    "c4energy": {"points": 18, "booster": None},
    "BlitzWarlord": {"points": 18, "booster": 1.3},
    "TheRuleBreaker122": {"points": 15, "booster": 1.2},
    "Supperhero_2012": {"points": 13, "booster": 1.1},
    "TacticalCrush_404": {"points": 12, "booster": None},
    "bulletmaniac": {"points": 6, "booster": None},
    "Devraj-123": {"points": 6, "booster": None},
    "Arjun-Saha6": {"points": 6, "booster": None},
    "EgorGromovYT": {"points": 6, "booster": None},
    "dunk-master": {"points": 5, "booster": None},
    "Skysparks": {"points": 4, "booster": None},
    "Zerkycharlie": {"points": 3, "booster": None},
    "Ozgur3838": {"points": 3, "booster": None},
    "borak-kopitiam": {"points": 2, "booster": None},
    "blueblue8887": {"points": 2, "booster": None},
    "ciyaerdal4735": {"points": 2, "booster": None},
    "Checkmate_Drifters": {"points": 2, "booster": None},
    "BlackPanda2024": {"points": 1, "booster": None},
    "jash_the_goat": {"points": 1, "booster": None},
}

new_table_json = """
{"rank":1,"score":66,"rating":2632,"username":"Satranc599","flair":"activity.1st-place-medal","performance":2233}
{"rank":2,"score":15,"rating":2115,"username":"bbk10s","performance":2147}
{"rank":3,"score":14,"rating":2064,"username":"Justinsenpai","performance":2151}
{"rank":4,"score":6,"rating":2653,"username":"VariantsMain","flair":"people.backhand-index-pointing-down-light-skin-tone","performance":2073}
{"rank":5,"score":6,"rating":1886,"username":"POPOIPOIPOI","flair":"nature.monkey","performance":2009}
{"rank":6,"score":4,"rating":1998,"username":"GeekingKing","performance":2165}
{"rank":7,"score":4,"rating":1690,"username":"A_Khurramov_05","performance":1826}
{"rank":8,"score":3,"rating":2526,"username":"DarkOnCrack","flair":"nature.glowing-star","patronColor":5,"performance":2387}
{"rank":9,"score":2,"rating":1940,"username":"RumijaBarCG21","flair":"people.flexed-biceps","performance":1865}
{"rank":10,"score":0,"rating":2417,"username":"SoyTuPadre2026","flair":"people.zombie"}
"""

# =========================
# APPLY SCORES (OLD BOOSTERS APPLY ONCE)
# =========================

new_table = []

for line in new_table_json.strip().splitlines():
    line = line.strip()
    if not line:
        continue
    new_table.append(json.loads(line))


for entry in new_table:
    username = entry["username"]
    score = entry["score"]

    if username not in current_ranking:
        current_ranking[username] = {"points": 0, "booster": None}

    booster = current_ranking[username]["booster"]
    if booster:
        score = int(score * booster)

    current_ranking[username]["points"] += score

# =========================
# RESET ALL BOOSTERS
# =========================

for user in current_ranking:
    current_ranking[user]["booster"] = None

# =========================
# ASSIGN NEW BOOSTERS TO TOP 10
# =========================

booster_levels = [2.0, 1.9, 1.8, 1.7, 1.6, 1.5, 1.4, 1.3, 1.2, 1.1]

new_table_sorted = sorted(new_table, key=lambda x: x["score"], reverse=True)

for i in range(min(10, len(new_table_sorted))):
    current_ranking[new_table_sorted[i]["username"]]["booster"] = booster_levels[i]

# =========================
# SORT FINAL RANKING
# =========================

sorted_ranking = sorted(
    current_ranking.items(),
    key=lambda x: x[1]["points"],
    reverse=True
)

# =========================
# OUTPUT
# =========================

for rank, (username, data) in enumerate(sorted_ranking, start=1):
    booster_str = f" ({data['booster']}x boost next arena)" if data["booster"] else ""
    print(f"{rank}. @{username}: {data['points']}{booster_str}")

print("\n# ===== COPY FOR NEXT ARENA =====\n")
print("current_ranking = {")
for username, data in sorted_ranking:
    booster = data["booster"]
    booster_str = booster if booster else "None"
    print(f'    "{username}": {{"points": {data["points"]}, "booster": {booster_str}}},')
print("}")
