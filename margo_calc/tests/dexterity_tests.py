import pytest
from services.dexterity import *

def test_calculate_attack_speed_dexterity_cap():
    assert calculate_attack_speed(0) == 0
    assert calculate_attack_speed(1) == 0.02
    assert calculate_attack_speed(100) == 2

def test_calculate_attack_speed_normal_values():
    assert calculate_attack_speed(101) == pytest.approx(2.002)
    assert calculate_attack_speed(1000) == 3.8
    assert calculate_attack_speed(3000) == 7.8

def test_calculate_evade_gain():
    assert calculate_evade_gain(0) == 0
    assert calculate_evade_gain(1) == pytest.approx(0.03333333)
    assert calculate_evade_gain(100) == pytest.approx(3.333333)
    assert calculate_evade_gain(3000) == 100