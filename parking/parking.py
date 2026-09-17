import math

FREE_MINUTES = 30
PRICE_PER_HALF_HOUR = 1.50

def final_price(minutes: int) -> float:
    paid_minutes = max(0, minutes - FREE_MINUTES)
    return math.ceil(paid_minutes / 30) * PRICE_PER_HALF_HOUR
