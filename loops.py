# Craps By Brandon Riley
# 9/29/17
# Simulates craps to check probability of winning

import random


def craps():
    """
    Simulates the game of craps, player wins if they roll 7 or 11 on first roll or lose if roll 2, 3 or 12
    or lose if roll 7 on next rolls or win if they roll their original number
    :return: True if player wins or False if player loses
    """
    point = roll_dice()
    if point == 7 or point == 11:
        return True
    else:
        if point == 2 or point == 3 or point == 12:
            return False
        else:
            total = roll_dice()
            while total != 7 or total != point:
                total = roll_dice()
                if total == 7:
                    return False
                else:
                    if total == point:
                        return True


def roll_dice():
    """
    Simulates rolling two dice
    :return: number between 2 and 12
    """
    die_one = random.randint(1, 6)
    die_two = random.randint(1, 6)
    return die_one + die_two


def main():
    number_of_games = int(input("How many games would you like to simulate?"))
    win = 0
    lose = 0
    tries = 0
    for x in range(number_of_games):
        result = craps()
        if result:
            win += 1
        else:
            lose += 1
        tries += 1
    win_percent = round(win/number_of_games, 4) * 100
    print("You played", number_of_games, "games")
    print("You won", win, "and lost", lose)
    print("You won", win_percent, "percent of the time")


main()
