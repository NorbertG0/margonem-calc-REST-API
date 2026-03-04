
def calculate_base_hp(strength: int) -> int:
    return strength * 5

def calculate_armor_hp(strength: int, armor_level: int | None) -> float:
    if armor_level is None:
        return 0
    return strength * max(0.1, round(armor_level / 10) / 10)

def calculate_crit_value(strength: int, level: int) -> float:
    if level <= 20:
        return 0.0
    return strength / (0.5 * min(level, 300))
