import pytest

def separador():
    letras="Python es el mejor lenguaje de programación del mundo mundial"
    print(type(letras))
    assert(type(letras))==str
    letra= [i for i in letras]
    print(letra)
    
separador()

def numerospares():
    pares=[i for i in range(1,21) if i%2==0]
    print("Los números pares entre 1 y 20 son: ", pares)
    
numerospares()

def cuadrado():
    elementos=[2,3,5,4,1,3]
    cuadrados=[]
    
    for i in elementos:
        cuadrados.append(i**2)
    
    print("El cuadrado de la lista ", elementos, " es ", cuadrados)

print(cuadrado)