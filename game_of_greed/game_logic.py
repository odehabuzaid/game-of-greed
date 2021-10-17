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
    rolled = Counter(rolled)
    score = 0
    if len(rolled) == 6:
      straight =  all(value == 1 for value in rolled.values())
      if straight:
        score = 1500
    if len(rolled) == 3:
      three_pairs = all(value == 2 for value in rolled.values())
      if three_pairs:
        score = 750 * 2
    if score == 0:
      for number in rolled:
        appears = rolled[number]
        if appears >= 3:
          if number == 1:
            score+= (number *1000) * (appears-2)
          else:   
            score+= (number *100) * (appears-2)
        else:
          if number == 1: 
            score+= 100*appears
          if number == 5: 
            score+= 50*appears
    return score
  
  @staticmethod
  def roll_dice(roll=6):
    rolls = tuple(randint(1,6) for _ in range(roll))
    return rolls
