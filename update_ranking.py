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
{"rank":1,"score":86,"rating":2482,"username":"DarkOnCrack","flair":"nature.glowing-star","patronColor":5,"performance":2363}
{"rank":2,"score":41,"rating":2170,"username":"Abd_el_wahab","flair":"smileys.face-with-tears-of-joy","performance":2387}
{"rank":3,"score":26,"rating":2201,"username":"BlotterFan","flair":"symbols.fleur-de-lis","performance":2234}
{"rank":4,"score":21,"rating":2435,"username":"Konariq7","flair":"nature.glowing-star","patronColor":6,"performance":2421}
{"rank":5,"score":16,"rating":2103,"username":"tunu2011","flair":"smileys.astonished-face-blob","performance":2301}
{"rank":6,"score":14,"rating":2189,"username":"Cold_Sewy12","performance":2318}
{"rank":7,"score":12,"rating":2014,"username":"Chonma","flair":"smileys.ogre","performance":2027}
{"rank":8,"score":6,"rating":1752,"username":"KillingHeartattack","flair":"activity.1st-place-medal","performance":1917}
{"rank":9,"score":4,"rating":2314,"username":"ComeToBaba1","flair":"objects.crown","performance":2004}
{"rank":10,"score":3,"rating":2324,"username":"ZugzwangMode","performance":2134}
{"rank":11,"score":3,"rating":2082,"username":"BlackPanda2024","flair":"nature.panda","performance":1904}
{"rank":12,"score":3,"rating":1952,"username":"Che947","flair":"activity.lichess-berserk","performance":1775}
{"rank":13,"score":2,"rating":2292,"username":"Bullet_Thomas","flair":"smileys.face-blowing-a-kiss","performance":2527}
{"rank":14,"score":2,"rating":2214,"username":"Skysparks","flair":"objects.kimono","performance":2098}
{"rank":15,"score":2,"rating":2221,"username":"kubak5","performance":2004}
{"rank":16,"score":2,"rating":1819,"username":"capt_ateradz","performance":1959}
{"rank":17,"score":2,"rating":2046,"username":"Justinsenpai","performance":1824}
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
