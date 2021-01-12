n, m = input().split()
set_n = set()
set_m = set()
for n in range(int(n)):
    set_n.add(input())
for m in range(int(m)):
    set_m.add(input())
print(*set_n & set_m, sep="\n")
