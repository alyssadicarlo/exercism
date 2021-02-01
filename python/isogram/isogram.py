def is_isogram(string):
    return len([char for char in string if string.lower().count(char.lower()) > 1 and char.isalpha()]) == 0