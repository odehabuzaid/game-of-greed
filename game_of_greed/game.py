from game_of_greed.banker import Banker
from game_of_greed.game_logic import GameLogic

#


class Game:
    def __init__(self):
        self.rounds = 1
        self.dice = 6
        self.score = 0
        self.banker = Banker()

    def play(self, roller):
        user_input = ""
        if self.rounds == 1:
            print("Welcome to Game of Greed")
            print("(y)es to play or (n)o to decline")
            user_input = input("> ")
        if user_input == "n":
            print("OK. Maybe another time")
            exit()
        else:
            print("Starting round {}".format(self.rounds))
            print("Rolling 6 dice...")
            #
            rolls = roller(self.dice)
            print("*** {} ***".format(" ".join(map(str, rolls))))
            print("Enter dice to keep, or (q)uit:")
            user_input = input("> ")
            if user_input == "q":
                print(
                    "Thanks for playing. You earned {} points".format(
                        self.banker.balance
                    )
                )
            else:
                
                calculated = GameLogic.calculate_score(tuple(rolls))
                self.banker.shelf(calculated)
                self.calculate_dice(user_input)
                print(
                    "You have {} unbanked points and {} dice remaining".format(
                        calculated, self.dice
                    )
                )
                print("(r)oll again, (b)ank your points or (q)uit:")
                user_input = input("> ")
                if user_input == "b":
                    print(
                        "You banked {} points in round {}".format(
                            calculated, self.rounds
                        )
                    )
                    print("Total score is {} points".format(self.banker.bank()))
                    self.rounds += 1
                    self.play(roller)
    
    def calculate_dice(self, input):
        self.dice -= len(input)
