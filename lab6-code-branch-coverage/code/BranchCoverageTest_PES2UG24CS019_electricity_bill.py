"""Branch coverage tests for electricity_bill.py.

Goal: every if / elif / else in electricity_bill.py is taken both ways.
This file keeps all the code coverage tests and adds the branches they
missed, plus the boundary values where each decision flips.
"""
import pytest
from electricity_bill import energy_charge, late_fee, subsidy


# Starter tests from the assigned repo

def test_low_usage_domestic():
    assert energy_charge(50, "domestic") == 200


def test_paid_on_time():
    assert late_fee(500, 0) == 0


# energy_charge: invalid input

def test_unknown_connection_raises():
    with pytest.raises(ValueError, match="unknown connection"):
        energy_charge(50, "industrial")


def test_negative_units_raises():
    with pytest.raises(ValueError, match="invalid units"):
        energy_charge(-1, "domestic")


# energy_charge: each slab, and the edges between slabs

def test_zero_units_domestic():
    # only the fixed charge
    assert energy_charge(0, "domestic") == 50


def test_exactly_100_units_stays_in_first_slab():
    assert energy_charge(100, "domestic") == 350


def test_101_units_moves_to_second_slab():
    assert energy_charge(101, "domestic") == 355


def test_middle_slab_domestic():
    assert energy_charge(150, "domestic") == 600


def test_exactly_300_units_stays_in_second_slab():
    assert energy_charge(300, "domestic") == 1350


def test_301_units_moves_to_top_slab():
    assert energy_charge(301, "domestic") == 1358


def test_top_slab_domestic():
    assert energy_charge(400, "domestic") == 2150


# energy_charge: connection type, True and False

def test_commercial_doubles_charge():
    assert energy_charge(50, "commercial") == 450


def test_commercial_top_slab():
    # 1300 doubled = 2600, plus commercial fixed 150
    assert energy_charge(300, "commercial") == 2750


# late_fee

def test_negative_days_counts_as_on_time():
    assert late_fee(500, -3) == 0


def test_late_within_15_days():
    assert late_fee(1000, 10) == 50


def test_exactly_15_days_late():
    assert late_fee(500, 15) == 50


def test_16_days_late_small_bill():
    # the branch the code coverage tests missed: over 15 days, bill not above 2000
    assert late_fee(500, 16) == 100


def test_over_15_days_bill_exactly_2000():
    # 2000 is not above 2000, so no extra fee
    assert late_fee(2000, 20) == 100


def test_over_15_days_bill_just_above_2000():
    # 100 flat plus 2001 // 20 = 100
    assert late_fee(2001, 20) == 200


def test_late_over_15_days_big_bill():
    assert late_fee(3000, 20) == 250


# subsidy

def test_no_subsidy_at_all():
    assert subsidy(50, False, False) == 0


def test_senior_low_usage_subsidy():
    assert subsidy(50, True, False) == 50


def test_senior_at_exactly_100_units():
    assert subsidy(100, True, False) == 50


def test_senior_above_100_units_gets_nothing():
    assert subsidy(101, True, False) == 0


def test_senior_with_solar_gets_both():
    assert subsidy(50, True, True) == 150


def test_solar_subsidy():
    assert subsidy(200, False, True) == 100


def test_solar_at_exactly_300_units_keeps_subsidy():
    assert subsidy(300, False, True) == 100


def test_solar_subsidy_removed_above_300_units():
    assert subsidy(400, False, True) == 0
