import random
import time

print("Welcome to my Deal or No Deal Game.")
print("The basic rules of the original deal or no deal apply.")
print("Except we not dealing with real money here , just a friendly game to try your luck.")
print("This is a simulation of the pressure you might fell in the real game show :)")
print("Enjoy")
print()

box_text = "Box_Number "
boxes = [ box_text + str(number) for number in range(1,21)]

amounts_in_boxes = ["1" ,"5" ,"10" ,"50" ,"100" ,"250" ,"500" ,"750" ,"1_000"
                    ,"2_500" ,"5_000" ,"7_500" ,"10_000" ,"20_000" ,"30_000"
                    ,"40_000" ,"50_000" ,"100_000" ,"150_000" ,"250_000"]

#Returns a randomly sorted list of amounts available
def shuffle_amounts(amounts_unshuffled : list):
    amounts_shuffled = random.sample(amounts_unshuffled,k=len(amounts_unshuffled))

    return amounts_shuffled

#Next part is to allocate the amounts randomly to each box
def pair_amounts_with_box_numbers(amounts_shuffled : list, box_numbers : list):
    #Create a key value pair of box number and respective amounts
    number_box_pair = {}

    for index_amount in range(len(amounts_shuffled)):
        for index_box_number in range(len(box_numbers)):
            if index_amount == index_box_number:
                number_box_pair[index_box_number+1] = amounts_shuffled[index_amount]

    return number_box_pair

#Returns all available amounts that have not been removed from money tree
def display_amounts(amounts_not_picked: dict):
    print("The following are the available amounts")
    amounts = list(amounts_not_picked.values())

    for amount in amounts:
        #Odd index will be left aligned
        if amounts.index(amount) % 2 != 0:
            print(amount, end="               ")
        #Even indexes will be right aligned
        if amounts.index(amount) % 2 == 0:
            print(amount)
    print()


    print("Box numbers avaiable: ")
    box_numbers = list(amounts_not_picked.keys())
    for number in box_numbers:
        #Odd index will be left aligned
        if box_numbers.index(number) % 2 != 0:
            print(number, end="               ")
        #Even indexes will be right aligned
        if box_numbers.index(number) % 2 == 0:
            print(number)
    print()

def pick_a_box(money_tree: dict, box_player_picked : dict):
    while True:
        number_picked_by_player = input("Pick a box number which you think has the amount you want: ")

        #Checks if user input is a number
        if number_picked_by_player.isalnum() == False:
            print("Error invalid input, Enter only numbers.")
            continue
            
        #Connvert user input to an interger
        number_picked_by_player = int(number_picked_by_player)

        if number_picked_by_player > 20 or number_picked_by_player <= 0:
            print("Error enter a number between 1 and 20")
            continue

        available_box_numbers = money_tree.keys()
        if number_picked_by_player not in available_box_numbers:
            print("The number you picked has been already removed from the money tree.")
            print("Try again")
            continue

        box_amount_pair_picked = {number_picked_by_player : money_tree[number_picked_by_player]}

        print(f"You picked Box Number {number_picked_by_player} ")
        print(f"You picked  {number_picked_by_player} has been removed from money tree.")
        print()
        
        #Move box_number_money_pair picked to the removed boxes list
        money_tree.pop(number_picked_by_player)

        return True
        
#This function asks player which box they will like to remove from the money trees
def remove_box_player(money_tree: dict, boxes_removed : dict, round : int):
    while True:
        number_picked_by_player = input("Enter a number to remove the amounts in the money tree: ")

        #Checks if user input is a number
        if number_picked_by_player.isalnum() == False:
            print("Error invalid input, Enter only numbers.")
            continue
        
        #Connvert user input to an interger
        number_picked_by_player = int(number_picked_by_player)

        if number_picked_by_player > 20 or number_picked_by_player <= 0:
            print("Error enter a number between 1 and 20")
            continue

        available_box_numbers = money_tree.keys()
        if number_picked_by_player not in available_box_numbers:
            print("The number you picked has been already removed from the money tree.")
            print("Try again")
            continue

        box_amount_pair_picked = {number_picked_by_player : money_tree[number_picked_by_player]}

        print(f"(Round {round}) Your Box Number {number_picked_by_player} has R{money_tree[number_picked_by_player]}")
        print(f"Box number {number_picked_by_player} has been removed from money tree.")
        time.sleep(5)
        print()
        
        #Move box_number_money_pair picked to the removed boxes list
        money_tree.pop(number_picked_by_player)
        boxes_removed.update(box_amount_pair_picked)

        return True


