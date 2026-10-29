def is_valid_dna(dna):
    valid_nuc=['A', 'T', 'G', 'C']
    for nuc in dna:
        if nuc not in valid_nuc:
            return False
    return True
def hamming_distance(s1, s2):
    if not is_valid_dna(s1) or not is_valid_dna(s2):
        return None
    if len(s1)!=len(s2):
        return None
    return sum(n1!=n2 for n1,n2 in zip(s1,s2))
s1=input()
s2=input()
print(hamming_distance(s1,s2))

