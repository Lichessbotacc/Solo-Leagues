import json

# Aktuelle Rangliste als Dict: username -> {'points': int, 'booster': float or None}
current_ranking = {
    "DarkOnCrack": {"points": 1603, "booster": 1.7},
    "Alex-31": {"points": 424, "booster": 1.6},
    "VariantsMain": {"points": 334, "booster": 2.0},
    "Justinsenpai": {"points": 318, "booster": None},
    "Abd_el_wahab": {"points": 176, "booster": None},
    "Helokid": {"points": 148, "booster": None},
    "tomkruz88": {"points": 142, "booster": None},
    "artoftheblade": {"points": 127, "booster": None},
    "Satranc599": {"points": 122, "booster": None},
    "POPOIPOIPOI": {"points": 100, "booster": None},
    "Konariq7": {"points": 98, "booster": None},
    "Kurse-Aura1": {"points": 95, "booster": None},
    "Mahamaha14": {"points": 87, "booster": 1.9},
    "Clesio-MorgaM": {"points": 81, "booster": None},
    "BlotterFan": {"points": 75, "booster": None},
    "AhsapAhsap": {"points": 73, "booster": None},
    "FranceWinsWorldCup": {"points": 72, "booster": 1.8},
    "DRUHA12": {"points": 70, "booster": None},
    "Last_Suspect": {"points": 65, "booster": None},
    "IZerkYouLose": {"points": 63, "booster": None},
    "just_chess12": {"points": 56, "booster": None},
    "Cold_Sewy12": {"points": 48, "booster": None},
    "tunu2011": {"points": 48, "booster": None},
    "PushAttack14": {"points": 47, "booster": None},
    "Chonma": {"points": 47, "booster": 1.4},
    "mike-bear": {"points": 47, "booster": 1.5},
    "This-Is-Agamveer": {"points": 41, "booster": None},
    "manglee": {"points": 41, "booster": None},
    "BlackPanda2024": {"points": 38, "booster": None},
    "RodriFK": {"points": 33, "booster": None},
    "Janislav2000": {"points": 32, "booster": None},
    "BlitzWarlord": {"points": 31, "booster": None},
    "Agam2013": {"points": 29, "booster": 1.3},
    "doruk2606": {"points": 28, "booster": None},
    "KillingHeartattack": {"points": 28, "booster": None},
    "VTacademy": {"points": 25, "booster": None},
    "Conrad_Gagnon": {"points": 24, "booster": 1.1},
    "koreshok73": {"points": 23, "booster": None},
    "bbk10s": {"points": 22, "booster": None},
    "kubak5": {"points": 22, "booster": None},
    "Che947": {"points": 22, "booster": None},
    "LucienTupin": {"points": 21, "booster": None},
    "tharindujayasuriya": {"points": 19, "booster": None},
    "c4energy": {"points": 18, "booster": None},
    "handyacc": {"points": 18, "booster": None},
    "Mc-ArboledaAxel": {"points": 16, "booster": None},
    "TheRuleBreaker122": {"points": 15, "booster": None},
    "Try_Different_Bro28": {"points": 15, "booster": None},
    "Tipchess": {"points": 14, "booster": None},
    "RWDHDK67": {"points": 14, "booster": None},
    "Andyisagoodboy": {"points": 14, "booster": 1.2},
    "Supperhero_2012": {"points": 13, "booster": None},
    "TacticalCrush_404": {"points": 12, "booster": None},
    "vwz": {"points": 9, "booster": None},
    "SilentExecution": {"points": 8, "booster": None},
    "Vidishnarra": {"points": 8, "booster": None},
    "Livoncik": {"points": 8, "booster": None},
    "bulletmaniac": {"points": 6, "booster": None},
    "Devraj-123": {"points": 6, "booster": None},
    "Arjun-Saha6": {"points": 6, "booster": None},
    "EgorGromovYT": {"points": 6, "booster": None},
    "Skysparks": {"points": 6, "booster": None},
    "Aura_Farming77": {"points": 6, "booster": None},
    "test_acc123": {"points": 6, "booster": None},
    "dunk-master": {"points": 5, "booster": None},
    "GeekingKing": {"points": 4, "booster": None},
    "A_Khurramov_05": {"points": 4, "booster": None},
    "coldkarmaguy": {"points": 4, "booster": None},
    "ComeToBaba1": {"points": 4, "booster": None},
    "PhilipX_2023": {"points": 4, "booster": None},
    "schwarzerrabe": {"points": 4, "booster": None},
    "Ochesage": {"points": 4, "booster": None},
    "Zerkycharlie": {"points": 3, "booster": None},
    "Ozgur3838": {"points": 3, "booster": None},
    "ZugzwangMode": {"points": 3, "booster": None},
    "sribna": {"points": 3, "booster": None},
    "learningchess6": {"points": 3, "booster": None},
    "borak-kopitiam": {"points": 2, "booster": None},
    "blueblue8887": {"points": 2, "booster": None},
    "ciyaerdal4735": {"points": 2, "booster": None},
    "Checkmate_Drifters": {"points": 2, "booster": None},
    "RumijaBarCG21": {"points": 2, "booster": None},
    "Bullet_Thomas": {"points": 2, "booster": None},
    "capt_ateradz": {"points": 2, "booster": None},
    "Asherdarin": {"points": 2, "booster": None},
    "VenusaurBeedrill": {"points": 2, "booster": None},
    "jash_the_goat": {"points": 1, "booster": None},
}

new_table_json = """
{"rank":1,"score":114,"rating":2422,"username":"phone-zerk","flair":"smileys.anxious-face-with-sweat","performance":2429}
{"rank":2,"score":65,"rating":2359,"username":"DarkOnCrack","flair":"nature.glowing-star","patronColor":6,"performance":2346}
{"rank":3,"score":54,"rating":2206,"username":"tomkruz88","performance":2223}
{"rank":4,"score":50,"rating":2171,"username":"ElBasmgy","performance":2078}
{"rank":5,"score":38,"rating":2372,"username":"Retasea_400","performance":2352}
{"rank":6,"score":18,"rating":2002,"username":"GeekingKing","performance":1966}
{"rank":7,"score":16,"rating":2288,"username":"Best_Chess_Player15","flair":"food-drink.mango","performance":2185}
{"rank":8,"score":6,"rating":2270,"username":"ComeToBaba1","flair":"objects.crown","performance":2201}
{"rank":9,"score":6,"rating":1622,"username":"Alcedo","flair":"symbols.small-blue-diamond","patronColor":1,"performance":1780}
{"rank":10,"score":3,"rating":2048,"username":"DIMAStup","flair":"food-drink.doughnut","performance":1946}
{"rank":11,"score":3,"rating":2085,"username":"Tipchess","flair":"food-drink.green-apple","patronColor":3,"performance":1909}
{"rank":12,"score":2,"rating":1979,"username":"EEAguitarn1","flair":"smileys.disguised-face","performance":2456}
{"rank":13,"score":2,"rating":1610,"username":"FatDummy","performance":2108}
{"rank":14,"score":2,"rating":2216,"username":"Retroceso","flair":"people.crossed-fingers","performance":1958}
{"rank":15,"score":2,"rating":1099,"username":"fin34601473braunpaul","flair":"activity.lichess-horsey","patronColor":10,"performance":1748}
{"rank":16,"score":2,"rating":1900,"username":"RookNRollMaster","flair":"symbols.transgender-flag","performance":1582}
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
