from colorama import Fore, Style
import board
from random import randrange
import time

# define ship and hit icons for visual indicator on maps
ships = ["B"]
hit = ["X"]
miss = ["O"]

# define small/medium/large user boards
user_small = board.Board((6, 6))

user_med = board.Board((8, 8))

user_large = board.Board((10, 10))

# define computer board size
comp_small = board.Board((6, 6))

comp_med = board.Board((8, 8))

comp_large = board.Board((10, 10))

# define small/medium/large dummy boards
# dummy board for visual of user attack without showing comp ship positions
dummy_small = board.Board((6, 6))

dummy_med = board.Board((8, 8))

dummy_large = board.Board((10, 10))


def create_user():
    """
    function for player username registration for later use
    """

    while True:
        username = input("\nWho are you?\n")
        if username:
            print(
                Fore.BLUE +
                f"\nWelcome to the fleet {username}!\n" +
                Style.RESET_ALL)
            return username
        else:
            print(Fore.RED + "I can't hear you! Try again." + Style.RESET_ALL)


def choose_map(
    username, user_small, user_med, user_large, comp_small, comp_med,
    comp_large, dummy_small, dummy_med, dummy_large
        ):
    """
    function to choose map size for game
    """

    while True:

        map_size = input("Please choose a map size - [S/M/L]\n")
        if map_size in ["S", "s"]:
            # populate board axis with numbers for small boards
            user_small.populate("012345", user_small.iterline((0, 0), (1, 0)))
            user_small.populate("12345", user_small.iterline((0, 1), (0, 1)))

            comp_small.populate("012345", user_small.iterline((0, 0), (1, 0)))
            comp_small.populate("12345", user_small.iterline((0, 1), (0, 1)))

            dummy_small.populate("012345", user_small.iterline((0, 0), (1, 0)))
            dummy_small.populate("12345", user_small.iterline((0, 1), (0, 1)))

            print("\nSmall map selected!\n")
            print("\nYou have 5 ships!\n")
            print("------------")
            print(
                Fore.BLUE + "\nPlease choose coordinates from 1 to 5!\n"
                + Style.RESET_ALL)
            print(f"{username}'s board")

            user_small.draw()
            player_map = user_small

        elif map_size in ["M", "m"]:
            # populate board axis with numbers for medium boards
            user_med.populate("01234567", user_med.iterline((0, 0), (1, 0)))
            user_med.populate("1234567", user_med.iterline((0, 1), (0, 1)))

            comp_med.populate("01234567", user_med.iterline((0, 0), (1, 0)))
            comp_med.populate("1234567", user_med.iterline((0, 1), (0, 1)))

            dummy_med.populate("01234567", user_med.iterline((0, 0), (1, 0)))
            dummy_med.populate("1234567", user_med.iterline((0, 1), (0, 1)))

            print("\nMedium map selected!\n")
            print("\nYou have 8 ships!\n")
            print("------------")
            print(
                Fore.BLUE + "\nPlease choose coordinates from 1 to 7!\n"
                + Style.RESET_ALL)
            print(f"{username}'s board")
            user_med.draw()
            player_map = user_med

        elif map_size in ["L", "l"]:
            # populate board axis with numbers for large boards
            user_large.populate("0123456789",
                                user_large.iterline((0, 0), (1, 0)))
            user_large.populate("123456789",
                                user_large.iterline((0, 1), (0, 1)))

            comp_large.populate("0123456789",
                                user_large.iterline((0, 0), (1, 0)))
            comp_large.populate("123456789",
                                user_large.iterline((0, 1), (0, 1)))

            dummy_large.populate("0123456789",
                                 user_large.iterline((0, 0), (1, 0)))
            dummy_large.populate("123456789",
                                 user_large.iterline((0, 1), (0, 1)))

            print("\nLarge map selected!\n")
            print("\nYou have 10 ships!\n")
            print("------------")
            print(
                Fore.BLUE + "\nPlease choose coordinates from 1 to 9!\n"
                + Style.RESET_ALL)
            print(f"{username}'s board")
            user_large.draw()
            player_map = user_large

        else:
            print(Fore.RED + "What! Please select S/M/L\n" + Style.RESET_ALL)
            return choose_map(
                    username, user_small, user_med, user_large,
                    comp_small, comp_med, comp_large,
                    dummy_small, dummy_med, dummy_large
                        )

        return player_map


