ref=input()
samp=input()
for i, (old,new) in enumerate(zip(ref,samp), start=1):
    if old!=new:
        print(i, old, new)

