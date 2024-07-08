import random
def homepage_menu():
    print("1 View Cards at Pool ")
    print("2 View your cards ")
    print("3 Play a card ")
    print("4 Exit the game")

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
    
    for suit in suits:
        if suit in card:
            return suit
            break

#From computer cards one card will be picked and played on the pool
def play_card_computer(computer_cards,pool):
    if len(pool) == 1:
        current_card = pool[0]
    else:
        current_card = pool[-1]

    valid_cards = []
    # Checks if there are computer cards which match the current card suit and store them in valid cards list
    for card in computer_cards:
        if get_card_suit(card) == get_card_suit(current_card):
            valid_cards.append(card)

    if valid_cards == []:
        return None

    #Picks random card for computer to be put in pool
    computer_pick = random.sample(valid_cards,k=1)

    return computer_pick[0]

def play_card_player(player_cards,pool):
    if len(pool) == 1:
        current_card = pool[0]
    else:
        current_card = pool[-1]

    print(f"Please pick index of card number inbetween 0 and {len(player_cards)}")
    print(player_cards)

    user_input = input("Enter index/position of card you want to play here: ")
    if user_input.isnumeric() == False:
        print("Invalid input try again")
        quit()

    user_input = int(user_input)
    if user_input < 0 and user_input >= len(player_cards):
        print("Invalid Index")
        quit()

    if get_card_suit(current_card) in player_cards[user_input]:
        return player_cards[user_input]
    else:
        print(f"Error suit doesnt match {current_card} suit. Pick another card :(")
        quit()

def main():
    #Get all cards and shuffle them
    all_cards_unshuffled = deck_of_cards()
    cards_shuffled = shuffle_card_deck(all_cards_unshuffled)

    #Game starts with assigning 8 cards to computer and player
    computer_cards = take_cards(cards_shuffled,8)
    player_cards = take_cards(cards_shuffled,8)

    #This is where all cards played by computer and player will be stored in the game
    #By default there must a card placed on the pool 
    first_card = random.sample(cards_shuffled,k=1)
    pool = [first_card]
    cards_shuffled.remove(first_card[0])
    print(f"First card placed {first_card}")

    print("Welcome to my crazy eight game Enjoy:)")
    print("Below is the option menu where you can see your cards, the cards at the pool , play a card or exit the game.")
    homepage_menu()

    print(f"Computer played {play_card_computer(computer_cards,pool)}")
    print(f"You played {play_card_player(player_cards,pool)}")
        
        

if __name__ == "__main__":
    main()


