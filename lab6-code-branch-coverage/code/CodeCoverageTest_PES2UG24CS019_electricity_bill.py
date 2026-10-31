"""Code (line) coverage tests for electricity_bill.py.

Goal: every line of electricity_bill.py runs at least once.
Each test below is there to reach lines the starter tests never touched.
"""
import pytest
from electricity_bill import energy_charge, late_fee, subsidy


# Starter tests from the assigned repo

def test_low_usage_domestic():
    assert energy_charge(50, "domestic") == 200


def test_paid_on_time():
    assert late_fee(500, 0) == 0


# energy_charge

def test_unknown_connection_raises():
    with pytest.raises(ValueError, match="unknown connection"):
        energy_charge(50, "industrial")


def test_negative_units_raises():
    with pytest.raises(ValueError, match="invalid units"):
        energy_charge(-1, "domestic")


def test_middle_slab_domestic():
    # 100 units at 3 = 300, then 50 units at 5 = 250, plus fixed 50
    assert energy_charge(150, "domestic") == 600


def test_top_slab_domestic():
    # 1300 for the first 300 units, then 100 units at 8 = 800, plus fixed 50
    assert energy_charge(400, "domestic") == 2150


def test_commercial_doubles_charge():
    # 50 units at 3 = 150, doubled = 300, plus commercial fixed 150
    assert energy_charge(50, "commercial") == 450


# late_fee

def test_late_within_15_days():
    assert late_fee(1000, 10) == 50


def test_late_over_15_days_big_bill():
    # 100 flat plus 3000 // 20 = 150
    assert late_fee(3000, 20) == 250


# subsidy

def test_senior_low_usage_subsidy():
    assert subsidy(50, True, False) == 50


def test_solar_subsidy():
    assert subsidy(200, False, True) == 100


def test_solar_subsidy_removed_above_300_units():
    assert subsidy(400, False, True) == 0
