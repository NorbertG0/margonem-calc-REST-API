import pytest
from services.intellect import *

# ABSORB LIMIT TESTS
def test_calculate_absorb_limit():
    assert calculate_absorb_limit(0) == 0
    assert calculate_absorb_limit(1) == 7
    assert calculate_absorb_limit(1000) == 7000

# CRIT VALUE TESTS
def test_calculate_crit_value_down_cap():
    assert calculate_crit_value(0, 20) == 0
    assert calculate_crit_value(0, 15) == 0
    assert calculate_crit_value(0, 9) == 0
    assert calculate_crit_value(0, 0) == 0

    assert calculate_crit_value(1, 20) == 0
    assert calculate_crit_value(1, 15) == 0
    assert calculate_crit_value(1, 9) == 0
    assert calculate_crit_value(1, 0) == 0

    assert calculate_crit_value(100, 20) == 0
    assert calculate_crit_value(100, 15) == 0
    assert calculate_crit_value(100, 9) == 0
    assert calculate_crit_value(100, 0) == 0

def test_calculate_crit_value_intellect_zero():
    assert calculate_crit_value(0, 0) == 0
    assert calculate_crit_value(0, 21) == 0
    assert calculate_crit_value(0, 50) == 0
    assert calculate_crit_value(0, 301) == 0

def test_calculate_crit_value_normal_values():
    assert calculate_crit_value(1, 21) == pytest.approx(0.09523809)
    assert calculate_crit_value(1, 50) == pytest.approx(0.04)
    assert calculate_crit_value(1, 300) == pytest.approx(0.006666666666666667)

    assert calculate_crit_value(100, 21) == pytest.approx(9.523809)
    assert calculate_crit_value(100, 50) == 4
    assert calculate_crit_value(100, 300) == pytest.approx(0.6666666666666667)

def test_calculate_crit_value_up_level_cap():
    assert calculate_crit_value(1, 301) == pytest.approx(0.006666666666666667)
    assert calculate_crit_value(1, 500) == pytest.approx(0.006666666666666667)
    assert calculate_crit_value(1, 1000) == pytest.approx(0.006666666666666667)
