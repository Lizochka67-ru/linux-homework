nucleotides=set("ATGC")
lenghts=[]
while True:
    s=input()
    if s=="STOP":
        break
    if  s=="" or any(ch not in nucleotides for ch in s):
        print("некорректно введена последовательность ДНК")
        continue
    lenghts.append(len(s))
print(len(lenghts))  
print(lenghts)

