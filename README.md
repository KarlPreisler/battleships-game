## Battleships Game
The Battleship Game is a game that runs in the Python terminal window, which runs in the Code Institute mock terminal on Heroku. 
Users can practice their Battleships skills against a computer.

[Here is the live version of my project.](https://thebattleships-game.herokuapp.com/)

## How to play
- The Battleships game is a classic game usually played with pen and paper. Here is a link that further explains the game on [Wikipedia](https://en.wikipedia.org/wiki/Battleship_(game))
- When entering the game the user will be asked to provide their name, once submitted the user and computer boards will be displayed.

![Screenshot_20221128_010211](https://user-images.githubusercontent.com/114813115/204273765-99c29d07-b2ce-489c-ac07-f46a367f6f01.png)

- Both boards will contain 5 rows and 5 columns, on the players board there are 4 ships, indicated with "@".

![Screenshot_20221128_010254](https://user-images.githubusercontent.com/114813115/204273865-3555bf43-603f-42bf-ae57-bf827aac3bff.png)

- The computer's ships are hidden from the user, since showing them would defeat the object of the game.
- Users are then able to choose a row and a column to try to hit the computers ships, and the computer is assigned random coordinates to try and hit the users ships.
- All guesses that misses a ship are indicated with "X" on the boards, and any hit on a ship is indicated with "*". 
- After each round, the result of the round is printed to the terminal, together with the current scores.

![Screenshot_20221128_010318](https://user-images.githubusercontent.com/114813115/204274007-f43a1396-354f-4b9f-b03e-c08bd77ce347.png)

- This is followed by a question being displayed asking the user if they wish to continue, restart or quit the game completely.
- A hit increases the score by 1, and the first one to reach a score of 4 wins the game.
- This is because a score of 4 means that all enemy ships have been hit, and this will cause the game to restart. 
- If both user and computer hit their opponent's last ship simultaneously, the game is a draw and will start over.

## Features
Random Board generation
- Ships are randomly placed on both the computers and players board.
- The computer's ships are hidden from the player.
- Collect user input 
- Keep track of scores
- Determine winner 
- Input Validation
- Name input must be a string of letters between 1-20 letters.
- Row and column guesses must be a number.
- Warning message if player guess is outside of grid.
- Users cannot guess the same coordinates twice.
- Data is maintained in class instances. 

## Future Features
- Let users choose the size of the grid.
- Let users choose the number of ships on each board.
- Let users choose the locations for their ships.
- Allow ships to be larger than 1x1.


## Data Model
- I used a Board class as my model in order to create two class instances to hold both the player's and computer's board.
- The Board class stores the board size, number of ships, positions of the ships, type of board, name of board and the guesses by the player and the computer.
- The class also contains methods for the logic of the game, such as a print method to print out current board, a validate method to validate user input, add_ship 
- method to add ships to the board, as well as add_guess method to add guesses and return a result. This class also contains the guesses and ships list. 

## Testing
- I have confirmed that the game functions as it should in the Python terminal.
- I have confirmed that the game functions as it should in the Code Institute Heroku terminal.
- I have confirmed that the terminal output is clear in terms of readability.
- I have made sure that the program does not crash because of invalid user input.

![Screenshot_20221128_010415](https://user-images.githubusercontent.com/114813115/204274218-623113c7-e35c-4094-96c2-582f64fbad90.png)

- I have made sure that all error messages clearly explain the given issue and provide a solution for the user.
- 
![Screenshot_20221128_010438](https://user-images.githubusercontent.com/114813115/204274265-59c27e5d-f20b-4018-8d93-215cfd08cc2b.png)

## Further Testing
![PP3 Mockup](https://user-images.githubusercontent.com/114813115/204272317-35dda2a7-f7e4-4008-a296-5ccfec17f9fe.png)

## Bugs
- There are no unfixed bugs.

## Validator Testing
- PEP8: 

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




