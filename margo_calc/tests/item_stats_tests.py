import pytest
from services.item_stats import (calculate_all_stats, calculate_strength, calculate_intellect,
                                 calculate_dexterity, calculate_attack_speed, calculate_health_points, calculate_heal)


@pytest.mark.parametrize(
    'level, amount_of_bon, expected',
    [
        (1, 0, 0),
        (1, 1, 8.25),
        (1, 2, 8.5),
        (1, 3, 8.75),
        (1, 4, 9),
        (1, 5, 9.25),
        (1, 6, 9.5),

        (300, 0, 0),
        (300, 1, 83),
        (300, 2, 158),
        (300, 3, 233),
        (300, 4, 308),
        (300, 5, 383),
        (300, 6, 458),
    ],
)

def test_calculate_all_stats(level, amount_of_bon, expected):
    assert calculate_all_stats(level, amount_of_bon) == pytest.approx(expected)


@pytest.mark.parametrize(
    'level, amount_of_bon, expected',
    [
        (1, -2, 2.888888),
        (1, -1, 3.444444),
        (1, 0, 0),
        (1, 1, 4.555555),
        (1, 2, 5.111111),
        (1, 3, 5.666666),
        (1, 4, 6.222222),
        (1, 5, 6.777777),
        (1, 6, 7.333333),

        (300, -2, -329.333333),
        (300, -1, -162.666666),
        (300, 0, 0),
        (300, 1, 170.666666),
        (300, 2, 337.333333),
        (300, 3, 504),
        (300, 4, 670.666666),
        (300, 5, 837.333333),
        (300, 6, 1004.0),
    ],
)

def test_calculate_strength(level, amount_of_bon, expected):
    assert calculate_strength(level, amount_of_bon) == pytest.approx(expected)

@pytest.mark.parametrize(
    'level, amount_of_bon, expected',
    [
        (1, -2, 2.888888),
        (1, -1, 3.444444),
        (1, 0, 0),
        (1, 1, 4.555555),
        (1, 2, 5.111111),
        (1, 3, 5.666666),
        (1, 4, 6.222222),
        (1, 5, 6.777777),
        (1, 6, 7.333333),

        (300, -2, -329.333333),
        (300, -1, -162.666666),
        (300, 0, 0),
        (300, 1, 170.666666),
        (300, 2, 337.333333),
        (300, 3, 504),
        (300, 4, 670.666666),
        (300, 5, 837.333333),
        (300, 6, 1004.0),
    ]
)

def test_calculate_dexterity(level, amount_of_bon, expected):
    assert calculate_dexterity(level, amount_of_bon) == pytest.approx(expected)

@pytest.mark.parametrize(
    'level, amount_of_bon, expected',
    [
        (1, -2, 2.888888),
        (1, -1, 3.444444),
        (1, 0, 0),
        (1, 1, 4.555555),
        (1, 2, 5.111111),
        (1, 3, 5.666666),
        (1, 4, 6.222222),
        (1, 5, 6.777777),
        (1, 6, 7.333333),

        (300, -2, -329.333333),
        (300, -1, -162.666666),
        (300, 0, 0),
        (300, 1, 170.666666),
        (300, 2, 337.333333),
        (300, 3, 504),
        (300, 4, 670.666666),
        (300, 5, 837.333333),
        (300, 6, 1004.0),
    ]
)

def test_calculate_intellect(level, amount_of_bon, expected):
    assert calculate_intellect(level, amount_of_bon) == pytest.approx(expected)

@pytest.mark.parametrize(
    'level, amount_of_bon, expected',
    [
        (1, -2, 0.08),
        (1, -1, 0.08),
        (1, 0, 0),
        (1, 1, 0.08),
        (1, 2, 0.08),
        (1, 3, 0.09),
        (1, 4, 0.09),
        (1, 5, 0.09),

        (300, -2, -1.42),
        (300, -1, -0.67),
        (300, 0, 0),
        (300, 1, 0.83),
        (300, 2, 1.58),
        (300, 3, 2.33),
        (300, 4, 3.08),
        (300, 5, 3.83),
    ]
)

