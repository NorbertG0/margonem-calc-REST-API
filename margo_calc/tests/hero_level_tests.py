from services.hero_level import calculate_base_hp, calculate_exp_amount, calculate_experience, calculate_base_crit_value,  \
    calculate_crit_chance_gain, calculate_crit_power_gain
import pytest

@pytest.mark.parametrize(
    'level, expected',
    [
        (1, 20),
        (300, 50941.499),
        (301, 50941.499),
        (500, 50941.499)
    ]
)

def test_calculate_base_hp(level, expected):
    assert calculate_base_hp(level) == pytest.approx(expected)


@pytest.mark.parametrize(
    'level, expected',
    [
        (1, 10),
        (300, 7992538811),
        (500, 62001498011)
    ]
)

def test_calculate_exp_amount(level, expected):
    assert calculate_exp_amount(level) == pytest.approx(expected)

@pytest.mark.parametrize(
    'player_level, npc_level, expected',
    [
        (1, 1, 1),
        (1, 3, 7.24661),
        (1, 100, 4031.99514),

        (100, 10, 0),
        (100, 100, 4031.99514),
        (100, 300, 29218.3113),

        (300, 1, 0),
        (300, 100, 0),
        (300, 300, 29218.3113)
    ]
)

def test_calculate_experience(player_level, npc_level, expected):
    assert calculate_experience(player_level, npc_level) == pytest.approx(expected)

@pytest.mark.parametrize(
    'level, expected',
    [
        (1, 1.02),
        (100, 3),
        (300, 7)
    ]
)

def test_calculate_base_crit_value(level, expected):
    assert calculate_base_crit_value(level) == pytest.approx(expected)

@pytest.mark.parametrize(
    'player_level, enemy_level, expected',
    [
        (1, 1, 0),
        (100, 100, 0),
        (300, 300, 0),
        (301, 301, 0),

        (1, 10, 0),
        (1, 100, 0),
        (1, 300, 0),
        (1, 301, 0),

        (100, 1, 282),
        (100, 50, 135),
        (100, 90, 15),

        (301, 100, 585),
        (301, 200, 285),
        (301, 300, 0)
    ]
)

def test_calculate_crit_chance_gain(player_level, enemy_level, expected):
    assert calculate_crit_chance_gain(player_level, enemy_level) == expected

@pytest.mark.parametrize(
    'player_level, enemy_level, expected',
    [
        (1, 1, 0),
        (100, 100, 0),
        (300, 300, 0),

        (1, 100, 0),
        (1, 200, 0),
        (1, 300, 0),

        (100, 90, 50),
        (200, 190, 50),
        (300, 290, 50),

        (301, 10, 300),
        (301, 100, 300),
        (301, 200, 300)
    ]
)

def test_calculate_crit_power_gain(player_level, enemy_level, expected):
    assert calculate_crit_power_gain(player_level, enemy_level) == pytest.approx(expected)