
def calculate_absorb_limit(intellect: int) -> int:
    return intellect * 7

def calculate_crit_value(intellect: int, level: int) -> float:
    if level <= 20:
        return 0.0
    return intellect / (0.5 * min(level, 300))