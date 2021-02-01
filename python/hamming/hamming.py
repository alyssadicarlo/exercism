def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Length of strings do not match")
    output = [strand_b[i] for i in range(len(strand_a)) if strand_a[i] != strand_b[i]]
    return len(output)