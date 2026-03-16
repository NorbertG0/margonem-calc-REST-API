from services.hero_level import calculate_base_hp, calculate_exp_amount, calculate_experience
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
