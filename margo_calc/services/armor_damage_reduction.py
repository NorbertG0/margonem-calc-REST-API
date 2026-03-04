from exceptions import ValidationError, MathError

def calculate_physical_damage_reduction(damage: int, armor: int) -> float:
    return damage - armor * (1.13 - 0.31 * armor / damage)

def calculate_range_damage_reduction(damage: int, armor: int) -> float:
    return damage - armor * (1.13 - 0.31 * armor / damage)

def calculate_secondary_damage_reduction(damage: int, armor: int) -> float:
    return damage - armor * (1.13 - 0.31 * armor / damage)

def calculate_fire_damage_reduction(damage: int, armor: int) -> float:
    return damage - 0.5 * armor * (1.13 - 0.31 * 0.5 * armor / damage)

def calculate_frost_damage_reduction(damage: int, armor: int) -> float:
    return damage - 0.5 * armor * (1.13 - 0.31 * 0.5 * armor / damage)

def calculate_light_damage_reduction(damage: int, armor: int) -> float:
    return damage - 0.5 * armor * (1.13 - 0.31 * 0.5 * armor / damage)