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
    import random
    import string
    while True:
        yield random.choice("~")


def csea():
    """
    function to fill empty board with 'sea' icons for computer and dummy board
    """
    import random
    import string
    while True:
        yield random.choice("-")

# define small/medium/large user boards & populate grid with bsea background


bsmall = board.Board((8, 8))
bsmall.populate(bsea())

bmed = board.Board((10, 10))
bmed.populate(bsea())

blarge = board.Board((12, 12))
blarge.populate(bsea())

# define computer board size & populate grid with csea background
csmall = board.Board((8, 8))
csmall.populate(csea())

cmed = board.Board((10, 10))
cmed.populate(csea())

clarge = board.Board((12, 12))
clarge.populate(csea())

# define small/medium/large dummy boards & populate grid with csea background
# dummy board for visual of user attack without showing comp ship positions
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


def player_coords(player_map, bsmall, bmed, blarge, occupied):
    """
    Function for selection of ship placement on user board
    """

    while True:

        if player_map == bsmall:
            try:
                col = int(input("\nPlease select column: "))
                row = int(input("Please select row: "))
                if 0 <= row < 8 and 0 <= col < 8 and (row, col) not in occupied:
                    bsmall.populate(ships, bsmall.iterline((row, col), (1, 0)))
                    occupied.add((row, col))
                else:
                    print("Invalid coordinates - please try again!")
                    player_coords(player_map, bsmall, bmed, blarge, occupied)
                    break
            except ValueError:
                print("Invalid input! Please enter a number!")
                player_coords(player_map, bsmall, bmed, blarge, occupied)
            break

        elif player_map == bmed:
            try:
                row = int(input("\nPlease select column: "))
                col = int(input("Please select row: "))
                if 0 <= row < 10 and 0 <= col < 10 and (row, col) not in occupied:
                    bmed.populate(ships, bmed.iterline((row, col), (1, 0)))
                    occupied.add((row, col))
                else:
                    print("Invalid coordinates - please try again!")
                    player_coords(player_map, bsmall, bmed, blarge, occupied)
                    break
            except ValueError:
                print("Invalid input! Please enter a number!")
                player_coords(player_map, bsmall, bmed, blarge, occupied)
            break

        elif player_map == blarge:
            try:
                row = int(input("\nPlease select column: "))
                col = int(input("Please select row: "))
                if 0 <= row < 12 and 0 <= col < 12 and (row, col) not in occupied:
                    blarge.populate(ships, blarge.iterline((row, col), (1, 0)))
                    occupied.add((row, col))
                else:
                    print("Invalid coordinates - please try again!")
                    player_coords(player_map, bsmall, bmed, blarge, occupied)
                    break
            except ValueError:
                print("Invalid input! Please enter a number!")
                player_coords(player_map, bsmall, bmed, blarge, occupied)
            break

    return player_map, occupied


def comp_coords(comp_map, csmall, cmed, clarge, c_occupied):
    """
    Function for computer ship placement on all board sizes
    """

    while True:

        if comp_map == csmall:
            for ship in ships:
                while True:
                    row = randrange(0, 7)
                    col = randrange(0, 7)
                    if ((row, col)) in c_occupied:
                        comp_coords(comp_map, csmall, cmed, clarge, c_occupied)
                    else:
                        csmall.populate(ships, csmall.iterline((row, col), (1, 0)))
                    c_occupied.add((row, col))
                    break
            return comp_map

        elif comp_map == cmed:
            for ship in ships:
                while True:
                    row = randrange(0, 9)
                    col = randrange(0, 9)
                    if ((row, col)) in c_occupied:
                        comp_coords(comp_map, csmall, cmed, clarge, c_occupied)
                    else:
                        cmed.populate(ships, cmed.iterline((row, col), (1, 0)))
                    c_occupied.add((row, col))
                    break
            return comp_map

        elif comp_map == clarge:
            for ship in ships:
                while True:
                    row = randrange(0, 11)
                    col = randrange(0, 11)
                    if ((row, col)) in c_occupied:
                        comp_coords(comp_map, csmall, cmed, clarge, c_occupied)
                    else:
                        clarge.populate(ships, clarge.iterline((row, col), (1, 0)))
                    c_occupied.add((row, col))
                    break
            return comp_map


