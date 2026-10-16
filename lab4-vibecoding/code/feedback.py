from collections import Counter


def evaluate(target, guess):
    """Wordle feedback for one guess.

    Exact matches are marked first. Every target letter that was not an exact
    match can then turn at most one other guess letter yellow, so a guess with
    more copies of a letter than the target gets gray for the extra copies.
    """
    result = ["gray"] * len(guess)
    unmatched = Counter()
    for i, (t, g) in enumerate(zip(target, guess)):
        if g == t:
            result[i] = "green"
        else:
            unmatched[t] += 1
    for i, g in enumerate(guess):
        if result[i] != "green" and unmatched[g] > 0:
            result[i] = "yellow"
            unmatched[g] -= 1
    return result
