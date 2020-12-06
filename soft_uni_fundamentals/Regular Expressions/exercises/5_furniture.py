import re

line = input()
pattern = r">>\b(?P<name>\w+)<<\b(?P<price>\d+(\.\d+)?)!(?P<quantity>\d+)\b"
names = []
total_price = 0
while not line == "Purchase":
    matches = re.match(pattern, line)
    if matches:
        obj = matches.groupdict()
        names.append(obj["name"])
        total_price += float(obj["price"]) * int(obj["quantity"])
    line = input()
print("Bought furniture:")
[print(name) for name in names]
print(f"Total money spend: {total_price:.2f}")