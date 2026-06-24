# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error                  |
|-------|-------------------|-----------------|-----------------------------------------|
|  77   |  Hint: Go LOWER!  | Hint: Go Higher!| Hints always backwards                  |
|  30   |  Final score: 100 | Final score: 70 | Inaccurate grade w/correct first attempt|
|  200  |  Error: Try again | Hint: Go Higher!| No contraint on input and incorrect     |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
--> Claude Code

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
--> An example of a AI suggestion that was correct was the higher/lower update. It suggested to update the check_guess function, by swapping the print statements.
I verfied the updates were correct by running and testing the application on the user side.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
--> An example of an AI suggestion that was incorrect was the refactoring of the check_guess function to the logic_utils.py file. I wasn't 100% certain where the error stemed from, as it ran just fine. I only noticed the error after viewing the application on the browser. To fix the error, I undid the AI changes, started a new AI chat, and gave it specific instructions on how to refactor, which successfully resulted in an errorless game. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
--> If the program ran as expected, despite edge cases, it was determined to be fixed. 

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
--> One test I ran (both manually and using pytest) was the contraints on the range. Prior to fixing it, guesses that were out of range, were considered valid and were deducted from the guesses. However, after the necessary updates, i tested numbers that were out of range (including negative numbers) and it gave a "Try again" output, without deducting attempts. 

- Did AI help you design or understand any tests? How?
--> Yes, it provided addiional tests, specifically generating testing for the guessing contraints. It also helped me learn how to run pytests. I was having many issues with the command line not finding the tests. The problem was how I was writing my commands and the directories I was in. Thankfully, AI helped me verify I was in the correct directory and gave me exact command line prompts to ensure the the code was running the tests in test_game_logic.py. 

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
--> I'd explain that every time you use an application with Streamlit, it reruns the entire script from top to bottom, which is similar to refreshing the page. The problem is that any normal variable would reset to its starting value on every rerun, so the game would forget your score, attempts, and secret number each time. Session state is how you get around that, it's a dictionary that "remembers" values between reruns, which is why this game stores secret, attempts, score, and history there. 

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
- This could be a testing habit, a prompting strategy, or a way you used Git.
--> One habit I want to reuse is testing edge cases. Often times, programmers are only think about the expected input instead of the unexpected. I also want to keep up the habbit of commiting as frequently as possible, since I typically only do 1-2 large commits per project.

- What is one thing you would do differently next time you work with AI on a coding task?
--> Next time I'd give the AI more specific instructions up front instead of letting it make broad changes on its own. I learned that scoping my prompts tightly, and reviewing changes before running, saves a lot of backtracking.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
--> This project taught me that AI generated code can look correct and even run without crashing while still being wrong, thus it can't be trusted blindly. Moving forward I will continue to use AI as a fast teammate whose suggestions I always have to verify by reviewing all changes and completing many tests. 
