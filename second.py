#!/usr/bin/env python3
t=int(input())
h=t//3600
m= (t%3600)//60
s=t%60
print(f"{h:02d}:{m:02d}:{s:02d}")


