text = tuple(input())
character_and_occurrence = {}
for t in text:
    if t not in character_and_occurrence:
        character_and_occurrence[t] = 1
    else:
        character_and_occurrence[t] += 1
for key, value in dict(sorted(character_and_occurrence.items(), key=lambda x: x[0])).items():
    print(f"{key}: {value} time/s")
