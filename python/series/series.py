def slices(series, length):
    if series == "" or length <= 0 or len(series) < length:
        raise ValueError("Invalid input")
    output = []
    for i in range(0, len(series)):
        if i <= len(series) - length:
            output.append(series[i:i + length])
    return output