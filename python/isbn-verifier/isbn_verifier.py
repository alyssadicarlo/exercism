def is_valid(isbn):
    isbn_list = parseISBN(isbn)

    if len(isbn_list) != 10:
        return False
    
    sum = 0
    for i in range(0,len(isbn_list)-1):
        if isbn_list[i].isnumeric():
            sum += ((len(isbn_list)-i) * int(isbn_list[i]))
        else:
            return False

    if isbn_list[-1] == 'X':
        sum += 10
    elif isbn_list[-1].isnumeric():
        sum += int(isbn_list[-1])
    else:
        return False
    
    if sum % 11 == 0:
        return True
    else:
        return False


def parseISBN(isbn):
    sections = isbn.split("-")
    isbn_list = []
    for section in sections:
        for i in range(0,len(section)):
            isbn_list.append(section[i])
    return isbn_list