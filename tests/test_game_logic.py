from logic_utils import check_guess, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High" and say go lower
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low" and say go higher
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_high_low_hints_point_toward_secret():
    # Regression test for the swapped hint bug: hints must point toward the secret
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_parse_guess_rejects_out_of_range():
    # Guesses just outside 1-100 should be rejected
    ok, value, err = parse_guess("0", 1, 100)
    assert ok is False
    assert value is None

    ok, value, err = parse_guess("101", 1, 100)
    assert ok is False
    assert value is None

def test_parse_guess_accepts_range_edges():
    # The range is inclusive, so 1 and 100 are valid guesses
    assert parse_guess("1", 1, 100) == (True, 1, None)
    assert parse_guess("100", 1, 100) == (True, 100, None)

def test_parse_guess_respects_easy_range():
    # On Easy (1-20), 20 is valid but 21 is not
    assert parse_guess("20", 1, 20) == (True, 20, None)

    ok, value, err = parse_guess("21", 1, 20)
    assert ok is False
    assert value is None
