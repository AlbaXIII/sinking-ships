from colorama import Fore, Back, Style
import board
from random import randrange, randint

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
            print(
                Fore.BLUE +
                f"\nWelcome to the fleet {username}!\n" +
                Style.RESET_ALL)
            return username
        else:
            print(Fore.RED + "I can't hear you! Try again." + Style.RESET_ALL)


def choose_map(
    bsmall, bmed, blarge, csmall, cmed, clarge, dsmall, dmed, dlarge
        ):
    """
    function to choose map size for game
    """

    while True:

        map_size = input("Please choose a map size - [S/M/L]\n")
        if map_size in ["S", "s"]:
            print("\nSmall map selected - 5 ships (Range 0-4)\n")
            bsmall.draw()
            player_map = bsmall
            comp_map = csmall
            dummy_map = dsmall
            return player_map
            return comp_map

        elif map_size in ["M", "m"]:
            print("\nMedium map selected - 7 ships (Range 0-6)\n")
            bmed.draw()
            player_map = bmed
            comp_map = cmed
            dummy_map = dmed
            return player_map
            return comp_map

        elif map_size in ["L", "l"]:
            print("\nLarge map selected - 10 ships (Range 0-9)\n")
            blarge.draw()
            player_map = blarge
            comp_map = clarge
            dummy_map = dlarge
            return player_map
            return comp_map

        else:
            print("What! Please select S/M/L")


def player_coords(player_map, bsmall, bmed, blarge, occupied, maxcol, maxrow):
    """
    Function for selection of ship placement on user board
    """
    # Place player coords within maxcol/row parameters
    while True:
        try:
            col = int(input("Please select column: "))
            row = int(input("Please select row: "))
            if 0 <= col <= maxcol \
                    and 0 <= row <= maxrow \
                    and (row, col) \
                    not in occupied:
                player_map.populate(
                    ships, player_map.iterline((row, col), (1, 0)))
                # Add to occupied set to avoid repetition
                occupied.add((row, col))
            # Validation for coordinates out of bounds
            else:
                print(
                    Fore.RED +
                    "Invalid coordinates - please try again!"
                    + Style.RESET_ALL)
                player_coords(
                    player_map, bsmall, bmed, blarge, occupied, maxcol, maxrow)
                break
        # Validation for invalid data types
        except ValueError:
            print(
                Fore.RED +
                "Invalid input! Please enter a number!" +
                Style.RESET_ALL)
            player_coords(
                player_map, bsmall, bmed, blarge,
                occupied, maxcol, maxrow)
        break

    return player_map, occupied


def comp_coords(comp_map, csmall, cmed, clarge, c_occupied, maxcol, maxrow):
    """
    Function for computer ship placement on all board sizes
    """
    # Random integer range defined by maxcol/row
    while True:
        for ship in ships:
            col = randrange(0, maxcol)
            row = randrange(0, maxrow)
            if ((row, col)) in c_occupied:
                comp_coords(
                    comp_map, csmall, cmed, clarge, c_occupied, maxcol, maxrow)
            # Populate map with ships
            else:
                comp_map.populate(
                    ships, comp_map.iterline((row, col), (1, 0)))
                # Add to computer occupied set
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

        if ((col, row)) in attempts:
            # Check if in attempts array before hit check
            print(Fore.BLUE + "Please use new coordinates!" + Style.RESET_ALL)
            check_hit_player(comp_map, dummy_map, username, attempts)
            impact = 0

        elif comp_map[col, row] == "B":
            # Hit message for successful attack, using Colorama
            print(Fore.GREEN + "\nKABOOOOOM! Direct hit!\n" + Style.RESET_ALL)
            # Print attack to dummy board for user visual
            dummy_map.populate(hit, dummy_map.iterline((col, row), (1, 0)))
            print("Enemy board:")
            # Display dummy board
            dummy_map.draw()
            # Add chosen integers to attempts array
            attempts.append((col, row))

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
        impact = 0
        # Specific error for board out of bounds integers
    except board.Board.OutOfBoundsError:
        print(
            Fore.RED + "Please select a coordinate within game bounds!"
            + Style.RESET_ALL)
        check_hit_player(comp_map, dummy_map, username, attempts)
        impact = 0

    return impact


