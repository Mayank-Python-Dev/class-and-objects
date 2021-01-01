players_data = {}

with open("scores.csv",'r') as f:
    for line in f:
        token = line.split(",")
        player = token[0]
        player_score = int(token[1])

        if player in players_data:
            players_data[player].append(player_score)
        else:
            players_data[player] = [player_score]

print(players_data)

for x,y in players_data.items():
    min_score = min(y)
    max_score = max(y)
    avg_score = sum(y)/len(y)
    print(f"player name : {x}, maxscore : {max_score}, minscore : {min_score}, avgscore = {avg_score}")