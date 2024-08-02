import time
from crazy_eight_game import deck_of_cards ,add_card_to_pool, \
pick_a_card, perform_magic_of_card, magic_card, play_card_computer, play_card_computer, \
take_cards,shuffle_card_deck, deck_of_cards, play_card_player

def main():
    #Get all cards and shuffle them
    all_cards_unshuffled = deck_of_cards()
    cards_shuffled = shuffle_card_deck(all_cards_unshuffled)

    #Game starts with assigning 8 cards to computer and player
    computer_cards = take_cards(cards_shuffled,8)
    player_cards = take_cards(cards_shuffled,8)

    #This is where all cards played by computer and player will be stored in the game
    #By default there must a card placed on the pool 
    first_card = cards_shuffled[-1]
    pool = [first_card]
    cards_shuffled.remove(first_card)
    print(f"First card placed {first_card}")
    print()

    print("Welcome to my crazy eight game Enjoy:)")
    print("Below is the option menu where you can see your cards, the cards at the pool , play a card or exit the game.")
    print()

    while len(cards_shuffled) != 1:
        #All cards in pool will be displayed to guide the player in making their move
        print(pool)

        #Before card is official played l  must check for functions which will output None
        #This is an indication that the player or bot cant play a valid card
        playable_computer_card = play_card_computer(computer_cards,pool)

        #First checcks if computer card is a magic card
        if magic_card(playable_computer_card) == True:
            #TODO : Perform specific card magic based on card
            perform_magic_of_card(playable_computer_card, computer_card_deck=computer_cards, player_card_deck=player_cards)

        elif playable_computer_card != None:
            #Add card to pool
            print(f"Computer has {len(computer_cards)} left watch out")
            add_card_to_pool(card=playable_computer_card, pool=pool, player_card_deck=computer_cards)
        
        elif playable_computer_card == None:
            time.sleep(4)
            print("Computer picked a card due to no valid cards")
            pick_a_card(computer_cards, cards_shuffled)
        
        playable_player_card = play_card_player(player_cards, pool)
        if playable_player_card != None:
            #Remove card from deck and add card to pool 
            add_card_to_pool(card=playable_player_card, pool=pool, player_card_deck=player_cards)
        else:
            time.sleep(4)
            pick_a_card(player_cards, cards_shuffled)
            print("Due to no playable cards in your deck.")
            print("You picked a card")
            print()
        

if __name__ == "__main__":\
    main()