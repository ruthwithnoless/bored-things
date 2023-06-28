import random

def draw_cards(n):
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['hearts', 'diamonds', 'clubs', 'spades']
    deck = [r + ' of ' + s for r in ranks for s in suits]

    if n > len(deck):
        print("There are only 52 cards in the deck.")
        return

    drawn_cards = random.sample(deck, n)

    for card in drawn_cards:
        print(card)

# Ask user for the number of cards to draw
num_cards = int(input("Enter the number of cards you want to draw: "))
draw_cards(num_cards)