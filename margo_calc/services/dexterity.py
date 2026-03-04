
def calculate_attack_speed(dexterity: int) -> float:
    return min(2, 0.02 * dexterity) + max(0, 0.002 * (dexterity - 100))

def calculate_evade_gain(dexterity: int) -> float:
    return dexterity / 30
