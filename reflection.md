# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

When I first ran the game, I noticed that the hints were backwards. For example, when I guessed `1`, the game told me to go lower even though 1 was already the lowest valid number, and this comes from the reversed hint messages in `check_guess()` in `app.py`. I also found that I could enter numbers outside the stated 1–100 range, such as `0` or negative numbers, because `parse_guess()` checks whether the input is a number but does not validate its range. Finally, the attempt counter was off by one because `st.session_state.attempts` starts at `1` instead of `0`, which caused the game to say I was out of attempts too early.

**Bug Reproduction Log**

| Input Used | Expected Behavior | Actual Behavior | Console Error / Output | Suspected Code Location |
|---|---|---|---|---|
| Guess `1` | The game should either say correct or tell me to go higher; it should never tell me to go below the minimum of 1 | The game displayed `Go LOWER!` | none | `app.py`, `check_guess()` |
| Guess `0` or a negative number such as `-5000000` | The game should reject the guess because it is outside the 1–100 range | The game accepted the number and gave a hint | none | `app.py`, `parse_guess()` |
| Reach the final attempts on Normal difficulty | The game should allow all 8 attempts before ending | The game said I was out of attempts too early | none | `app.py`, session state initialization and attempt-counting logic |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

I used ChatGPT and Claude Code to inspect, edit, and test the project code.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

Claude suggested moving `check_guess()` into `logic_utils.py` and correcting the reversed high/low hint messages. I reviewed the changes and verified them with pytest tests that checked both directions. I also manually tested the game to confirm that guesses above the secret now tell the player to go lower and guesses below the secret tell the player to go higher.



- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

Claude identified additional problems such as invalid guesses using an attempt, the New Game button always generating a secret from 1–100, and the displayed range being hard-coded to 1–100. I chose not to fix those because they were outside the two bugs I selected for this phase. I verified that leaving those issues unchanged did not interfere with my selected fixes by running the tests and manually checking the repaired behavior in the game.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

I considered a bug fixed after reviewing the code changes, running the automated tests, and checking the behavior in the game. I did not rely only on the AI saying that its changes worked.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

I initially ran pytest and all 7 tests passed. One test checked that guessing 60 when the secret is 50 gives a “Too High” outcome and tells the player to go lower. I also manually entered 0 in the Streamlit game and confirmed that it was rejected with a message saying the guess must be between 1 and 100. I later added three edge-case tests for Challenge 1, bringing the total to 10 passing tests.

- Did AI help you design or understand any tests? How?

Yes. Claude generated tests for the corrected high/low hints and for the new range validation in `parse_guess()`. It also added a test using the Easy range of 1–20, which helped verify that `parse_guess()` uses the supplied difficulty range instead of always assuming 1–100.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Streamlit reruns the Python script from top to bottom whenever the user interacts with the app. Session state allows values like the secret number, attempts, score, and game status to persist between those reruns. Without session state, those values could be reset whenever the app reruns.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

I want to continue verifying fixes with tests instead of assuming that a change works. Using pytest along with manually testing the application made it easier to confirm that the behavior actually matched what I expected.

- What is one thing you would do differently next time you work with AI on a coding task?

I would give the AI focused instructions and tell it not to change unrelated code. Working on one bug at a time made it easier to understand and verify the changes.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

This project showed me that AI-generated code still needs to be reviewed and tested carefully. AI can help find and fix problems, but I still need to decide which changes make sense and verify that they actually work.