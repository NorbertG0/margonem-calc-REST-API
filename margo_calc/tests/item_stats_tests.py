import pytest
from services.item_stats import *


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

def test_calcuate_attack_speed(level, amount_of_bon, expected):
    assert calculate_attack_speed(level, amount_of_bon) == pytest.approx(expected)
