from schemas.item_stats import ItemStatsInput
from additional_functions import calculate_range

RANGE_NEG2_5 = range(-2, 6)
RANGE_0_5 = range(0, 6)


def calculate_all_stats(level: int, amount_of_bon: int) -> float:
    if amount_of_bon == 0:
        return 0
    return 0.25 * level * amount_of_bon + 8

def calculate_strength(level: int, amount_of_bon: int) -> float:
    if amount_of_bon == 0:
        return 0
    return 5 * level * amount_of_bon / 9 + 4

def calculate_dexterity(level: int, amount_of_bon: int) -> float:
    if amount_of_bon == 0:
        return 0
    return 5 * level * amount_of_bon / 9 + 4

def calculate_intellect(level: int, amount_of_bon: int) -> float:
    if amount_of_bon == 0:
        return 0
    return 5 * level * amount_of_bon / 9 + 4

def calculate_attack_speed(level: int, amount_of_bon: int) -> float:
    if amount_of_bon == 0:
        return 0
    return 0.01 * round(8 + amount_of_bon * 0.25 * level)

def calculate_health_points(level: int, amount_of_bon: int, level_power: float, class_power: float) -> float:
    return amount_of_bon * 3.08 * round(8 + level + 0.2 * level_power * class_power)

def calculate_heal(level: int, amount_of_bon: int, level_power: float, class_power: float) -> float:
    return 8 * amount_of_bon * (0.8 * level + 0.2 * level_power * class_power)

def calculate_armor(amount_of_bon: int, level_power: float, class_power: float) -> float:
    return amount_of_bon * 0.15 * level_power * class_power

def calculate_poison_res(amount_of_bon: int) -> int:
    return 5 * amount_of_bon

def calculate_block(amount_of_bon: int, level: int) -> float:
    return amount_of_bon * level * 3 / 20

def calculate_evade(amount_of_bon: int, level: int) -> float:
    return amount_of_bon * level / 10

def calculate_weapon_armor_destruction(amount_of_bon: int, level_power: float) -> float:
    if amount_of_bon == 0:
        return 0
    return 1 + amount_of_bon * level_power / 50

def calculate_armor_destruction(amount_of_bon: int, level_power: float) -> float:
    if amount_of_bon == 0:
        return 0
    return 1 + amount_of_bon * 0.75 * level_power / 50

def calculate_resist_destruction(amount_of_bon: int) -> int:
    return amount_of_bon

def calculate_absorption(amount_of_bon: int, level_power: float, class_power: float) -> float:
    return amount_of_bon * 0.6 * level_power * class_power

def calculate_magic_absorption(amount_of_bon: int, level_power: float, class_power: float) -> float:
    return amount_of_bon * 0.6 * level_power * class_power

def calculate_mana(amount_of_bon: int, level: int) -> float:
    return amount_of_bon * (5 + level / 4)

def calculate_energy(amount_of_bon: int, level: int) -> float:
    return amount_of_bon * (10 + level / 15)

def calculate_attack_speed_reduction(amount_of_bon: int, level: int) -> float:
    if amount_of_bon == 0:
        return 0
    return 0.01 * round(8 + amount_of_bon * 2 * level / 7)

def calculate_crit(amount_of_bon: int) -> int:
    return amount_of_bon

def calculate_physical_crit_power(amount_of_bon: int) -> int:
    return amount_of_bon * 6

def calculate_magic_crit_power(amount_of_bon: int) -> int:
    return amount_of_bon * 6

def calculate_crit_chance_reduction(amount_of_bon: int) -> int:
    return amount_of_bon * 2

def calculate_energy_reduction_chance(amount_of_bon: int) -> float:
    if amount_of_bon == 3:
        return 1.0
    return min(100, 0.40 * amount_of_bon)

def calculate_energy_reduction_value(level: int) -> float:
    return 2 + 0.04 * level

def calculate_mana_reduction_chance(amount_of_bon: int) -> float:
    if amount_of_bon == 3:
        return 1.0
    return min(100, 0.40 * amount_of_bon)