def test_calculate_attack_speed(level, amount_of_bon, expected):
    assert calculate_attack_speed(level, amount_of_bon) == pytest.approx(expected)

@pytest.mark.parametrize(
    'level, amount_of_bon, level_power, class_power, expected',
    [
        (1, -2, 2.62, 1, -61.6),
        (1, -1, 2.62, 1, -30.8),
        (1, 0, 2.62, 1, 0),
        (1, 1, 2.62, 1, 30.8),
        (1, 2, 2.62, 1, 61.6),
        (1, 3, 2.62, 1, 92.4),
        (1, 4, 2.62, 1, 123.2),
        (1, 5, 2.62, 1, 154.0),
        (1, 6, 2.62, 1, 184.8),

        (1, -2, 2.62, 0.33, -55.44),
        (1, -1, 2.62, 0.33, -27.72),
        (1, 0, 2.62, 0.33, 0),
        (1, 1, 2.62, 0.33, 27.72),
        (1, 2, 2.62, 0.33, 55.44),
        (1, 3, 2.62, 0.33, 83.16),
        (1, 4, 2.62, 0.33, 110.88),
        (1, 5, 2.62, 0.33, 138.6),
        (1, 6, 2.62, 0.33, 166.32),

        (300, -2, 2580, 1, -5075.84),
        (300, -1, 2580, 1, -2537.92),
        (300, 0, 2580, 1, 0),
        (300, 1, 2580, 1, 2537.92),
        (300, 2, 2580, 1, 5075.84),
        (300, 3, 2580, 1, 7613.76),
        (300, 4, 2580, 1, 10151.68),
        (300, 5, 2580, 1, 12689.6),
        (300, 6, 2580, 1, 15227.52),

        (300, -2, 2580, 0.33, -2944.48),
        (300, -1, 2580, 0.33, -1472.24),
        (300, 0, 2580, 0.33, 0),
        (300, 1, 2580, 0.33, 1472.24),
        (300, 2, 2580, 0.33, 2944.48),
        (300, 3, 2580, 0.33, 4416.72),
        (300, 4, 2580, 0.33, 5888.96),
        (300, 5, 2580, 0.33, 7361.2),
        (300, 6, 2580, 0.33, 8833.44),
    ],
)

def test_calculate_health_points(level, amount_of_bon, level_power, class_power, expected):
    assert calculate_health_points(level, amount_of_bon, level_power, class_power) == pytest.approx(expected)

@pytest.mark.parametrize(
    'level, amount_of_bon, level_power, class_power, expected',
    [
        (1, 0, 2.62, 1, 0),
        (1, 1, 2.62, 1, 10.592),
        (1, 2, 2.62, 1, 21.184),
        (1, 3, 2.62, 1, 31.776000),
        (1, 4, 2.62, 1, 42.368),
        (1, 5, 2.62, 1, 52.96),

        (1, 0, 2.62, 0.33, 0),
        (1, 1, 2.62, 0.33, 7.78336),
        (1, 2, 2.62, 0.33, 15.56672),
        (1, 3, 2.62, 0.33, 23.35008),
        (1, 4, 2.62, 0.33, 31.13344),
        (1, 5, 2.62, 0.33, 38.9168),

        (300, 0, 2580, 1, 0),
        (300, 1, 2580, 1, 6048),
        (300, 2, 2580, 1, 12096),
        (300, 3, 2580, 1, 18144),
        (300, 4, 2580, 1, 24192),
        (300, 5, 2580, 1, 30240),

        (300, 0, 2580, 0.33, 0),
        (300, 1, 2580, 0.33, 3282.24),
        (300, 2, 2580, 0.33, 6564.48),
        (300, 3, 2580, 0.33, 9846.72),
        (300, 4, 2580, 0.33, 13128.96),
        (300, 5, 2580, 0.33, 16411.199999),
    ],
)

def test_calculate_heal(level, amount_of_bon, level_power, class_power, expected):
    assert calculate_heal(level, amount_of_bon, level_power, class_power) == pytest.approx(expected)