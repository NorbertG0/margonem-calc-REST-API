from services.legendary_bonuses import calculate_first_nerf_level, calculate_legendary_bonus_expiration, calculate_very_crit_chance, calculate_holy_touch_heal_value, calculate_anguish_damage
import pytest

@pytest.mark.parametrize(
    'level, expected',
    [
        (200, 250),
        (120, 150),
        (119, 149),
        (50, 80),
    ]
)

def test_calculate_first_nerf_level(level, expected):
    assert calculate_first_nerf_level(level) == expected

@pytest.mark.parametrize(
    'level, expected',
    [
        (200, 300),
        (120, 200),
        (119, 199),
        (50, 130),
    ]
)

def test_calculate_legendary_bonus_expiration(level, expected):
    assert calculate_legendary_bonus_expiration(level) == expected

@pytest.mark.parametrize(
    'crit_chance, expected',
    [
        (0, 0),
        (10, 17),
        (33, 56.1),
        (100, 170),
    ]
)

def test_calculate_very_crit_chance(crit_chance, expected):
    assert calculate_very_crit_chance(crit_chance) == pytest.approx(expected)

@pytest.mark.parametrize(
    'hp, expected',
    [
        (0, 0),
        (1000, 60),
        (10000, 600),
        (100000, 6000),
    ]
)

def test_calculate_holy_touch_heal_value(hp, expected):
    assert calculate_holy_touch_heal_value(hp) == expected

@pytest.mark.parametrize(
    'level, strength, intellect, agility, expected',
    [
        (1, 1, 1, 1, 0.847),
        (25, 1, 1, 1, 1.015),
        (300, 1, 1, 1, 2.94),

        (1, 100, 100, 100, 84.7),
        (25, 100, 100, 100, 101.5),
        (300, 100, 100, 100, 294),

        (1, 999, 999, 999, 846.15299),
        (25, 999, 999, 999, 1013.98499),
        (300, 999, 999, 999, 2937.06),
    ]
)
def test_calculate_anguish_damage(level, strength, intellect, agility, expected):
    assert calculate_anguish_damage(level, strength, intellect, agility) == pytest.approx(expected)


