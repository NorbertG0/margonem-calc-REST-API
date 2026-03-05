from services.legendary_bonuses import *
import pytest

def test_calculate_first_nerf_level():
    assert calculate_first_nerf_level(200) == 250
    assert calculate_first_nerf_level(120) == 150
    assert calculate_first_nerf_level(119) == 149
    assert calculate_first_nerf_level(50) == 80

def test_calculate_legendary_bonus_expiration():
    assert calculate_legendary_bonus_expiration(200) == 300
    assert calculate_legendary_bonus_expiration(120) == 200
    assert calculate_legendary_bonus_expiration(119) == 199
    assert calculate_legendary_bonus_expiration(50) == 130

def test_calculate_very_crit_chance():
    assert calculate_very_crit_chance(0) == 0
    assert calculate_very_crit_chance(10) == 17
    assert calculate_very_crit_chance(33) == 56.1
    assert calculate_very_crit_chance(100) == 170

def test_calculate_holy_touch_heal_value():
    assert calculate_holy_touch_heal_value(0) == 0
    assert calculate_holy_touch_heal_value(1000) == 60
    assert calculate_holy_touch_heal_value(10000) == 600
    assert calculate_holy_touch_heal_value(100000) == 6000

def test_calculate_anguish_damage():
    assert calculate_anguish_damage(1, 1, 1, 1) == 0.847
    assert calculate_anguish_damage(25, 1, 1, 1) == 1.015
    assert calculate_anguish_damage(300, 1, 1, 1) == 2.94

    assert calculate_anguish_damage(1, 100, 100, 100) == 84.7
    assert calculate_anguish_damage(25, 100, 100, 100) == 101.5
    assert calculate_anguish_damage(300, 100, 100, 100) == 294

    assert calculate_anguish_damage(1, 999, 999, 999) == pytest.approx(846.15299)
    assert calculate_anguish_damage(25, 999, 999, 999) == pytest.approx(1013.98499)
    assert calculate_anguish_damage(300, 999, 999, 999) == 2937.06


