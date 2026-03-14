import pytest
from services.strength import calculate_base_hp, calculate_armor_hp, calculate_crit_value

@pytest.mark.parametrize(
    'strength, expected',
    [
        (100, 500),
        (0, 0),
        (10000, 50000),
    ]
)

# BASE HP TESTS
def test_calculate_base_hp(strength, expected):
    assert calculate_base_hp(strength) == expected

@pytest.mark.parametrize(
    'strength, armor_level, expected',
    [
        (100, None, 0),
        (0, None, 0),

        (0, 300, 0),
        (0, 50, 0),
        (0, 0, 0),

        (100, 0, 10),
        (50, 0, 5),
        (100, 10, 10),
        (100, 50, 50),
        (100, 300, 300),

        (100, 0, 10),
        (50, 0, 5),

        (100, 10, 10),
        (100, 50, 50),
        (100, 300, 300),

        (100, 19, 20),
        (100, 15, 20),
        (100, 14, 10),
        (100, 11, 10),
    ]
)
# ARMOR HP GAINS TESTS
def test_calculate_armor_hp(strength, armor_level, expected):
    assert calculate_armor_hp(strength, armor_level) == expected

@pytest.mark.parametrize(
    'strength, level, expected',
    [
        (0, 20, 0),
        (0, 15, 0),
        (0, 9, 0),
        (0, 0, 0),

        (1, 20, 0),
        (1, 15, 0),
        (1, 9, 0),
        (1, 0, 0),

        (100, 20, 0),
        (100, 15, 0),
        (100, 9, 0),
        (100, 0, 0),

        (0, 0, 0),
        (0, 21, 0),
        (0, 50, 0),
        (0, 301, 0),

        (1, 21, 0.09523809),
        (1, 50, 0.04),
        (1, 300, 0.006666666666666667),

        (100, 21, 9.523809),
        (100, 50, 4),
        (100, 300, 0.6666666666666666),

        (1, 301, 0.006666666666666667),
        (1, 500, 0.006666666666666667),
        (1, 1000, 0.006666666666666667),
    ]
)
# CRIT VALUE TESTS
def test_calculate_crit_value(strength, level, expected):
    assert calculate_crit_value(strength, level) == pytest.approx(expected)

