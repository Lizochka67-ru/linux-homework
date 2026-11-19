def findmotif(motif, seq):
    motif=motif.upper().strip()
    seq=seq.upper().strip()
    positions=[]
    start=0
    while True:
        pos=seq.find(motif, start)
        if pos=-1:
            break
        positions.append(pos+1)
        start=pos+1
    return len(positions), positions
motif=input()
seq=input()
print(findmotif(motif,seq))

