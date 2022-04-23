import random


class Currency:

    def __init__(self, player: str, chips: int):
        self.player = player
        self.chips = chips

    def __str__(self):
        return f"--> Player {self.player} has {self.chips} chips <--"

    def bet(self):
        amount = input("Please enter the amount of chips you would like to bet?: ")
        if amount.isdigit():
            amount = int(amount)
            if amount <= self.chips:
                self.chips -= amount
                # print("Your bet is successful!")
                print(f"You bet {amount} chips. You now have {self.chips} chips left")
            else:
                print("Sorry you do not have enough chips to do that bet")
                print("Please, bet again")
                self.bet()
        else:
            print("Sorry your input was invalid, try again")
            self.bet()
        return amount

    def add(self, amount):
        self.chips += amount
        print(f"You gained {amount} chips. You now have {self.chips} chips")

    def loan(self):
        pass


class Cards:
    """
    Cards between 1-13 are clubs, 14-26 are diamonds, 27-39 are hearts, 40-52
    """
    CARDS = {
        1: "ace",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "jack",
        12: "queen",
        13: "king",
    }
    SUITS = ("of clubs", "of diamonds", "of hearts", "of spades")
    # Cannot draw same cards twice, so I have to keep track which cards have been drawn already
    drawn_cards = []
    current_card = 0

    def card(self):
        self.draw_card()
        card = self.current_card

        def check_card_number(card_num, num1):  # Now cards between 11-13 are always 10
            if 11 <= card_num - num1 <= 13:
                self.card_number = 10
            elif card_num - num1 == 1:  # ace can be 1 or 11 WARNING ONLY STRING??
                return "1 or 11"
            else:
                self.card_number = card_num - num1
            return self.card_number

        if card <= 13:
            return f"{self.CARDS[card]} {self.SUITS[0]} ({check_card_number(card, 0)})"
        elif card <= 26:
            return f"{self.CARDS[card - 13]} {self.SUITS[1]} ({check_card_number(card, 13)})"
        elif card <= 39:
            return f"{self.CARDS[card - 26]} {self.SUITS[2]} ({check_card_number(card, 26)})"
        else:
            return f"{self.CARDS[card - 39]} {self.SUITS[3]} ({check_card_number(card, 39)})"

    def draw_card(self):
        self.current_card = random.randint(1, 52)
        # Check whether the card is still in draw pile
        if self.current_card not in self.drawn_cards:
            self.drawn_cards.append(self.current_card)
            return self.current_card
        elif len(self.drawn_cards) >= 52:
            print("Out of cards")  # Draw deck is out of cards to draw #TODO final
        else:
            self.draw_card()

    def reset(self):
        self.drawn_cards = []


class Hand(Cards):
    player_current_hand = []

    def __init__(self):
        self.current_cards = [self.card() for _ in range(2)]

    def add_card(self):
        self.current_cards.append(self.card())

    def stop(self):
        pass

    def double_down(self):
        pass

    def split_hand(self):
        pass

    def current_hand(self):
        self.player_current_hand = self.current_cards

        return f"|{' | '.join(self.player_current_hand)}|"

    def reset_hand(self):
        self.player_current_hand = []

    def __str__(self):
        return self.current_hand()


class House(Cards):
    house_current_hand = []

    # House cards, second one should be hidden
    def __init__(self):
        self.house_cards = [self.card() for _ in range(2)]

    def add_card(self):
        self.house_cards.append(self.card())

    def house_hand(self):
        self.house_current_hand = self.house_cards

        return f"|{' | '.join(self.house_current_hand)}|"

    def reset_hand(self):
        self.house_current_hand = []

    def __str__(self):
        return self.house_hand()


if __name__ == "main":
    pass
