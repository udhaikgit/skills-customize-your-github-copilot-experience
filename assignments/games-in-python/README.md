
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a classic Hangman game in Python using strings, loops, conditionals, and user input. Students will practice random word selection, tracking game state, and creating a complete turn-based gameplay loop.

## 📝 Tasks

### 🛠️ Set Up the Game State

#### Description
Create the core game structure for a Hangman game. The program should choose a secret word, initialize the guessed letters list, and show the current progress to the player.

#### Requirements
Completed program should:

- Store a list of words and randomly choose one at the start of the game.
- Display a placeholder for each letter in the word, such as `_ _ _ _`.
- Track which letters have already been guessed.
- Keep a counter for incorrect guesses remaining or total wrong attempts.

### 🛠️ Play the Guessing Loop

#### Description
Write the main gameplay loop so the player can guess letters and the game responds appropriately until the word is solved or the player runs out of attempts.

#### Requirements
Completed program should:

- Prompt the player to enter one letter at a time.
- Check whether the guessed letter is in the secret word.
- Reveal correctly guessed letters in the word display.
- Decrease remaining attempts for incorrect guesses.
- Prevent repeated guesses from counting twice.
- End the game with a win message if the word is fully guessed.
- End the game with a lose message if the player runs out of attempts.
