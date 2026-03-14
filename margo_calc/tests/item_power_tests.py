import pytest
from services.item_power import calculate_item_rarity_power, calculate_item_level_power, calculate_weapon_slow, calculate_weapon_damage

@pytest.mark.parametrize(
    'level, expected',
    [
        (1, 2.62),
        (50, 180),
        (300, 2580),
    ]
)

def test_calculate_item_level_power(level, expected):
    assert calculate_item_level_power(level) == pytest.approx(expected)

@pytest.mark.parametrize(
    'level, rarity_factor, expected',
    [
        (1, 0, 0),
        (100, 0, 0),
        (300, 0, 0),

        (1, 1, 10.48),
        (100, 1, 18.4),
        (300, 1, 34.4),

        (1, 2, 18.34),
        (100, 2, 32.2),
        (300, 2, 60.2),

        (1, 3, 26.2),
        (100, 3, 46.0),
        (300, 3, 86),

        (1, 4, 34.08),
        (100, 4, 61.8),
        (300, 4, 117.8),
    ]
)

def test_calculate_item_rarity_power(level, rarity_factor, expected):
    assert calculate_item_rarity_power(level, rarity_factor) == pytest.approx(expected)

@pytest.mark.parametrize(
    'weapon_factor, item_rarity_power, item_level_power, expected',
    [
        (0.3378, 0, 2.62, 7.0802888),
        (0.3378, 0, 460, 1243.104),
        (0.3378, 0, 2580, 6972.192),

        (0.5578, 0, 2.62, 11.691488),
        (0.5578, 0, 460, 2052.7039),
        (0.5578, 0, 2580, 11512.9919),

        (0.3188, 0, 2.62, 6.682048),
        (0.3188, 0, 460, 1173.184),
        (0.3188, 0, 2580, 6580.03),

        (0.3378, 1, 2.62, 9.782688),
        (0.3378, 1, 460, 1245.8064),
        (0.3378, 1, 2580, 6974.8944),

        (0.5578, 1, 2.62, 16.153888),
        (0.5578, 1, 460, 2057.1664),
        (0.5578, 1, 2580, 11517.45439),

        (0.3188, 1, 2.62, 9.232448),
        (0.3188, 1, 460, 1175.73439),
        (0.3188, 1, 2580, 6582.58239),

        (0.3378, 2, 2.62, 12.485088),
        (0.3378, 2, 460, 1248.5088),
        (0.3378, 2, 2580, 6977.59679),

        (0.5578, 2, 2.62, 20.616288),
        (0.5578, 2, 460, 2061.6288),
        (0.5578, 2, 2580, 11521.91679),

        (0.3188, 2, 2.62, 11.782848),
        (0.3188, 2, 460, 1178.2848),
        (0.3188, 2, 2580, 6585.13279),

        (0.3378, 3, 2.62, 15.187488),
        (0.3378, 3, 460, 1251.2112),
        (0.3378, 3, 2580, 6980.29919),

        (0.5578, 3, 2.62, 25.078688),
        (0.5578, 3, 460, 2066.0912),
        (0.5578, 3, 2580, 11526.3792),

        (0.3188, 3, 2.62, 14.333248),
        (0.3188, 3, 460, 1180.8352),
        (0.3188, 3, 2580, 6587.68319),

        (0.3378, 4, 2.62, 17.889888),
        (0.3378, 4, 460, 1253.91359),
        (0.3378, 4, 2580, 6983.0016),

        (0.5578, 4, 2.62, 29.541088),
        (0.5578, 4, 460, 2070.55359),
        (0.5578, 4, 2580, 11530.8416),

        (0.3188, 4, 2.62, 16.8836479),
        (0.3188, 4, 460, 1183.38559),
        (0.3188, 4, 2580, 6590.2336),

    ]
)

def test_calculate_weapon_damage(weapon_factor, item_rarity_power, item_level_power, expected):
    assert calculate_weapon_damage(weapon_factor, item_rarity_power, item_level_power) == pytest.approx(expected)

@pytest.mark.parametrize(
    'slow_factor, item_level, expected',
    [
        (0.009566, 1, 0.009566),
        (0.009566, 100, 0.9566),
        (0.009566, 300, 2.8698),

        (0.010000, 1, 0.01),
        (0.010000, 100, 1),
        (0.010000, 300, 3),

        (0.0044625, 1, 0.0044625),
        (0.0044625, 100, 0.446250),
        (0.0044625, 300, 1.33875),

        (0.0073529, 1, 0.0073529),
        (0.0073529, 100, 0.73529),
        (0.0073529, 300, 2.20587),

    ]
)
def test_calculate_weapon_slow(slow_factor, item_level, expected):
    assert calculate_weapon_slow(slow_factor, item_level) == pytest.approx(expected)
