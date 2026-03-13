import pytest
from services.dexterity import calculate_attack_speed, calculate_evade_gain

@pytest.mark.parametrize(
    'dexterity, expected',
    [
        (0, 0),
        (1, 0.02),
        (100, 2)
    ]
)
def test_calculate_attack_speed_dexterity_cap(dexterity, expected):
    assert calculate_attack_speed(dexterity) == pytest.approx(expected)

@pytest.mark.parametrize(
    'dexterity, expected',
    [
        (101, 2.002),
        (1000, 3.8),
        (3000, 7.8)
    ]
)

def test_calculate_attack_speed_normal_values(dexterity, expected):
    assert calculate_attack_speed(dexterity) == pytest.approx(expected)

@pytest.mark.parametrize(
    'dexterity, expected',
    [
        (0, 0),
        (1, 0.03333333),
        (100, 3.333333),
        (3000, 100)
    ]
)

def test_calculate_evade_gain(dexterity, expected):
    assert calculate_evade_gain(dexterity) == pytest.approx(expected)