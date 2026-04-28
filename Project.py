import time
import doctest

def print_board(board) -> None:
    """
        Takes a 2d list of the board, prints the board

        Args:
            board(list): the 2d list of the boards state

        Returns:
            None
        
        Tests:
            >>> print_board([[" "," "," "],[" "," "," "],[" "," "," "]])
               |   |   
            ---+---+---
               |   |   
            ---+---+---
               |   |   

            >>> print_board([["X","O","O"],["X","O","X"],["O","X","X"]])
             X | O | O 
            ---+---+---
             X | O | X 
            ---+---+---
             O | X | X 
            
            >>> print_board([["X"," ","O"],["X","O","X"],["O","X"," "]])
             X |   | O 
            ---+---+---
             X | O | X 
            ---+---+---
             O | X |   
    """

    count = 0

    #prints the board each row at a time, count is so that there are only 2 horizontal lines printed
    for row in board:
        print(f" {row[0]} | {row[1]} | {row[2]} ")
        if count < 2:
            print("---+---+---")

        count += 1





def clear_board():
    """
        Clears the board by printing 20 empty lines

        Args:
            None
        
        Returns:
            None
    """

    #prints new line 20 times
    for i in range(20):
        print("\n")





def check_winner(board: list, player: str) -> bool:
    """
        Takes a 2d list of the board and the current player and determine if the player won

        Args:
            board(list): the 2d list of the boards state
            player(str): the current player

        Returns:
            (bool): True if the player won, False if the player has not won
        
        Tests:
            >>> check_winner([[" "," "," "],[" "," "," "],[" "," "," "]], "O")
            False
            >>> check_winner([["X"," "," "],[" "," "," "],[" "," "," "]], "X")
            False
            >>> check_winner([["X"," "," "],[" ","O"," "],[" "," "," "]], "O")
            False
            >>> check_winner([["X"," "," "],[" ","O"," "],[" "," ","X"]], "X")
            False
            >>> check_winner([["X"," "," "],[" ","O"," "],["O"," ","X"]], "O")
            False
            >>> check_winner([["X"," ","X"],[" ","O"," "],["O"," ","X"]], "X")
            False
            >>> check_winner([["X","O","X"],[" ","O"," "],["O"," ","X"]], "O")
            False
            >>> check_winner([["X","O","X"],[" ","O","X"],["O"," ","X"]], "X")
            True
            >>> check_winner([["X","O","O"],["X","O","X"],["O","X","X"]], "X")
            False
            >>> check_winner([["X","O","O"],["X","O","X"],["O","X","X"]], "O")
            True
            >>> check_winner([["O","O","O"],[" "," "," "],[" "," "," "]], "O")
            True
            >>> check_winner([["O","X","O"],[" "," "," "],[" "," "," "]], "O")
            False
            >>> check_winner([[" "," "," "],["O","O","O"],[" "," "," "]], "O")
            True
            >>> check_winner([[" "," "," "],[" "," "," "],["O","O","O"]], "O")
            True
            >>> check_winner([["O"," "," "],["O"," "," "],["O"," "," "]], "O")
            True
            >>> check_winner([[" ","O"," "],[" ","O"," "],[" ","O"," "]], "O")
            True
            >>> check_winner([[" "," ","O"],[" "," ","O"],[" "," ","O"]], "O")
            True
            >>> check_winner([["O"," "," "],[" ","O"," "],[" "," ","O"]], "O")
            True
            >>> check_winner([[" "," ","O"],[" ","O"," "],["O"," "," "]], "O")
            True

    """

    #checks each row:
    for row in board:
        if row[0] == row[1] == row[2] == player:
            return True
        
    #checks each column:
    for column in range(len(board)):
        if board[0][column] == board[1][column] == board[2][column] == player:
            return True
        
    #check diagonals:
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    
    #No winner, returns False
    return False





def is_draw(board: list) -> bool:
    """
        Determines if the game is a draw, does not check if there is a winner

        Args:
            board(list): the 2d list of the boards state

        Returns:
            (bool) -> True if game is draw, false if game is not a draw

        Tests:
            >>> is_draw([[" "," "," "],[" "," "," "],[" "," "," "]])
            False
            >>> is_draw([["X","X"," "],["X"," ","X"],[" ","X","X"]])
            False
            >>> is_draw([["X","X","X"],["X","X","X"],["X","X","X"]])
            True
            >>> is_draw([["X","O","O"],["O","X","X"],["X","X","O"]])
            True
            >>> is_draw([["X","X","O"],["O","O","X"],["X","O","X"]])
            True
            >>> is_draw([["X","X","O"],["O","O","X"],["X","X","O"]])
            True
            >>> is_draw([["X","X","X"],["O","O"," "],[" "," "," "]])
            False

    """

    #checks if there is any empty space in the board
    if " " in board[0] or " " in board[1] or " " in board[2]:
        return False

    else:
        return True





def play_game(board: list, current_player: str = "X") -> str:
    """
        The main function, gets the input from the player, and sets the state of the board

        Args:
            board(list): the 2d list of the boards state
            current_player(str): the starting player, default value is player "X"

        Returns:
            (str): the winner of the game, or "-" if it was a draw
    """

    #the main while loop, gets input, sets state, and determines winner
    while not is_draw(board):
        players_input = get_input(board)
        board[players_input[0]][players_input[1]] = current_player

        print_board(board)
        if check_winner(board, current_player):
            return current_player
        
        current_player = switch_players(current_player)
        
    return "-"
        




