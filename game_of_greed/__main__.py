from pyfiglet import Figlet
from termcolor import colored

if __name__ == "__main__":
    logo = Figlet(font="standard")
    print(colored(logo.renderText("Game of Greed"), "red"))
    print(colored(("=" * 70), "red"))
    print(colored(("Welcome to Game of Greed!"), "white"))
