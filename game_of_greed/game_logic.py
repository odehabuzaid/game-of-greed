from collections import Counter
from random import randint


class GameLogic:
  """
  this class will control the basic game features:
  calculate_score 
  roll_dice 
  
  """
  def __init__(self):
    self.score = 0
    
  @staticmethod
  def calculate_score(rolled):
    """
    Handle calculating score for dice roll

    Args:
        rolled (tuple): a list of random integers, each represent a random dice roll.

    Returns:
        int: calculated score as a result of rolling the dice's based on the game rules.
    """
    rolled = Counter(rolled)
    score = check_straight_or_pairs(rolled)
    
    if not score:
      for number in rolled:
        appears = rolled[number]
        if appears >= 3 and number == 1:score+= (number *1000) * (appears-2)
        if appears >= 3 and number != 1:score+= (number *100) * (appears-2)
        if appears < 3 and number == 1: score+= 100*appears
        if appears < 3 and number == 5: score+= 50*appears
    
    
    return score

  
  @staticmethod
  def roll_dice(roll=6):
    """
    aHandle rolling dice

    Args:
        roll (int, optional): how many dices to roll. Defaults to 6.
    
    Returns:
         rolls (tuple): a list of random integers, each represent a random dice roll.
    """
    rolls = tuple(randint(1,6) for _ in range(roll))
    return rolls

def check_straight_or_pairs(rolled):
  """
  checking weather the result of rolling dice contains the pattern of straight or three pairs
  
  Args:
      rolled (tuple): a list of random integers, each represent a random dice roll.
  
  Returns:
      int: calculated score as a result of rolling the dice's based on the game rules.
  """
  score = 0
  if len(rolled) == 6:
    straight =  all(value == 1 or value ==2 for value in rolled.values())
    if straight:
      score = 1500
  
  if len(rolled) == 3:
    three_pairs = all(value == 2 for value in rolled.values())
    if three_pairs:
      score = 750 * 2
      
  return score