def player_coords(player_map, user_small, user_med, user_large, occupied,
                  maxcol, maxrow):
    """
    Function for selection of ship placement on user board
    """
    # Place player coords within maxcol/row parameters
    while True:
        try:
            col = int(input("Please select column: "))
            row = int(input("Please select row: "))
            if 1 <= col <= maxcol \
                    and 1 <= row <= maxrow \
                    and (row, col) \
                    not in occupied:
                player_map.populate(
                    ships, player_map.iterline((col, row), (1, 0)))
                # Add to occupied set to avoid repetition
                occupied.add((row, col))
                # Comfirmation of placed coordinates
                print(Fore.GREEN + f"\n Ship placed! - {col}, {row} \n"
                      + Style.RESET_ALL)
            # Validation for coordinates out of bounds
            else:
                print(
                    Fore.RED +
                    "\nPlease select new coordinates within game bounds!\n"
                    + Style.RESET_ALL)
                player_coords(
                    player_map, user_small, user_med, user_large,
                    occupied, maxcol, maxrow)
                break
        # Defensive programming for invalid data types
        except ValueError:
            print(
                Fore.RED +
                "\nInvalid input! Please enter a number!\n" +
                Style.RESET_ALL)
            player_coords(
                player_map, user_small, user_med, user_large,
                occupied, maxcol, maxrow)
        break

    return player_map, occupied


def comp_coords(comp_map, comp_small, comp_med, comp_large,
                c_occupied, comp_maxcol, comp_maxrow):
    """
    Function for computer ship placement on all board sizes
    """
    # Random integer range defined by comp_maxcol/row
    while True:
        for ship in ships:
            col = randrange(1, comp_maxcol)
            row = randrange(1, comp_maxrow)
            if ((row, col)) in c_occupied:
                comp_coords(
                    comp_map, comp_small, comp_med, comp_large,
                    c_occupied, comp_maxcol, comp_maxrow)
            # Populate map with ships
            else:
                comp_map.populate(
                    ships, comp_map.iterline((col, row), (1, 0)))
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
    print(Fore.BLUE + "Squid Map" + Style.RESET_ALL)
    dummy_map.draw()
    try:
        # Input prompt for user attack
        col = int(input("\nEnter your attack column: "))
        row = int(input("Enter your attack row: "))
        # Suspend function for more digestible game flow
        time.sleep(1)

        if ((col, row)) in attempts:
            # Check if in attempts array before hit check
            print(Fore.BLUE + "Please use new coordinates!" + Style.RESET_ALL)
            return check_hit_player(comp_map, dummy_map, username, attempts)
            # Disallow hits to number axis
        elif col == 0:
            print(Fore.RED + "Please select a coordinate within game bounds!"
                  + Style.RESET_ALL)
            return check_hit_player(comp_map, dummy_map, username, attempts)

        elif row == 0:
            print(Fore.RED + "Please select a coordinate within game bounds!"
                  + Style.RESET_ALL)
            return check_hit_player(comp_map, dummy_map, username, attempts)

        elif comp_map[col, row] == "B":
            print(Fore.BLUE + f"\n{username} attacks {col}, {row}!"
                  + Style.RESET_ALL)
            # Hit message for successful attack
            print(Fore.GREEN + "\nKABOOOOOM! Direct hit!\n" + Style.RESET_ALL)
            # Print attack to dummy board for user visual
            dummy_map.populate(hit, dummy_map.iterline((col, row), (1, 0)))
            print(Fore.BLUE + "Squid Map" + Style.RESET_ALL)
            # Display dummy board
            dummy_map.draw()
            # Add chosen integers to attempts array
            attempts.append((col, row))

        else:
            # Miss message for unsuccessful attack
            print(Fore.BLUE + f"\n{username} attack {col}, {row}!"
                  + Style.RESET_ALL)
            print(Fore.BLUE + "\nSPLOOOOOSH! Missed!\n" + Style.RESET_ALL)
            dummy_map.populate(miss, dummy_map.iterline((col, row), (1, 0)))
            # Display dummy board
            print(Fore.BLUE + "Squid Map" + Style.RESET_ALL)
            dummy_map.draw()
            attempts.append((col, row))
            # If failed attack, nullify hit count
            impact = 0

    except ValueError:
        # Validation for non-integer input
        print(Fore.RED + "Please enter a number!" + Style.RESET_ALL)
        return check_hit_player(comp_map, dummy_map, username, attempts)
        # Specific error for board out of bounds integers
    except board.Board.OutOfBoundsError:
        print(
            Fore.RED + "Please select a coordinate within game bounds!"
            + Style.RESET_ALL)
        return check_hit_player(comp_map, dummy_map, username, attempts)

    return impact


