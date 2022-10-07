deck_of_cards = input().split()
shuffles_count = int(input())
for shuffle in range(shuffles_count):
    new_deck_of_cards = []
    middle_deck = len(deck_of_cards) // 2
    left_part = deck_of_cards[0:middle_deck]
    right_part = deck_of_cards[middle_deck::]
    for card_index in range(len(left_part)):
        new_deck_of_cards.append(left_part[card_index])
        new_deck_of_cards.append(right_part[card_index])
    deck_of_cards = new_deck_of_cards
print(deck_of_cards)