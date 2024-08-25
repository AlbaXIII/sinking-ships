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


bsmall = board.Board((5, 5))
bsmall.populate(bsea())

bmed = board.Board((7, 7))
bmed.populate(bsea())

blarge = board.Board((9, 9))
blarge.populate(bsea())

# define computer board size & populate grid with csea background
csmall = board.Board((5, 5))
csmall.populate(csea())

cmed = board.Board((7, 7))
cmed.populate(csea())

clarge = board.Board((9, 9))
clarge.populate(csea())

# define small/medium/large dummy boards & populate grid with csea background
# dummy board for visual of user attack without showing comp ship positions
dsmall = board.Board((5, 5))
dsmall.populate(csea())

dmed = board.Board((7, 7))
dmed.populate(csea())

dlarge = board.Board((9, 9))
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


def choose_map(
    bsmall, bmed, blarge, csmall, cmed, clarge, dsmall, dmed, dlarge
        ):
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
            return comp_map

        elif map_size in ["M", "m"]:
            print("\nMedium map selected - 7 ships\n")
            bmed.draw()
            player_map = bmed
            comp_map = cmed
            dummy_map = dmed
            return player_map
            return comp_map

        elif map_size in ["L", "l"]:
            print("\nLarge map selected - 10 ships\n")
            blarge.draw()
            player_map = blarge
            comp_map = clarge
            dummy_map = dlarge
            return player_map
            return comp_map

        else:
            print("What! Please select S/M/L")


def player_coords(player_map, bsmall, bmed, blarge, occupied):
    """
    Function for selection of ship placement on user board
    """

    while True:
        # Placement of player ships on a small board
        if player_map == bsmall:
            try:
                col = int(input("Please select column: "))
                row = int(input("Please select row: "))
                if 0 <= row < 5 \
                        and 0 <= col < 5 \
                        and (row, col) \
                        not in occupied:
                    bsmall.populate(ships, bsmall.iterline((row, col), (1, 0)))
                    # Add chosen integer to occupied set
                    occupied.add((row, col))
                else:
                    print(
                        Fore.RED +
                        "Invalid coordinates - please try again!"
                        + Style.RESET_ALL)
                    player_coords(player_map, bsmall, bmed, blarge, occupied)
                    break
            except ValueError:
                print(
                    Fore.RED +
                    "Invalid input! Please enter a number!" +
                    Style.RESET_ALL)
                player_coords(player_map, bsmall, bmed, blarge, occupied)
            break
        # Placement of player ships on a medium board
        elif player_map == bmed:
            try:
                row = int(input("Please select column: "))
                col = int(input("Please select row: "))
                if 0 <= row < 7 \
                        and 0 <= col < 7 \
                        and (row, col) \
                        not in occupied:
                    bmed.populate(ships, bmed.iterline((row, col), (1, 0)))
                    occupied.add((row, col))
                else:
                    print(
                        Fore.RED +
                        "Invalid coordinates - please try again!"
                        + Style.RESET_ALL)
                    player_coords(player_map, bsmall, bmed, blarge, occupied)
                    break
            except ValueError:
                print(
                    Fore.RED +
                    "Invalid input! Please enter a number!"
                    + Style.RESET_ALL)
                player_coords(player_map, bsmall, bmed, blarge, occupied)
            break
        # Placement of player ships on a large board
        elif player_map == blarge:
            try:
                row = int(input("Please select column: "))
                col = int(input("Please select row: "))
                if 0 <= row < 9 \
                        and 0 <= col < 9 \
                        and (row, col) \
                        not in occupied:
                    blarge.populate(ships, blarge.iterline((row, col), (1, 0)))
                    occupied.add((row, col))
                else:
                    print(
                        Fore.RED +
                        "Invalid coordinates - please try again!"
                        + Style.RESET_ALL)
                    player_coords(player_map, bsmall, bmed, blarge, occupied)
                    break
            except ValueError:
                print(
                    Fore.RED +
                    "Invalid input! Please enter a number!"
                    + Style.RESET_ALL)
                player_coords(player_map, bsmall, bmed, blarge, occupied)
            break

    return player_map, occupied


def comp_coords(comp_map, csmall, cmed, clarge, c_occupied):
    """
    Function for computer ship placement on all board sizes
    """

    if comp_map == csmall:
        maxcol = 4
        maxrow = 4
    elif comp_map == cmed:
        maxcol = 6
        maxrow = 6
    elif comp_map == clarge:
        maxcol = 8
        maxrow = 8

    while True:
        for ship in ships:
            col = randrange(0, maxcol)
            row = randrange(0, maxrow)
            if ((row, col)) in c_occupied:
                comp_coords(comp_map, csmall, cmed, clarge, c_occupied)
            else:
                comp_map.populate(
                    ships, comp_map.iterline((row, col), (1, 0)))
                c_occupied.add((row, col))
                break
        return comp_map


