import json

# Aktuelle Rangliste als Dict: username -> {'points': int, 'booster': float or None}
current_ranking = {
    "DarkOnCrack": {"points": 1499, "booster": 1.8},
    "Alex-31": {"points": 377, "booster": 1.9},
    "Justinsenpai": {"points": 318, "booster": None},
    "VariantsMain": {"points": 213, "booster": 2.0},
    "Abd_el_wahab": {"points": 176, "booster": 1.7},
    "Helokid": {"points": 148, "booster": 1.5},
    "tomkruz88": {"points": 138, "booster": None},
    "artoftheblade": {"points": 127, "booster": None},
    "Satranc599": {"points": 122, "booster": None},
    "POPOIPOIPOI": {"points": 100, "booster": None},
    "Konariq7": {"points": 98, "booster": None},
    "Kurse-Aura1": {"points": 95, "booster": None},
    "Clesio-MorgaM": {"points": 81, "booster": 1.4},
    "BlotterFan": {"points": 75, "booster": None},
    "AhsapAhsap": {"points": 73, "booster": None},
    "DRUHA12": {"points": 70, "booster": None},
    "Last_Suspect": {"points": 65, "booster": None},
    "IZerkYouLose": {"points": 63, "booster": None},
    "just_chess12": {"points": 56, "booster": None},
    "Cold_Sewy12": {"points": 48, "booster": None},
    "PushAttack14": {"points": 47, "booster": None},
    "This-Is-Agamveer": {"points": 41, "booster": None},
    "manglee": {"points": 41, "booster": None},
    "BlackPanda2024": {"points": 38, "booster": None},
    "RodriFK": {"points": 33, "booster": 1.6},
    "Janislav2000": {"points": 32, "booster": None},
    "BlitzWarlord": {"points": 31, "booster": None},
    "tunu2011": {"points": 29, "booster": None},
    "doruk2606": {"points": 28, "booster": None},
    "KillingHeartattack": {"points": 28, "booster": None},
    "VTacademy": {"points": 25, "booster": None},
    "koreshok73": {"points": 23, "booster": None},
    "bbk10s": {"points": 22, "booster": None},
    "kubak5": {"points": 22, "booster": None},
    "Che947": {"points": 22, "booster": 1.3},
    "LucienTupin": {"points": 21, "booster": None},
    "tharindujayasuriya": {"points": 19, "booster": None},
    "c4energy": {"points": 18, "booster": None},
    "handyacc": {"points": 18, "booster": None},
    "Chonma": {"points": 18, "booster": None},
    "Mc-ArboledaAxel": {"points": 16, "booster": None},
    "TheRuleBreaker122": {"points": 15, "booster": None},
    "Try_Different_Bro28": {"points": 15, "booster": 1.2},
    "Tipchess": {"points": 14, "booster": 1.1},
    "Supperhero_2012": {"points": 13, "booster": None},
    "TacticalCrush_404": {"points": 12, "booster": None},
    "vwz": {"points": 9, "booster": None},
    "SilentExecution": {"points": 8, "booster": None},
    "RWDHDK67": {"points": 8, "booster": None},
    "Conrad_Gagnon": {"points": 8, "booster": None},
    "bulletmaniac": {"points": 6, "booster": None},
    "Devraj-123": {"points": 6, "booster": None},
    "Arjun-Saha6": {"points": 6, "booster": None},
    "EgorGromovYT": {"points": 6, "booster": None},
    "Skysparks": {"points": 6, "booster": None},
    "Aura_Farming77": {"points": 6, "booster": None},
    "dunk-master": {"points": 5, "booster": None},
    "GeekingKing": {"points": 4, "booster": None},
    "A_Khurramov_05": {"points": 4, "booster": None},
    "coldkarmaguy": {"points": 4, "booster": None},
    "Vidishnarra": {"points": 4, "booster": None},
    "ComeToBaba1": {"points": 4, "booster": None},
    "PhilipX_2023": {"points": 4, "booster": None},
    "schwarzerrabe": {"points": 4, "booster": None},
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
    "jash_the_goat": {"points": 1, "booster": None},
}

new_table_json = """
{"rank":1,"score":4,"rating":2164,"username":"tomkruz88","performance":2389}
{"rank":2,"score":4,"rating":2068,"username":"Ochesage","performance":2299}
{"rank":3,"score":2,"rating":1949,"username":"VenusaurBeedrill","flair":"activity.lichess-variant-atomic","patronColor":1,"performance":1997}
{"rank":4,"score":0,"rating":2695,"username":"Chess_Training_2021","flair":"objects.crown"}
{"rank":5,"score":0,"rating":2532,"username":"DarkOnCrack","flair":"nature.glowing-star","patronColor":5}
{"rank":6,"score":0,"rating":2065,"username":"tunu2011","flair":"nature.bison"}
{"rank":7,"score":0,"rating":1987,"username":"OneOfTheWorldsBest","flair":"nature.horse"}
{"rank":8,"score":0,"rating":1766,"username":"jash_the_goat","flair":"smileys.alien","performance":1565}
{"rank":9,"score":0,"rating":1825,"username":"Conrad_Gagnon","performance":1557}
{"rank":10,"score":0,"rating":1500,"username":"tasteyourloss2015"}
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
