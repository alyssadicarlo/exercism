def classify(number):
    if number <= 0:
        raise ValueError("Number must be greater than 0")
    factors = []
    for num in range(1, number):
        if number % num == 0:
            factors.append(num)
    sum_factors = 0
    for i in range(len(factors)):
        sum_factors += factors[i]

    if sum_factors == number:
        return "perfect"
    if sum_factors > number:
        return "abundant"
    if sum_factors < number:
        return "deficient"
