#Game board
board = ["-","-","-",
        "-","-","-",
        "-","-","-"]

game_still_going = True

winner = None

current_player = "A"

def display_board():
    print(board[0]+"|",board[1] +"|",board[2]+"|")
    print(board[3]+"|",board[4] +"|",board[5]+"|")
    print(board[6]+"|",board[7] +"|",board[8]+"|")

def play_game():
    #display initial board
    display_board()

    

    while game_still_going:
        handle_turn(current_player)
        check_if_game_over()
        flip_player()

    if winner == "A" or winner == "B":
        print(winner + " Won.")
    elif winner == None:
        print("Tie")    


def handle_turn(player):
    print(player + "'s Turn")
    position = input("Choose a number from 1-9: ")

    valid = False
    while not valid:
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input("Invalid number .Choose a number from 1-9: ") 
        position = int(position) -1  

        if board[position] == "-":
            valid = True
        else:    
            print("You can't go there")  
    board[position] = player
    display_board()
      

def check_if_game_over():
    check_win()
    check_if_tie()

    return

def check_win():
    global winner
    #check rows
    row_winner = check_rows()

    #check columns
    column_winner = check_columns()

    #check diagonals
    diagonal_winner = check_diagonals()
    
    #Get the winner
    if row_winner:
        winner = row_winner

    elif column_winner:
        winner = column_winner

    elif diagonal_winner:
        winner = diagonal_winner

    else:
         winner = None   
    return

def check_rows():
    #Set up global variables
    global game_still_going
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_still_going = False
     #return the winner   
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]    
    return

def check_columns():
    #Set up global variables
    global game_still_going

    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"

    
    if col_1 or col_2 or col_3:
        game_still_going = False
     #return the winner   
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[3]
    return

def check_diagonals():
    #Set up global variables
    global game_still_going
    
    Dia_1 = board[0] == board[4] == board[8] != "-"
    Dia_2 = board[2] == board[4] == board[6] != "-"

    
    if Dia_1 or Dia_2:
        game_still_going = False
     #return the winner   
    if Dia_1:
        return board[0]
    elif Dia_2:
        return board[2]
    
    return    

def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False

    return  

def flip_player():
    global current_player 

    if current_player == "A":
        current_player = "B"
    elif current_player == "A":
        current_player = "B"    
    return          
play_game()




