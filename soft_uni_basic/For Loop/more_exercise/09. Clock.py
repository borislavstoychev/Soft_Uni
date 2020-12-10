h = 0
m = 0
s = 0

print(f'{h} : {m} : {s}')
while h < 24:
    h = h
    m = m
    s += 1
    if s > 59:
        h = h
        m += 1
        s = 0
    if m > 59:
        h += 1
        m = 0
    if h != 24:

        print(f'{h} : {m} : {s}')




