deck = input().split()
num_of_shuffles = int(input())

middle = len(deck) // 2
top_card = deck[0]
bottom_card = deck[-1]

for shuffles in range(num_of_shuffles):

    left_deck = []
    right_deck = []
    shuffled_card = []

    for index in range(1, middle):
        left_deck.append(deck[index])
    for index in range(middle, len(deck) - 1):
        right_deck.append(deck[index])
    for index in range(len(left_deck)):
        shuffled_card.append(right_deck[index])
        shuffled_card.append(left_deck[index])
    
    deck = shuffled_card
    deck.append(bottom_card)
    deck.insert(0, top_card)

print(deck)

