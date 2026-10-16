rna=input()
k=0
count=0
for i in range (0, len(rna)-2, 3):
    k=rna[i:i+3]
    if k=='UAA':
        break
    count+=1
print(count,k)


                       
                      
                     
                    
                                              
                           
                        
                         
                   

