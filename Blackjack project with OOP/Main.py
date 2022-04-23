import cards_and_bank as b
import os

# Making objects here
player1_bank = b.Currency("Sam", 500)
player1_hand = b.Hand()
house_hand = b.House()
cards = b.Cards()
bet_amount = 0


def hand_total(hand):
    # Getting the card value from string
    # print(hand)
    card_total = 0
    amount_of_aces = 0

    temp_list = str(hand).split("|")
    temp_list = list(filter(None, temp_list))
    temp_list = [x.split() for x in temp_list]  # Every card is one element in the list

    for num in range(len(temp_list)):
        card_total += int(temp_list[num][-1][1:-1])
        if int(temp_list[num][-1][1:-1]) == 1:  # Checking here if any of the numbers is ace
            amount_of_aces += 1

    total_value_str = f"{card_total} ({card_total + (10 * amount_of_aces)})"  # adding ace amount to ()

    return total_value_str


def board_draw():
    print(f"""
    Bet {bet_amount}
    {player1_bank}    

    The house hand is {house_hand}
    --- Total {hand_total(house_hand)} ---
    ------------------------------------------------------
    --- Total {hand_total(player1_hand)} ---
    Your Hand is {player1_hand} 
    """)


def check_if_over_21(hand):  # Checking if total over 21
    # print(hand_total(hand))
    value = int(hand_total(hand)[:2])
    # print(value)
    return value > 21


def round_over():
    decision = input("Do you want to play another round?(y/n) ")
    if decision == "y":
        reset()  # resets the player/house hands and draw pile
        round_init()
    else:
        print(f"Game over. {player1_bank}")


def hit():
    player1_hand.add_card()
    clear_console()
    board_draw()

    if check_if_over_21(player1_hand):
        print(f"You lost!")
        print(player1_bank)
        round_over()


def stay():  # House drawing cards until it wins or loses
    while int(hand_total(house_hand)[:2]) < 21:

        if check_house_win():  # if house already won
            print(f"House wins, you lost {bet_amount}")
            print(player1_bank)
            break

        house_hand.add_card()
        clear_console()
        board_draw()
        # print(f"{int(hand_total(house_hand)[:2])} {int(hand_total(player1_hand)[:2])}")
        # print(check_if_over_21(house_hand))

        if check_if_over_21(house_hand):  # if house goes over 21
            print("You WIN!")
            player1_bank.add(bet_amount * 2)

        elif check_house_win():  # if house goes over your value without going over 21 and wins
            print(f"House wins, you lost {bet_amount}")
            print(player1_bank)
            break

    round_over()


def check_house_win():  # Checking if house value is higher than player to win
    player_values = hand_total(player1_hand).split()
    house_values = hand_total(house_hand).split()
    # Setting normal value and "ace" value when ace can be 1 or 11
    player_value = int(player_values[0])
    house_value = int(house_values[0])
    player_ace_value = int(player_values[1][1:-1])
    house_ace_value = int(house_values[1][1:-1])
    # Checking if ace value for either is higher
    if player_value < player_ace_value < 22:
        player_value = player_ace_value
    if house_value < house_ace_value < 22:
        house_value = house_ace_value

    if house_value == 21 and player_value == 21:  # check if both hit 21 and goes to draw
        print("DRAW!")
        player1_bank.add(bet_amount)

    return house_value > player_value


def reset():  # resets the player/house hands and draw pile
    global house_hand
    global player1_hand

    cards.reset()  # Reset the card deck
    house_hand.reset_hand()  # reset house hand
    player1_hand.reset_hand()  # reset player hand
    player1_hand = b.Hand()
    house_hand = b.House()


def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def play():
    decision = input("Do you want to hit or stay?(hit/stay): ")
    if decision == "hit":
        hit()
        play()

    elif decision == "stay":
        stay()

    else:
        print("Your input was invalid")
        play()


def round_init():
    global bet_amount
    bet_amount = player1_bank.bet()
    board_draw()
    play()


round_init()
