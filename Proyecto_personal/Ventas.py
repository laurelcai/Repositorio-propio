import validaciones
import CRUD_ventas





def interfaz_ventas(matriz_ventas,matriz_ahorros):
    band=0
    
    while band == 0:
        print('-'*100)
        print('1)imprimir matriz')
        print('2)agregar')
        print('3)borrar')
        print('4)cambiar estado')
        print('-'*100)
        print('0)Inicio.'.center(10,' '),'-1)Salir.'.center(10,' '))
        print('-'*100)
        elegir=input("Que desea hacer? ")
        if validaciones.validar(elegir)==1:
            elegir=int(elegir)
            if elegir == 1:
                CRUD_ventas.imprimir(matriz_ventas)
                band=0

            if elegir == 2:
                CRUD_ventas.agregar(matriz_ventas)
                band=0
                
            if elegir == 3:
                CRUD_ventas.borrar(matriz_ventas)
                band=0

            if elegir == 4:
                CRUD_ventas.cambiar_estado(matriz_ventas,matriz_ahorros)
                band=0

            if elegir == 0:
                band=1
                return 0
            
            if elegir==-1:
                print('fin')
                band=1
                return 1
            
            auxiliar=matriz_ventas
            matriz_ventas=0
            matriz_ventas=CRUD_ventas.ordenar_y_recortar(auxiliar)
        else:
            print("Opción no encontrada")