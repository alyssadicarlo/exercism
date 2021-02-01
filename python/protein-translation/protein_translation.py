def proteins(strand):
    protein_list = {
        "AUG": "Methionine",
        "UUU": "Phenylalanine",
        "UUC": "Phenylalanine",
        "UUA": "Leucine",
        "UUG": "Leucine",
        "UCU": "Serine",
        "UCC": "Serine",
        "UCA": "Serine",
        "UCG": "Serine",
        "UAU": "Tyrosine",
        "UAC": "Tyrosine",
        "UGU": "Cysteine",
        "UGC": "Cysteine",
        "UGG": "Tryptophan",
        "UAA": "STOP",
        "UAG": "STOP",
        "UGA": "STOP",
    }
    codons = []
    output = []
    for i in range(0, len(strand), 3):
        if i < len(strand) - 2:
            codons.append(strand[i:i + 3])
    for codon in codons:
        if codon in protein_list:
            if protein_list[codon] == "STOP":
                break
            else:
                output.append(protein_list[codon])
    return output