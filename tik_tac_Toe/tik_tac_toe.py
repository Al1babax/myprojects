"""
Making game of Tic Tac Toe.

Made by Al1baba

TODO AI player
TODO Game still has some bugs
"""
import os

player1 = "X"
player2 = "O"
score = {"X": 0, "O": 0}
turn_count = 0
players_turn = ""
game_going = True
dict_keymapping = {
    1: " ",
    2: " ",
    3: " ",
    4: " ",
    5: " ",
    6: " ",
    7: " ",
    8: " ",
    9: " ",
}


def draw_board():
    row1 = f"   {dict_keymapping[7]} | {dict_keymapping[8]} | {dict_keymapping[9]}"
    row2 = f"4  {dict_keymapping[4]} | {dict_keymapping[5]} | {dict_keymapping[6]}  6"
    row3 = f"   {dict_keymapping[1]} | {dict_keymapping[2]} | {dict_keymapping[3]}"
    print("Scores:")
    print(f"Player X: {score['X']}    Player O: {score['O']}")
    print("   7   8   9")
    print(row1)
    print(f"  ---|---|---")
    print(row2)
    print(f"  ---|---|---")
    print(row3)
    print("   1   2   3")


def update_board(player_input, player):
    clear_console()
    dict_keymapping[player_input] = f"{player}"
    draw_board()


def user_input():
    print(f"Player {players_turn} turn: ")
    player_input = input(f"Select a number between 1-9: ")
    if player_input in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        player_input = int(player_input)
        if dict_keymapping[player_input] == " ":
            return player_input
        else:
            print(f"Player has already played same number, please choose another number!")
            user_input()

    else:
        print(f"Your input {player_input} is not a number between 1-9")
        print(f"Please try again")
        user_input()


def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def play_again():
    global turn_count

    choose = (input("Do you want to play again yes or no?: ")).lower()
    if choose == "yes":
        turn_count = 0
        for mark in dict_keymapping:
            dict_keymapping[mark] = " "
        clear_console()
        draw_board()
        return True
    elif choose == "no":
        print("Game over")
        return False
    else:
        print("Invalid input try again!")
        play_again()


def check_win():
    x = 1
    y = 1
    # Checking every row
    for row in range(3):
        if dict_keymapping[x] == dict_keymapping[x + 1] == dict_keymapping[x + 2] == "X":
            print("Player 1 wins!")
            return True
        if dict_keymapping[x] == dict_keymapping[x + 1] == dict_keymapping[x + 2] == "O":
            print("Player 2 wins!")
            return True
        x += 3
    # Checking every column
    for column in range(3):
        if dict_keymapping[y] == "X" and dict_keymapping[y + 3] == "X" and dict_keymapping[y + 6] == "X":
            print("Player 1 wins!")
            return True
        if dict_keymapping[y] == "O" and dict_keymapping[y + 3] == "O" and dict_keymapping[y + 6] == "O":
            print("Player 2 wins!")
            return True
        y += 1
    # Checking every diagonal
    if dict_keymapping[1] == "X" and dict_keymapping[5] == "X" and dict_keymapping[9] == "X":
        print("Player 1 wins!")
        return True
    if dict_keymapping[1] == "O" and dict_keymapping[5] == "O" and dict_keymapping[9] == "O":
        print("Player 2 wins!")
        return True
    if dict_keymapping[3] == "X" and dict_keymapping[5] == "X" and dict_keymapping[7] == "X":
        print("Player 1 wins!")
        return True
    if dict_keymapping[3] == "O" and dict_keymapping[5] == "O" and dict_keymapping[7] == "O":
        print("Player 2 wins!")
        return True


def play():
    global turn_count
    global player1
    global player2
    global game_going
    global players_turn

    draw_board()

    while game_going:
        if turn_count in [0, 2, 4, 6, 8]:
            turn_count += 1
            players_turn = "X"
            update_board(user_input(), player1)
            if check_win():
                score["X"] += 1
                game_going = play_again()

        elif turn_count in [1, 3, 5, 7]:
            turn_count += 1
            players_turn = "O"
            update_board(user_input(), player2)
            check_win()
            if check_win():
                score["O"] += 1
                game_going = play_again()
        else:
            print("DRAW!")
            game_going = play_again()


play()
