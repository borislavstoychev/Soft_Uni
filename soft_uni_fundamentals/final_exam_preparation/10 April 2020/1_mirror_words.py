import re

line = input()
pattern = r"(@[A-Za-z]{3,}@){2}|(#[A-Za-z]{3,}#){2}"
matches = [match.group() for match in re.finditer(pattern, line)]
collection = []
if matches:
    for word in matches:
        if "#" in word:
            line1, line2 = word.split("##")
            line1, line2 = line1[1:], line2[:-1]
            reversed_line = line1[::-1]
            if line2 == reversed_line:
                collection.append(f"{line1} <=> {line2}")
        else:
            line1, line2 = word.split("@@")
            line1, line2 = line1[1:], line2[:-1]
            reversed_line = line1[::-1]
            if line2 == reversed_line:
                collection.append(f"{line1} <=> {line2}")
    print(f"{len(matches)} word pairs found!")
else:
    print("No word pairs found!")
if collection:
    print("The mirror words are:")
    print(", ".join(collection))
else:
    print("No mirror words!")