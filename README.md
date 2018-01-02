# csc148assignment1_subtract_squares

Overview: 

Assignment 1 begins a series of three related assignments on computerised games. In this assignment you will hone your skills at designing and implementing classes, including inheritance. You will end up with a simple game interface that will pit you against a weak computer opponent.

Description of classes:

The state of the game:
You will need code to keep track of the game state. The game state will need to represent which player moves next, which legal moves are available to that player, whether the game is over, and whether a particular player has won. Implement the game state features that are common to all games in a generic games state class, but implement game specific features in a subclass for each game. 

The computer's strategy:
You will also need to create code that uses some strategy to choose a move for the computer to make. 

The overall play of the game:
Finally, you will need code that manages the player's view of the game. It must allow a user to play a complete game against a computer opponent. The player's view will be text-based. It will include informing them of the aim of the game and relevant rule, prompting for a move, indicating whether a chose n move is legal, showing that move the computer has chosen, and indicating whether a player has won. 

subtract square
You will implement subtract square, a game which is played as  follows:
1. a positive whole number is randomly chosen was the starting value by some neutral entity. In our case, the computer will choose it randomly.
2.The player whose turn it is chooses some square of a positive whole number to subtract from the value, provided the chosen square is not larger. After subtracting, we have a new value and the next player chooses a square to subtract from it.
3.play continuous to alternate between the two players until no moves are possible. Whoever is about to play at that point loses!

Your job:
You will design and implement classes to support the simple game playing interface described above, class design names, and other implementation choices are left up to your taste, applying the concepts you have learned in this course. However, we insist on the following:

You must implement appropriate __repr__, __str__ and __eq__ method for each class that you define
You must have both a class for a generic game state, and a subclass for a subtract square game state. Your generic game state should be designed so that additional subclasses for other specific as-yet-unspecified, games can be added. 
You must have both a generic class for choosing moves, and a subclass that uses some really simple strategy to choose moves.
You must have a class for the game view. It must be saved in a file called game_view.py and we must be able to invoke:
$ python3 game_view.py

.... in order to play subtract square against a computer opponent.
