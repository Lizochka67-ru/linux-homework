#!/usr/bin/env python3
import sys
dna=sys.argv[1].upper()
compl={"A": "T", "T": "A", "C": "G", "G": "C"}
revcomp=" ".join(compl[base] for base in reversed(dna))
rna=dna.replace("T","U")
start=dna.find("ATG")  
print(revcomp, rna, start)


