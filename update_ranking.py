import json

# Aktuelle Rangliste als Dict: username -> {'points': int, 'booster': float or None}
"DarkOnCrack": {"points": 0, "booster": None},


new_table_json = """
{"rank":1,"score":82,"rating":2518,"username":"DarkOnCrack","flair":"nature.glowing-star","patronColor":5,"performance":2396}
{"rank":2,"score":73,"rating":2376,"username":"Konariq7","flair":"nature.glowing-star","patronColor":6,"performance":2353}
{"rank":3,"score":70,"rating":2451,"username":"DRUHA12","flair":"people.folded-hands-medium-skin-tone","patronColor":1,"performance":2404}
{"rank":4,"score":65,"rating":2407,"username":"Last_Suspect","performance":2336}
{"rank":5,"score":48,"rating":2610,"username":"Satranc599","flair":"activity.1st-place-medal","patronColor":1,"performance":2511}
{"rank":6,"score":41,"rating":2830,"username":"Kurse-Aura1","flair":"people.fingerprint","performance":2719}
{"rank":7,"score":39,"rating":2058,"username":"This-Is-Agamveer","flair":"symbols.white-exclamation-mark","performance":2223}
{"rank":8,"score":39,"rating":1965,"username":"Justinsenpai","performance":2003}
{"rank":9,"score":32,"rating":2410,"username":"Janislav2000","performance":2326}
{"rank":10,"score":27,"rating":1824,"username":"POPOIPOIPOI","flair":"nature.badger","performance":1945}
{"rank":11,"score":26,"rating":2210,"username":"Abd_el_wahab","flair":"smileys.face-with-tears-of-joy","performance":2090}
{"rank":12,"score":25,"rating":2295,"username":"BlotterFan","flair":"symbols.fleur-de-lis","performance":2299}
{"rank":13,"score":23,"rating":2168,"username":"koreshok73","performance":2051}
{"rank":14,"score":18,"rating":2520,"username":"c4energy","performance":2417}
{"rank":15,"score":18,"rating":2195,"username":"kubak5","performance":2167}
{"rank":16,"score":12,"rating":2547,"username":"TacticalCrush_404","performance":2357}
{"rank":17,"score":6,"rating":2663,"username":"bulletmaniac","performance":2420}
{"rank":18,"score":6,"rating":2086,"username":"Devraj-123","performance":2115}
{"rank":19,"score":6,"rating":1703,"username":"Arjun-Saha6","flair":"smileys.alien","performance":1703}
{"rank":20,"score":4,"rating":2253,"username":"Skysparks","flair":"objects.kimono","performance":2144}
{"rank":21,"score":3,"rating":1846,"username":"EgorGromovYT","flair":"activity.trophy","performance":2144}
{"rank":22,"score":3,"rating":2227,"username":"Zerkycharlie","flair":"activity.lichess-berserk","performance":2126}
{"rank":23,"score":3,"rating":1357,"username":"Ozgur3838","performance":1679}
{"rank":24,"score":2,"rating":2353,"username":"borak-kopitiam","performance":2004}
{"rank":25,"score":1,"rating":2038,"username":"BlackPanda2024","flair":"nature.panda","performance":2038}
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