def round_1(money_tree: dict, boxes_removed : dict, box_amount_pairs : dict, round : int):
    #Round 1 - Remove 6 boxes and offer an amount
    for i in range(6):
        display_amounts(box_amount_pairs)
        remove_box_player(money_tree=box_amount_pairs, boxes_removed=boxes_removed, round=round)

def round_2(money_tree: dict, boxes_removed : dict, box_amount_pairs, round : int):
    #Round 2 -  Remove 5 boxes and offer an amount
    for i in range(5):
        display_amounts(box_amount_pairs)
        remove_box_player(money_tree=box_amount_pairs, boxes_removed=boxes_removed, round=round)

def round_3(money_tree: dict, boxes_removed : dict, box_amount_pairs, round : int):
    #Round 3 - Removes 4 boxes and offer an amount
    for i in range(4):
        display_amounts(box_amount_pairs)
        remove_box_player(money_tree=box_amount_pairs, boxes_removed=boxes_removed, round=round)

def round_4(money_tree: dict, boxes_removed : dict, box_amount_pairs, round : int):
    #Round 4 - Removes 3 boxes and offer an amount
    for i in range(3):
        display_amounts(box_amount_pairs)
        remove_box_player(money_tree=box_amount_pairs, boxes_removed=boxes_removed, round=round)

def round_5(money_tree: dict, boxes_removed : dict, box_amount_pairs, round : int):
    #Round 5 - Removes 2 boxes and final offer
    for i in range(3):
        display_amounts(box_amount_pairs)
        remove_box_player(money_tree=box_amount_pairs, boxes_removed=boxes_removed, round=round)

def round_6(money_tree: dict, boxes_removed : dict, box_amount_pairs, round : int):
    #Round 6 - Player must final box 
    for i in range(2):
        display_amounts(box_amount_pairs)
        remove_box_player(money_tree=box_amount_pairs, boxes_removed=boxes_removed, round=round)


def main():
    randomly_sorted_amounts = shuffle_amounts(amounts_unshuffled=amounts_in_boxes)
    box_amount_pairs = pair_amounts_with_box_numbers(amounts_shuffled=randomly_sorted_amounts, box_numbers=boxes)

    #Store the removed boxes in separate list called removed_boxes
    boxes_removed = {}

    #This is box which the player will keep until round 6 if he doesnt accept bankers offer
    box_player_picked = {}

    round = 0
    
    while True:
        #First of all player must pick a box which he thinks has the amount he wants before removing other boxes
        if round == 0:
            print("First things first, pick a box you think has the amount you want. ")
            display_amounts(box_amount_pairs)
            pick_a_box(money_tree=box_amount_pairs , box_player_picked=box_player_picked)
            round += 1
            continue
        elif round == 1:
            print("We are in Round 1 right now elimate 6 boxes")
            display_amounts(box_amount_pairs)
            round_1(money_tree=box_amount_pairs, boxes_removed=boxes_removed, box_amount_pairs=box_amount_pairs, round=round )
            round += 1
            continue
        elif round == 2:
            print("Round 2 eliminate 5 more boxes")
            display_amounts(box_amount_pairs)
            round_2(money_tree=box_amount_pairs, boxes_removed=boxes_removed, box_amount_pairs=box_amount_pairs, round=round )
            round += 1
            continue
        elif round == 3:
            print("Round 3 remove 4 more boxes from the money tree")
            display_amounts(box_amount_pairs)
            round_3(money_tree=box_amount_pairs, boxes_removed=boxes_removed, box_amount_pairs=box_amount_pairs, round=round )
            round += 1
            continue
        elif round == 4:
            print("Round 4 eliminate 3 more boxes")
            display_amounts(box_amount_pairs)
            round_4(money_tree=box_amount_pairs, boxes_removed=boxes_removed, box_amount_pairs=box_amount_pairs, round=round )
            round += 1
            continue
        else:
            #Final round
            print("Round 5 eliminate 1 more box")
            print("Here you have choice to exchange your box with the reamining box")
            print("Or remove the last box remaining in the money tree")
            display_amounts(box_amount_pairs)
            round_5(money_tree=box_amount_pairs, boxes_removed=boxes_removed, box_amount_pairs=box_amount_pairs, round=round )
            
            #If player refued all offers from banker up to this point
            print(f"Lets what is in your box number {box_player_picked.keys}")
            print(f"Theres an amount of {box_player_picked.values()} in your box ")
            break


if __name__ == "__main__":
    try:    
        main()
    except KeyboardInterrupt:
            print()
            print("Thanks for playing Deal or No Deal .")
            print("Goodbye")
            quit()


