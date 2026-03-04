import pytest

from services.item_defense import *

def test_calculate_item_armor():
    assert calculate_item_armor(0.11250, 1, 0, 2.62) == 2.358
    assert calculate_item_armor(0.11250, 1, 1, 2.62) == 3.258
    assert calculate_item_armor(0.11250, 1, 2, 2.62) == 4.158
    assert calculate_item_armor(0.11250, 1, 3, 2.62) == 5.058
    assert calculate_item_armor(0.11250, 1, 4, 2.62) == 5.958

    assert calculate_item_armor(0.11250, 0.33, 0, 2.62) == pytest.approx(0.778140)
    assert calculate_item_armor(0.11250, 0.33, 1, 2.62) == pytest.approx(1.075140)
    assert calculate_item_armor(0.11250, 0.33, 2, 2.62) == pytest.approx(1.372140)
    assert calculate_item_armor(0.11250, 0.33, 3, 2.62) == pytest.approx(1.669140)
    assert calculate_item_armor(0.11250, 0.33, 4, 2.62) == pytest.approx(1.966140)

    assert calculate_item_armor(0.11250, 1, 0, 180) == 162.0
    assert calculate_item_armor(0.11250, 1, 1, 180) == 162.9
    assert calculate_item_armor(0.11250, 1, 2, 180) == 163.8
    assert calculate_item_armor(0.11250, 1, 3, 180) == pytest.approx(164.70)
    assert calculate_item_armor(0.11250, 1, 4, 180) == 165.6

    assert calculate_item_armor(0.11250, 0.33, 0, 180) == pytest.approx(53.460)
    assert calculate_item_armor(0.11250, 0.33, 1, 180) == pytest.approx(53.757)
    assert calculate_item_armor(0.11250, 0.33, 2, 180) == pytest.approx(54.054)
    assert calculate_item_armor(0.11250, 0.33, 3, 180) == pytest.approx(54.351)
    assert calculate_item_armor(0.11250, 0.33, 4, 180) == pytest.approx(54.648)

    assert calculate_item_armor(0.13500, 1, 0, 2.62) == 2.8296
    assert calculate_item_armor(0.13500, 1, 1, 2.62) == 3.9096
    assert calculate_item_armor(0.13500, 1, 2, 2.62) == 4.9896
    assert calculate_item_armor(0.13500, 1, 3, 2.62) == 6.0696
    assert calculate_item_armor(0.13500, 1, 4, 2.62) == 7.1496

    assert calculate_item_armor(0.13500, 0.33, 0, 2.62) == pytest.approx(0.933768)
    assert calculate_item_armor(0.13500, 0.33, 1, 2.62) == pytest.approx(1.290168)
    assert calculate_item_armor(0.13500, 0.33, 2, 2.62) == pytest.approx(1.646568)
    assert calculate_item_armor(0.13500, 0.33, 3, 2.62) == pytest.approx(2.002968)
    assert calculate_item_armor(0.13500, 0.33, 4, 2.62) == pytest.approx(2.359368)

    assert calculate_item_armor(0.13500, 1, 0, 180) == 194.4
    assert calculate_item_armor(0.13500, 1, 1, 180) == pytest.approx(195.48)
    assert calculate_item_armor(0.13500, 1, 2, 180) == 196.56
    assert calculate_item_armor(0.13500, 1, 3, 180) == pytest.approx(197.64)
    assert calculate_item_armor(0.13500, 1, 4, 180) == pytest.approx(198.72)

    assert calculate_item_armor(0.13500, 0.33, 0, 180) == pytest.approx(64.1520)
    assert calculate_item_armor(0.13500, 0.33, 1, 180) == pytest.approx(64.5084)
    assert calculate_item_armor(0.13500, 0.33, 2, 180) == pytest.approx(64.8648)
    assert calculate_item_armor(0.13500, 0.33, 3, 180) == pytest.approx(65.2212)
    assert calculate_item_armor(0.13500, 0.33, 4, 180) == pytest.approx(65.5776)


