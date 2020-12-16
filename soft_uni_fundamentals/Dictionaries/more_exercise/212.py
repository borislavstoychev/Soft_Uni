line = input()
player_position_skill = {}
total_skills = {}

while line != 'Season end':
    try:
        player, position, skill = line.split(" -> ")
        skill = int(skill)
        if player not in player_position_skill:
            player_position_skill[player] = {}
            player_position_skill[player][position] = skill
        else:
            if position not in player_position_skill[player]:
                player_position_skill[player][position] = skill
            else:
                if player_position_skill[player][position] < skill:
                    player_position_skill[player][position] = 0
                    player_position_skill[player][position] += skill

    except ValueError:
        player_1, player_2 = line.split(" vs ")
        player_1_dict = {}
        player_2_dict = {}
        if player_1 in player_position_skill and player_2 in player_position_skill:
            for key, value in player_position_skill.items():
                if key == player_1:
                    for position, points in value.items():
                        player_1_dict[position] = points

                elif key == player_2:
                    for position, points in value.items():
                        player_2_dict[position] = points

            for p, s in player_1_dict.items():
                if p in player_2_dict:
                    if player_1_dict[p] > player_2_dict[p]:
                        del player_position_skill[player_2]

                    elif player_2_dict[p] > player_1_dict[p]:
                        del player_position_skill[player_1]
    line = input()
for k, v in player_position_skill.items():
    total_skills[k] = 0
    for s, m in v.items():
        total_skills[k] += m
total_points = dict(sorted(total_skills.items(), key=lambda x: (-x[1], x[0])))
for player, points in total_points.items():
    print(f'{player}: {points} skill')
    for key, value in player_position_skill.items():
        value = dict(sorted(value.items(), key=lambda x: (-x[1], x[0])))
        if player == key:
            for position, skill in value.items():
                print(f'- {position} <::> {skill}')
