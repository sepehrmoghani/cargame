# Sepehr's Car Game
This is a simple car game written in Python using the Pygame library. The game features a player-controlled car and an enemy car that move across the screen, with the player trying to avoid collision with the enemy car. The game becomes progressively harder over time, with the enemy car moving faster as the player progresses through levels.

## Getting Started
To run this game, you will need to have Python and Pygame installed on your computer. You can install them by following the instructions on the official Python and Pygame websites. You will also need to have an image of a car saved on your computer with the name "myCar.png" and another image of a car with the name "theyCar.png"

### Prerequisites
* Python 3.x
* Pygame library
* "myCar.png" and "theyCar.png" images
### Running the game
1. Clone or download the repository to your computer
2. Open a terminal and navigate to the directory where you have cloned the repository
3. Run the command python main.py
### Gameplay
The game starts with the player-controlled car on the left lane and the enemy car on the right lane. The player can use the left and right arrow keys to move the car between lanes to avoid collision with the enemy car. As the player progresses through levels, the enemy car moves faster and becomes harder to avoid.

### Scoring
The player's score is determined by the level they reach before they collide with the enemy car. The level increases every 3 seconds and the speed of the enemy car increases with each level.

### Game Over
When the player collides with the enemy car, the game is over. The player is prompted to enter their name and the game saves their score to a local SQLite3 database and shows the top 10 scores. The player can then choose to play again.

### Built With
* Python - Programming language
* Pygame - Game development library
* SQLite3 - Database management system

### Author
SEPEHR MOGHANI

### Acknowledgments
Pygame documentation and tutorials

GitHub community
