# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] **Game purpose:** The game is a number guessing game where the player tries to guess a randomly generated secret number within a limited number of attempts. After each valid guess, the game gives a hint to help the player get closer to the secret number.

- [x] **Bugs found:** I found that the higher/lower hints pointed in the wrong direction, numbers outside the allowed range were accepted as guesses, and the attempt counter could end the game too early.

- [x] **Fixes applied:** I moved `check_guess()` and `parse_guess()` into `logic_utils.py`. I corrected the higher/lower hint directions and added validation so guesses outside the current difficulty's range are rejected. I also added pytest tests to verify both fixes.

## 📸 Demo Walkthrough

1. The user starts a game on Normal difficulty, which uses a range of 1–100.
2. The user enters a guess below the secret number, and the game tells them to go higher.
3. The user enters a guess above the secret number, and the game tells them to go lower.
4. If the user enters an out-of-range number such as `0`, the game rejects it and displays `Guess must be between 1 and 100.`
5. The user continues guessing until they find the secret number or run out of attempts.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

All 7 automated tests passed using pytest.

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
