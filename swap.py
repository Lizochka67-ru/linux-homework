#!/usr/bin/env python3
a=int(input())
b=int(input())
print(f"до перестановки: a={a}(id: {id(a)}), b={b}(id: {id(b)})")
a, b=b, a
print(f"1 способ: a={a}(id: {id(a)}), b={b} (id: {id(b)})")
a,b=b,a
t=a
a=b
b=t
print(f"второй способ: a={a} (id: {id(a)}), b={b}(id: {id(b)}")


