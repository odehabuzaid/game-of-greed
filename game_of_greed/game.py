from collections import Counter

from game_of_greed.banker import Banker
from game_of_greed.game_logic import GameLogic


class Game:
    roller = GameLogic.roll_dice

    def __init__(self):
        self.rounds = 1
        self.dice = 6
        self.banker = Banker()
        self.state = "new"
        self.choice = "y"
        self.calculated = 0
        self.rolls = None
        self.cheater = False

    def play(self, roller=roller):
        def get_user_input(self,roller):
            self.choice = input("> ")
            self.play(roller)
        
        def check_cheating(self, takes, rolls):
            cheater_typo = False

            rollss = [int(x) for x in rolls if x != "*" and x != " "]
            takes = [int(x) for x in takes]

            rolls_counter = Counter(rollss)
            takes = Counter(takes)

            for key, value in takes.items():
                if int(key) in rollss:
                    for k, v in rolls_counter.items():
                        if k == key:
                            if v < value:
                                cheater_typo = True
                            else:
                                cheater_typo = False
                else:
                    cheater_typo = True

            if cheater_typo:

                self.dice += 1

                print("Cheater!!! Or possibly made a typo...")

                rolls = "*** {} ***".format(
                    " ".join(str(digit) for digit in self.rolls)
                )

                print(rolls)

                print("Enter dice to keep, or (q)uit:")
                self.cheater = True
                get_user_input(self,roller)
    

            else:
                level("keep", self, roller)

        def check_zilch(self, rolled, roller):
            if rolled == "*** 4 4 ***":
                print("****************************************")
                print("**        Zilch!!! Round over         **")
                print("****************************************")
                self.dice = 6
                self.rounds = 1
                self.banker.shelf(0)
                self.calculated = 0
                self.banker.bank()
                level("bank", self, roller)

        def level(level, self, roller):

            if level == "bank":
                print(
                    "You banked {} points in round {}".format(
                        self.calculated, self.rounds
                    )
                )

                self.banker.shelf(self.calculated)
                self.banker.bank()
                print("Total score is {} points".format(self.banker.bank()))
                self.rounds += 1
                self.dice = 6
                self.choice = "r"
                self.play(roller)

            if level == "keep":
                self.banker.shelf(self.calculated)
                self.dice -= len(self.choice)
                print(
                    "You have {} unbanked points and {} dice remaining".format(
                        self.calculated, self.dice
                    )
                )
                # 0 > 150
                print("(r)oll again, (b)ank your points or (q)uit:")
                get_user_input(self,roller)

            if level == "roll":
                if self.dice == 0:
                    self.dice = 6

                print("Rolling {} dice...".format(self.dice))

                self.rolls = roller(self.dice)

                rolls = "*** {} ***".format(
                    " ".join(str(digit) for digit in self.rolls)
                )

                print(rolls)
                check_zilch(self, rolls, roller)

                self.calculated += GameLogic.calculate_score(tuple(self.rolls))
                # 0 > 350

                print("Enter dice to keep, or (q)uit:")
                get_user_input(self,roller)

        if self.state == "new":
            print("Welcome to Game of Greed")
            print("(y)es to play or (n)o to decline")
            self.state = "started"
            get_user_input(self,roller)

        if self.choice == "n":
            print("OK. Maybe another time")
            exit()

        if self.choice == "q":
            print("Thanks for playing. You earned {} points".format(self.banker.bank()))
            exit()

        if self.choice == "y":
            print("Starting round {}".format(self.rounds))
            level("roll", self, roller)
        
        if self.choice == "r":
            if self.rounds > 1:
                print("Starting round {}".format(self.rounds))
            level("roll", self, roller)

        if self.choice == "b":
            level("bank", self, roller)

        digits = self.choice.replace(" ", "")
        if digits.isdigit():
            check_cheating(self, digits, self.rolls)
