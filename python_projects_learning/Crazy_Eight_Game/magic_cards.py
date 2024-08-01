import time
import random
from crazy_eight_game import play_card_computer, pick_a_card, play_card_player

#Returns true if card played is a magic card otherwise None
def magic_card(card):
    magic_cards = ["1","2","7","8","J"]
    for number in magic_cards:
        if number in card:
            return True
    else:
        return None
    
def perform_magic_of_card(card : str,computer_card_deck :list ,player_card_deck : list, pool : list, card_deck : list):
    magic_cards = ["1","2","7","8","J"]

    #When 1 or Ace is played any card must be placed on pool
    if "1" in card:
        for computer_card in computer_card_deck:
            if computer_card == card:
                #Moves card from deck to pool
                pool.append(card)
                computer_card_deck.remove(card)

                #Next is for the other player to play any card
                play_any_card_player_magic(player_card_deck=player_card_deck, pool=pool)

        for my_card in player_card_deck:
            if my_card == card:
                pool.append(card)
                player_card_deck.remove(card)

                #Computer must play any card
                play_any_card_computer_magic(computer_card_deck=computer_card_deck, pool=pool)
            
    elif "2" in card:
        #If a player plays any with on it then the opponent must pick two cards from card_deck
        for computer_card in computer_card_deck:
            if computer_card == card:
                #Takes two cards from deck and adds to player deck of cards
                take_two_cards = card_deck[-2]
                print("You took 2 cards from deck.")
                player_card_deck.append(take_two_cards)
            
        for my_card in player_card_deck:
            if my_card == card:
                take_two_cards = card_deck[-2]
                print("Computer took 2 cards from deck.")
                computer_card_deck.append(take_two_cards)

    elif "7" in card:
        for computer_card in computer_card_deck:
            if computer_card == card:
                #If 7 played then the opponent move is skipped and computer must play again
                card_picked = play_card_computer(computer_cards=computer_card_deck, pool=pool)

                if card_picked != None:
                    pool.append(card_picked)
                    print(f"{card_picked} added to pool")
                    computer_card_deck.remove(card)
                else:
                    pick_a_card(computer_or_player_deck=computer_card_deck, card_deck=card_deck)

        for my_card in player_card_deck:
            if my_card == card:
                #If 7 is played by player then computer move is skipped and player must play again
                print("Play again since you played 7.")

                card_picked = play_card_player(player_cards=player_card_deck, pool=pool)

                if card_picked != None:
                    pool.append(card_picked)
                    print(f"{card_picked} added to pool")
                    player_card_deck.remove(card_picked)
                else:
                    pick_a_card(computer_or_player_deck=player_card_deck, card_deck=card_deck)
    elif "8" in card:
        #If 8 is played then player must pick a suit which will determine what card the other player will play
        for computer_card in computer_card_deck:
            if computer_card == card:
                #Computer must pick a suit 
                suits = ["Diamonds","Clubs","Hearts","Spades"]

                suit_picked = random.sample(suits,k=1)

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
                        index_of_card = int(input(f"Pick index of card to play between 0 and {len(player_card_deck) - 1}"))
                        card_picked = player_card_deck[index_of_card]
                        if card_picked in valid_cards_based_on_suit:
                            pool.append(card_picked)
                            player_card_deck.remove(card_picked)
                            
                            return f"{card_picked} successfully added to pool"

                        else:
                            print("The card you picked does not match the suit chosen by Computer")
                            print("Try again")
                            continue
                    except:
                        print("An error occured invalid index, Try again :(")
                        continue
        
        for my_card in player_card_deck:
            if my_card == card:
                #Player must pick a suit which will be determine the card played by 
                suits = ["Diamonds","Clubs","Hearts","Spades"]

                while True:
                    try:
                        picked_suit = int(input("Pick a suit for the computer to play: "))
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
        try:
            index_picked = int(input(f"Pick any number from 0 to {len(player_card_deck)- 1}"))
            print()

            card_picked = play_card_player[index_picked]
            pool.append(card_picked)
            print(f"You played {card_picked}")
            play_card_player.remove(card_picked)

            return True
            
        except:
            print("Invalid index entered try again :(")
            continue

def play_any_card_computer_magic(computer_card_deck, pool):
    print("You played 1 which is a magic card.")
    print()

    #Picks any card from deck and places it on pool
    card_picked = random.sample(computer_card_deck,k=1)

    pool.append(card_picked)
    computer_card_deck.remove(card_picked)

    print(f"Computer played {card_picked}")

    return card_picked
