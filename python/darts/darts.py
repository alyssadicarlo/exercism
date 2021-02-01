import math

def score(x, y):
    diagonal = math.sqrt(x**2 + y**2)
    if diagonal <= 1:
        return 10
    elif diagonal <= 5:
        return 5
    elif diagonal <= 10:
        return 1
    return 0