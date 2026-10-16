import random
from words import WORDS
from feedback import evaluate

MAX_GUESSES = 6
LENGTHS = (4, 5, 6)


class WordleGame:
    def __init__(self, length=5, target=None):
        if length not in LENGTHS:
            raise ValueError(f"length must be one of {LENGTHS}")
        self.length = length
        self.target = target or random.choice([w for w in WORDS if len(w) == length])
        self.history = []

    def show_history(self):
        print("History:")
        for n, (guess, feedback) in enumerate(self.history, 1):
            print(f"  {n}. {guess.upper()}  " + " ".join(f.ljust(6) for f in feedback))

    def run(self):
        """Play one game. Returns "won", "lost" or "quit"."""
        print(f"Wordle: {self.length} letters, {MAX_GUESSES} guesses. Type q to quit.")
        while len(self.history) < MAX_GUESSES:
            turn = len(self.history) + 1
            guess = input(f"Guess {turn}/{MAX_GUESSES} > ").strip().lower()
            if guess == "q":
                print(f"You quit. The word was: {self.target}")
                return "quit"
            if len(guess) != self.length or not guess.isalpha():
                # Invalid input is not added to history, so it does not use a turn.
                print(f"Invalid guess. Enter a {self.length} letter word using letters only.")
                continue
            self.history.append((guess, evaluate(self.target, guess)))
            self.show_history()
            if guess == self.target:
                print(f"You won in {turn} guess{'es' if turn > 1 else ''}!")
                return "won"
        print(f"Out of guesses. The word was: {self.target}")
        return "lost"


def ask_length():
    """Ask for 4, 5 or 6. Enter means 5, q means stop. Returns None to stop."""
    while True:
        choice = input("Word length (4, 5 or 6, Enter for 5, q to stop) > ").strip().lower()
        if choice == "q":
            return None
        if choice == "":
            return 5
        if choice.isdigit() and int(choice) in LENGTHS:
            return int(choice)
        print("Please type 4, 5 or 6.")


def play_session():
    """Play games until the player stops, then print a session summary."""
    results = []  # (length, outcome, guesses used)
    while True:
        length = ask_length()
        if length is None:
            break
        game = WordleGame(length)
        outcome = game.run()
        results.append((length, outcome, len(game.history)))
        if outcome == "quit" or input("Play again? (y/n) > ").strip().lower() != "y":
            break
    print_summary(results)
    return results


def print_summary(results):
    print("\nSession summary")
    if not results:
        print("  No games played.")
        return
    wins = [r for r in results if r[1] == "won"]
    print(f"  Games played: {len(results)}")
    print(f"  Won: {len(wins)}  Lost: {sum(r[1] == 'lost' for r in results)}"
          f"  Quit: {sum(r[1] == 'quit' for r in results)}")
    if wins:
        print(f"  Average guesses per win: {sum(r[2] for r in wins) / len(wins):.1f}")
    for n, (length, outcome, used) in enumerate(results, 1):
        print(f"  Game {n}: {length} letters, {outcome}, {used} guess{'es' if used != 1 else ''}")
