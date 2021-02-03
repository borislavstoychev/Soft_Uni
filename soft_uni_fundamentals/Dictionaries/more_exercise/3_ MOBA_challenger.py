line = input()
total_skills = {}
players = {}
while not line == "Season end":
    try:
        player, position, skill = line.split(" -> ")
        skill = int(skill)
        if player not in players:
            players[player] = {position: skill}
        else:
            if position in players[player]:
                if players[player][position] < skill:
                    players[player][position] = skill
            else:
                players[player].update({position: skill})
    except ValueError:
        is_win = False
        player1, player2 = line.split(" vs ")
        if player1 in players and player2 in players:
            for k, v in players.items():
                if k == player1 or k == player2:
                    for p, s in v.items():
                        if p in players[player1] and p in players[player2]:
                            if players[player1][p] < players[player2][p]:
                                del players[player1]
                                is_win = True
                            else:
                                del players[player2]
                                is_win = True
                            break
                    if is_win:
                        break
    line = input()
for k, v in players.items():
    total_skills[k] = 0
    for s, m in v.items():
        total_skills[k] += m
for key, value in dict(sorted(total_skills.items(), key=lambda el: (-el[1], el[0]))).items():
    print(f"{key}: {value} skill")
    for gamer, skills in players.items():
        skills = dict(sorted(skills.items(), key=lambda x: (-x[1])))
        if gamer == key:
            for position, skill in skills.items():
                print(f'- {position} <::> {skill}')
