n = int(input())
hero = {}

for _ in range(n):
    line = input()
    name, hp, mp = line.split()[::]
    hp = int(hp)
    mp = int(mp)
    hero[name] = [hp] + [mp]
while True:
    commands = input()
    if commands == "End":
        break
    try:
        command, token1, token2, token3 = commands.split(" - ")[::]
        if command == "CastSpell":
            hero_name, mp_needed, spell_name = token1, token2, token3
            mp_needed = int(mp_needed)
            if hero[hero_name][1] >= mp_needed:
                hero[hero_name][1] -= mp_needed
                print(f"{hero_name} has successfully cast {spell_name} and now has {hero[hero_name][1]} MP!")
            else:
                print(f"{hero_name} does not have enough MP to cast {spell_name}!")
        elif command == "TakeDamage":
            hero_name_d, damage, attacker = token1, token2, token3
            damage = int(damage)
            if hero[hero_name_d][0] > damage:
                hero[hero_name_d][0] -= damage
                print(f"{hero_name_d} was hit for {damage} HP by {attacker} and now has {hero[hero_name_d][0]} HP left!")
            else:
                del hero[hero_name_d]
                print(f"{hero_name_d} has been killed by {attacker}!")
    except ValueError:
        command, token1, token2,  = commands.split(" - ")[::]
        if command == "Recharge":
            hero_name_r, amount = token1, token2
            amount = int(amount)
            hero[hero_name_r][1] += amount
            if hero[hero_name_r][1] > 200:
                hero[hero_name_r][1] -= amount
                print(f"{hero_name_r} recharged for {200 - hero[hero_name_r][1]} MP!")
                hero[hero_name_r][1] = 200
            else:
                print(f"{hero_name_r} recharged for {amount} MP!")
        elif command == "Heal":
            hero_name_h, amount_h = token1, token2
            amount_h = int(amount_h)
            hero[hero_name_h][0] += amount_h
            if hero[hero_name_h][0] > 100:
                hero[hero_name_h][0] -= amount_h
                print(f"{hero_name_h} healed for {100 - hero[hero_name_h][0]} HP!")
                hero[hero_name_h][0] = 100
            else:
                print(f"{hero_name_h} healed for {amount_h} HP!")
for (key, value) in dict(sorted(hero.items(), key=lambda el: (-el[1][0], el[0]))).items():
    print(f'{key}')
    print('HP:' + ' ' + "\nMP: ".join(list(map(str, value))))


