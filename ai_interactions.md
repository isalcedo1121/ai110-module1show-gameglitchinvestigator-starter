# AI Interactions Log

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

**Prompt used:**

> Read `logic_utils.py` and `tests/test_game_logic.py`. Identify three edge-case inputs that could cause problems in `parse_guess()`, such as a negative number, a decimal, or an extremely large number. Add pytest tests for exactly three useful edge cases. Do not modify `app.py` or `logic_utils.py` and do not fix any additional bugs. Only add tests that verify the current behavior handles these inputs gracefully.

| Edge Case | AI-Suggested Test | Did It Pass? | Your Reasoning |
|---|---|---|---|
| Negative number | Verify a negative guess is rejected | Yes | Tests that input below the allowed range is rejected. |
| Decimal (`50.7`) | Verify the current decimal parsing behavior | Yes | Tests how decimal input is converted and handled. |
| Extremely large number (`1e999`) | Verify extreme input is rejected without crashing | Yes | Tests that unusually large numeric input is handled gracefully. |