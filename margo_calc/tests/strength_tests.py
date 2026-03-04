import pytest
from services.strength import *

# BASE HP TESTS
def test_calculate_base_hp_positive():
    assert calculate_base_hp(100) == 500

def test_calculate_base_hp_zero():
    assert calculate_base_hp(0) == 0

def test_calculate_base_hp_large_value():
    assert calculate_base_hp(10000) == 50000



# ARMOR HP GAINS TESTS
def test_calculate_armor_hp_amor_level_none():
    assert calculate_armor_hp(100, None) == 0
    assert calculate_armor_hp(0, None) == 0

def test_calculate_armor_hp_strength_zero():
    assert calculate_armor_hp(0, 300) == 0
    assert calculate_armor_hp(0, 50) == 0
    assert calculate_armor_hp(0, 0) == 0

def test_calculate_armor_hp_min_multiplier():
    assert calculate_armor_hp(100, 0) == 10
    assert calculate_armor_hp(50, 0) == 5

def test_calculate_armor_hp_normal_values():
    assert calculate_armor_hp(100, 10) == 10
    assert calculate_armor_hp(100, 50) == 50
    assert calculate_armor_hp(100, 300) == 300

def test_calculate_armor_hp_rounding():
    assert calculate_armor_hp(100, 19) == 20 # 19 / 10 = 1.9 -> 2
    assert calculate_armor_hp(100, 15) == 20 # 15 / 10 = 1.5 -> 2
    assert calculate_armor_hp(100, 14) == 10 # 14 / 10 = 1.4 -> 1
    assert calculate_armor_hp(100, 11) == 10 # 11 / 10 = 1.1 -> 1



# CRIT VALUE TESTS
def test_calculate_crit_value_level_down_level_cap():
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

def test_calculate_crit_value_strength_zero():
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