def calculate_mana_reduction_value(level: int) -> float:
    return 6 + 0.08 * level

def calculate_evade_reduction(amount_of_bon: int, level: int) -> float:
    return amount_of_bon * level / 10

def calculate_fire_resists(amount_of_bon: int) -> int:
    return amount_of_bon * 3

def calculate_frost_resists(amount_of_bon: int) -> int:
    return amount_of_bon * 3

def calculate_light_resists(amount_of_bon: int) -> int:
    return amount_of_bon * 3

def calculate_item_stats(data: ItemStatsInput):

    level_power = data.level_power or 1
    class_power = data.class_power or 1

    return {
        'all_stats': calculate_range(range(0, 7), lambda a: calculate_all_stats(data.level, a)),
        'strength': calculate_range(RANGE_NEG2_5, lambda a: calculate_strength(data.level, a)),
        'dexterity': calculate_range(RANGE_NEG2_5, lambda a: calculate_dexterity(data.level, a)),
        'intellect': calculate_range(RANGE_NEG2_5, lambda a: calculate_intellect(data.level, a)),
        'attack_speed': calculate_range(RANGE_NEG2_5, lambda a: calculate_attack_speed(data.level, a)),
        'health_points': calculate_range(range(-2, 7), lambda a: calculate_health_points(data.level, a, level_power, class_power)),
        'heal': calculate_range(range(0, 4), lambda a: calculate_heal(data.level, a, level_power, class_power)),
        'armor': calculate_range(RANGE_NEG2_5, lambda a: calculate_armor(a, level_power, class_power)),
        'poison_resistance': calculate_range(RANGE_NEG2_5, lambda a: calculate_poison_res(a)),
        'evade': calculate_range(RANGE_NEG2_5, lambda a: calculate_evade(a, data.level)),
        'block': calculate_range(range(-1, 6), lambda a: calculate_block(a, data.level)),
        'weapon_armor_destruction': calculate_range(RANGE_0_5, lambda a: calculate_weapon_armor_destruction(a, level_power)),
        'armor_destruction': calculate_range(RANGE_0_5, lambda a: calculate_armor_destruction(a, level_power)),
        'resistance_destruction': calculate_range(RANGE_0_5, lambda a: calculate_resist_destruction(a)),
        'absorption': calculate_range(RANGE_0_5, lambda a: calculate_absorption(a, level_power, class_power)),
        'magic_absorption': calculate_range(RANGE_0_5, lambda a: calculate_magic_absorption(a, level_power, class_power)),
        'mana': calculate_range(RANGE_0_5, lambda a: calculate_mana(a, data.level)),
        'energy': calculate_range(RANGE_0_5, lambda a: calculate_energy(a, data.level)),
        'attack_speed_reduction': calculate_range(RANGE_0_5, lambda a: calculate_attack_speed_reduction(a, data.level)),
        'crit': calculate_range(RANGE_0_5, lambda a: calculate_crit(a)),
        'physical_crit_power': calculate_range(RANGE_NEG2_5, lambda a: calculate_physical_crit_power(a)),
        'magic_crit_power': calculate_range(RANGE_NEG2_5, lambda a: calculate_magic_crit_power(a)),
        'crit_chance_reduction': calculate_range(range(0, 4), lambda a: calculate_crit_chance_reduction(a)),
        'energy_reduction_chance': calculate_range(range(0, 4), lambda a: calculate_energy_reduction_chance(a)),
        'energy_reduction_value': calculate_energy_reduction_value(data.level),
        'mana_reduction_chance': calculate_range(range(0, 4), lambda a: calculate_mana_reduction_chance(a)),
        'mana_reduction_value': calculate_mana_reduction_value(data.level),
        'evade_reduction': calculate_range(RANGE_0_5, lambda a: calculate_evade_reduction(a, data.level)),
        'fire_resists': calculate_range(range(-3, 11), lambda a: calculate_fire_resists(a)),
        'frost_resists': calculate_range(range(-3, 11), lambda a: calculate_frost_resists(a)),
        'light_resists': calculate_range(range(-3, 11), lambda a: calculate_light_resists(a))
    }
