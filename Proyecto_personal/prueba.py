import validaciones
import CRUD_mensualidad

gastos={}

def agregar():
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
                                        bandera_cantidad = 1
                                        fecha=validaciones.validar_fecha()
                                        band=0
                                        for key in gastos:
                                            if key == fecha:
                                                band=1
                                                matriz=gastos[key]
                                                matriz.append([fecha,tipo,donde,cantidad])
                                                CRUD_mensualidad.ordenar_y_recortar(matriz)
                                        if band==0:
                                            matriz.append([fecha,tipo,donde,cantidad])
                                            CRUD_mensualidad.ordenar_y_recortar(matriz)
                                            gastos[fecha] = matriz
                                        print(gastos, matriz)

agregar()