def check_hit_comp(player_map, username, comp_maxcol, comp_maxrow, c_attempts):
    """
    Function to check if player hit on comp_board is successful
    """
    # Suspend function for more digestible game flow
    time.sleep(1)

    # Same as player attack, assume hit by default
    impact = 1

    # Random integers called for attack on player board within comp_maxcol/row
    col = randrange(1, comp_maxcol)
    row = randrange(1, comp_maxrow)

    if player_map[row, col] == "B":
        print(Fore.RED + "OH NO! They got us!\n" + Style.RESET_ALL)
        # Add hit marker to player board
        player_map.populate(hit, player_map.iterline((col, row), (1, 0)))
        print(Fore.BLUE + f"{username}'s board: " + Style.RESET_ALL)
        # Display player board
        player_map.draw()
        c_attempts.append((col, row))

    elif ((col, row)) in c_attempts:
        impact = 0
        return check_hit_comp(player_map, username, comp_maxcol,
                              comp_maxrow, c_attempts)

    else:
        print(Fore.BLUE + "Not even close!\n" + Style.RESET_ALL)
        # Add miss marker to player board
        player_map.populate(miss, player_map.iterline((col, row), (1, 0)))
        # Display user board
        print(Fore.BLUE + f"{username}'s board: " + Style.RESET_ALL)
        c_attempts.append((col, row))
        player_map.draw()
        impact = 0

    return impact


def game_loop(
        player_map, comp_map, dummy_map,
        username, attempts, c_attempts,
        win, maxcol, maxrow, comp_maxcol, comp_maxrow):
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
        print(f"{username} score: {player_hits}!")
        print("\nThe squid are closing in...!\n")
        if player_hits == win:
            print(Fore.BLUE + "\nGAME OVER!\n" + Style.RESET_ALL)
            print(
                Fore.GREEN +
                f"\nExcellent work {username}, you've saved the island!"
                + Style.RESET_ALL)
            break

        # Add up return from computer check hit function for winning score
        comp_hits += check_hit_comp(
            player_map, username, comp_maxcol, comp_maxrow, c_attempts)
        print(f"Squid score: {comp_hits}!")
        if comp_hits == win:
            print(Fore.BLUE + "\nGAME OVER!\n" + Style.RESET_ALL)
            print(
                Fore.RED +
                "\nMission failed, we'll get 'em next time!\n" +
                Style.RESET_ALL)
            break


def game_restart(player_map, comp_map, dummy_map):
    """
    Function to prompt user to play again or break loop
    """
    # Clear all boards for repopulation on next game loop
    player_map.clear()
    comp_map.clear()
    dummy_map.clear()

    restart = input("\nWould you like to play again? (Y/N)\n")

    if restart in ["Y", "y"]:
        return play_game()

    elif restart in ["N", "n"]:
        print(Fore.BLUE + "Thank you for playing!" + Style.RESET_ALL)
    # Validating input to only Y or N, or raise an error
    else:
        print("Please enter Y/N!")
        return game_restart(player_map, comp_map, dummy_map)


