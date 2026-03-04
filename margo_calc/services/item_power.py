import math
from additional_functions import sign

def calculate_item_level_power(level: int) -> float:
    return 0.02 * level ** 2 + 2.6 * level

def calculate_item_rarity_power(level: int, rarity_factor: int) -> float:
    return 0.02 * level * math.ceil(10 * rarity_factor / 3) + sign(rarity_factor) * (7.8 * rarity_factor + 2.6)

def calculate_weapon_damage(weapon_factor: float, item_rarity_power: float, item_level_power: float) -> float:
    return 8 * weapon_factor * (item_rarity_power + item_level_power)

def calculate_weapon_slow(slow_factor:  float, item_level: int) -> float:
    return slow_factor * item_level