def check_hit_comp(player_map, username, maxcol, maxrow, c_attempts):
    """
    Function to check if player hit on comp_board is successful
    """

    # Same as player attack, assume hit by default
    impact = 1

    # Random integers called for attack on player board within maxcol/row
    col = randrange(0, maxcol)
    row = randrange(0, maxrow)

    if player_map[row, col] == "B" and ((col, row)) not in c_attempts:
        print(Fore.GREEN + "Oh no! They got us!\n" + Style.RESET_ALL)
        # Add hit marker to player board
        player_map.populate(hit, player_map.iterline((col, row), (1, 0)))
        print(f"{username}'s board: ")
        # Display player board
        player_map.draw()
        c_attempts.append((col, row))

    elif ((col, row)) in c_attempts:
        impact = 0
        print(
            Fore.RED +
            "\nThe squid are biding their time..." +
            Style.RESET_ALL)

    else:
        print(Fore.RED + "Not even close!\n" + Style.RESET_ALL)
        # Add miss marker to player board
        player_map.populate(miss, player_map.iterline((col, row), (1, 0)))
        print(f"{username}'s board: ")
        c_attempts.append((col, row))
        player_map.draw()
        impact = 0

    return impact


def game_loop(
        player_map, comp_map, dummy_map,
        username, attempts, c_attempts,
        win, maxcol, maxrow):
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
        print(player_hits)
        if player_hits == win:
            print(
                Fore.GREEN +
                f"\nExcellent work {username}, you've saved the island!"
                + Style.RESET_ALL)
            break

        # Add up return from computer check hit function for winning score
        comp_hits += check_hit_comp(
            player_map, username, maxcol, maxrow, c_attempts)
        print(comp_hits)
        if comp_hits == win:
            print(
                Fore.RED +
                "\nMission failed, we'll get 'em next time!\n" +
                Style.RESET_ALL)
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
    # If block to match map sizes & declare maxcol/row and win threshold
    if player_map == bsmall:
        comp_map = csmall
        dummy_map = dsmall
        maxcol = 5
        maxrow = 5
        win = 5
        # For loop to apply function for as many ships
        for x in range(0, 5):
            player_coords(
                player_map, bsmall, bmed, blarge,
                occupied, maxcol, maxrow)
            comp_coords(
                comp_map, csmall, cmed, clarge,
                c_occupied, maxcol, maxrow)
    elif player_map == bmed:
        comp_map = cmed
        dummy_map = dmed
        maxcol = 7
        maxrow = 7
        win = 7
        for x in range(0, 7):
            player_coords(
                player_map, bsmall, bmed, blarge,
                occupied, maxcol, maxrow)
            comp_coords(
                comp_map, csmall, cmed, clarge,
                c_occupied, maxcol, maxrow)
    elif player_map == blarge:
        comp_map = clarge
        dummy_map = dlarge
        maxcol = 9
        maxrow = 9
        win = 10
        for x in range(0, 10):
            player_coords(
                player_map, bsmall, bmed, blarge,
                occupied, maxcol, maxrow)
            comp_coords(
                comp_map, csmall, cmed, clarge,
                c_occupied, maxcol, maxrow)

    print(f"\n{username} formation confirmed!")
    # Formation review for player
    player_map.draw()

    print("\nSquid formation assembling...\n")
    print(Fore.BLUE + "\nBEGIN THE ATTACK!\n" + Style.RESET_ALL)
    # Initialise attempts array
    attempts = []
    c_attempts = []
    # Main game loop call
    game_loop(
        player_map, comp_map, dummy_map,
        username, attempts, c_attempts,
        win, maxcol, maxrow)
    # Restart game when winnner
    game_restart()


play_game()
