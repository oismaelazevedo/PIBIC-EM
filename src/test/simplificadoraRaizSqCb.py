from sympy import pretty, sqrt, cbrt


num, indiceRaiz = input().split(" ")

if indiceRaiz == '2':
    print(pretty(sqrt(int(num))))
else:
    print(pretty(cbrt(int(num))))
    
