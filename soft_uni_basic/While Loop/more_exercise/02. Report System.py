money_expected = int(input())
count_transaction = 0
count_transaction_cash = 0
count_transaction_credit_card = 0
line = input()
credit_card = 0
cash = 0
while line != 'End':
    price = int(line)
    count_transaction += 1
    if count_transaction % 2 == 0:
        if price < 10:
            print('Error in transaction!')
        else:
            count_transaction_credit_card += 1
            credit_card += price
            print('Product sold!')
    else:
        if price > 100:
            print('Error in transaction!')
        else:
            count_transaction_cash += 1
            cash += price
            print('Product sold!')
    total_price = cash + credit_card
    if total_price >= money_expected:
        print(f'Average CS: {cash / count_transaction_cash:.2f}')
        print(f'Average CC: {credit_card / count_transaction_credit_card:.2f}')
        break
    line = input()
if line == 'End':
    print('Failed to collect required money for charity.')

