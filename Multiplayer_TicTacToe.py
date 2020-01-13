# TIC TAC TOE
# Author: JAIMIK PATEL
# Date: AUG 16, 2019

#creates board for game
game_board = ["-","-","-",
              "-","-","-",
              "-","-","-"]
player = "X"

valid = None

flipper = False


game_still_going = True
 
def show_board():
    print(game_board[0], " | ", game_board[1], " | ", game_board[2])
    print(game_board[3], " | ", game_board[4], " | ", game_board[5])
    print(game_board[6], " | ", game_board[7], " | ", game_board[8])
    

def main():
    #displays initial board
    show_board() 
    
    while game_still_going:
        handle_player(player)
        check_for_win()
        check_tie()
        flip_player()

    
def handle_player(Xor0):
    
    global flipper
    
    #askes player for number of square
    position = int(input("\nChoose a number between 1-9: "))
    
    #Takes the number and adds it to the appropriate square
    position = position - 1
    
    if game_board[position] == "-":
        game_board[position] = Xor0
        flipper = True
        show_board()
    else:
        print("\nThat spot is taken. Choose again!")
        flipper = False
        
        
    

def check_for_win():
    #check rows
    check_rows()
    
    #checks columns 
    check_columns()
    
    #checks diagonals
    check_diagonals()
    


def check_rows():
    
    global valid
    global game_still_going
    
    #check if any of the rows are matching
    row1 = game_board[0] == game_board[1] == game_board[2] != "-"
    row2 = game_board[3] == game_board[4] == game_board[5] != "-"
    row3 = game_board[6] == game_board[7] == game_board[8] != "-"
    
    rows_lst = [row1,row2,row3]
    for row in rows_lst:
        if row:
            game_still_going = False
            valid = True
            print("The winner is", player)
    return
    
def check_columns():
    
    global valid
    global game_still_going
    
    #check if any of the columns are matching
    column1 = game_board[0] == game_board[3] == game_board[6] != "-"
    column2 = game_board[1] == game_board[4] == game_board[7] != "-"
    column3 = game_board[2] == game_board[5] == game_board[8] != "-"
    
    columns_lst = [column1,column2,column3]
    for column in columns_lst:
        if column:
            game_still_going = False
            valid = True
            print("The winner is", player)
    return
    
    
def check_diagonals():
    
    global valid
    global game_still_going
    
    #check if any of the diagonals are matching
    diag1 = game_board[0] == game_board[4] == game_board[8] != "-"
    diag2 = game_board[2] == game_board[4] == game_board[6] != "-"
    
    diags_lst = [diag1,diag2]
    for diag in diags_lst:
        if diag:
            game_still_going = False
            valid = True
            print("\nThe winner is", player)
    return



def check_tie():
    
    global valid
    global game_still_going
    
    if not valid:
        #for i in range(len(game_board)):
        if game_board[0] != "-" and game_board[1] != "-" and game_board[2] != "-" and game_board[3] != "-" and game_board[4] != "-" and game_board[5] != "-" and game_board[6] != "-" and game_board[7] != "-" and game_board[8] != "-": 
            print("\nTie Game. Play Again!")
            game_still_going = False
    
    return



def flip_player():
    
    global player
    global flipper
    
    # Constantly changes between players after every turn
    while flipper:
        if player == "X":
            player = "0"
        elif player == "0":
            player = "X"
        break;
    return

main()
        
    
    
            

