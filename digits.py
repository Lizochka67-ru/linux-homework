#!/usr/bin/env python3
n=int(input())
h=n//100
t=(n//10)%10
o=n%10
summa=h+t+o
reversn=o*100+t*10+h
                       
print(summa, reversn) 


