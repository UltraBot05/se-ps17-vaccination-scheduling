"""Checks for the README's required testing list. Run with: python test_wordle.py"""
import io
from contextlib import redirect_stdout
from unittest.mock import patch

from feedback import evaluate
from game import WordleGame, play_session
from words import WORDS

G, Y, X = "green", "yellow", "gray"


def play(target, inputs):
    """Run one game with typed inputs, return (outcome, game, printed text)."""
    game = WordleGame(len(target), target=target)
    out = io.StringIO()
    with patch("builtins.input", side_effect=inputs), redirect_stdout(out):
        outcome = game.run()
    return outcome, game, out.getvalue()


# Repeated letters: guess has more copies than the target
assert evaluate("stare", "start") == [G, G, G, G, X]
assert evaluate("stare", "stars") == [G, G, G, G, X]
assert evaluate("stare", "toast") == [Y, X, G, Y, X]
assert evaluate("crane", "eerie") == [X, X, Y, X, G]
# Repeated letters: target has the copies
assert evaluate("eerie", "crane") == [X, Y, X, X, G]
assert evaluate("apple", "papal") == [Y, Y, G, X, Y]
# Exact match and fully absent
assert evaluate("stare", "stare") == [G] * 5
assert evaluate("stare", "plumb") == [X] * 5

# All three lengths, including repeats in 4 and 6 letter words
assert evaluate("book", "boot") == [G, G, G, X]
assert evaluate("door", "odor") == [Y, Y, G, G]
assert evaluate("banana", "nanaba") == [Y, G, G, G, Y, G]
assert evaluate("letter", "settle") == [X, G, G, G, Y, Y]
for n in (4, 5, 6):
    assert any(len(w) == n for w in WORDS)
    assert len(WordleGame(n).target) == n

# Invalid guesses do not use a turn and are not added to history
outcome, game, text = play("stare", ["ab", "12345", "starer", "stare"])
assert outcome == "won" and len(game.history) == 1
assert text.count("Invalid guess") == 3

# Winning on the final allowed guess
outcome, game, _ = play("stare", ["plant"] * 5 + ["stare"])
assert outcome == "won" and len(game.history) == 6

# Losing after six accepted guesses, even with invalid ones in between
outcome, game, text = play("stare", ["plant", "x", "plant", "plant", "1", "plant", "plant", "plant"])
assert outcome == "lost" and len(game.history) == 6
assert "The word was: stare" in text

# Quitting
outcome, game, _ = play("stare", ["plant", "q"])
assert outcome == "quit" and len(game.history) == 1

# Session: bad length input, two games, then summary
out = io.StringIO()
with patch("builtins.input", side_effect=["7", "4"] + ["zzzz"] * 6 + ["y", "", "q"]), redirect_stdout(out):
    results = play_session()
assert results == [(4, "lost", 6), (5, "quit", 0)]
assert "Please type 4, 5 or 6." in out.getvalue() and "Games played: 2" in out.getvalue()

print("All checks passed.")
