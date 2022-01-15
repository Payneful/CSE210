# 1. Name:
#      Bradley Payne
# 2. Assignment Name:
#      Lab 01: Tic-Tac-Toe
# 3. Assignment Description:
#      Play the game of Tic-Tac-Toe
# 4. What was the hardest part? Be as specific as possible.
#      It went pretty good till I hit the write to json part.
#      I did not see that what I was trying to send was a list.
#      This was what slowed me down the most.
# 5. How long did it take for you to complete the assignment?
#      3 hours

import json
import os

# The characters used in the Tic-Tac-Too board
X = 'X'
O = 'O'
Blank = ' '

# A blank Tic-Tac-Toe board
blank_board = {
            "board": [
                Blank, Blank, Blank,
                Blank, Blank, Blank,
                Blank, Blank, Blank ]
        }


def main():
    # The file read code, game loop code, and file close code goes here
    replay = "y"

    while replay == "y":

        message = True
        filename = ("tictactoe/Board.json")
        board = read_board(filename)

        clear_screen()
        play_game(board, blank_board, filename)
        game = game_done(board)
        if game == True:
            while replay != "y" or replay != "n":
                replay = input("Play again? (y/n) ").lower()
        else:
            print("Your game was saved.")
            replay = "n"

def clear_screen():
    # Clears the terminal
    os.system('cls' if os.name=='nt' else 'clear')

def read_board(filename):
    # Read the previously existing board from the file if it exists
    with open(filename) as f:
        previous_board = json.load(f)
        f.close()
    return previous_board["board"]

def save_board(filename, board):
    # Save the current game to a file.
    with open(filename, 'w') as f:
        save = {
        "board": board
        }
        json.dump(save, f)
        # could do board_json = json.dumps(board) then file.write(board_json)
        f.close()

def display_board(board):
    # Display a Tic-Tac-Toe board on the screen in a user-friendly way
    for i in range(0,3):
        if i == 1:
                print("---------------------------------------------")
        for j in range(0,3):
            print(f"  {board[i][j]}  | {board[i][j + 1]} | {board[i][j + 2]}   |   {board[i + 1][j]} | {board[i + 1][j + 1]} | {board[i + 1][j + 2]}   |   {board[i + 2][j]} | {board[i + 2][j + 1]} | {board[i + 2][j + 2]}")
            if j == 0 or j == 1:
                print("  ---+---+---  |  ---+---+---  |  ---+---+---")
        if i == 1:
            print("---------------------------------------------")
    
def is_x_turn(board):
    # Determine whose if its X or O's turn
    turn = board.count("X")
    if board.count("O") == turn:
        return "X"
    else:
        return "O"

def game_done(board, message=True):
    # Game is finished if all the squares are filled
    tie = True
    for square in board:
        if square == Blank:
            tie = False
    if tie:
        if message:
            print("The game is a tie!\n")
        return True

    # Game is finished if someone has completed a row
    for row in range(3):
        if board[row * 3] != Blank and board[row * 3] == board[row * 3 + 1] == board[row * 3 + 2]:
            if message:
                clear_screen()
                print("The game was won by", board[row * 3],"\n")
            return True

    # Game is finished if someone has completed a column
    for col in range(3):
        if board[col] != Blank and board[col] == board[3 + col] == board[6 + col]:
            if message:
                clear_screen()
                print("The game was won by", board[col],"\n")
            return True

    # Game is finished if someone has a diagonal
    if board[4] != Blank and (board[0] == board[4] == board[8] or
                              board[2] == board[4] == board[6]):
        if message:
            clear_screen()
            print("The game was won by", board[4],"\n")
        return True
    return False

def guide():
    # Shows the information for the board locations and save command
    print("Enter 'q' to suspend your game. Otherwise, enter a number from 1 to 9\n"
          "where the following numbers correspond to the locations on the grid:\n"
          " 1 | 2 | 3 \n"
          "---+---+---\n"
          " 4 | 5 | 6 \n"
          "---+---+---\n"
          " 7 | 8 | 9 \n"
          "The current board is:")

def play_game(board, blank_board, filename):
    # Put game play code here. Return False when the user has indicated they are done
    
    while game_done(board) == False:
        '''Loop to check who's turn it is and check perameters of number.'''
        '''save the board if input is q if not it places the piece.'''
        clear_screen()
        guide()
        display_board(board)
        
        turn = is_x_turn(board)
        forward = False
        
        while forward == False:
            num_input = input(f"{turn}> ")
            if num_input == "q":
                save_board(filename, board)
                return False
            num_input = int(num_input)
            if  num_input > 0 and num_input < 10:
                if board[num_input - 1] == " ":
                    forward = True
        
        location = num_input - 1
        board[location] = (f"{turn}")

        display_board(board)

        if game_done(board):
            reset(blank_board, filename)
    
    return False
      
def reset(blank_board, filename):
    # Resets the board in the json with a blank board.
    with open(filename, 'w') as f:
        json.dumps(blank_board)
        json.dump(blank_board, f)
        f.close()
        
if __name__ == "__main__":
    main()