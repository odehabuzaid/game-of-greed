"""Place in root of Game of Greed Project,
at same level as pyproject.toml
"""
import builtins
import re
from abc import ABC, abstractmethod

from D_M.decide import DesicionMaker
from game_of_greed.game import Game
from game_of_greed.game_logic import GameLogic


class BaseBot(ABC):
    """Base class for Game of Greed bots"""

    def __init__(self, print_all=False):
        self.last_print = ""
        self.last_roll = []
        self.print_all = print_all
        self.dice_remaining = 0
        self.unbanked_points = 0
        self.desicion_maker = DesicionMaker()
        self.SR_results = None
        self.last_choice = None
        self.real_print = print
        self.real_input = input
        builtins.print = self._mock_print
        builtins.input = self._mock_input
        self.total_score = 0

    def reset(self):
        """restores the real print and input builtin functions"""

        builtins.print = self.real_print
        builtins.input = self.real_input

    def report(self, text):
        """Prints out final score, and all other lines optionally"""

        if text.startswith("Thanks for playing."):
            score = re.sub("\D", "", text)
            self.total_score += int(score)
        elif self.print_all:
            self.real_print(text)

    def _mock_print(self, *args, **kwargs):
        """steps in front of the real builtin print function"""

        line = " ".join(args)

        if "unbanked points" in line:

            # parse the proper string
            # E.g. "You have 700 unbanked points and 2 dice remaining"
            unbanked_points_part, dice_remaining_part = line.split("unbanked points")

            # Hold on to unbanked points and dice remaining for determining rolling vs. banking
            self.unbanked_points = int(re.sub("\D", "", unbanked_points_part))

            self.dice_remaining = int(re.sub("\D", "", dice_remaining_part))

        elif line.startswith("*** "):

            self.last_roll = [int(ch) for ch in line if ch.isdigit()]

        else:
            self.last_print = line

        self.report(*args, **kwargs)

    def _mock_input(self, *args, **kwargs):
        """steps in front of the real builtin print function"""

        if self.last_print == "(y)es to play or (n)o to decline":

            return "y"

        elif self.last_print == "Enter dice to keep, or (q)uit:":

            return self._enter_dice()

        elif self.last_print == "(r)oll again, (b)ank your points or (q)uit:":

            return self._roll_bank_or_quit()

        raise ValueError(f"Unrecognized last print {self.last_print}")

    def _enter_dice(self):
        """simulate user entering which dice to keep.
        Defaults to all scoring dice"""

        roll = GameLogic.get_scorers(self.last_roll)

        roll_string = ""
        
        
        # NoneType is not iterable, fixed with
        roll = [''] if roll is None else roll
        for value in roll:
            roll_string += str(value)

        self.report("> " + roll_string)
        
        return roll_string
    
    @abstractmethod
    def _roll_bank_or_quit(self):
        """decide whether to roll the dice, bank the points, or quit"""

        # subclass MUST implement this method
        pass

    @classmethod
    def play(cls, num_games=1):
        """Tell Bot play game a given number of times.
        Will report average score"""

        mega_total = 0

        for _ in range(num_games):
            player = cls()
            game = Game()
            try:
                game.play()
            except SystemExit:
                # in game system exit is fine
                # because that's how they quit.
                pass

            mega_total += player.total_score
            player.reset()

        print(
            f"{cls.__name__}: {num_games} games played with average score of {mega_total // num_games}"
        )


class NervousNellie(BaseBot):
    """NervousNellie banks the first roll always"""

    def _roll_bank_or_quit(self):
        return "b"


class Sharper(BaseBot):
    def _enter_dice(self):
        self.SR_results = list(self.desicion_maker.determin(self.last_roll))
        choice = self.SR_results[0][0]
        self.last_choice = choice

        self.report("\u001b[33m > " + str(choice) + "\u001b[37m")
        return str(choice)

    def _roll_bank_or_quit(self):

        choice = "r" if len(self.last_choice) < 4 else "b"

        if len(self.last_choice) > 1:
            tup = [int(digit) for digit in self.last_choice]

            last_score = GameLogic.calculate_score(tup)

            choice = "b" if last_score > 1000 else choice

        if len(self.SR_results[0][1]) == 2 or len(self.SR_results[0][1]) == 1:
            choice = "b"

        not_zilch = GameLogic.calculate_score(self.last_roll)

        choice = choice if not_zilch else "b"

        self.report("\u001b[32m > " + choice + "\u001b[37m")
        return choice


if __name__ == "__main__":
    num_games = 2
    NervousNellie.play(num_games)
    Sharper.play(num_games)
