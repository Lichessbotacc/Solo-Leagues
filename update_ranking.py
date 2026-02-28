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
{"rank":1,"score":113,"rating":2538,"username":"DarkOnCrack","flair":"nature.glowing-star","patronColor":5,"performance":2569}
{"rank":2,"score":81,"rating":2679,"username":"VariantsMain","flair":"people.backhand-index-pointing-down-light-skin-tone","performance":2565}
{"rank":3,"score":47,"rating":2477,"username":"PushAttack14","flair":"food-drink.cherries","performance":2453}
{"rank":4,"score":36,"rating":2811,"username":"Kurse-Aura1","flair":"people.fingerprint","performance":2715}
{"rank":5,"score":29,"rating":2215,"username":"Cold_Sewy12","performance":2261}
{"rank":6,"score":25,"rating":2410,"username":"VTacademy","flair":"smileys.angry-face-with-horns","performance":2267}
{"rank":7,"score":19,"rating":2318,"username":"tharindujayasuriya","performance":2384}
{"rank":8,"score":18,"rating":2204,"username":"BlitzWarlord","flair":"activity.lichess-blitz","performance":2216}
{"rank":9,"score":15,"rating":2252,"username":"TheRuleBreaker122","flair":"smileys.alien-monster","performance":2294}
{"rank":10,"score":13,"rating":2185,"username":"Supperhero_2012","flair":"activity.lichess-berserk","performance":2299}
{"rank":11,"score":10,"rating":2240,"username":"BlotterFan","flair":"symbols.fleur-de-lis","performance":2257}
{"rank":12,"score":5,"rating":2411,"username":"dunk-master","performance":2319}
{"rank":13,"score":3,"rating":1869,"username":"EgorGromovYT","flair":"activity.trophy","performance":2062}
{"rank":14,"score":2,"rating":2175,"username":"kubak5","performance":2541}
{"rank":15,"score":2,"rating":2397,"username":"blueblue8887","performance":2339}
{"rank":16,"score":2,"rating":1617,"username":"ciyaerdal4735","flair":"smileys.cold-face","performance":2193}
{"rank":17,"score":2,"rating":1999,"username":"This-Is-Agamveer","flair":"symbols.white-exclamation-mark","performance":2162}
{"rank":18,"score":2,"rating":2526,"username":"Checkmate_Drifters","flair":"objects.muted-speaker","performance":2062}
{"rank":19,"score":1,"rating":1711,"username":"jash_the_goat","flair":"nature.four-leaf-clover","performance":1716}
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
