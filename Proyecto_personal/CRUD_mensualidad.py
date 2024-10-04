import validaciones
from functools import reduce

def borrar(gastos):
    cont=0
    band=0
    while band==0:
        fecha=validaciones.validar_fecha()
        for key in gastos:
            if key == fecha:
                band=1
                matriz=gastos[key]
                print(f"{'Fecha':<10}{'Tipo':<12} {'Donde':<25} {'Cantidad':<15}")
                print('-' * 100)
                for fecha, tipo, donde, cantidad in matriz:
                    cont=cont+1
                    print(cont,")",f"{fecha:<10}{tipo:<12} {donde:<25} {cantidad:<15}")
        
                eleccion=input("Cual es la fila que desea eliminar? ")
                if validaciones.validar(eleccion)==1:
                    eleccion=int(eleccion)
                    eliminado=matriz.pop(eleccion-1)
                    print("Usted ha eliminado:",eliminado)
                    band=1


def agregar(gastos):
    matriz=[]
    bandera_tipo = 0 
    while bandera_tipo == 0:
        print('-'*100)
        print('0)Inicio.'.center(10,' '))
        tipo = input("Ingrese con que se realizo el gasto: ").upper()
        if tipo != '0':
            if validaciones.validar(tipo)== 0:
                bandera_tipo = 1

                bandera_donde = 0 
                while bandera_donde == 0:
                    print('-'*100)
                    print('0)Inicio.'.center(10,' '))
                    donde = input("Ingrese la razon del gasto: ").upper()
                    if donde != '0':
                        if validaciones.validar(donde)== 0:
                            bandera_donde = 1
                    
                            bandera_cantidad = 0 
                            while bandera_cantidad == 0:
                                print('-'*100)
                                print('0)Inicio.'.center(10,' '))
                                cantidad = input("Ingrese la cantidad del gasto: ")
                                if cantidad != '0':
                                    if validaciones.validar(cantidad)== 1:
                                        cantidad=int(cantidad)
                                        fecha=validaciones.validar_fecha()
                                        band=0
                                        for key in gastos:
                                            if key == fecha:
                                                band=1
                                                matriz=gastos[key]
                                                matriz.append([fecha,tipo,donde,cantidad])
                                                ordenar_y_recortar(matriz)
                                                
                                                break

                                        if band==0:
                                            matriz.append([fecha,tipo,donde,cantidad])
                                            ordenar_y_recortar(matriz)
                                            gastos[fecha] = matriz
                                            
                                        
                                        break
                                        bandera_cantidad = 1
                                        
                                                                       

                                    elif bandera_cantidad==0:
                                        print("Inválido, por favor ingréselo nuevamente")


                                else:
                                    bandera_cantidad=1
                        else:
                            print("Inválido, por favor ingréselo nuevamente")
                    else:
                        bandera_donde=1
            else:
                print("Inválido, por favor ingréselo nuevamente")        
        else:
            bandera_tipo=1

            
    


def imprimir_completo(gastos):

    # Imprimir la lista ordenada con formato
    print(f"{'Fecha':<10}{'Tipo':<12} {'Donde':<25} {'Cantidad':<15}")
    print('-' *75)
    for fecha, tipo, donde, cantidad in gastos:
        print(f"{fecha:<10}{tipo:<12} {donde:<25} {cantidad:<15}")


def imprimir_fecha(gastos):
    band=0
    while band==0:
        fecha=validaciones.validar_fecha()
        for key in gastos:
            if key == fecha:
                band=1
                matriz=gastos[key]
                print(f"{'Fecha':<10}{'Tipo':<12} {'Donde':<25} {'Cantidad':<15}")
                print('-' * 100)
                for fecha, tipo, donde, cantidad in matriz:
                    print(f"{fecha:<10}{tipo:<12} {donde:<25} {cantidad:<15}")


def sumatoria(gastos):

    fecha=validaciones.validar_fecha()
    for key in gastos:
        if key == fecha:
            matriz = gastos[key]  # Obtenemos la "matriz" desde el diccionario gastos
            filtrados = [f[3] for f in matriz]  # Accedemos a la columna 3
            total_gastos = reduce(lambda x, y: x + y, filtrados)  # Sumamos los valores
            print("En",fecha,"se ha gastado un total de",total_gastos)
            print("Y un restante de",total_gastos+120000,"de $120000 de presupuesto")


def ordenar_y_recortar(gastos):
        # Recorta
    gastos_recortados = [[fecha,tipo[:7], donde[:22], cantidad,] for fecha, tipo, donde, cantidad, in gastos]

        # Ordenar la lista
    gastos_ordenados = sorted(gastos_recortados, key=lambda x: (x[0]))

    return gastos_ordenados



def agregar_ahorros(gastos, ahorros):

    # Para cada fila existente en ahorros
    for fila in ahorros:
        for key, matriz in gastos.items():
            # Verificar si la clave del gasto coincide con la fila en ahorros y es 'MENSUALIDAD'
            if key == fila[0] and fila[1] == 'MENSUALIDAD':
                # Procesar la matriz para sumar los gastos
                filtrados = [f[3] for f in matriz if len(f) > 3]  # Verificamos que haya suficiente longitud en cada fila
                if filtrados:  # Si hay valores en filtrados
                    total_gastos = reduce(lambda x, y: x + y, filtrados)
                else:
                    total_gastos = 0  # Si no hay valores, el total es 0
                sumatoria = total_gastos + 120000  # Agregamos los 120000
                fila[2] = sumatoria  # Actualizamos el valor en ahorros

    # Ahora revisamos si hay claves en 'gastos' que no están en 'ahorros'
    for key, matriz in gastos.items():
        # Verificar si ya existe una entrada en ahorros con esta clave y 'MENSUALIDAD'
        if not any(fila[0] == key and fila[1] == 'MENSUALIDAD' for fila in ahorros):
            # Si no existe, creamos una nueva entrada en ahorros
            filtrados = [f[3] for f in matriz if len(f) > 3]
            if filtrados:
                total_gastos = reduce(lambda x, y: x + y, filtrados)
            else:
                total_gastos = 0
            sumatoria = total_gastos + 120000
            # Agregar la nueva entrada a ahorros
            ahorros.append([matriz[0][0], 'MENSUALIDAD', sumatoria, 'PESOS'])






    


                    





            
    
        