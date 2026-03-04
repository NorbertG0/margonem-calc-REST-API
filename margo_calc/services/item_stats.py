
def calculate_all_stats(level: int, amount_of_bon: int) -> float:
    return 0.25 * level * amount_of_bon + 8

def calculate_strength(level: int, amount_of_bon: int) -> float:
    return 5 * level * amount_of_bon / 9 + 4

def calculate_dexterity(level: int, amount_of_bon: int) -> float:
    return 5 * level * amount_of_bon / 9 + 4

def calculate_intellect(level: int, amount_of_bon: int) -> float:
    return 5 * level * amount_of_bon / 9 + 4

def calculate_attack_speed(level: int, amount_of_bon: int) -> float:
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
    return 1 + amount_of_bon * level_power / 50

def calculate_armor_destruction(amount_of_bon: int, level_power: float) -> float:
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
    return 0.01 * round(8 + amount_of_bon * 2 * level / 7)

def calculate_crit(amount_of_bon: int) -> int:
    return amount_of_bon

def calculate_phisycal_crit_power(amount_of_bon: int) -> int:
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