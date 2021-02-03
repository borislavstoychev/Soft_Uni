data = input()
dwarfs = {}
colors = {}
while not data == "Once upon a time":
    dwarf_name, dwarf_hat_color, dwarf_physics = data.split(" <:> ")
    dwarf_physics = int(dwarf_physics)
    name_color = f"{dwarf_name}:{dwarf_hat_color}"
    if name_color not in dwarfs:
        if dwarf_hat_color not in colors:
            colors[dwarf_hat_color] = 1
        else:
            colors[dwarf_hat_color] += 1
        dwarfs[name_color] = [0, dwarf_hat_color]
    dwarfs[name_color][0] = max([dwarfs[name_color][0], dwarf_physics])
    data = input()

for key, value in dict(sorted(dwarfs.items(), key=lambda el: (-el[1][0], -colors[el[1][1]]))).items():
    tokens = key.split(":")
    print(f"({tokens[1]}) {tokens[0]} <-> {value[0]}")
