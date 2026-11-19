def func(seq1, seq2):
    seq1=seq1.upper().strip()
    seq2=seq2.upper().strip()
    max_matches=-1
    coords=[]
    for start in range(len(seq1)-len(seq2)+1):
        window=seq1[start:start +len(seq2)]
        matches=sum(1 for a, b in zip(window,seq2) if a==b)
        if matches > max_matches:
            max_matches=matches
            coords=[(start+1, start+len(seq2)]
        elif matches==max_matches:
            coords.append((start+1, start+len(seq2))
    return max_matches, coords
seq1=input()
seq2=input()
print(func(seq1,seq2))
                        
