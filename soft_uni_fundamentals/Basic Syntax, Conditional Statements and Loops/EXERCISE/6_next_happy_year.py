# year = int(input())
#
# while True:
#     year += 1
#     if len(str(year)) == len(set(str(year))):
#         print(year)
#         break

year = int(input())
year += 1
while len(set(str(year))) != len(str(year)):
    year += 1

print(year)
