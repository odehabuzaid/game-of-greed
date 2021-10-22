# Pull Request

[Pull request](https://github.com/odehabuzaid/game-of-greed/pull/1) 


# Test
    
    pytest --cov

    pytest


```txt
======================================== test session starts  ========================================
platform win32 -- Python 3.10.0a6, pytest-6.2.5, py-1.10.0, pluggy-1.0.0
rootdir: I:\labs\game_of_greed, configfile: pytest.ini
plugins: cov-3.0.0
collected 147 items

tests\test_game_of_greed.py .......................................................[ 38%]
tests\version_1\test_banker.py ....[ 41%]
tests\version_1\test_calculate_score.py ........................................................[ 79%]
tests\version_1\test_roll_dice.py ............[ 87%]
tests\version_2\test_sim_basic.py ....[ 90%]
tests\version_3\test_get_scorers.py .......[ 95%]
tests\version_3\test_sim_advanced.py ....[ 97%]
tests\version_3\test_validate_keepers.py ...[100%] 

---------- coverage: platform win32, python 3.10.0-alpha-6 -----------
Name                                       Stmts   Miss  Cover
--------------------------------------------------------------
game_of_greed\__init__.py                      1      0   100%
game_of_greed\banker.py                       14      1    93%
game_of_greed\game.py                        109      3    97%
game_of_greed\game_logic.py                   48      1    98%
tests\__init__.py                              0      0   100%
tests\flo.py                                  55      3    95%
tests\test_game_of_greed.py                   69      0   100%
tests\version_1\test_banker.py                26      0   100%
tests\version_1\test_calculate_score.py       67      0   100%
tests\version_1\test_roll_dice.py             39      0   100%
tests\version_2\test_sim_basic.py             20      0   100%
tests\version_3\test_get_scorers.py            7      0   100%
tests\version_3\test_sim_advanced.py          16      0   100%
tests\version_3\test_validate_keepers.py      21      0   100%
--------------------------------------------------------------
TOTAL                                        492      8    98%


======================================== 147 passed in 1.11s ========================================
@Odeh ➜ game_of_greed git(Bot)
```