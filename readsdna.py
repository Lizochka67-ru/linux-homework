reads=[
        "ATGCC",
        "GCCAA",
        "CAAAT",
        "TTTGG"
        ]
k=int(input())
for i in range(len(reads)):
    for j in range(i+1, len(reads)):
        if reads[i][-k:]==reads[j][:k]:
            print(f"{i+1}-{j+1}")
                                
                                  
                                
                         
                             
                         
                              
                                           
                                              
                                                 
                                           

