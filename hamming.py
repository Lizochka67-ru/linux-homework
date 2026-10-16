sequences=[
        "AACG",
        "AATG",
        "TATG",
        "TTTG"
        ]
def hamming(seq1, seq2):
    return sum(1 for ch1, ch2 in zip(seq1, seq2) if ch1 != ch2)
matrix=[]
for i in range(len(sequences)):
        row=[]
        for j in range(len(sequences)):
            row.append(hamming(sequences[i], sequences[j]))
        matrix.append(row)
for row in matrix:
    print(" ".join(map(str, row)))

                                                                  



