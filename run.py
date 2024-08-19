from colorama import Fore, Back, Style
import board
from random import randrange



# define ship and hit icons for visual indicator on maps
ships = ["B"]
hit = ["X"]
miss = ["O"]

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

def choose_map(bsmall, bmed, blarge, csmall, cmed, clarge, dsmall, dmed, dlarge):
    """
    function to choose map size for game
    """
    while True:

        map_size = input("Please choose a map size - [S/M/L]\n")
        if map_size in ["S", "s"]:
            print("\nSmall map selected - 5 ships\n")
            bsmall.draw()
            player_map = bsmall
            comp_map = csmall
            dummy_map = dsmall
            return player_map

        elif map_size in ["M", "m"]:
            print("\nMedium map selected - 7 ships\n")
            bmed.draw()
            player_map = bmed
            comp_map = cmed
            dummy_map = dmed
            return player_map
        elif map_size in ["L", "l"]:

            print("\nLarge map selected - 10 ships\n")
            blarge.draw()
            player_map = blarge
            comp_map = clarge
            dummy_map = dlarge
            return player_map

        else:
            print("What! Please select S/M/L")

def player_coords(player_map, bsmall, bmed, blarge):
    """
    Function for selection of ship placement on user board
    """
    while True:
        
        if player_map == bsmall: 
            try:
                row = int(input("\nPlease select column: ")) 
                col = int(input("Please select row: "))
                if 0 <= row < 8 and 0 <= col < 8 and (row, col):
                    bsmall.populate(ships, bsmall.iterline((row, col), (1, 0)))
                else:
                    print("Invalid markers - please try again!")
                    player_coords(player_map, bsmall, bmed, blarge)
                    break
            except ValueError:
                print("Invalid input! Please enter a number!")
                player_coords(player_map, bsmall, bmed, blarge)
            break
        
        elif player_map == bmed:
            try:
                row = int(input("\nPlease select column: ")) 
                col = int(input("Please select row: "))
                if 0 <= row < 10 and 0 <= col < 10 and (row, col):
                    bmed.populate(ships, bmed.iterline((row, col), (1, 0)))
                else:
                    print("Invalid markers - please try again!")
                    player_coords(player_map, bsmall, bmed, blarge)
                    break
            except ValueError:
                print("Invalid input! Please enter a number!")
                player_coords(player_map, bsmall, bmed, blarge)
            break

        elif player_map == blarge:
            try:
                row = int(input("\nPlease select column: ")) 
                col = int(input("Please select row: "))
                if 0 <= row < 12 and 0 <= col < 12 and (row, col):
                    blarge.populate(ships, blarge.iterline((row, col), (1, 0)))
                else:
                    print("Invalid markers - please try again!")
                    player_coords(player_map, bsmall, bmed, blarge)
                    break
            except ValueError:
                print("Invalid input! Please enter a number!")
                player_coords(player_map, bsmall, bmed, blarge)
            break

def comp_coords(comp_map, csmall, cmed, clarge):
    """
    Function for computer ship placement on all board sizes
    """
    while True:

        if comp_map == csmall:
            for ship in ships:
                while True: 
                    row = randrange(0, 7)
                    col = randrange(0, 7)
                    csmall.populate(ships, csmall.iterline((row, col), (1, 0)))
                    break
            return comp_map

        elif comp_map == cmed:
            for ship in ships:
                while True: 
                    row = randrange(0, 9)
                    col = randrange(0, 9)
                    cmed.populate(ships, cmed.iterline((row, col), (1, 0)))
                    break
            return comp_map

        elif comp_map == clarge:
            for ship in ships:
                while True: 
                    row = randrange(0, 11)
                    col = randrange(0,11)
                    clarge.populate(ships, clarge.iterline((row, col), (1, 0)))
                    break
            return comp_map

