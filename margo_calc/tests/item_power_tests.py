import pytest
from services.item_power import *

def test_calculate_item_level_power():
    assert calculate_item_level_power(1) == 2.62
    assert calculate_item_level_power(50) == 180
    assert calculate_item_level_power(300) == 2580

def test_calculate_item_rarity_power_normal():
    assert calculate_item_rarity_power(1, 0) == 0
    assert calculate_item_rarity_power(100, 0) == 0
    assert calculate_item_rarity_power(300, 0) == 0

def test_calculate_item_rarity_power_unique():
    assert calculate_item_rarity_power(1, 1) == 10.48
    assert calculate_item_rarity_power(100, 1) == 18.4
    assert calculate_item_rarity_power(300, 1) == 34.4

def test_calculate_item_rarity_power_heroic():
    assert calculate_item_rarity_power(1, 2) == 18.34
    assert calculate_item_rarity_power(100, 2) == 32.2
    assert calculate_item_rarity_power(300, 2) == 60.2

def test_calculate_item_rarity_power_legendary():
    assert calculate_item_rarity_power(1, 3) == 26.2
    assert calculate_item_rarity_power(100, 3) == 46.0
    assert calculate_item_rarity_power(300, 3) == 86.0

def test_calculate_item_rarity_power_artifact():
    assert calculate_item_rarity_power(1, 4) == 34.08
    assert calculate_item_rarity_power(100, 4) == 61.8
    assert calculate_item_rarity_power(300, 4) == 117.8

def test_calculate_weapon_damage_normal():
    assert calculate_weapon_damage(0.3378, 0, 2.62) == 7.080288
    assert calculate_weapon_damage(0.3378, 0, 460) == 1243.104
    assert calculate_weapon_damage(0.3378, 0, 2580) == 6972.192

    assert calculate_weapon_damage(0.5578, 0, 2.62) == 11.691488
    assert calculate_weapon_damage(0.5578, 0, 460) == pytest.approx(2052.7039)
    assert calculate_weapon_damage(0.5578, 0, 2580) == pytest.approx(11512.991)

    assert calculate_weapon_damage(0.3188, 0, 2.62) == 6.682048
    assert calculate_weapon_damage(0.3188, 0, 460) == 1173.184
    assert calculate_weapon_damage(0.3188, 0, 2580) == pytest.approx(6580.0319)

def test_calculate_weapon_damage_unique():
    assert calculate_weapon_damage(0.3378, 1, 2.62) == 9.782688
    assert calculate_weapon_damage(0.3378, 1, 460) == 1245.8064
    assert calculate_weapon_damage(0.3378, 1, 2580) == 6974.8944

    assert calculate_weapon_damage(0.5578, 1, 2.62) == 16.153888
    assert calculate_weapon_damage(0.5578, 1, 460) == 2057.1664
    assert calculate_weapon_damage(0.5578, 1, 2580) == pytest.approx(11517.45439)

    assert calculate_weapon_damage(0.3188, 1, 2.62) == 9.232448
    assert calculate_weapon_damage(0.3188, 1, 460) == pytest.approx(1175.73439)
    assert calculate_weapon_damage(0.3188, 1, 2580) == pytest.approx(6582.58239)

def test_calculate_weapon_damage_heroic():
    assert calculate_weapon_damage(0.3378, 2, 2.62) == 12.485088
    assert calculate_weapon_damage(0.3378, 2, 460) == 1248.5088
    assert calculate_weapon_damage(0.3378, 2, 2580) == pytest.approx(6977.59679)

    assert calculate_weapon_damage(0.5578, 2, 2.62) == 20.616288
    assert calculate_weapon_damage(0.5578, 2, 460) == 2061.6288
    assert calculate_weapon_damage(0.5578, 2, 2580) == pytest.approx(11521.91679)

    assert calculate_weapon_damage(0.3188, 2, 2.62) == 11.782848
    assert calculate_weapon_damage(0.3188, 2, 460) == 1178.2848
    assert calculate_weapon_damage(0.3188, 2, 2580) == pytest.approx(6585.13279)

def test_calculate_weapon_damage_legendary():
    assert calculate_weapon_damage(0.3378, 3, 2.62) == 15.187488
    assert calculate_weapon_damage(0.3378, 3, 460) == 1251.2112
    assert calculate_weapon_damage(0.3378, 3, 2580) == pytest.approx(6980.29919)

    assert calculate_weapon_damage(0.5578, 3, 2.62) == 25.078688
    assert calculate_weapon_damage(0.5578, 3, 460) == 2066.0912
    assert calculate_weapon_damage(0.5578, 3, 2580) == 11526.3792

    assert calculate_weapon_damage(0.3188, 3, 2.62) == 14.333248
    assert calculate_weapon_damage(0.3188, 3, 460) == 1180.8352
    assert calculate_weapon_damage(0.3188, 3, 2580) == pytest.approx(6587.68319)

def test_calculate_weapon_damage_artifact():
    assert calculate_weapon_damage(0.3378, 4, 2.62) == 17.889888
    assert calculate_weapon_damage(0.3378, 4, 460) == pytest.approx(1253.91359)
    assert calculate_weapon_damage(0.3378, 4, 2580) == 6983.0016

    assert calculate_weapon_damage(0.5578, 4, 2.62) == 29.541088
    assert calculate_weapon_damage(0.5578, 4, 460) == pytest.approx(2070.55359)
    assert calculate_weapon_damage(0.5578, 4, 2580) == 11530.8416

    assert calculate_weapon_damage(0.3188, 4, 2.62) == pytest.approx(16.8836479)
    assert calculate_weapon_damage(0.3188, 4, 460) == pytest.approx(1183.38559)
    assert calculate_weapon_damage(0.3188, 4, 2580) == 6590.2336

def test_calculate_weapon_slow():
    assert calculate_weapon_slow(0.009566, 1) == 0.009566
    assert calculate_weapon_slow(0.009566, 100) == 0.9566
    assert calculate_weapon_slow(0.009566, 300) == 2.8698

    assert calculate_weapon_slow(0.010000, 1) == 0.01
    assert calculate_weapon_slow(0.010000, 100) == 1
    assert calculate_weapon_slow(0.010000, 300) == 3

    assert calculate_weapon_slow(0.0044625, 1) == 0.0044625
    assert calculate_weapon_slow(0.0044625, 100) == pytest.approx(0.446250)
    assert calculate_weapon_slow(0.0044625, 300) == 1.33875

    assert calculate_weapon_slow(0.0073529, 1) == 0.0073529
    assert calculate_weapon_slow(0.0073529, 100) == 0.73529
    assert calculate_weapon_slow(0.0073529, 300) == 2.20587