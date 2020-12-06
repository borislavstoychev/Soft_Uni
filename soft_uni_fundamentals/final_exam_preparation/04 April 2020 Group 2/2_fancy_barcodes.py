import re
pattern = r"^@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+"
n = int(input())
for _ in range(n):
    barcode = input()
    matches = re.match(pattern, barcode)
    if matches:
        digit = re.findall(r"\d", barcode)
        if digit:
            print(f"Product group: {''.join(digit)}")
        else:
            print("Product group: 00")
    else:
        print("Invalid barcode")