def check_hit_player(comp_map, dummy_map, username, attempts):
    """
    Function to check if player hit on comp_board is successful
    """

    print(f"\n{username}'s turn to attack!\n")

    impact = 1

    try:

        col = int(input("Enter your attack column: "))
        row = int(input("Enter your attack row: "))

        if comp_map[col, row] == "B":
            print(Fore.GREEN + "\nKABOOOOOM! Direct hit!\n" + Style.RESET_ALL)
            dummy_map.populate(hit, dummy_map.iterline((col, row), (1, 0)))
            print("\nEnemy board:")
            dummy_map.draw()
            attempts.append((col, row))

        elif ((col, row)) in attempts:
            print(Fore.BLUE + "Please select new coordinates!" + Style.RESET_ALL)
            check_hit_player(comp_map, dummy_map, username, attempts)

        else:
            print(Fore.RED + "\nSPLOOOOOSH! Missed!\n" + Style.RESET_ALL)
            dummy_map.populate(miss, dummy_map.iterline((col, row), (1, 0)))
            print("\nEnemy board:")
            dummy_map.draw()
            attempts.append((col, row))
            impact = 0

    except ValueError:
        print("Please enter a number!")
        check_hit_player(comp_map, dummy_map, username, attempts)

    except board.Board.OutOfBoundsError:
        print("Please select a coordinate within game bounds!")
        check_hit_player(comp_map, dummy_map, username, attempts)

    return impact


def check_hit_comp(player_map, username):
    """
    Function to check if player hit on comp_board is successful
    """

    print("\nThe Squid are closing in...\n")

    impact = 1

    if player_map == bsmall:
        col = randrange(0, 7)
        row = randrange(0, 7)
    elif player_map == bmed:
        col = randrange(0, 9)
        row = randrange(0, 9)
    elif player_map == blarge:
        col = randrange(0, 11)
        row = randrange(0, 11)

    if player_map[row, col] == "B":
        print(Fore.GREEN + "Oh no! They got us!\n" + Style.RESET_ALL)
        player_map.populate(hit, player_map.iterline((col, row), (1, 0)))
        print(f"\n{username}'s board: ")
        player_map.draw()

    else:
        print(Fore.RED + "Not even close!\n" + Style.RESET_ALL)
        player_map.populate(miss, player_map.iterline((col, row), (1, 0)))
        print(f"\n{username}'s board: ")
        player_map.draw()
        impact = 0

    return impact


def game_loop(player_map, comp_map, dummy_map, username, attempts):
    """
    Function to loop player & computer attacks until winner
    """

    player_hits = 0
    comp_hits = 0

    while True:
        player_hits += check_hit_player(comp_map, dummy_map, username, attempts)
        if player_map == bsmall and player_hits == 5:
            print(Fore.GREEN + f"\nExcellent work {username}, you've successfully defended the peace!\n" + Style.RESET_ALL)
            break

        elif player_map == bmed and player_hits == 7:
            print(Fore.GREEN + f"\nExcellent work {username}, you've successfully defended the peace!\n" + Style.RESET_ALL)
            break

        elif player_map == blarge and player_hits == 10:
            print(Fore.GREEN + f"\nExcellent work {username}, you've successfully defended the peace!\n" + Style.RESET_ALL)
            break

        comp_hits += check_hit_comp(player_map, username)
        if comp_map == csmall and comp_hits == 5:
            print(Fore.RED + "\nMission failed, we'll get 'em next time!\n" + Style.RESET_ALL)
            break

        elif comp_map == cmed and comp_hits == 7:
            print(Fore.RED + "\nMission failed, we'll get 'em next time!\n" + Style.RESET_ALL)
            break

        elif comp_map == clarge and comp_hits == 10:
            print(Fore.RED + "\nMission failed, we'll get 'em next time!\n" + Style.RESET_ALL)
            break


def game_restart():
    """
    Function to prompt user to play again or break loop
    """

    restart = input("\nWould you like to play again? (Y/N)\n")

    if restart in ["Y", "y"]:
        play_game()

    elif restart in ["N", "n"]:
        print("Thank you for playing!")

    else:
        print("Please enter Y/N!")
        game_restart()


def play_game():
    """
    Main game loop function incorperating all functions above with flavor text for story
    """

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

    player_map = choose_map(bsmall, bmed, blarge, csmall, cmed, clarge, dsmall, dmed, dlarge)

    occupied = set()
    c_occupied = set()

    print("\nPlease select coordinates for your ships!\n")
    if player_map == bsmall:
        comp_map = csmall
        dummy_map = dsmall
        for x in range(0, 5):
            player_coords(player_map, bsmall, bmed, blarge, occupied)
            comp_coords(comp_map, csmall, cmed, clarge, c_occupied)
    elif player_map == bmed:
        comp_map = cmed
        dummy_map = dmed
        for x in range(0, 7):
            player_coords(player_map, bsmall, bmed, blarge, occupied)
            comp_coords(comp_map, csmall, cmed, clarge, c_occupied)
    elif player_map == blarge:
        comp_map = clarge
        dummy_map = dlarge
        for x in range(0, 10):
            player_coords(player_map, bsmall, bmed, blarge, occupied)
            comp_coords(comp_map, csmall, cmed, clarge, c_occupied)

    print(f"\n{username} formation confirmed!")
    player_map.draw()

    print("\nSquid formation assembling...\n")
    print(Fore.BLUE + "\nBEGIN THE ATTACK!\n" + Style.RESET_ALL)

    attempts = []

    game_loop(player_map, comp_map, dummy_map, username, attempts)

    game_restart()


play_game()
