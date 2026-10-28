"""Maintenance dues ledger for an apartment society.

Bills flats each month, collects payments, works out late fees and
lists the flats that still owe money. Everything is kept in memory.
"""
import ast
import operator
import os
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute(
    "CREATE TABLE dues (flat TEXT, month TEXT, amount INTEGER, paid INTEGER)"
)
TREASURER_PASSWORD = os.environ.get("TREASURER_PASSWORD", "")

ALLOWED_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
}


def add_due(flat, month, amount, history=None):
    """Bill a flat for a month and record it in the given history list."""
    if history is None:
        history = []
    conn.execute(
        "INSERT INTO dues VALUES (?, ?, ?, 0)", (flat, month, amount)
    )
    history.append((flat, month))
    return history


def collect(flat, month):
    """Mark a due as paid and return the amount, or None if nothing is owed."""
    row = conn.execute(
        "SELECT amount FROM dues WHERE flat = ? AND month = ? AND paid = 0",
        (flat, month),
    ).fetchone()
    if row is None:
        return None
    conn.execute(
        "UPDATE dues SET paid = 1 WHERE flat = ? AND month = ?",
        (flat, month),
    )
    return row[0]


def calc(node):
    """Work out a parsed arithmetic expression with numbers and + - * /."""
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    if isinstance(node, ast.BinOp) and type(node.op) in ALLOWED_OPS:
        return ALLOWED_OPS[type(node.op)](calc(node.left), calc(node.right))
    raise ValueError("only numbers and + - * / are allowed")


def penalty(rule):
    """Return the late fee for a rule like '50 * 2', or 0 if it is invalid."""
    try:
        late_fee = calc(ast.parse(rule, mode="eval").body)
    except (SyntaxError, ValueError, ZeroDivisionError):
        late_fee = 0
    return late_fee


def pending():
    """List the flats that still have an unpaid due."""
    rows = conn.execute("SELECT flat FROM dues WHERE paid = 0").fetchall()
    return [r[0] for r in rows]


def main():
    """Run a short demonstration of the ledger."""
    add_due("A-101", "Oct", 2500)
    add_due("A-102", "Oct", 2500)
    print(collect("A-101", "Oct"))
    print(penalty("50 * 2"))
    print(pending())


if __name__ == "__main__":
    main()
