line = input().split(", ")
special_symbols = ["@", "#", "$", "^"]
for t in line:
    ticket = t.strip()
    if len(ticket) == 20:
        right = ticket[10:]
        left = ticket[:10]
        for symbol in special_symbols:
            if symbol * 6 in right:
                count_left = left.count(symbol)
                count_right = right.count(symbol)
                if count_left == 10 and count_right == 10:
                    print(f'ticket "{ticket}" - {count_right}{symbol} Jackpot!')
                else:
                    print(f'ticket "{ticket}" - {min(count_left, count_right)}{symbol}')
                break
        else:
            print(f'ticket "{ticket}" - no match')
    else:
        print("invalid ticket")