def play_game():
    """
    Main game loop function containing all functions
    """

    print(Style.RESET_ALL + "\nWelcome to\n")
    print("------------------\n")
    print(Fore.CYAN + "S I N K I N G  S H I P S\n" + Style.RESET_ALL)
    print("------------------\n")

    username = create_user()
    # Flavor text for game setting
    print("\nI am the great Admiral Dolvalski!\n")
    print("Look sharp, for we are the sole protectors of this island!\n")
    print("Red alert! Schools of deadly squid are attacking!\n")
    print("The fiends approach! Command the fleet and defend the island!\n")
    print("Choose an angle of attack, and sink them all!\n")
    print(Fore.BLUE + f"We're counting on you {username}!\n" + Style.RESET_ALL)
    # Call 9 global variable maps
    player_map = choose_map(
        username, user_small, user_med, user_large, comp_small, comp_med,
        comp_large, dummy_small, dummy_med, dummy_large
        )
    # Initialise occupied cell sets to be added to in coord functions
    occupied = set()
    c_occupied = set()

    print("\nPlease select coordinates for your ships!\n")
    # If block to match map sizes & declare maxcol/row and win threshold
    if player_map == user_small:
        comp_map = comp_small
        dummy_map = dummy_small
        maxcol = 5
        comp_maxcol = 6
        maxrow = 5
        comp_maxrow = 6
        win = 5
        # For loop to apply function for as many ships
        for x in range(0, 5):
            player_coords(
                player_map, user_small, user_med, user_large,
                occupied, maxcol, maxrow)
            comp_coords(
                comp_map, comp_small, comp_med, comp_large,
                c_occupied, comp_maxcol, comp_maxrow)
    elif player_map == user_med:
        comp_map = comp_med
        dummy_map = dummy_med
        maxcol = 7
        comp_maxcol = 8
        maxrow = 7
        comp_maxrow = 8
        win = 8
        for x in range(0, 8):
            player_coords(
                player_map, user_small, user_med, user_large,
                occupied, maxcol, maxrow)
            comp_coords(
                comp_map, comp_small, comp_med, comp_large,
                c_occupied, comp_maxcol, comp_maxrow)
    elif player_map == user_large:
        comp_map = comp_large
        dummy_map = dummy_large
        maxcol = 9
        comp_maxcol = 10
        maxrow = 9
        comp_maxrow = 10
        win = 10
        for x in range(0, 10):
            player_coords(
                player_map, user_small, user_med, user_large,
                occupied, maxcol, maxrow)
            comp_coords(
                comp_map, comp_small, comp_med, comp_large,
                c_occupied, comp_maxcol, comp_maxrow)

    # Coordinates review for player
    print(Fore.GREEN + f"{username} coordinates - {occupied}\n")
    print(f"{username} formation confirmed!" + Style.RESET_ALL)
    # Formation review for player
    player_map.draw()

    # Squid formation coordinates with breathers
    print("\nSquid formation assembling...")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("Squid formation assembled!\n")

    time.sleep(1)

    # Game rules
    print("------------")
    print("Game Rules!\n")
    print(f"{username}'s ships = 'B' ")
    print(Fore.GREEN + "Hit = X" + Style.RESET_ALL)
    print(Fore.RED + "Miss = O" + Style.RESET_ALL)
    print("------------")
    print(Fore.BLUE + "\nMay your aim be true!" + Style.RESET_ALL)
    print(Fore.BLUE + "\nBEGIN THE DEFENCE!\n" + Style.RESET_ALL)

    # Initialise attempts array
    attempts = []
    c_attempts = []
    # Main game loop call
    game_loop(
        player_map, comp_map, dummy_map,
        username, attempts, c_attempts,
        win, maxcol, maxrow, comp_maxcol, comp_maxrow)
    # Restart game when winnner
    game_restart(player_map, comp_map, dummy_map)


play_game()
