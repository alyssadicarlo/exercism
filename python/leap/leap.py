def leap_year(year):
    output = False
    if year % 4 == 0:
        output = True
        if year % 100 == 0:
            output = False
            if year % 400 == 0:
                output = True
    return output