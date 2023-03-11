class Error(Exception):
    pass

class ValorDemasiadoPequeñoError(Error):
    pass

class ValorDemasiadoGrandeError(Error):
    pass

numero=10

while(True):
    try:
        numero_entrada=int(input("Introduce un número:"))
        if(numero_entrada<numero):
            raise ValorDemasiadoPequeñoError
        elif(numero_entrada>numero):
            raise ValorDemasiadoGrandeError
        break
    except ValorDemasiadoPequeñoError:
        print("El número es demasiado pequeño. Inténtalo de nuevo.")
        print()
    except ValorDemasiadoGrandeError:
        print("El número es demasiado grande. Inténtalo de nuevo.")
        print()
        
print("Has encontado el número a adivinar. ¡¡Enhorabuena!!")

