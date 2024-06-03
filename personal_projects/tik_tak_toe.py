from random import randrange, sample

#html branch test 
print("Welcome to my X and O game")
print("This is part of showcase in understanding python essentials with a simple project :)")
                
def computer_move(board):
    board = list(board)
    number_list = [str(i) for i in range(1,10)]
    
    #A key value pair of the numbers in the board and their index in the board
    number_index_pair = {}
    
    for i in range(len(board)):
        for number in number_list:
            if board[i] == number:
                number_index_pair[number] = i
                
    computer_choice = randrange(1,10)
    while True:
        computer_choice = randrange(1,10)
        if str(computer_choice) not in number_index_pair.keys():
            continue
        else:
            break
        
    place_x_here_computer = number_index_pair[str(computer_choice)]
    board[place_x_here_computer] = "X"
    
    return "".join(board)
        
def user_move(board):
    board = list(board)
    number_list = [str(i) for i in range(1,10)]
    
    #A key value pair of the numbers in the board and their index in the board
    number_index_pair = {}
    
    for i in range(len(board)):
        for number in number_list:
            if board[i] == number:
                number_index_pair[number] = i
    
    try:
        user_input = int(input("Enter you move: "))
    except:
        print("Invalid input")
        quit()
        
    if user_input < 1 and user_input >= 10:
        print("Error :( Number must be between 1 and 9")
        quit()
        
    if str(user_input) not in number_index_pair.keys():
        print("Number has been picked by X try again")
        quit()
    
    place_o_here_user = number_index_pair[str(user_input)]
    board[place_o_here_user] = "O"
    
    return "".join(board)

def get_number_indexes(board):
    list_of_number_indexes = []
    number_list = [i for i in range(1,10)]
    
    for i in range(len(board)):
        for number in number_list:
            if str(number) == board[i]:
                list_of_number_indexes.append(i)
    
    return list_of_number_indexes
            

def check_winner(board, list_of_number_indexes):
    board = list(board)
    
    #List of all valid wins possible
    all_possible_wins = [[1,2,3],[4,5,6],[7,8,9] #All horizontal wins possible
                         ,[1,4,7],[2,5,8],[3,6,9] #All vertical wins possible
                         ,[1,5,9],[3,5,7]] #All diagonal wins possible
    #Ths is the same as the all possible wins list but instead of numbers 1- 9there is indexes of the positions where x and o are placed
    all_possible_wins_indexes = []
    
    for win in all_possible_wins:
        wins = []
        for number in win:
            if number == 1:
                wins.append(list_of_number_indexes[0])
            elif number ==2:
                wins.append(list_of_number_indexes[1])
            elif number == 3:
                wins.append(list_of_number_indexes[2])
            elif number == 4:
                wins.append(list_of_number_indexes[3])
            elif number == 5:
                wins.append(list_of_number_indexes[4])
            elif number == 6:
                wins.append(list_of_number_indexes[5])
            elif number == 7:
                wins.append(list_of_number_indexes[6])
            elif number == 8:
                wins.append(list_of_number_indexes[7])
            else:
                wins.append(list_of_number_indexes[8])
        all_possible_wins_indexes.append(wins)
    #Lopks for matches in the board that might be a win
    x_indexes_board = []
    o_indexes_board = []
    possible_win_check_x = []
    possible_win_check_o = []
    
    for i in range(len(board)):
        if board[i] == "X":
            x_indexes_board.append(i)
    
    for i in range(len(board)):
        if board[i] == "O":
            o_indexes_board.append(i)
    
    #Cretaes a list with lists of 3 random selected values from the x_indexes_board
    if len(x_indexes_board) >= 3:
        for i in range(25):
            possible_win_check_x.append(sample(x_indexes_board,3))
    
    if len(o_indexes_board) >= 3:
        for i in range(25):
            possible_win_check_o.append(sample(o_indexes_board,3))
      
    for possible_win in all_possible_wins_indexes:
        for win in possible_win_check_x:
            if possible_win == win:
                return "X won the game"
                break
    
    for possible_win in all_possible_wins_indexes:
        for win in possible_win_check_o:
            if possible_win == win:
                return "O won the game"
                break
    
moves =  0
board = "+-------+-------+-------+\n|       |       |       |\n|   1   |   2   |   3   |\n|       |       |       |\n+-------+-------+-------+\n|       |       |       |\n|   4   |   5   |   6   |\n|       |       |       |\n+-------+-------+-------+\n|       |       |       |\n|   7   |   8   |   9   |\n|       |       |       |\n+-------+-------+-------+"
original_board_number_indexes_list = get_number_indexes(board)


while moves < 9:
    moves += 1
    board = computer_move(board)
    print(board)
    try:
        if "X won the game" in check_winner(board,original_board_number_indexes_list)  :
            print("X is the winner GG")
            break
    except:
        moves += 1
        board = user_move(board)
        try:
            if "O won the game" in check_winner(board,original_board_number_indexes_list) :
                print(board)
                print("O is the winner GG")
                break
        except:
            print(board)
    if moves == 8:
        print("Its a tie")
        break