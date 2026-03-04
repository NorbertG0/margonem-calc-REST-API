
def calculate_evade(evade: int, enemy_level: int) -> float:
    return evade * 20 / min(enemy_level, 300)