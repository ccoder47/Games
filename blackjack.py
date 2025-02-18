import random

# Card values and deck setup
def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
             'J': 10, 'Q': 10, 'K': 10, 'A': 11}
    return [{'rank': rank, 'suit': suit, 'value': value} for suit in suits for rank, value in ranks.items()]

# Draw a card from the deck
def draw_card(deck):
    return deck.pop(random.randint(0, len(deck) - 1))

# Calculate hand value
def calculate_hand(hand):
    value = sum(card['value'] for card in hand)
    aces = sum(1 for card in hand if card['rank'] == 'A')
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

# Display hand
def display_hand(player, hand):
    cards = ', '.join([f"{card['rank']} of {card['suit']}" for card in hand])
    print(f"{player}'s hand: {cards} (Value: {calculate_hand(hand)})")

# Main game loop
def blackjack():
    deck = create_deck()
    random.shuffle(deck)
    
    player_hand = [draw_card(deck), draw_card(deck)]
    dealer_hand = [draw_card(deck), draw_card(deck)]
    
    while True:
        display_hand("Player", player_hand)
        print(f"Dealer's first card: {dealer_hand[0]['rank']} of {dealer_hand[0]['suit']}")
        
        if calculate_hand(player_hand) == 21:
            print("Blackjack! You win!")
            return
        
        action = input("Hit or Stand? (h/s): ").strip().lower()
        if action == 'h':
            player_hand.append(draw_card(deck))
            if calculate_hand(player_hand) > 21:
                display_hand("Player", player_hand)
                print("Bust! You lose.")
                return
        else:
            break
    
    while calculate_hand(dealer_hand) < 17:
        dealer_hand.append(draw_card(deck))
    
    display_hand("Dealer", dealer_hand)
    
    player_value = calculate_hand(player_hand)
    dealer_value = calculate_hand(dealer_hand)
    
    if dealer_value > 21 or player_value > dealer_value:
        print("You win!")
    elif player_value < dealer_value:
        print("Dealer wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    blackjack()
