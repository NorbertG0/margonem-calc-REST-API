
def calculate_block(block: int, enemy_level: int) -> float:
    return block * 20 / min(enemy_level, 300)