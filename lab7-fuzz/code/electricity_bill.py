"""Electricity bill helpers, hardened against bad input.

Each function either returns a valid answer or raises ValueError with a
message saying what was wrong. No other exception type gets out.
"""
RATES = {"DOM": 3, "COM": 6}
SLAB = {"A": 1, "B": 2}


def _require_text(value, what):
    if not isinstance(value, str):
        raise ValueError(f"{what} must be text, got {type(value).__name__}")


def _whole_number(text, what):
    try:
        value = int(text)
    except ValueError:
        raise ValueError(f"{what} must be a whole number, got {text!r}") from None
    if value < 0:
        raise ValueError(f"{what} cannot be negative, got {value}")
    return value


def units_consumed(reading):
    _require_text(reading, "meter reading")
    parts = reading.split(':')
    if len(parts) != 2:
        raise ValueError("meter reading must look like previous:current, e.g. 1200:1350")
    previous = _whole_number(parts[0], "previous reading")
    current = _whole_number(parts[1], "current reading")
    if current < previous:
        raise ValueError(f"current reading {current} is lower than previous reading {previous}")
    return current - previous


def daily_average(units_csv):
    _require_text(units_csv, "daily units")
    if not units_csv.strip():
        raise ValueError("no daily units given")
    units = [_whole_number(u, "daily units") for u in units_csv.split(',')]
    try:
        return round(sum(units) / len(units), 2)
    except OverflowError:
        raise ValueError("daily units are too large to average") from None


def tariff_rate(code):
    _require_text(code, "tariff code")
    parts = code.split('-')
    if len(parts) != 2:
        raise ValueError("tariff code must look like DOM-A")
    category = parts[0].strip().upper()
    slab = parts[1].strip().upper()
    if category not in RATES:
        raise ValueError(f"unknown category {category!r}, expected DOM or COM")
    if slab not in SLAB:
        raise ValueError(f"unknown slab {slab!r}, expected A or B")
    return RATES[category] * SLAB[slab]


def run_step(title, prompt, func, label):
    print(f"==== Running {title} ====")
    user_input = input(prompt)
    try:
        print(f"{label}:", func(user_input))
    except ValueError as err:
        print("Invalid input:", err)


def main():
    run_step("units_consumed",
             "Enter meter readings as previous:current (e.g. 1200:1350): ",
             units_consumed, "Units Consumed")
    print()
    run_step("daily_average",
             "Enter daily units as CSV (e.g. 5,7,6): ",
             daily_average, "Daily Average")
    print()
    run_step("tariff_rate",
             "Enter a tariff code (e.g. DOM-A): ",
             tariff_rate, "Rate per Unit")


if __name__ == "__main__":
    main()
