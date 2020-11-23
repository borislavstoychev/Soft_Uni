n = int(input())
p = int(input())
if n % p == 0:
    courses = n//p
else:
    courses = n // p + 1
print(courses)