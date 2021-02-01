def to_rna(dna_strand):
    dna_map = {
        "G": "C",
        "C": "G",
        "T": "A",
        "A": "U",
    }
    output = ""
    for dna in dna_strand:
        output += dna_map[dna]
    return output
