def find_anagrams(word, candidates):
    output = []
    for candidate in candidates:
        if candidate.lower() != word.lower():
            if "".join(sorted(word.lower())) == "".join(sorted(candidate.lower())):
                output.append(candidate)
    return output