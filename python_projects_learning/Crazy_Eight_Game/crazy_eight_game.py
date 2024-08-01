import random
import time
from magic_cards import perform_magic_of_card, magic_card

def deck_of_cards():
    suits = ["Diamonds","Clubs","Hearts","Spades"]

    #Returns a list of card numbers with suits
    cards_1_10 = [ str(num) + " of " + suit for num in range(1,11) for suit in suits]
    other_cards = ["J","K","Q"]
    royal_cards = [ card + " of " + suit for card in other_cards for suit in suits]
    
    all_cards = cards_1_10 + royal_cards
    return all_cards

#Takes a specific number of cards from deck and asign to player or computer
def shuffle_card_deck(card_deck):
    #This will randomly sort all the cards in deck hence shuffling
    shuffled_cards = random.sample(card_deck,k=len(card_deck))
    return shuffled_cards

def take_cards(card_deck,number_of_cards=0):
    #Picks a certain number of cards and asigns to computer or player
    if len(card_deck) < number_of_cards:
        print(f"Invalid number of cards there are only {len(card_deck)} cards left.")
    
    cards_taken = random.sample(card_deck,k=number_of_cards)

    #The cards taken from deck have to be removed from deck as they have moved to another destination
    for chosen_card in cards_taken:
        for card in card_deck:
            if card == chosen_card:
                card_deck.remove(chosen_card)
    
    return cards_taken

def get_card_suit(card):
    suits = ["Diamonds","Clubs","Hearts","Spades"]
    
    result = None
    for suit in suits:
        if suit in card:
            result = suit
    
    return result

#TODO: Make a get card number function which returns number in a card or J,K,Q
def get_card_number(card):
    possible_options = ["1","2","3","4","5","6","7","8","9","10","J","K","Q"]

    result = None
    for option in possible_options:
        if option in card:
            result = option

    return result

#From computer cards one card will be picked and played on the pool
def play_card_computer(computer_cards,pool):
    if len(pool) == 1:
        current_card = pool[0]
    else:
        current_card = pool[-1]

    valid_cards = []
    # Checks if there are computer cards which match the current card suit and store them in valid cards list
    #Checks if there are computer cards which have matching numbers
    for card in computer_cards:
        if get_card_suit(card) == get_card_suit(current_card):
            valid_cards.append(card)
        elif get_card_number(current_card) in card:
            valid_cards.append(card) 

    if valid_cards == []:
        return None

    #Picks random playable card for computer to be put in pool
    computer_pick = random.sample(valid_cards,k=1)

    #Returns a card picked by computer
    print(f"Computer played {computer_pick[0]}")
    print()
    return computer_pick[0]

def play_card_player(player_cards,pool):
    if len(pool) == 1:
        current_card = pool[0]
    else:
        current_card = pool[-1]

    print(f"Please pick index of card number inbetween 0 and {len(player_cards) - 1}")
    #Prints cards in a friendly format and correct index
    for index in range(len(player_cards)):
        print(f"{index} - {player_cards[index]}")
    print()

    #Stores all valid cards a player can pick from else an empty list
    playable_cards = []

    for card in player_cards:
        if get_card_suit(current_card) == get_card_suit(card):
            playable_cards.append(card)
        elif get_card_number(current_card) in card:
            playable_cards.append(card)

    if playable_cards == []:
        print("You do not have any valid playable cards")
        return None
    
    user_input = input("Enter index/position of card you want to play here: ")
    if user_input.isnumeric() == False:
        print("Invalid input try again :(")
        quit()

    user_input = int(user_input)
    if user_input < 0 and user_input >= len(player_cards):
        print("Invalid Index :(")
        quit()

    if get_card_suit(current_card) in player_cards[user_input]:
        print(f"You played {player_cards[user_input]}")
        return player_cards[user_input]

#When player or bor cant play a card with a valid suit they have to pick a card
def pick_a_card(computer_or_player_deck,card_deck):
    #Remove the card from deck 
    last_card_from_deck = card_deck[-1]
    card_deck.remove(last_card_from_deck)

    #Add card to player or computer deck
    computer_or_player_deck.append(last_card_from_deck)
    print("Player picked a card successfully")

    return True

def add_card_to_pool(card,pool, player_card_deck):
    #Moves playable card in deck to pool
    pool.append(card)
    player_card_deck.remove(card)





