
import random
def dice(n):
    total = 0
    for i in range(n):
        total += random.randint(1, 6)
    return total