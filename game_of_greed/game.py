from collections import Counter

from game_of_greed.banker import Banker
from game_of_greed.game_logic import GameLogic


class Game:
    roller = GameLogic.roll_dice

    def __init__(self):
        """
        banker => Banker CLass instance : used to perform banking operations for player.

        rounds => integer : perform as a counter for the rounds being played.

        dice => integer   : perform as a counter for player remaining dice.

        state => string   : holds the game state

                  values  : started > means that the game is currently being played.
                            new > the begining of a new game.

        choice => string  : holds the last user input value.

        calculated =>
                    integer : holds the current player score that not yet Baker or shelved.

                    note    : possible bug in the calculation process.

        rolls =>      tuple : holds the previously reolled dice values

        cheater =>
        =======================
        methods :

        play : instance method
             gameplay

             args :
                self : [object] represent class  Game instance.

                roller: [reference] dice roller function method imported from GameLogic class.

                    args : integer = > represent dice count.

                    return : tuple = > random dice value for each dice.
        """
        self.rounds = 1
        self.dice = 6
        self.banker = Banker()
        self.choice = "new"
        self.calculated = 0
        self.rolls = None
        self.cheater = False

    def play(self, roller=roller):
        def get_user_input():
            self.choice = input("> ")
            self.play(roller)
        def checkout_round():
            if self.rounds < 6:
                self.rounds += 1
                self.dice = 6
                self.choice = "r"
            else:
                self.choice = "q"
        
        def check_cheating(takes, rolls):
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
                get_user_input()
            else:
                player_choice("keep")

        
        def player_choice(choice):
            def check_score():
                score = GameLogic.calculate_score(self.rolls)
                if score:
                    self.calculated += score
                    print("Enter dice to keep, or (q)uit:")
                    get_user_input()

                else:
                    print("****************************************")
                    print("**        Zilch!!! Round over         **")
                    print("****************************************")
                    self.banker.shelf(0)
                    self.calculated = 0
                    self.banker.bank()
                    self.dice = 6
                    self.rounds = 1
                    player_choice("bank")
            match choice:
                case "roll":
                    # Should allow user to continue rolling with 6 new dice
                    # when all dice have scored in current turn.
                    # In this game build , player will reach this point with 0 dice left
                    # only if all dice have scored
                    # TODO [X] find another way to validate 0 dice left and all previous rolled dice scored
                    if not self.dice : self.dice = 6
                        
                    
                    print("Rolling {} dice...".format(self.dice))
                    
                    self.rolls = roller(self.dice)

                    rolls = "*** {} ***".format(
                        " ".join(str(digit) for digit in self.rolls)
                    )
                    
                    print(rolls)
                    check_score()

                case "keep":
                    self.banker.shelf(self.calculated)
                    self.dice -= len(self.choice)
                    print(
                        "You have {} unbanked points and {} dice remaining".format(
                            self.calculated, self.dice
                        )
                    )

                    print("(r)oll again, (b)ank your points or (q)uit:")
                    get_user_input()
                    
                case 'bank':
                    print(
                        "You banked {} points in round {}".format(
                            self.calculated, self.rounds
                        )
                    )
                    self.banker.shelf(self.calculated)
                    self.banker.bank()

                    print("Total score is {} points".format(self.banker.bank()))
                    
                    checkout_round()
                    
                    self.play(roller)
  
        match self.choice:
            case "new":
                print("Welcome to Game of Greed")
                print("(y)es to play or (n)o to decline")
                self.state = "started"
                get_user_input()
                
            case "n":
                print("OK. Maybe another time")
                exit()
                
            case "q":
                print("Thanks for playing. You earned {} points".format(self.banker.bank()))
                exit()
                
            case "y":
                print("Starting round {}".format(self.rounds))
                player_choice("roll")
                
            case "r":
                if self.rounds > 1:
                    print("Starting round {}".format(self.rounds))
                player_choice("roll")
                
            case "b":
                player_choice("bank")
                
            case "":
                player_choice("roll")
                
            case _:
                digits = self.choice.replace(" ", "")
                if digits.isdigit():
                   check_cheating(digits, self.rolls)  
