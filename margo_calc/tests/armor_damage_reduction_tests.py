from services.armor_damage_reduction import calculate_physical_damage_reduction, calculate_range_damage_reduction, calculate_secondary_damage_reduction, calculate_fire_damage_reduction, calculate_frost_damage_reduction, calculate_light_damage_reduction
import pytest

@pytest.mark.parametrize(
    'damage, armor, expected',
    [
        (1000, 100, 890.1),
        (1000, 1, 998.87031),
        (1000, 1000, 180.00),
    ]
)

def test_calculate_physical_damage_reduction(damage: int, armor: int, expected: float) -> None:
    assert calculate_physical_damage_reduction(damage, armor) == pytest.approx(expected)


@pytest.mark.parametrize(
    'damage, armor, expected',
    [
        (1000, 100, 890.1),
        (1000, 1, 998.87031),
        (1000, 1000, 180.00),
    ]
)
def test_calculate_range_damage_reduction(damage: int, armor: int, expected: float) -> None:
    assert calculate_range_damage_reduction(damage, armor) == pytest.approx(expected)

@pytest.mark.parametrize(
    'damage, armor, expected',
    [
        (1000, 100, 890.1),
        (1000, 1, 998.87031),
        (1000, 1000, 180.00),
    ]
)
def test_calculate_secondary_damage_reduction(damage: int, armor: int, expected: float) -> None:
    assert calculate_secondary_damage_reduction(damage, armor) == pytest.approx(expected)

@pytest.mark.parametrize(
    'damage, armor, expected',
    [
        (1000, 100, 890.1),
        (1000, 1, 998.87031),
        (1000, 1000, 180.00),
    ]
)
def test_calculate_secondary_damage_reduction(damage: int, armor: int, expected: float) -> None:
    assert calculate_secondary_damage_reduction(damage, armor) == pytest.approx(expected)

@pytest.mark.parametrize(
    'damage, armor, expected',
    [
        (1000, 100, 944.275),
        (1000, 1, 999.4350775),
        (1000, 1000, 512.5),
    ]
)
def test_calculate_fire_damage_reduction(damage: int, armor: int, expected: float) -> None:
    assert calculate_fire_damage_reduction(damage, armor) == pytest.approx(expected)

@pytest.mark.parametrize(
    'damage, armor, expected',
    [
        (1000, 100, 944.275),
        (1000, 1, 999.4350775),
        (1000, 1000, 512.5),
    ]
)
def test_calculate_frost_damage_reduction(damage: int, armor: int, expected: float) -> None:
    assert calculate_frost_damage_reduction(damage, armor) == pytest.approx(expected)

@pytest.mark.parametrize(
    'damage, armor, expected',
    [
        (1000, 100, 944.275),
        (1000, 1, 999.4350775),
        (1000, 1000, 512.5),
    ]
)
def test_calculate_light_damage_reduction(damage: int, armor: int, expected: float) -> None:
    assert calculate_light_damage_reduction(damage, armor) == pytest.approx(expected)



