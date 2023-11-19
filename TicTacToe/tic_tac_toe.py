from copy import deepcopy
import random
from typing import List, Tuple


def print_rules(filename: str) -> None:
    """
    Given the name of a file containing the rules of the game, prints the rules to the console.
    """
    with open(filename) as f:
        rules = f.read()
        print(rules)

def get_player_name() -> str:
    """
    Prompts the user to enter a player name and returns it.
    """
    name = input(f"Enter your name: ")
    return name

def get_random_player(players: Tuple[str]) -> str:
    """
    Given a list of players, returns one of them at random.
    """
    return random.choice(players)

def print_board(board: List[str]) -> None:
    """Prints the current state of the board"""
    print("   |   |")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("___|___|___")
    print("   |   |")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("___|___|___")
    print("   |   |")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("   |   |")

def select_difficulty() -> str:
    """
    Prompts the player to select the difficulty level (easy or hard), and returns the corresponding game mode.
    """
    choice = input("Select the difficulty: easy or hard: ")
    if choice != "easy" and choice != "hard":
        print("Wrong input!")
        return select_difficulty()
    return choice

def get_move(player: str, board: List[str], difficulty: str="easy") -> int:
    """Gets the index of the next user move on the board, for all users and difficulties."""
    
    if player == "computer":
        if difficulty == "easy":
            return get_computer_move(board)
        else:
            return get_best_move(board)
    else:
        return get_user_move(player, board)

def get_user_move(player: str, board: List[str]) -> int:
    """Gets the move from the player"""
    
    user_move = input("Enter your move: (1-9): ")
    if user_move not in ["1","2","3","4","5","6","7","8","9"] :
        print("Wrong input!")
        return get_user_move(player, board)
    
    move = int(user_move) -1
    if board[move] == "X" or board[move] == "O":
        print("The field is already taken")
        return get_user_move(player, board)
    else:
        return move

def get_computer_move(board: List[str]) -> int:
    """Gets random move from the computer"""
    
    available_moves = []
    for i in range(9):
        if board[i] != "X" and board[i] != "O":
            available_moves.append(i)
    return random.choice(available_moves)

def get_best_move(board: List[str]) -> int:
    """Returns the best move for the X player on the board."""
    
    for i in range(9):
        if board[i] != "X" and board[i] != "O":
            tmp = board[i]
            board[i] = "X"
            if check_win(board):
                board[i] = tmp
                return i
            board[i] = tmp

    for i in range(9):
        if board[i] != "X" and board[i] != "O":
            tmp = board[i]
            board[i] = "O"
            if check_win(board):
                board[i] = tmp
                return i
            board[i] = tmp

    if board[4] != "X" and board[4] != "O":
        return 4

    return get_computer_move(board)
        
def update_board(move: int, player: str, board:  List[str]) -> None:
    """Updates the board with the player's move"""

    if player == "computer":
        board[move] = "X"
    else:
        board[move] = "O"
    print(f"{player.capitalize()} played on field {move + 1}.")
    
def switch_player(player: str, players: Tuple[str]) -> str:
    """
    Given the current player and a list of players, returns the next player in the list.
    """
    if player == players[0]:
       return players[1]
    else:
        return players[0]

def game_over(board: List[str]) -> bool:
    """
    Returns True if the game is over (i.e., there is a winner or a tie), and False otherwise.
    """
    if check_win(board) or check_tie(board):
        return True
    return False


def check_win(board: List[str]) -> bool:
    """Checks if a figure (X or O) has a winning pattern."""
    
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2]:
            return True
    
    for i in range(3):
        if board[i] == board[i+3] == board[i+6]:
            return True
    
    if board[0] == board[4] == board[8]:
        return True
    if board[2] == board[4] == board[6]:
        return True
    return False

def check_tie(board: List[str]) -> bool:
    """Checks if the game is a tie"""
    
    for i in range(9):
        if board[i] != "O" and board[i] != "X":
            return False
    
    if not check_win(board):
        return True

def does_game_continue() -> bool:
    """
    Prompts the player to enter "Y" or "N" to indicate whether they want to continue playing,
    and returns True if the player enters "Y", and False if the player enters "N".
    """
    choice = input("Do you want to continue playing? (Y/N) ").strip().upper()
    while choice not in ["Y", "N"]:
        print("Invalid choice. Please enter 'Y' or 'N'.")
        choice = input("Do you want to continue playing? (Y/N) ").strip().upper()
    return False if choice == "N" else True
