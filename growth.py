growth=[
        [0,2,4,8],
        [0,1,1,2],
        [0,3,6,9]
        ]
t=5
result=[]
for culture in growth:
    found=False
    for i, value in enumerate(culture):
        if value>=t:
            result.append(str(i))
            found=True
            break
    if not found:
        result.append("отсутствует")
                                        
print(", ".join(result))


            
