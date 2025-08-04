import random

# Create the full deck of cards
def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
             'J': 10, 'Q': 10, 'K': 10, 'A': 11}
    return [{'rank': rank, 'suit': suit, 'value': value} for suit in suits for rank, value in ranks.items()]

# Draw a card randomly
def draw_card(deck):
    return deck.pop(random.randint(0, len(deck) - 1))

# Calculate the value of a hand, adjusting Aces as needed
def calculate_hand(hand):
    value = sum(card['value'] for card in hand)
    aces = sum(1 for card in hand if card['rank'] == 'A')
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

# Display a hand
def display_hand(player, hand, reveal_all=True):
    if player == "Dealer" and not reveal_all:
        print(f"Dealer's hand: {hand[0]['rank']} of {hand[0]['suit']} and [Hidden]")
    else:
        cards = ', '.join([f"{card['rank']} of {card['suit']}" for card in hand])
        print(f"{player}'s hand: {cards} (Value: {calculate_hand(hand)})")

# The main game logic
def blackjack():
    print("\nThank you for visiting my GitHub and running my program.")
    print("Welcome to Blackjack — built by Clarence, your digital dealer for today.")
    print("Let's have some fun!\n")

    bankroll = 100

    while bankroll > 0:
        print(f"\n💰 Current bankroll: ${bankroll}")
        try:
            bet = int(input("Place your bet: $"))
            if bet <= 0 or bet > bankroll:
                print("Invalid bet. Try again.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue

        deck = create_deck()
        random.shuffle(deck)

        player_hand = [draw_card(deck), draw_card(deck)]
        dealer_hand = [draw_card(deck), draw_card(deck)]

        display_hand("Player", player_hand)
        display_hand("Dealer", dealer_hand, reveal_all=False)

        while True:
            action = input("Hit or Stand? (h/s): ").strip().lower()
            if action == 'h':
                player_hand.append(draw_card(deck))
                display_hand("Player", player_hand)
                if calculate_hand(player_hand) > 21:
                    print("Bust! You lose.")
                    bankroll -= bet
                    break
            elif action == 's':
                break
            else:
                print("Please enter 'h' or 's'.")

        if calculate_hand(player_hand) <= 21:
            while calculate_hand(dealer_hand) < 17:
                dealer_hand.append(draw_card(deck))
            display_hand("Dealer", dealer_hand)

            player_value = calculate_hand(player_hand)
            dealer_value = calculate_hand(dealer_hand)

            if dealer_value > 21 or player_value > dealer_value:
                print("You win!")
                bankroll += bet
            elif player_value < dealer_value:
                print("Dealer wins!")
                bankroll -= bet
            else:
                print("It's a tie!")

        if bankroll <= 0:
            print("You're out of money!")
            break

        play_again = input("\nPlay again? (y/n): ").strip().lower()
        if play_again != 'y':
            break

    print("\nThanks for playing Blackjack by Clarence!")
    print("I Hope you enjoyed your time!")

# Run the game
if __name__ == "__main__":
    blackjack()
