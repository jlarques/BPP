'''Operaciones de adivinar un número y crear una tabla de multiplicar'''

def adivinanumero(numero):
    '''
    Función:    adivinanumero
    Versión:    0.1
    Autor:      José Luis Arqués
    Fecha:      09/03/2023
    Descripción:Esta función permite al usuario introducir números hasta adivinar el número a partir de un número que se le pasa como parámetro
    '''
    adivina=int(input("Escribe el número a adivinar: "))
    while adivina!=numero:
        print("No has acertado el número. Inténtalo otra vez.")
        adivina=int(input("Escribe el número a adivinar: "))
 
    print("¡Enhorabuena! Acertaste el número!")                     

    adivinanumero(34)
    #print(print.__doc__)