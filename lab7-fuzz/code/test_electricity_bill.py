"""Fuzz tests for electricity_bill.py using Hypothesis.

Rule for "crash": ValueError is the agreed way to reject bad input. Any other
exception (TypeError, KeyError, AttributeError, ...) is a crash. A function
that returns an impossible answer, like negative units, also fails.

Two kinds of tests for each function:
1. no_crash: random text, None and half-valid "messy" strings.
2. properties: well formed input gives the right answer, and input that
   breaks a rule (negative units, readings going backwards) is rejected.
"""
import pytest
from hypothesis import given, strategies as st

from electricity_bill import RATES, SLAB, daily_average, tariff_rate, units_consumed

VALID_RATES = {rate * slab for rate in RATES.values() for slab in SLAB.values()}

# Pieces that look almost right, so Hypothesis builds strings close to real input
number_bits = st.one_of(
    st.integers(min_value=-1000, max_value=10**6).map(str),
    st.sampled_from(["", " ", "abc", "1.5", "+7", " 12 "]),
    st.text(max_size=3),
)
messy_readings = st.lists(number_bits, max_size=4).map(":".join)
messy_csv = st.lists(number_bits, max_size=6).map(",".join)
messy_codes = st.lists(
    st.sampled_from(["DOM", "COM", "dom", "A", "B", "b", "XYZ", "", " "]) | st.text(max_size=3),
    max_size=4,
).map("-".join)


def call_and_check(func, value):
    """Call func, let ValueError through as a clean rejection, fail on anything else."""
    try:
        return func(value), True
    except ValueError:
        return None, False
    except Exception as e:  # pylint: disable=broad-except
        pytest.fail(f"{func.__name__}({value!r}) crashed with {type(e).__name__}: {e}")


# units_consumed

@given(st.text() | st.none() | messy_readings)
def test_units_consumed_no_crash(s):
    result, ok = call_and_check(units_consumed, s)
    if ok:
        assert isinstance(result, int) and result >= 0, f"{s!r} gave {result!r} units"


@given(st.integers(min_value=0, max_value=10**9), st.integers(min_value=0, max_value=10**9))
def test_units_consumed_readings(previous, current):
    reading = f"{previous}:{current}"
    if current >= previous:
        assert units_consumed(reading) == current - previous
    else:
        with pytest.raises(ValueError):
            units_consumed(reading)


# daily_average

@given(st.text() | st.none() | messy_csv)
def test_daily_average_no_crash(s):
    result, ok = call_and_check(daily_average, s)
    if ok:
        assert isinstance(result, (int, float)) and result >= 0, f"{s!r} gave {result!r}"


@given(st.lists(st.integers(min_value=0, max_value=10**6), min_size=1))
def test_daily_average_matches_mean(values):
    csv = ",".join(str(v) for v in values)
    assert daily_average(csv) == round(sum(values) / len(values), 2)


@given(st.lists(st.integers(min_value=0, max_value=10**6)), st.integers(max_value=-1))
def test_daily_average_rejects_negative_units(values, negative):
    csv = ",".join(str(v) for v in values + [negative])
    with pytest.raises(ValueError):
        daily_average(csv)


# tariff_rate

@given(st.text() | st.none() | messy_codes)
def test_tariff_rate_no_crash(s):
    result, ok = call_and_check(tariff_rate, s)
    if ok:
        assert result in VALID_RATES, f"{s!r} gave rate {result!r}"


@given(
    st.sampled_from(sorted(RATES)),
    st.sampled_from(sorted(SLAB)),
    st.booleans(),
    st.sampled_from(["", " ", "  "]),
)
def test_tariff_rate_valid_codes(category, slab, lower, pad):
    code = f"{pad}{category}-{slab}{pad}"
    if lower:
        code = code.lower()
    assert tariff_rate(code) == RATES[category] * SLAB[slab]
