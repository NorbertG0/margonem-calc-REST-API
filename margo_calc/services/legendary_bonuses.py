
NAMES_AND_CHANCES = {
    'very_crit': ['Cios bardzo krytyczny', 0.17],
    'holy_touch': ['Dotyk anioła', 0.07],
    'curse': ['Klątwa', 0.09],
    'glare': ['Oślepienie', 0.09],
    'last_heal': ['Ostatni ratunek', 0.18],
    'critred': ['Krytyczna osłona', 0.25],
    'facade': ['Fasada opieki', 0.13],
    'cleanse': ['Płomienne oczyszczenie', 0.12],
    'anguish': ['Krwawa udręka', 0.08],
    'puncture': ['Przeszywająca skuteczność', 0.12]
}


def calculate_first_nerf_level(item_level: int) -> float:
    if item_level >= 120:
        return 1.25 * item_level
    else:
        return 30 + item_level

def calculate_legendary_bonus_expiration(item_level: int) -> float:
    if item_level >= 120:
        return 50 + 1.25 * item_level
    else:
        return 80 + item_level

def calculate_very_crit_chance(crit_chance: float) -> float:
    return 17 * crit_chance * 0.1

def calculate_very_crit_power(crit_power: float, very_crit_chance: float) -> float:
    return crit_power * 1.75

def calculate_holy_touch_heal_value(hp: int) -> float:
    return hp * 0.06

def calculate_anguish_damage(level: int, strength: int, intellect: int, agility: int) -> float:
    return (0.0025 * level + 0.3) * (strength + intellect + 0.8 * agility)
