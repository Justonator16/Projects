import random
import time

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
    
    while True:
        user_input = input("Enter index/position of card you want to play here: ")
        if user_input.isnumeric() == False:
            print("Invalid input enter a valid number try again :(")
            continue

        user_input = int(user_input)
        if user_input < 0 and user_input >= len(player_cards):
            print("Error enter a number according to card indexs provided :(")
            continue
        else:
            break

    if get_card_suit(current_card) in player_cards[user_input]:
        print(f"You played {player_cards[user_input]}")
        return player_cards[user_input]
    elif get_card_number(current_card) in player_cards[user_input]:
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

    #You cant end crazy 8 with a magic card
    magic_cards = ["1","2","7","8"]
    if len(player_card_deck) == 1 and get_card_number(card) not in magic_cards:
        print("We have winner GG")
        print("Hooray")
        quit()

    pool.append(card)
    player_card_deck.remove(card)


#Returns true if card played is a magic card otherwise None
def magic_card(card=None):
    if card == None:
        return None
    
    magic_cards = ["1","2","7","8","J"]
    for number in magic_cards:
        if number == get_card_number(card):
            return True
    return False
    
def perform_magic_of_card(card : str,computer_card_deck :list ,player_card_deck : list, pool : list, card_deck : list):
    magic_cards = ["1","2","7","8","J"]

    #When 1 or Ace is played any card must be placed on pool
    if "1" == get_card_number(card):
        if card in computer_card_deck:
            for computer_card in computer_card_deck:
                if computer_card == card:
                    #Moves card from deck to pool
                    pool.append(card)
                    computer_card_deck.remove(card)

                    #Next is for the other player to play any card
                    play_any_card_player_magic(player_card_deck=player_card_deck, pool=pool)
        else:
            for my_card in player_card_deck:
                if my_card == card:
                    pool.append(card)
                    player_card_deck.remove(card)

                    #Computer must play any card
                    play_any_card_computer_magic(computer_card_deck=computer_card_deck, pool=pool)
            
    elif "2" == get_card_number(card):
        #If a player plays any with on it then the opponent must pick two cards from card_deck
        if card in computer_card_deck:
            for computer_card in computer_card_deck:
                if computer_card == card:
                    pool.append(card)
                    computer_card_deck.remove(card)

                    #Takes two cards from deck and adds to player deck of cards
                    take_two_cards = card_deck[-2]
                    print("Computer played a magic card 2 . When this card is played the opponent has to pick two cards from deck")
                    print("You took 2 cards from deck.")
                    print()
                    player_card_deck.append(take_two_cards)
        else:
            for my_card in player_card_deck:
                if my_card == card:
                    pool.append(card)
                    player_card_deck.remove(card)

                    take_two_cards = card_deck[-2]
                    print("Computer played a magic card 2 . When this card is played the opponent has to pick two cards from deck")
                    print("Computer took 2 cards from deck.")
                    print()
                    computer_card_deck.append(take_two_cards)

    elif "7" == get_card_number(card):
        if card in computer_card_deck:
            for computer_card in computer_card_deck:
                if computer_card == card:
                    #If 7 played then the opponent move is skipped and computer must play again
                    card_picked = play_card_computer(computer_cards=computer_card_deck, pool=pool)

                    if card_picked != None:
                        pool.append(card_picked)
                        print("Special card 7 played by computer meaning computer can play again ")
                        print(f"Computer played again ,{card_picked} added to pool")
                        print()
                        print(pool)
                        computer_card_deck.remove(card)
                    else:
                        pick_a_card(computer_or_player_deck=computer_card_deck, card_deck=card_deck)

        else:
            for my_card in player_card_deck:
                if my_card == card:
                    #If 7 is played by player then computer move is skipped and player must play again
                    print("You played a magic card 7")
                    print("Play Again")

                    card_picked = play_card_player(player_cards=player_card_deck, pool=pool)

                    if card_picked != None:
                        pool.append(card_picked)
                        print(f"{card_picked} added to pool")
                        print(pool)
                        print()
                        player_card_deck.remove(card_picked)
                    else:
                        pick_a_card(computer_or_player_deck=player_card_deck, card_deck=card_deck)

    elif "8" == get_card_number(card):
        #If 8 is played then player must pick a suit which will determine what card the other player will play
        if card in computer_card_deck:
            for computer_card in computer_card_deck:
                if computer_card == card:

                    print("Computer played magic card 8")
                    #Computer must pick a suit 
                    suits = ["Diamonds","Clubs","Hearts","Spades"]
                    
                    #Sample method returns a list so its best l get the item in that list to aviod errors
                    suit_picked = random.sample(suits,k=1)
                    suit_picked = suit_picked[0]
                    print(f"You must play a card with suit {suit_picked}")

                    #Player must play a card based on suit chosen by computer
                    valid_cards_based_on_suit = []
                    for possible_card in player_card_deck:
                        if suit_picked in possible_card:
                            valid_cards_based_on_suit.append(possible_card)
                    
                    if valid_cards_based_on_suit == None:
                        pick_a_card(computer_or_player_deck=player_card_deck, card_deck=card_deck)
                        time.sleep(4)
                        print("Due to no playable cards in your deck , you picked a card")
                        return None

                    #Player must play a card in valid cards
                    while True:
                        try:
                            #Prints player card deck
                            for index_of_card in range(len(player_card_deck)):
                                print(f"{index_of_card} - {player_card_deck[index_of_card]}")

                            index_of_card = int(input(f"Pick index of card to play between 0 and {len(player_card_deck) - 1} : "))
                            card_picked = player_card_deck[index_of_card]
                            if card_picked in valid_cards_based_on_suit:
                                pool.append(card_picked)
                                print()
                                print(pool)
                                player_card_deck.remove(card_picked)
                                
                                return f"{card_picked} successfully added to pool"

                            else:
                                print("The card you picked does not match the suit chosen by Computer")
                                print("Try again")
                                continue
                        except:
                            print("An error occured invalid index, Try again :(")
                            continue
        else:
            for my_card in player_card_deck:
                if my_card == card:
                    #Player must pick a suit which will be determine the card played by 
                    print("You played a magic card 8")
                    print("You can change the current suit to be played by the computer")
                    print()
                    suits = ["Diamonds","Clubs","Hearts","Spades"]

                    for index_of_suit in range(len(suits)):
                        print(f"{index_of_suit} - {suits[index_of_suit]}")

                    while True:
                        try:
                            picked_suit = int(input("Pick a suit index for the computer to play: "))
                            valid_cards_based_on_suit = []

                            for computer_card in computer_card_deck:
                                if picked_suit in computer_card :
                                    valid_cards_based_on_suit.append(computer_card)

                            if valid_cards_based_on_suit == []:
                                pick_a_card(computer_or_player_deck=computer_card_deck, card_deck=card_deck)
                                print("Computer picked a card due to no playable cards")
                                return None
                            
                            #From valid cards pick a card to play
                            card_picked = random.sample(valid_cards_based_on_suit, k=1)

                            pool.append(card_picked)
                            print(f"Computer played {card_picked}")
                            player_card_deck.remove(card_picked)

                            return None
                        except:
                            print("Invalid index for suit entered")
                            continue
        
def play_any_card_player_magic(player_card_deck : list, pool : list):
    print("Computer played a magic card 1/Ace on the board")
    
    for index in range(len(player_card_deck)):
        print(f"{index} - {player_card_deck[index]}")

    while True:
        index_picked = input("Pick any index of card to play: ")

        if index_picked.isalnum() == False:
            print("Invalid index entered (enter only numbers) try again :(")
            continue
        print()

        #Makes str into int
        index_picked = int(index_picked)

        if index_picked not in range(len(player_card_deck)):
            print(f"Index is out of range {range(len(player_card_deck))}")
            continue

        card_picked = player_card_deck[index_picked]

        pool.append(card_picked)
        print(f"You played {card_picked}")
        player_card_deck.remove(card_picked)

        return True
        

def play_any_card_computer_magic(computer_card_deck, pool):
    print("You played 1 which is a magic card.")

    #Picks any card from deck and places it on pool
    card_picked = random.sample(computer_card_deck,k=1)

    pool.append(card_picked)
    computer_card_deck.remove(card_picked)

    print(f"Computer played {card_picked}")

    return card_picked



