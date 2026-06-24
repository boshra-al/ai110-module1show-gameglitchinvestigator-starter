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

- [ ] Describe the game's purpose.
  This is a number guessing game built with Streamlit. The app picks a secret number within a range that depends on the chosen difficulty (Easy: 1–20, Normal: 1–100, Hard: 1–50), and the player tries to guess it before running out of attempts. After each guess the game gives a "Go HIGHER!" or "Go LOWER!" hint, tracks your score and guess history, and lets you start a new game.

- [ ] Detail which bugs you found.
  --> Backwards hints: guessing too high told you to "Go Higher!" and guessing too low told you to "Go Lower!"
  --> Inaccurate scoring: a correct guess on the first attempt did not award the expected score (e.g. 70 instead of 100).
  --> No input constraint: Out-of-range inputs were accepted as valid guesses and still counted against  attempts instead of being rejected.

- [ ] Explain what fixes you applied.
  --> Swapped the "Higher"/"Lower" messages in `check_guess` so the hints point in the correct direction.
  --> Added a range check so guesses below `low` or above `high` show a "Try again" warning, and undid the attempt increment so an invalid guess no longer costs the player a turn.
  --> Refactored the `check_guess` logic out of `app.py` and into `logic_utils.py`, then updated the import in `app.py` to use it.
  --> Updated the import statement and the difficulty-aware subheader/range text so the displayed range matches the selected difficulty.
  --> Verified every fix by running the app in the browser and by running `pytest` until all tests passed.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Start the app with `streamlit run app.py` and open it in the browser. Pick a difficulty from the sidebar (e.g. Normal), which sets the range to 1–100 and the attempt limit.
2. Enter a guess in the text box and click **Submit Guess 🚀**. The game compares your guess to the secret number stored in session state, so the secret stays the same across reruns instead of changing every click.
3. Read the hint: guessing too high now correctly shows "📉 Go LOWER!" and guessing too low shows "📈 Go HIGHER!", so each guess narrows the range.
4. Try an out-of-range guess like 200 (or a negative number). The game shows a "Guess must be between 1 and 100. Try again." warning and does **not** deduct an attempt.
5. Keep guessing using the hints until you land on the secret number. When you win, the app shows balloons, reveals the secret, and displays your final score.
6. Click **New Game 🔁** to reset and play again, or open the **Developer Debug Info** panel at any time to see the secret, attempts, score, and guess history.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```
(.venv) boshraalzindeni@Boshras-MacBook-Pro ai110-module1show-gameglitchinvestigator-starter % python3 -m pytest
====================================================================== test session starts =======================================================================
platform darwin -- Python 3.14.4, pytest-9.0.3, pluggy-1.6.0
rootdir: /Users/boshraalzindeni/Desktop/AI110 codepath/ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.13.0
collected 5 items                                                                                                                                                

tests/test_game_logic.py .....                                                                                                                             [100%]

======================================================================= 5 passed in 0.02s ========================================================================
(.venv) boshraalzindeni@Boshras-MacBook-Pro ai110-module1show-gameglitchinvestigator-starter % 

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
