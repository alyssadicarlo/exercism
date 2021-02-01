def is_pangram(sentence):
    alphabet = {
        "a": False,
        "b": False,
        "c": False,
        "d": False,
        "e": False,
        "f": False,
        "g": False,
        "h": False,
        "i": False,
        "j": False,
        "k": False,
        "l": False,
        "m": False,
        "n": False,
        "o": False,
        "p": False,
        "q": False,
        "r": False,
        "s": False,
        "t": False,
        "u": False,
        "v": False,
        "w": False,
        "x": False,
        "y": False,
        "z": False
    }
    for i in range(len(sentence)):
        curr_char = sentence[i].lower()
        if curr_char == " " or curr_char.isnumeric():
            continue
        alphabet[curr_char] = True
    for character in alphabet:
        if not alphabet[character]:
            return False
    return True