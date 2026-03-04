
def sign(x: int) -> int:
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0

def calculate_range(range_, fn):
    return [0 if a == 0 else fn(a) for a in range_]