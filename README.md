# Sinking Ships!

## Welcome to the fleet!

Sinking ships is a command-line Python3 game of strategy (and more than a bit of luck).

Based primarily on the classic pen-and-paper game Battleships, Sinking Ships takes further inspiration from the eponymous 'Sinking Ships' mini-game in the 2002 video game Legend of Zelda - Wind Waker, where the player must locate and eliminate enemy squid before they have the chance to wreack havoc. The setting of the minigame combined with the mechanism of battleships is what constitutes Sinking Ships - a casual game with a humerous edge for anyone to while away a few minutes on.

Zee fiends approach!

---

## How to play

1. Run the program from the host site on Heroku.
2. Enter your username when prompted.
3. Choose your map size from small, medium or large - the number of 'ships' at your disposal is notified to the user here.
4. Check over your board, and use the prompt to position your ships by using columns and rows - ships are signified by the string "B" - and see the result of your board when finished.
5. Begin attacking your opponents board by supplying a column and row integer to prompt an attack on the corresponding unit of the board.
6. When all of your opponents squid are sunk, or your own ships, you win or lose!
7. Play again or quit the game.

## Target users

The scope of user for a program like this is very wide - it is hopefully a diversionary bit of software for anyone to enjoy, but will most likely be most enjoyed by a user with a background in coding.

## Features and functions

- **Username** 

When first running the program, the first function is to record the players username. This function is in place to increase familiarity with the game and for future text prompts to have a personal touch to them, as well as providing the first instance of input validation in the codebase.

- **Map size & board**

There are 3 sizes of map to select, with each increase in size providing more ships to place. This is accomplished by use of the board package (see technologies used), declaring a small, medium and large map as a global variable for both the computer and the user to interact with, and the code to call back to throughout the code structure. The board itself is populated by a anterior function that populates each 'cell' of the board with the tilde key - this was chosen to represent the sea waves and give a visual pop to the game space, to avoid it feeling to visually empty.
To differentiate between the boards, the computer board is populated by the dash symbol. This is to help the user know which board is being shown, especially important on the smaller display afforded by the Heroku app.

-**Ship placement**

The next stage in the application is for the user to select the coordinates for their ships. This function is run a set amount of times depending on map size and will populate the board with the ship symbol, which is a "B" string.

Once selected, the user can see the end result of their formation choice. The aim here was for the board to be called immediately to give an optical reminder to the player and keep the flow of information coming.

The application will then populate the computers map with a function that uses Python3's built-in random interger generator to initialise two random numbers, which is then used to populate the computer board. At the same time, there is a dummy board being generated and populated in the same cells, which is used to give a visual for the players attacks without revealing the location of the computers other ships.

- **Attacking & game loop**

The game will then prompt the user for the first attack. The input of the function is identical to the coordination of the defence - ie entering an attack column and row. The game will then interpret the input depending on the fill of the opposition board - if the cell contains a ship, an X symbol will be printed onto the dummy board which is then displayed to the player. 

Concurrently the computer attack function will check for a hit on the player board, again utilising the randrange function to pull integers within the boards bounds and enter them into the function, which then checks the cell population.

Misses are displayed on the board as a O symbol. This is a point of differentiation so the player can determine the state of their board and from there be able to make an informed decision on where to attack next.

When the game is completed, the player will be presented with an option to either break the game loop and leave the application or play again, starting the main play game function again and beggining another play loop.

## Future features

- **Colored boards**

(See bugs) One of the problems encountered in creation of the game is the dovetail between the package generating the board and the one generating color for the characters in the command line didn't gel, and provided boards with a lot of ascii errors. Future releases of the game would hopefully rectify this and have the board be more visually appealing to the user.

- **Ship variants**

Further versions of the game will give the user an ability to have an array of multi-celled ships rather than just the single string. This makes the game more interesting and tactical, and dampen the role of luck in a win or a loss. This feature was a casualty of time constraints during development.

- **Diagonal positioning**

Following on from ship variants, the multi-celled ships will have the ability to be placed diagonally and not just on a x or y-axis.

## Testing

### Validation


### PEP8 (Pycodestyle)



## Technology and additional software used
- Python3
    - [random](https://docs.python.org/3/library/random.html)
        - Random.randrange function used to generate random coordinates for placement of enemy ships on computer board.
    - [board](https://pypi.org/project/board/#description)
        - Used to implement a general board structure in order to somplify the actual process of generating a game space.
    - [colorama](https://pypi.org/project/colorama/)
        - Fore aspect of Colorama used to provide a pop of color to increase visual enjoyment for the user.
    - [PEP8 (aka pycodestyle)](https://peps.python.org/pep-0008/)
        - Main linter used to list any abnormalities in code structure and layout.
        
## Bugs

# Development

# Unfixed Bugs

## Deployment

Application was created in Gitpod Code IDE and hosted on [Heroku](https://sinking-ships-ec79824176fc.herokuapp.com/).
The process for deployment is listed below;

1. Generate dependencies to the requirements.txt file in the IDE by running **pip3 freeze > requirements.txt**.
2. Log into Heroku and click **create new app**.
3. Name the app and fill in required information.
4. On the app dashboard, click on settings and go to **Config Vars**.
5. Add key -> **PORT** and value -> **8000**.
6. In the same page, add the **Python and NodeJS** buildpacks (in that order).
7. Click on deploy and then **deployment method -> GitHub**.
8. Connect to GitHub and **link to project name(Sinking Ships)**.
9. Click deploy -> main branch from **manual deployment** section.
10. Once successfully deployed, click **view app**.

## Credits

- As always many thanks to my mentor Dick Vlandaaren.
- Inspiration taken from Sinking Ships in the [Legend of Zelda : The Wind Waker](https://www.zeldadungeon.net/wiki/Sinking_Ships). 




