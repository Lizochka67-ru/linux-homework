def readfile(filename):
    seq=[]
    current=[]
    with open(filename, "r") as file:
        for line in file:
            line=line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if current:
                    seq.append("".join(current).upper())
                    current=[]
            else:
                current.append(line)
        if current:
            seq.append("".join(current).upper())
    return seq
sequenses=readfile("cda.fna")
def gc(seq):
    seq=sec.upper()
    if len seq==0:
        return 0.0
    return (seq.count("G")+seq.count("C"))/len(seq)*100
for seq in sequences:
    print(gc(seq))


