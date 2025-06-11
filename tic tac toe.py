import math
 
 
def end_game():
    restart = input("Do you want to play again?:")
    if restart.lower() == "yes":
        game(0)
    elif restart.lower() == "no":
        quit()
    else:
        print("What was that again? PLease type Yes no No")
        end_game()
    quit()  # End's the game if someone wins
 
 
def build_board(board):
    for x in range(3):
        print(board[x][0], " | ", board[x][1], " | ", board[x][2])
        if x < 2:
            print("-------------")  # Function to build board
 
 
def check_win(board, is_tie):
    print(is_tie)
    for x in range(3):
        c = 0
        d = 0
        for y in range(2):
            if board[x][y] == board[x][y + 1] and board[x][y + 1] == "X" and board[x][y] != " " or board[y][x] == \
                    board[y + 1][x] and board[y][x] \
                    != " " and board[y + 1][x] == "X":
                c = c + 1
                if c == 2:
                    print("X wins")
                    end_game()
            if board[x][y] == board[x][y + 1] and board[x][y + 1] == "O" and board[x][y] != " " or board[y][x] == \
                    board[y + 1][x] and board[y][x] \
                    != " " and board[y + 1][x] == "O":
                d = d + 1
                if d == 2:
                    print("O wins")
                    end_game()
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[1][1] != " " or board[0][2] == board[1][1] \
            and board[1][1] == board[2][0] and board[1][1] != " ":
        print(board[1][1], " Wins!")  # Checks if won by diagonal
        end_game()
    if is_tie == 9:
        print("Cat's game")  # Checks if Cat's Game
        end_game()
 
 
def who_turn_now(is_tie):
    if is_tie % 2 == 0:  # Figures out if it is X or O's turn
        return "X"
    else:
        return "O"
 
 
def position_finder(board, is_tie, turn):
    position = input("\n" + str(turn) + "'s Turn" + "\nWhere would you like to go:\n")
    try:
        spot = int(position) - 1
        if board[math.floor(spot / int(3))][spot % int(3)] == " ":
            board[math.floor(spot / int(3))][spot % int(3)] = turn
 
        else:
            print("Please go in a blank spot")
            build_board(board)
            position_finder(board, is_tie, turn)
    except:
        print("Please Type a whole number 1-9")  # Catches Errors
        build_board(board)
        position_finder(board, is_tie, turn)
 
 
def game(is_tie):
    loop = 0  # Helps the game play
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]  # Board 2dArray
    build_board(board)
    while loop != 1:  # Never ending loop
        turn = who_turn_now(is_tie)  # plays the game
        position_finder(board, is_tie, turn)
        is_tie = is_tie + 1
        build_board(board)
        check_win(board, is_tie)
 
 
game(0)  # runs the game