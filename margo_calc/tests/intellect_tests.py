import pytest
from services.intellect import calculate_absorb_limit, calculate_crit_value

# ABSORB LIMIT TESTS
@pytest.mark.parametrize(
    'intellect, expected',
    [
        (0, 0),
        (1, 7),
        (1000, 7000)
    ]
)
def test_calculate_absorb_limit(intellect: int, expected: int) -> None:
    assert calculate_absorb_limit(intellect) == expected

# CRIT VALUE TESTS
@pytest.mark.parametrize(
    'intellect, level, expected',
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
    ]
)
def test_calculate_crit_value_down_cap(intellect: int, level: int, expected: int) -> None:
    assert calculate_crit_value(intellect, level) == expected

@pytest.mark.parametrize(
    'intellect, level, expected',
    [
        (0, 0, 0),
        (0, 21, 0),
        (0, 50, 0),
        (0, 301, 0),
    ]
)
def test_calculate_crit_value_intellect_zero(intellect: int, level: int, expected: int) -> None:
    assert calculate_crit_value(intellect, level) == expected

@pytest.mark.parametrize(
    'intellect, level, expected',
    [
        (1, 21, 0.09523809),
        (1, 50, 0.04),
        (1, 300, 0.0066666666),

        (100, 21, 9.523809),
        (100, 50, 4),
        (100, 300, 0.66666666),
    ]
)

def test_calculate_crit_value_normal_values(intellect: int, level: int, expected: float) -> None:
    assert calculate_crit_value(intellect, level) == pytest.approx(expected)

@pytest.mark.parametrize(
    'intellect, level, expected',
    [
        (1, 301, 0.0066666666),
        (1, 500, 0.0066666666),
        (1, 1000, 0.0066666666),
    ]
)
def test_calculate_crit_value_up_level_cap(intellect: int, level: int, expected: float) -> None:
    assert calculate_crit_value(intellect, level) == pytest.approx(expected)
