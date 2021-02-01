def steps(number):
    if number <= 0:
        raise ValueError("Invalid number")
    count = 0
    while number > 1:
        count = count + 1
        if number % 2 == 0:
            number = number/2
        else:
            number = number*3+1
    return count