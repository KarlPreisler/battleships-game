## Battleships Game
The Battleship Game is a game that runs in the Python terminal window, which runs in the Code Institute mock terminal on Heroku. 
Users can practice their Battleships skills against a computer.

## How to play
The Battleships game is a classic game usually played with pen and paper. Here is a link that further explains the game on [Wikipedi](https://en.wikipedia.org/wiki/Battleship_(game))a
When entering the game the user will be asked to provide their name, once submitted the user and computers boards will be displayed.
Both boards will contain 5 rows and 5 columns, on the players board there are 4 ships, indicated with "@".
The computers ships are hidden from the user, since showing them would defeat the object of the game.
Users are then able to choose a row and a column to try to hit the computers ships, and the computer is assigned random coordinates to try and hit the users ships.
All guesses that misses a ship are indicated with "X" on the boards, and any hit on a ship is indicated with "*". 
After each round, the result of the round is printed to the terminal, together with the current scores.
This is followed by a question being displayed asking the user if they wish to continue, restart or quit the game completely.
A hit increases the scores by 1, and the first one to reach a score of 4 wins the game.
This is because a score of 4 means that all enemy ships have been hit, and this will cause the game to restart. 
If both user and computer hit their opponents last ship simultaneously, the game is a draw and will start over.

## Features
Random Board generation
- Ships are randomly placed on both the computers and players board.
- The computers ships are hidden from the player.
- Collect user input 
- Keep track of scores
- Determine winner 
- Input Validation
-- Name input must be a string of letters between 1-20 letters.
-- Row and column guesses must be a number.
-- Warning message if player guess is outside of grid.
-- Users cannot guess the same coordinates twice.
- Data is maintained in class instances. 

## Data Model
I used a Board class as my model in order to create two class instances to hold both the player's and computer's board.
The Board class stores the board size, number of ships, positions of the ships, type of board, name of board and the guesses by the player and the computer.
The class also contains methods for the logic of the game, such as a print method to print out current board, a validate method to validate user input, add_ship 
method to add ships to the board, as well as add_guess method to add guesses and return a result. This class also contains the guesses and ships list. 

## Testing
- I have confirmed that the game functions as it should in the Python terminal.
- I have confirmed that the game functions as it should in the Code Institute Heroku terminal.
- I have confirmed that the terminal output is clear in terms of readability.
- I have made sure that the program does not crash because of invalid user input.
- I have made sure that all error messages clearly explains the given issue and provides a solution for the user.

## Bugs
- There are no unfixed bugs.

## Deployment 
This project was deployed using Code Institute's mock terminal for Heroku.
- Steps to deploy the site are as follow:
- Fork or clone this repository.
- Create a new Horoku app
- Set the buildbacks to python and NodeJS in that order.
- Link to Heroku app to the repository
- Click on deploy.

## Credits 
- Basic structure for the project was inspired by Code Institute PP3 Sample project, such as Board class, functions and methods.

## Acknowledgements
- My mentor Brian Machiara for great support and guidance throughout the project.




