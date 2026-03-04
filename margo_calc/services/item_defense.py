
def calculate_item_armor(armor_factor: float, class_power: float, rarity_power: float, level_power: float) -> float:
    return 8 * armor_factor * class_power * (rarity_power + level_power)