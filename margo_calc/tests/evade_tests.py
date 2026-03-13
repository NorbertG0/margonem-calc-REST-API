from services.evade import calculate_evade
import pytest

@pytest.mark.parametrize(
    'evade, enemy_level, expected',
    [
        (1, 1, 20),
        (1, 299, 0.0668896),
        (1, 300, 0.06666666),
        (1, 301, 0.06666666),

        (100, 1, 2000),
        (100, 299, 6.6889632),
        (100, 300, 6.6666666),
        (100, 301, 6.6666666),
    ]
)

def test_calculate_evade(evade, enemy_level, expected):
    assert calculate_evade(evade, enemy_level) == pytest.approx(expected)