def winner():
    """
        Initializes and ends the game

        Args:
            None

        Returns:
            None
    """

    #initializes the game
    board: list = [[" "," "," "],[" "," "," "],[" "," "," "]]
    rules(board)
    print_board(board)


    #gets the winner of the game, then prints a draw if its a draw, or the winner
    winning_player = play_game(board)

    if winning_player == "-":
        print("It is a draw!\nNo one wins!")
    
    else:
        print(f"The winner is {winning_player}!")





def switch_players(player: str) -> str:
    """
        Inverts the current player, for switching sides

        Args:
            player(str): the current player

        Returns:
            (str): the other player

        Tests:
            >>> switch_players("X")
            'O'

            >>> switch_players("O")
            'X'
    """

    #inverts the current player
    if player == "X":
        return "O"
    else:
        return "X"





def get_input(board: list) -> list:
    """
        Gets the positional input from the player, which determines where to place the X or the O

        Args:
            board(list): the 2d list of the boards state

        Returns:
            (list): the position of where the player wants to input
    """

    #initial input
    CONSTANT_TIME = 2
    players_input = input("Please input your row and column: ")


    #While the players input is not valid, it repeats
    while not verify_move(board, players_input):
        print("\nPlease input a valid answer")
        time.sleep(CONSTANT_TIME)
        print("\nWhen inputing moves, input in form 'N,M' where N and M are integers\n")
        time.sleep(CONSTANT_TIME)
        print("Where N represents the row,\n0 is the top row, 2 is the bottom row\n")
        time.sleep(CONSTANT_TIME)
        print("And M represents the column,\n0 is the left column, 2 is the right column\n")


        players_input = input("Please input your row and column: ")


    #turns string into list with integers after being verified
    players_input = players_input.split(",")
    players_input[0] = int(players_input[0])
    players_input[1] = int(players_input[1])

    clear_board()
    return players_input





def verify_move(board: list, input_value: str) -> bool:
    """
        Determines if the players input is valid

        Args:
            board(list): the 2d list of the boards state
            input_value(str): the value being tested as valid

        Returns:
            (bool): True if input is valid, false otherwise

        Tests:
            >>> verify_move([[" "," "," "],[" "," "," "],[" "," "," "]], 'One,Two')
            False
            >>> verify_move([[" "," "," "],[" "," "," "],[" "," "," "]], 'blanks')
            False
            >>> verify_move([[" "," "," "],[" "," "," "],[" "," "," "]], '0,sdf')
            False
            >>> verify_move([[" "," "," "],[" "," "," "],[" "," "," "]], '{}/,1')
            False
            >>> verify_move([[" "," "," "],[" "," "," "],[" "," "," "]], '1,1,1')
            False
            >>> verify_move([[" "," "," "],[" "," "," "],[" "," "," "]], '1')
            False
            >>> verify_move([[" "," "," "],[" "," "," "],[" "," "," "]], ',,,')
            False
            >>> verify_move([[" "," "," "],[" "," "," "],[" "," "," "]], ',')
            False
            >>> verify_move([[" "," "," "],[" "," "," "],[" "," "," "]], '1,1')
            True
            >>> verify_move([[" "," "," "],[" ","X"," "],[" "," "," "]], '1,1')
            False
    """

    #checks to see if the player inputed 2 integers seperated by a comma
    try:
        input_value = input_value.split(",")
        if 0 <= int(input_value[0]) <= 2 and 0 <= int(input_value[1]) <= 2 and len(input_value) == 2:
            if board[int(input_value[0])][int(input_value[1])] == " ":
                return True
    except:
        return False
    return False
    




def rules(board: list):
    """
        Prints the rules of the game

        Args:
            board(list): the 2d list of the boards state

        Returns:
            None

        Tests:
            >>> rules([[" "," "," "],[" "," "," "],[" "," "," "]]) 
            Welcome to Tic-Tac-Toe!
            The aim of the game is to get 3 of your symbols in a row
            Shown below is the board with nothing in it
            <BLANKLINE>
               |   |   
            ---+---+---
               |   |   
            ---+---+---
               |   |   
            <BLANKLINE>
            When inputing moves, input in form '0,0'
            <BLANKLINE>
            Where the first integer represents the row,
            0 is the top row, 2 is the bottom row
            <BLANKLINE>
            The second integer represents the column,
            0 is the left column, 2 is the right column
            <BLANKLINE>
            Good Luck!
    """

    #A constant for the amount of time between prints, then prints the rules
    CONSTANT_TIME = 3

    print("Welcome to Tic-Tac-Toe!")
    time.sleep(CONSTANT_TIME)
    print("The aim of the game is to get 3 of your symbols in a row")
    time.sleep(CONSTANT_TIME)
    print("Shown below is the board with nothing in it\n")
    time.sleep(CONSTANT_TIME)
    print_board(board)
    time.sleep(CONSTANT_TIME)
    print("\nWhen inputing moves, input in form 'N,M' where N and M are integers\n")
    time.sleep(CONSTANT_TIME)
    print("Where N represents the row,\n0 is the top row, 2 is the bottom row\n")
    time.sleep(CONSTANT_TIME)
    print("And M represents the column,\n0 is the left column, 2 is the right column\n")
    time.sleep(CONSTANT_TIME)
    print("Good Luck!\n\n")





def main():
    #doctest.testmod(verbose=True)
    winner()

if __name__ == "__main__":
    main()
