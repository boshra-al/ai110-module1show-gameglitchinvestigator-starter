from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

# New tests targeting the higher/lower hint fix
def test_too_high_hint_says_go_lower():
    # When the guess is too high, the hint should tell the player to go LOWER
    _, message = check_guess(60, 50)
    assert message == "📉 Go LOWER!"

def test_too_low_hint_says_go_higher():
    # When the guess is too low, the hint should tell the player to go HIGHER
    _, message = check_guess(40, 50)
    assert message == "📈 Go HIGHER!"
