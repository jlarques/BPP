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
    print(adivinanumero(34).__doc__)
    
def tablamultiplicar(desde, hasta):
    '''
    Función:    tablamultlipcar
    Versión:    0.1
    Autor:      Desconocido
    Fecha:      09/03/2023
    Descripción:Esta función genera automáticamente todas las tablas de multiplicar de los valores que se pasen en las variables desde y hasta
    '''
    tabla_desde=desde
    tabla_hasta=hasta
    desde=1
    hasta=10

    for factor1 in range(tabla_desde, tabla_hasta+1):
        print(f'Tabla de multiplicar del {factor1}:')
        for factor2 in range(desde, hasta+1):
            print(f'{factor1} x {factor2}={factor1*factor2}')
            print()
            
    #Tabla de multiplicar a través de listas
    lista1=list()
    lista2=list()

    for i in range(10):
        lista1.append(i)
        lista2.append(i)
    
    for i in lista1:
        print(f'Tabla de multiplicar del {i+1}')
        print( "============================")
        
        for j in lista2:
            print(str(i+1) + 'x' + str(j+1)+ '='+ str(i*j))
        print( "============================")    
    
    tablamultiplicar(1,40)
    print(tablamultiplicar(1,40).__doc__)
    