def is_armstrong_number(number):
    str_num = str(number)
    length = len(str_num)
    sum = 0
    for i in range(length):
        curr = str_num[i]
        sum += (int(curr) ** length)
    if sum == number:
        return True
    else:
        return False
