import pytest
from services.item_stats import *

def test_calculate_all_stats():
    assert calculate_all_stats(1, 0) == 0
    assert calculate_all_stats(1, 1) == pytest.approx(8.25)
    assert calculate_all_stats(1, 2) == pytest.approx(8.5)
    assert calculate_all_stats(1, 3) == pytest.approx(8.75)
    assert calculate_all_stats(1, 4) == pytest.approx(9)
    assert calculate_all_stats(1, 5) == pytest.approx(9.25)
    assert calculate_all_stats(1, 6) == pytest.approx(9.5)

    assert calculate_all_stats(300, 0) == 0
    assert calculate_all_stats(300, 1) == pytest.approx(83)
    assert calculate_all_stats(300, 2) == pytest.approx(158)
    assert calculate_all_stats(300, 3) == pytest.approx(233)
    assert calculate_all_stats(300, 4) == pytest.approx(308)
    assert calculate_all_stats(300, 5) == pytest.approx(383)
    assert calculate_all_stats(300, 6) == pytest.approx(458)

def test_calculate_strength():
    assert calculate_strength(1, -2) == pytest.approx(2.888888)
    assert calculate_strength(1, -1) == pytest.approx(3.444444)
    assert calculate_strength(1, 0) == 0
    assert calculate_strength(1, 1) == pytest.approx(4.555555)
    assert calculate_strength(1, 2) == pytest.approx(5.111111)
    assert calculate_strength(1, 3) == pytest.approx(5.666666)
    assert calculate_strength(1, 4) == pytest.approx(6.222222)
    assert calculate_strength(1, 5) == pytest.approx(6.777777)
    assert calculate_strength(1, 6) == pytest.approx(7.333333)

    assert calculate_strength(300, -2) == pytest.approx(-329.333333)
    assert calculate_strength(300, -1) == pytest.approx(-162.666666)
    assert calculate_strength(300, 0) == 0
    assert calculate_strength(300, 1) == pytest.approx(170.666666)
    assert calculate_strength(300, 2) == pytest.approx(337.333333)
    assert calculate_strength(300, 3) == pytest.approx(504)
    assert calculate_strength(300, 4) == pytest.approx(670.666666)
    assert calculate_strength(300, 5) == pytest.approx(837.333333)
    assert calculate_strength(300, 6) == pytest.approx(1004.0)

def test_calculate_dexterity():
    assert calculate_dexterity(1, -2) == pytest.approx(2.888888)
    assert calculate_dexterity(1, -1) == pytest.approx(3.444444)
    assert calculate_dexterity(1, 0) == 0
    assert calculate_dexterity(1, 1) == pytest.approx(4.555555)
    assert calculate_dexterity(1, 2) == pytest.approx(5.111111)
    assert calculate_dexterity(1, 3) == pytest.approx(5.666666)
    assert calculate_dexterity(1, 4) == pytest.approx(6.222222)
    assert calculate_dexterity(1, 5) == pytest.approx(6.777777)
    assert calculate_dexterity(1, 6) == pytest.approx(7.333333)

    assert calculate_dexterity(300, -2) == pytest.approx(-329.333333)
    assert calculate_dexterity(300, -1) == pytest.approx(-162.666666)
    assert calculate_dexterity(300, 0) == 0
    assert calculate_dexterity(300, 1) == pytest.approx(170.666666)
    assert calculate_dexterity(300, 2) == pytest.approx(337.333333)
    assert calculate_dexterity(300, 3) == pytest.approx(504.0)
    assert calculate_dexterity(300, 4) == pytest.approx(670.666666)
    assert calculate_dexterity(300, 5) == pytest.approx(837.333333)
    assert calculate_dexterity(300, 6) == pytest.approx(1004)

def test_calculate_intellect():
    assert calculate_intellect(1, -2) == pytest.approx(2.888888)
    assert calculate_intellect(1, -1) == pytest.approx(3.444444)
    assert calculate_intellect(1, 0) == 0
    assert calculate_intellect(1, 1) == pytest.approx(4.555555)
    assert calculate_intellect(1, 2) == pytest.approx(5.111111)
    assert calculate_intellect(1, 3) == pytest.approx(5.666666)
    assert calculate_intellect(1, 4) == pytest.approx(6.222222)
    assert calculate_intellect(1, 5) == pytest.approx(6.777777)
    assert calculate_intellect(1, 6) == pytest.approx(7.333333)

    assert calculate_intellect(300, -2) == pytest.approx(-329.333333)
    assert calculate_intellect(300, -1) == pytest.approx(-162.666666)
    assert calculate_intellect(300, 0) == 0
    assert calculate_intellect(300, 1) == pytest.approx(170.666666)
    assert calculate_intellect(300, 2) == pytest.approx(337.333333)
    assert calculate_intellect(300, 3) == pytest.approx(504.0)
    assert calculate_intellect(300, 4) == pytest.approx(670.666666)
    assert calculate_intellect(300, 5) == pytest.approx(837.333333)
    assert calculate_intellect(300, 6) == pytest.approx(1004)

def test_calcuate_attack_speed():
    assert calculate_attack_speed(1, -2) == pytest.approx(0.08)
    assert calculate_attack_speed(1, -1) == pytest.approx(0.08)
    assert calculate_attack_speed(1, 0) == 0
    assert calculate_attack_speed(1, 1) == pytest.approx(0.08)
    assert calculate_attack_speed(1, 2) == pytest.approx(0.08)
    assert calculate_attack_speed(1, 3) == pytest.approx(0.09)
    assert calculate_attack_speed(1, 4) == pytest.approx(0.09)
    assert calculate_attack_speed(1, 5) == pytest.approx(0.09)

    assert calculate_attack_speed(300, -2) == pytest.approx(-1.42)
    assert calculate_attack_speed(300, -1) == pytest.approx(-0.67)
    assert calculate_attack_speed(300, 0) == 0
    assert calculate_attack_speed(300, 1) == pytest.approx(0.83)
    assert calculate_attack_speed(300, 2) == pytest.approx(1.58)
    assert calculate_attack_speed(300, 3) == pytest.approx(2.33)
    assert calculate_attack_speed(300, 4) == pytest.approx(3.08)
    assert calculate_attack_speed(300, 5) == pytest.approx(3.83)