import random
import getpass
import os
import time

winning_conditions = { # Left beats right
    ("R", "S"), # R = Rock
    ("P", "R"), # P = Paper
    ("S", "P")  # S = Scissors
}

valid_moves = {"R", "P", "S"}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def exit_pretty():
    for i in range(3, 0, -1):
        clear()
        print(f"Exiting game....\n\n{i}")
        time.sleep(1)


def print_main_menu():
    print("Rock Paper Scissors")
    print("-------------------")
    print("1. Play a game ")
    print("2. View game history")
    print("3. Exit")

def print_game_menu():
    print("Rock Paper Scissors")
    print("-------------------")
    print("1. Player vs Player")
    print("2. Player vs Computer")
    print("3. Exit to menu")

def print_pvp_menu():
    print("Rock Paper Scissors")
    print("-------------------")
    print("To play, simply enter your choice")
    print("(R = Rock, P = Paper, S = Scissors")

def game():
    clear()
    print_game_menu()
    option = input("> ")

    if option == "1":
        game_pvp(False)
    elif option == "2":
        game_pvp(True)
    elif option == "3":
        return

def get_valid_move(player):
    move = ""
    while move not in valid_moves:
        print(f"{player}, enter your choice (R, P, S)")
        move = getpass.getpass("> ").upper()
        if move not in valid_moves: print("Please enter a valid move. \n")
    return move


def game_pvp(is_computer):
    clear()
    print("First, enter your names.")
    p1 = input("Player 1 Name: ")
    p2 = input("Player 2 Name: ") if not is_computer else "Computer"
    clear()
    print(f"Welcome {p1} and {p2}!")
    #TODO: use time to make ui better
    print_pvp_menu()
    p1_move = get_valid_move(p1)
    p2_move = get_valid_move(p2) if not is_computer else random.choice(list(valid_moves))

    if (p1_move, p2_move) in winning_conditions:
        print(f"Player 1 {p1} wins!")
    elif (p2_move, p1_move) in winning_conditions:
        print(f"Player 2 {p2} wins!")
    else:
        print("This round is a tie!")

def view_history():
    pass


def main():
    while True:
        clear()
        print_main_menu()
        option = input("> ")

        if option == "1":
            game()
        elif option == "2":
            view_history()
        elif option == "3":
            exit_pretty()
        time.sleep(1)


main()