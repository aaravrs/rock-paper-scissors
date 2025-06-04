import random
import getpass
import os
import time

winning_conditions = { # Left beats right
    ("R", "S"), # R = Rock
    ("P", "R"), # P = Paper
    ("S", "P")  # S = Scissors
}
move_to_word = {
    "R": "Rock",
    "P": "Paper",
    "S": "Scissors"
}
valid_moves = {"R", "P", "S"}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def exit_pretty():
    for i in range(3, 0, -1):
        clear()
        print(f"Exiting game....\n\n{i}")
        time.sleep(1)
    exit()

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

def print_tutorial_menu():
    clear()
    print("To play, simply enter your choice")
    print("(R = Rock, P = Paper, S = Scissors")
    input("\nPress enter to continue:")
    clear()
    print("To win, you must be the first player to reach 3 round wins.")
    input("\nPress enter to continue and begin the game: ")
    clear()

def game_menu():
    clear()
    print_game_menu()
    option = input("> ")

    if option == "1":
        game(False)
    elif option == "2":
        game(True)
    elif option == "3":
        return
    else:
        game_menu()

def get_valid_move(player, text):
    move = ""
    while move not in valid_moves:
        clear()
        print(text)
        print(f"{player}, enter your move (R, P, S)")
        move = getpass.getpass("> ").upper()
        if move not in valid_moves:
            print("\nPlease enter a valid move. \n")
            time.sleep(1)
    return move

def game(is_computer):
    clear()
    print(f"First, enter your name{'s' if not is_computer else ''}.\n")
    p1 = input(f"Player{' 1' if not is_computer else ''} Name: ")
    p1_wins = 0
    p2 = input("Player 2 Name: ") if not is_computer else "Computer"
    p2_wins = 0
    clear()
    print_tutorial_menu()
    round = 1
    game_history = []
    while True: # Each loop is one round
        round_text = f"""{p1} vs {p2}
--------------
Round {round}
--------------\n"""
        p1_move = get_valid_move(p1, round_text)
        p2_move = get_valid_move(p2, round_text) if not is_computer else random.choice(list(valid_moves))

        print(f"{p1} plays {move_to_word[p1_move]}")
        print(f"{p2} plays {move_to_word[p2_move]}")
        if (p1_move, p2_move) in winning_conditions:
            print(f"{p1} wins!")
            p1_wins += 1
        elif (p2_move, p1_move) in winning_conditions:
            print(f"{p2} wins!")
            p2_wins += 1
        else:
            print("This round is a tie!")

        if p1_wins == 3:
            print(f"{p1} wins the game!")
            break
        elif p2_wins == 3:
            print(f"{p2} wins the game!")
            break

        round += 1
        time.sleep(2)

def view_history():
    pass

def main():
    while True:
        clear()
        print_main_menu()
        option = input("> ")

        if option == "1":
            game_menu()
        elif option == "2":
            view_history()
        elif option == "3":
            exit_pretty()

        # save
        time.sleep(1)

main()