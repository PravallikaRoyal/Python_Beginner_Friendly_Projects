The Number Guessing Game 🤔🔢
Welcome to the ultimate test of intuition and deduction! In this command-line game, you must guess a secret number between 1 and 100 before you run out of attempts. Can you beat the odds?

Features and Rules ✨:
1. Difficulty Modes: Challenge yourself with two distinct modes:
Easy: 10 attempts 🟢
Hard: 5 attempts 🔴

2. Intelligent Hints: After every incorrect guess, the program provides immediate feedback (Too High or Too Low) to guide your next attempt.

3. Randomized Target: The secret number is randomly generated between 1 and 100 at the start of every game.

4. Clear Tracking: The number of remaining turns is displayed before each new guess.

Code Structure Highlights 💡:
1. Difficulty Setting: The set_difficulty() function uses conditional logic to assign the correct number of attempts based on the user's choice.

2. Guess Validation: The check_answer() function determines if the user's input matches the actual_answer and manages the turn counter.

3. Game Loop: The main game() function runs continuously until the user guesses correctly or the turns counter hits zero.

Technologies Used 💻
1. Python: The core language for game logic.
2. random Module (specifically randint): Used to select the secret number.
3. art Module: (Assumed) Used to display a starting logo for an engaging visual entrance.

Contribution 🤝
Got ideas for how to make the game even more engaging? Potential contributions include:
1. Adding an 'Impossible' mode with only 3 turns.
2. Implementing a score tracker for multiple successful rounds.
3. Input validation to ensure the user only enters numbers.

Feel free to fork the repository and contribute! Happy guessing! 🚀