V = int(input())
P1 = int(input())
P2 = int(input())
H = float(input())

if 1 <= V <= 10000 or 1 <= P1 <= 5000 or 1 <= P2 <= 5000 or 1 <= H <= 24:
    P1_liters = (P1 * H)
    P2_liters = (P2 * H)
    total_V = P1_liters + P2_liters
    if total_V <= V:

        print(f'The pool is {(total_V / V) * 100: .2f}% full. Pipe 1: {(P1_liters / total_V) * 100: .2f}%. Pipe 2: {(P2_liters / total_V) * 100: .2f}%.')
    else:
        print(f'For {H} hours the pool overflows with {total_V - V: .2f} liters.')
else:
    print('Error')
