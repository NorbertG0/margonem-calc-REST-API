from additional_functions import sign

def calculate_base_hp(level: int) -> float:
    return 20 * min(level, 300) ** 1.375

def calculate_base_crit_value(level: int) -> float:
    return 1 + 0.02 * level

def calculate_crit_chance_gain(player_level: int, enemy_level: int) -> int:
    lvl_player = min(player_level, 300)
    lvl_enemy = min(enemy_level, 300)
    diff = lvl_player - lvl_enemy

    return sign(diff) * max(abs(diff) - 5, 0) * 3

def calculate_crit_power_gain(player_level: int, enemy_level: int) -> float:
    lvl_player = min(player_level, 300)
    lvl_enemy = min(enemy_level, 300)
    diff = lvl_player - lvl_enemy

    return min(300, sign(diff) * max(abs(diff) - 5, 0) * 10)