def check_hit_player(comp_map, player_hits, dummy_map, username): #dummy board with hits?
    print (f"{username}'s turn to attack!\n")
    
    player_hits = 1

    row = int(input("Enter your attack column: "))
    col = int(input("Enter your attack row: "))

    if comp_map == csmall:
        dummy_map = dsmall
        if row > 7 or col > 7:
            print("\nPlease select coordinates within boundaries!(0 - 7)\n")
            check_hit_player(comp_map, player_hits, username)

    elif comp_map == cmed:
        dummy_map = dmed
        if row > 9 or col > 9:
            print("\nPlease select coordinates within boundaries! (0-9)\n")
            check_hit_player(comp_map, player_hits, username)

    elif comp_map == clarge:
        dummy_map = dlarge
        if row > 11 or col > 11:
            print("\nPlease select coordinates within boundaries! (0-11)\n")
            check_hit_player(comp_map, player_hits, username)

    elif comp_map[row, col] == "B":
        print(Fore.GREEN + "\nKABOOOOOM! Direct hit!\n" + Style.RESET_ALL)
        dummy_map_map.populate(hit, player_map.iterline((row, col), (1, 0)))
        player_hits += 1
        print(f"Hit number : {player_hits}")

    else:
        print(Fore.RED + "\nSPLOOOOOSH! Missed!\n" + Style.RESET_ALL)
        dummy_map_map.populate(miss, player_map.iterline((row, col), (1, 0)))
        player_hits = 0

    return player_hits

def check_hit_comp(player_map, comp_hits, username):
    print("\nThe Squid are closing in...\n")

    comp_hits = 1
    
    if player_map == bsmall:
        row = randrange(0,7)
        col = randrange(0,7)
    elif player_map == bmed:
        row = randrange(0,9)
        col = randrange(0,9)
    elif player_map == blarge:
        row = randrange(0,11)
        col = randrange(0,11)

    if player_map[row, col] == "B":
        print(Fore.GREEN + "Oh no! They got us!\n" + Style.RESET_ALL)
        comp_hits += 1
        player_map.populate(hit, player_map.iterline((row, col), (1, 0)))
        print(f"Squid hits : {comp_hits}")
        print(f"\n{username}'s board:")
        player_map.draw()

    else:
        print(Fore.RED + "Not even close!\n" + Style.RESET_ALL)
        player_map.populate(miss, player_map.iterline((row, col), (1, 0)))
        print(f"\n{username}'s board:")
        player_map.draw()
        comp_hits = 0

    return comp_hits

def play_game():

    print(Style.RESET_ALL + "\nWelcome to\n")
    print("------------------\n")
    print(Fore.CYAN + "S I N K I N G  S H I P S\n" + Style.RESET_ALL)
    print("------------------\n")

    username = create_user()

    print("\nI am the great Admiral Dolvalski!\n")
    print("Look sharp, for we are the sole protectors of this island!\n")
    print("Red alert! Schools of deadly squid are attacking!\n")
    print("The fiends approach! Take command of our defenses and man the cannons!\n")
    print("Choose an angle of attack, and sink them all!\n")
    print(Fore.BLUE + f"We're counting on you {username}!\n" + Style.RESET_ALL)

    occupied = set()
    player_map = choose_map(bsmall, bmed, blarge, csmall, cmed, clarge, dsmall, dmed, dlarge)
    print("\nPlease select coordinates for your ships!\n")
    if player_map == bsmall:
        comp_map = csmall
        for x in range (0, 5):
            player_coords(player_map, bsmall, bmed, blarge)
            comp_coords(comp_map, csmall, cmed, clarge)
    elif player_map == bmed:
        comp_map = cmed
        for x in range (0, 7):
            player_coords(player_map, bsmall, bmed, blarge)
            comp_coords(comp_map, csmall, cmed, clarge)
    elif player_map == blarge:
        comp_map = clarge
        for x in range (0, 10):
            player_coords(player_map, bsmall, bmed, blarge)
            comp_coords(comp_map, csmall, cmed, clarge)

    print(f"\n {username} formation confirmed!")
    player_map.draw()

    print("Squid formation assembling...")
    print(Fore.BLUE + "Begin the attack!\n" + Style.RESET_ALL)

    while True:
        check_hit_player(comp_map, player_hits, username)

        check_hit_comp(player_map, comp_hits, username)




play_game()



        



