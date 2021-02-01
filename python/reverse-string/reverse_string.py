def reverse(text):
    output = ""
    for i in range(len(text) - 1, -1, -1):
        output += text[i]
    return output