import json

# Aktuelle Rangliste als Dict: username -> {'points': int, 'booster': float or None}
current_ranking = {
    "DarkOnCrack": {"points": 457, "booster": 1.9},
    "Justinsenpai": {"points": 164, "booster": 1.8},
    "artoftheblade": {"points": 127, "booster": 2.0},
    "Satranc599": {"points": 122, "booster": None},
    "POPOIPOIPOI": {"points": 98, "booster": 1.5},
    "Kurse-Aura1": {"points": 95, "booster": None},
    "VariantsMain": {"points": 92, "booster": None},
    "Konariq7": {"points": 73, "booster": None},
    "DRUHA12": {"points": 70, "booster": None},
    "Last_Suspect": {"points": 65, "booster": None},
    "Clesio-MorgaM": {"points": 59, "booster": 1.7},
    "PushAttack14": {"points": 47, "booster": None},
    "Abd_el_wahab": {"points": 46, "booster": 1.3},
    "This-Is-Agamveer": {"points": 41, "booster": None},
    "manglee": {"points": 41, "booster": 1.6},
    "BlotterFan": {"points": 35, "booster": None},
    "Cold_Sewy12": {"points": 34, "booster": None},
    "Janislav2000": {"points": 32, "booster": None},
    "VTacademy": {"points": 25, "booster": None},
    "koreshok73": {"points": 23, "booster": None},
    "bbk10s": {"points": 22, "booster": None},
    "LucienTupin": {"points": 21, "booster": 1.4},
    "kubak5": {"points": 20, "booster": None},
    "tharindujayasuriya": {"points": 19, "booster": None},
    "c4energy": {"points": 18, "booster": None},
    "BlitzWarlord": {"points": 18, "booster": None},
    "handyacc": {"points": 18, "booster": 1.2},
    "Mc-ArboledaAxel": {"points": 16, "booster": 1.1},
    "TheRuleBreaker122": {"points": 15, "booster": None},
    "Supperhero_2012": {"points": 13, "booster": None},
    "TacticalCrush_404": {"points": 12, "booster": None},
    "tunu2011": {"points": 10, "booster": None},
    "BlackPanda2024": {"points": 9, "booster": None},
    "bulletmaniac": {"points": 6, "booster": None},
    "Devraj-123": {"points": 6, "booster": None},
    "Arjun-Saha6": {"points": 6, "booster": None},
    "EgorGromovYT": {"points": 6, "booster": None},
    "dunk-master": {"points": 5, "booster": None},
    "Skysparks": {"points": 4, "booster": None},
    "GeekingKing": {"points": 4, "booster": None},
    "A_Khurramov_05": {"points": 4, "booster": None},
    "coldkarmaguy": {"points": 4, "booster": None},
    "Vidishnarra": {"points": 4, "booster": None},
    "Zerkycharlie": {"points": 3, "booster": None},
    "Ozgur3838": {"points": 3, "booster": None},
    "borak-kopitiam": {"points": 2, "booster": None},
    "blueblue8887": {"points": 2, "booster": None},
    "ciyaerdal4735": {"points": 2, "booster": None},
    "Checkmate_Drifters": {"points": 2, "booster": None},
    "RumijaBarCG21": {"points": 2, "booster": None},
    "jash_the_goat": {"points": 1, "booster": None},

new_table_json = """
{"rank":1,"score":127,"rating":2551,"username":"artoftheblade","flair":"objects.crossed-swords","performance":2528}
{"rank":2,"score":110,"rating":2516,"username":"DarkOnCrack","flair":"nature.glowing-star","patronColor":5,"performance":2428}
{"rank":3,"score":62,"rating":2048,"username":"Justinsenpai","performance":2089}
{"rank":4,"score":59,"rating":2227,"username":"Clesio-MorgaM","performance":2204}
{"rank":5,"score":41,"rating":2114,"username":"manglee","performance":2090}
{"rank":6,"score":41,"rating":1887,"username":"POPOIPOIPOI","flair":"nature.elephant","performance":1933}
{"rank":7,"score":21,"rating":2169,"username":"LucienTupin","flair":"food-drink.poultry-leg","performance":2207}
{"rank":8,"score":20,"rating":2144,"username":"Abd_el_wahab","flair":"smileys.face-with-tears-of-joy","performance":2001}
{"rank":9,"score":18,"rating":2614,"username":"handyacc","flair":"smileys.alien","performance":2471}
{"rank":10,"score":16,"rating":1829,"username":"Mc-ArboledaAxel","flair":"activity.lichess-berserk","performance":1902}
{"rank":11,"score":10,"rating":2065,"username":"tunu2011","flair":"smileys.astonished-face-blob","performance":1965}
{"rank":12,"score":8,"rating":2053,"username":"BlackPanda2024","flair":"nature.panda","performance":2043}
{"rank":13,"score":5,"rating":2219,"username":"Cold_Sewy12","performance":2044}
{"rank":14,"score":4,"rating":2640,"username":"Satranc599","flair":"activity.1st-place-medal","performance":2301}
{"rank":15,"score":4,"rating":2110,"username":"bbk10s","performance":2031}
{"rank":16,"score":4,"rating":1781,"username":"coldkarmaguy","performance":1843}
{"rank":17,"score":4,"rating":1621,"username":"Vidishnarra","flair":"smileys.shushing-face","performance":1794}
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
