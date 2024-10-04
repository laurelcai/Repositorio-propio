import validaciones

def ordenar_y_recortar(ventas):
        # Recorta
    ventas_recortados = [[fecha,producto[:22], precio,estado,plataforma] for fecha, producto,precio,estado,plataforma in ventas]

        # Ordenar la lista
    ventas_ordenados = sorted(ventas_recortados, key=lambda x: (x[0]))

    return ventas_ordenados

def borrar(ventas):
    band=0
    while band==0:
        cont=0
        # Imprimir la lista ordenada con formato
        print(f"{'Fecha':<10}{'Producto':<25}{'Precio':<15}{'Estado':<15}{'Plataforma':<20}")
        print('-' *100)
        for fecha, producto, precio,estado,plataforma in ventas:
            cont=cont+1
            print(cont,")",f"{fecha:<10}{producto:<25} {precio:<15}{estado:<15}{plataforma:<20}")

        
        eleccion=input("Cual es la fila que desea eliminar? ")
        if validaciones.validar(eleccion)==1:
            eleccion=int(eleccion)
            eliminado=ventas.pop(eleccion-1)
            print("Usted ha eliminado:",eliminado)
            band=1

def imprimir(ventas):
        # Imprimir la lista ordenada con formato
    print(f"{'Fecha':<10}{'Producto':<25}{'Precio':<15}{'Estado':<15}{'Plataforma':<20}")
    print('-' *100)
    for fecha, producto, precio,estado,plataforma in ventas:
        print(f"{fecha:<10}{producto:<25} {precio:<15}{estado:<15}{plataforma:<20}")

def agregar(ventas):
    bandera_producto = 0 
    while bandera_producto == 0:
        print('-'*100)
        print('0)Inicio.'.center(10,' '))
        producto = input("Ingrese el producto publicado: ").upper()
        if producto != '0':
            if validaciones.validar(producto)== 0:
                bandera_producto = 1

                bandera_plataforma = 0 
                while bandera_plataforma == 0:
                    print('-'*100)
                    print('0)Inicio.'.center(10,' '))
                    plataforma = input("Ingrese la plataforma donde esta publicado: ").upper()
                    if plataforma != '0':
                        if validaciones.validar(plataforma)== 0:
                            bandera_plataforma = 1
                    
                            bandera_precio = 0 
                            while bandera_precio == 0:
                                print('-'*100)
                                print('0)Inicio.'.center(10,' '))
                                precio = input("Ingrese el precio del producto: ")
                                if precio != '0':
                                    if validaciones.validar(precio)== 1:
                                        precio=int(precio)
                                        bandera_precio = 1
                                        fecha=validaciones.validar_fecha()
                                        ventas.append([fecha,producto,precio,'DISPONIBLE',plataforma])                                

                                    elif bandera_precio==0:
                                        print("Inválido, por favor ingréselo nuevamente")


                                else:
                                    bandera_precio=1
                        else:
                            print("Inválido, por favor ingréselo nuevamente")
                    else:
                        bandera_plataforma=1
            else:
                print("Inválido, por favor ingréselo nuevamente")        
        else:
            bandera_producto=1

def cambiar_estado(ventas,ahorros):
    band=0
    while band==0:
        cont=0
        # Imprimir la lista ordenada con formato
        print(f"{'Fecha':<10}{'Producto':<25}{'Precio':<15}{'Estado':<15}{'Plataforma':<20}")
        print('-' *100)
        for fecha, producto, precio,estado,plataforma in ventas:
            cont=cont+1
            print(cont,")",f"{fecha:<10}{producto:<25} {precio:<15}{estado:<15}{plataforma:<20}")

        
        eleccion=input("Cual es la fila que desea cambiar el estado? ")
        if validaciones.validar(eleccion)==1:
            eleccion=int(eleccion)
            estado=input("Cual es el nuevo estado del producto? ").upper()
            ventas[eleccion-1][3]=estado
            band=1
            if estado=='VENDIDO':
                fecha_vendido=validaciones.validar_fecha()
                ahorros.append([fecha_vendido,ventas[eleccion-1][1],ventas[eleccion-1][2],'PESOS'])
