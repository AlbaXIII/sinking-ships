from colorama import Fore, Back, Style
import board
from random import randrange



# define ship and hit icons for visual indicator on maps
ships = ["B"]
hit = ["X"]

def bsea():
    """
    function to fill empty board with 'sea' icons for user board
    """
    import random, string
    while True:
        yield random.choice("~")


def csea():
    """
    function to fill empty board with 'sea' icons for computer and dummy board
    """
    import random, string
    while True:
        yield random.choice("-")

# define small/medium/large user boards & populate grid with bsea background
bsmall = board.Board((8, 8))
bsmall.populate(bsea())

bmed = board.Board((10, 10))
bmed.populate(bsea())

blarge = board.Board((12, 12))
blarge.populate(bsea())

# define small/medium/large computer boards & populate grid with csea background
csmall = board.Board((8, 8))
csmall.populate(csea())

cmed = board.Board((10, 10))
cmed.populate(csea())

clarge = board.Board((12, 12))
clarge.populate(csea())

# define small/medium/large dummy boards & populate grid with csea background
# dummy board for visual indication of user attack without showing comp positions
dsmall = board.Board((8, 8))
dsmall.populate(csea())

dmed = board.Board((10, 10))
dmed.populate(csea())

dlarge = board.Board((12, 12))
dlarge.populate(csea())

def create_user():
    """
    function for player username registration for later use
    """
    while True:
        username = input("Who are you?\n")
        if username:
            print(f"\nWelcome to the fleet {username}!\n")
            return username
        else:
            print("I can't hear you! Try again.")

create_user()