def check_hit_player(comp_map, dummy_map, username, attempts):
    """
    Function to check if player hit on comp_board is successful
    """

    print(f"\n{username}'s turn to attack!\n")
    # Default to success to add to hit counter
    impact = 1

    try:

        col = int(input("Enter your attack column: "))
        row = int(input("Enter your attack row: "))

        if comp_map[col, row] == "B":
            # Hit message for successful attack, using Colorama
            print(Fore.GREEN + "\nKABOOOOOM! Direct hit!\n" + Style.RESET_ALL)
            # Print attack to dummy board for user visual
            dummy_map.populate(hit, dummy_map.iterline((col, row), (1, 0)))
            print("Enemy board:")
            # Display dummy board
            dummy_map.draw()
            # Add chosen integers to attempts array
            attempts.append((col, row))

        elif ((col, row)) in attempts:
            print(Fore.BLUE + "Please use new coordinates!" + Style.RESET_ALL)
            # Loop function if user input already used
            check_hit_player(comp_map, dummy_map, username, attempts)

        else:
            # Miss message for unsuccessful attack
            print(Fore.RED + "\nSPLOOOOOSH! Missed!\n" + Style.RESET_ALL)
            dummy_map.populate(miss, dummy_map.iterline((col, row), (1, 0)))
            print("Enemy board:")
            dummy_map.draw()
            attempts.append((col, row))
            # If failed attack, nullify hit count
            impact = 0

    except ValueError:
        # Validation for non-integer input
        print(Fore.RED + "Please enter a number!" + Style.RESET_ALL)
        check_hit_player(comp_map, dummy_map, username, attempts)
        # Specific error for board out of bounds integers
    except board.Board.OutOfBoundsError:
        print(
            Fore.RED + "Please select a coordinate within game bounds!"
            + Style.RESET_ALL)
        check_hit_player(comp_map, dummy_map, username, attempts)

    return impact


def check_hit_comp(player_map, username):
    """
    Function to check if player hit on comp_board is successful
    """

    print("\nThe Squid are closing in...\n")
    # Same as player attack, hit by default
    impact = 1
    # Random integers called for attack on player board
    if player_map == bsmall:
        col = randrange(0, 4)
        row = randrange(0, 4)
    elif player_map == bmed:
        col = randrange(0, 6)
        row = randrange(0, 6)
    elif player_map == blarge:
        col = randrange(0, 8)
        row = randrange(0, 8)

    if player_map[row, col] == "B":
        print(Fore.GREEN + "Oh no! They got us!\n" + Style.RESET_ALL)
        # Add hit marker to player board
        player_map.populate(hit, player_map.iterline((col, row), (1, 0)))
        print(f"{username}'s board: ")
        # Display player board
        player_map.draw()

    else:
        print(Fore.RED + "Not even close!\n" + Style.RESET_ALL)
        # Add miss marker to player board
        player_map.populate(miss, player_map.iterline((col, row), (1, 0)))
        print(f"{username}'s board: ")
        player_map.draw()
        impact = 0

    return impact


def game_loop(player_map, comp_map, dummy_map, username, attempts):
    """
    Function to loop player & computer attacks until winner
    """
    # Initialise score counters
    player_hits = 0
    comp_hits = 0

    while True:
        # Add up return from check hit function for winning score
        player_hits += check_hit_player(
            comp_map, dummy_map, username, attempts)
        if player_map == bsmall and player_hits == 5:
            print(
                Fore.GREEN +
                f"\nExcellent work {username}, you've saved the island!"
                + Style.RESET_ALL)
            break

        elif player_map == bmed and player_hits == 7:
            print(
                Fore.GREEN +
                f"\nExcellent work {username}, you've saved the island!"
                + Style.RESET_ALL)
            break

        elif player_map == blarge and player_hits == 10:
            print(
                Fore.GREEN +
                f"\nExcellent work {username}, you've saved the island!"
                + Style.RESET_ALL)
            break
        # Add up return from computer check hit function for winning score
        comp_hits += check_hit_comp(player_map, username)
        if comp_map == csmall and comp_hits == 5:
            print(
                Fore.RED +
                "\nMission failed, we'll get 'em next time!\n" +
                Style.RESET_ALL)
            break

        elif comp_map == cmed and comp_hits == 7:
            print(
                Fore.RED +
                "\nMission failed, we'll get 'em next time!\n" +
                Style.RESET_ALL)
            break

        elif comp_map == clarge and comp_hits == 10:
            print(
                Fore.RED +
                "\nMission failed, we'll get 'em next time!\n" +
                Style.RESET_ALL
                )
            break


def game_restart():
    """
    Function to prompt user to play again or break loop
    """

    restart = input("\nWould you like to play again? (Y/N)\n")

    if restart in ["Y", "y"]:
        play_game()

    elif restart in ["N", "n"]:
        print(Fore.BLUE + "Thank you for playing!" + Style.RESET_ALL)
    # Validating input to only Y or N, or raise a value error
    else:
        print("Please enter Y/N!")
        game_restart()


def play_game():
    """
    Main game loop function containing all functions
    """

    print(Style.RESET_ALL + "\nWelcome to\n")
    print("------------------\n")
    print(Fore.CYAN + "S I N K I N G  S H I P S\n" + Style.RESET_ALL)
    print("------------------\n")

    username = create_user()
    # Flavor text for "Story" background
    print("\nI am the great Admiral Dolvalski!\n")
    print("Look sharp, for we are the sole protectors of this island!\n")
    print("Red alert! Schools of deadly squid are attacking!\n")
    print("The fiends approach! Command the fleet and defend the island!\n")
    print("Choose an angle of attack, and sink them all!\n")
    print(Fore.BLUE + f"We're counting on you {username}!\n" + Style.RESET_ALL)
    # Call 9 global variable maps
    player_map = choose_map(
        bsmall, bmed, blarge, csmall, cmed, clarge, dsmall, dmed, dlarge
        )
    # Initialise occupied cell sets to be added to in coord functions
    occupied = set()
    c_occupied = set()

    print("\nPlease select coordinates for your ships!\n")
    # If block to match map sizes
    if player_map == bsmall:
        comp_map = csmall
        dummy_map = dsmall
        # For loop to apply function for as many ships
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
    # Initialise attempts array
    attempts = []
    # Main game loop call
    game_loop(player_map, comp_map, dummy_map, username, attempts)
    # Restart game when winnner
    game_restart()


play_game()
