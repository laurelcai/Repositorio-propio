import validaciones
from functools import reduce

acumulacion_peso=[]
acumulacion_dolar=[]

def borrar(ahorros):
    band=0
    while band==0:
        cont=0
        # Imprimir la lista ordenada con formato
        print(f"{'Fecha':<10}{'Movimiento':<25}{'Cantidad':<15}{'ID':<10}")
        print('-' *100)
        for fecha, producto, cantidad, id in ahorros:
            cont=cont+1
            print(cont,")",f"{fecha:<10}{producto:<25} {cantidad:<15}{id:<10}")

        
        eleccion=input("Cual es la fila que desea eliminar? ")
        if validaciones.validar(eleccion)==1:
            eleccion=int(eleccion)
            eliminado=ahorros.pop(eleccion-1)
            print("Usted ha eliminado:",eliminado)
            band=1


def agregar(ahorros):

    bandera_movimiento = 0 # Bandera para controlar el bucle de validación del Nombre
    while bandera_movimiento == 0:
        print('-'*100)
        print('0)Inicio.'.center(10,' '))
        movimiento = input("Ingrese la razon del movimiento: ").upper()
        if movimiento != '0':
            if validaciones.validar(movimiento)== 0:
                bandera_movimiento = 1

                bandera_cantidad = 0 # Bandera para controlar el bucle de validación del Nombre
                while bandera_cantidad == 0:
                    print('-'*100)
                    print('0)Inicio.'.center(10,' '))
                    cantidad = input("Ingrese la cantidad del movimiento: ")
                    if cantidad != '0':
                        if validaciones.validar(cantidad)== 1:
                            cantidad=int(cantidad)
                            bandera_cantidad = 1
                    
                            bandera_moneda = 0 # Bandera para controlar el bucle de validación del Nombre
                            while bandera_moneda == 0:
                                print('-'*100)
                                print('0)Inicio.')
                                print('1)Peso.'.ljust(10,' '),'2)Dolar.'.center(10,' '))
                                elegir_moneda = input("Ingrese la moneda utilizada: ")
                                if elegir_moneda != '0':
                                    if elegir_moneda=='1':
                                        moneda='PESOS'
                                        fecha=validaciones.validar_fecha()
                                        ahorros.append([fecha,movimiento,cantidad,moneda])
                                        bandera_moneda=1
                                    if elegir_moneda=='2':
                                        moneda='DOLAR'
                                        fecha=validaciones.validar_fecha()
                                        ahorros.append([fecha,movimiento,cantidad,moneda])                                
                                        bandera_moneda = 1

                                    elif bandera_moneda==0:
                                        print("Inválido, por favor ingréselo nuevamente")


                                else:
                                    bandera_moneda=1
                        else:
                            print("Inválido, por favor ingréselo nuevamente")
                    else:
                        bandera_cantidad=1
            else:
                print("Inválido, por favor ingréselo nuevamente")        
        else:
            bandera_movimiento=1

    


def imprimir_completo(ahorros):

    # Imprimir la lista ordenada con formato

    cont=0
    for fecha, producto, cantidad, Moneda in ahorros:
        cont=cont+1
        print(f"{fecha:<20}{producto:<25} {cantidad:<20}{Moneda:<10}")
        if cont==1:
            print('-' *100)
            print(f"{'Fecha':<20}{'Movimiento':<25}{'Cantidad':<20}{'Moneda':<10}")
            print('-' *100)





def ordenar_y_recortar(ahorros):
        # Recorta
    ahorros_recortados = [[fecha,producto, cantidad,moneda] for fecha, producto,cantidad,moneda in ahorros]

        # Ordenar la lista
    ahorros_ordenados = sorted(ahorros_recortados, key=lambda x: (x[0]))

    return ahorros_ordenados

def total(ahorros):
    cont=0
    for fila in ahorros:
        cont=cont+1
        if cont >1:
            if fila[3]=='PESOS':
                acumulacion_peso.append(fila[2])
            else:
                acumulacion_dolar.append(fila[2])

    if len(acumulacion_peso)>1:
        sumatoria_peso=reduce(lambda x, y : x + y, acumulacion_peso)
        ahorros[0][1]=sumatoria_peso
    elif len(acumulacion_peso)>0:
        sumatoria_peso=acumulacion_peso[0]
        ahorros[0][1]=sumatoria_peso
    if len(acumulacion_dolar)>1:
        sumatoria_dolar=reduce(lambda x, y : x + y, acumulacion_dolar)
        ahorros[0][3]=sumatoria_dolar
    elif len(acumulacion_dolar)>0:
        sumatoria_dolar=acumulacion_dolar[0]
        ahorros[0][3]=sumatoria_dolar
    
    acumulacion_peso.clear()
    acumulacion_dolar.clear()
    
    
    
