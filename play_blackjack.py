import random
import time

# function to create a deck of cards
def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
    deck = [{'value': value, 'suit': suit} for suit in suits for value in values]
    return deck

# function to shuffle the deck
def shuffle_deck(deck):
    random.shuffle(deck)

# function to deal a card from the deck
def deal_card(deck):
    return deck.pop()

# function to convert card value to string
def card_to_string(card):
    return f"{card['value']} of {card['suit']}"

# function to calculate the total value of a hand
def calculate_hand_value(hand):
    total_value = sum(card_value(card['value']) for card in hand)
    num_aces = sum(1 for card in hand if card['value'] == 'Ace')
    while total_value > 21 and num_aces:
        total_value -= 10
        num_aces -= 1
    return total_value

# function to get the value of a card
def card_value(value):
    if value in ['Jack', 'Queen', 'King']:
        return 10
    elif value == 'Ace':
        return 11
    else:
        return int(value)
    
# greet player
print("")
print("****** Welcome to Blackjack! Grab a seat and let's play! ******")
time.sleep(2)  
print("\nHello there! I'm Paca the Python Dealer and I'm here to take your money, just kidding. I hope you win, because I can't use money.")
player_name = input("Anyway, what's your name? ")
time.sleep(1)
print(f"\nAwesome, nice to meet you {player_name}! Now let's get started, here we go!")
print(f"\nThe dealer is shuffling the cards...")
time.sleep(4)
print(f"\nHere they come...")
time.sleep(2)

def play_blackjack():
    # Create a deck of cards
    deck = create_deck()

    # Shuffle the deck
    shuffle_deck(deck)

    # Deal two cards to the dealer and two cards to the player
    dealer_hand = [deal_card(deck), deal_card(deck)]
    player_hand = [deal_card(deck), deal_card(deck)]

    # Print the initial hands
    print(f"\nThe dealer has {card_to_string(dealer_hand[0])} and a face down card")
    time.sleep(3)
    print(f"{player_name} has {card_to_string(player_hand[0])} and {card_to_string(player_hand[1])}")
    time.sleep(3)

    # Check if the player has Blackjack
    if calculate_hand_value(player_hand) == 21:
        time.sleep(3)
        print(f"\n{player_name} has Blackjack!")

    # Player's turn
    while True:
        decision = input("\nDo you want to hit or stand? (h/s): ").lower()
        if decision == 'h':
            new_card = deal_card(deck)
            player_hand.append(new_card)
            print(f"\n{player_name} hits and receives: {card_to_string(new_card)}")
            time.sleep(2)
            print(f"{player_name}'s total: {calculate_hand_value(player_hand)}")
            time.sleep(2)
            if calculate_hand_value(player_hand) > 21:
                print(f"\n{player_name} busts! Dealer wins.")
                return False
        elif decision == 's':
            break
        else:
            print("Invalid input. Please enter 'h' to hit or 's' to stand.")

    # Reveal the dealer's unknown card
    print("\nDealer's turn:")
    time.sleep(2)  
    print(f"The dealer flips the face down card and shows {card_to_string(dealer_hand[1])}")
    time.sleep(2)  

    # Dealer's turn: Hit if the total value of the hand is 16 or less
    #print("\nDealer's turn:")
    time.sleep(2)
    while calculate_hand_value(dealer_hand) <= 16:
        new_card = deal_card(deck)
        dealer_hand.append(new_card)
        print("\nDealer's turn:")
        time.sleep(2)
        print(f"The dealer hits and receives: {card_to_string(new_card)}")
        time.sleep(2)
        print(f"Dealer's total: {calculate_hand_value(dealer_hand)}")
        time.sleep(2)  
        if calculate_hand_value(dealer_hand) > 21:
            print("\nDealer busts!")
            time.sleep(2) 
            return True

    # Determine the winner
    player_total = calculate_hand_value(player_hand)
    dealer_total = calculate_hand_value(dealer_hand)

    print("\nFINAL HANDS:")
    print(f"The dealer has {' and '.join(card_to_string(card) for card in dealer_hand)} (TOTAL: {dealer_total})")
    time.sleep(3)
    print(f"{player_name} has {' and '.join(card_to_string(card) for card in player_hand)} (TOTAL: {player_total})")
    time.sleep(3)

    if player_total > dealer_total:
        print("\nYou win!")
        return True
    elif player_total < dealer_total:
        print("\nDealer wins!")
        return False
    else:
        print("\nIt's a tie!")
        return False

# Main game loop
while True:
    if play_blackjack():
        print("\nCongratulations! You won!")
    else:
        print("\nWah wah, no luck this time!")
    time.sleep(2)
    play_again = input("\nDo you want to play again? (y/n): ").lower()
    if play_again != 'y':
        print(f"\nCome back again soon! See you next time {player_name}.")
        time.sleep(2)
        break
