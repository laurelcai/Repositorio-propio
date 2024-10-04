import validaciones
import CRUD_ahorros





def interfaz_ahorros(matriz_ahorros):
    band=0
    
    while band == 0:
        print('-'*100)
        print('1)imprimir matriz')
        print('2)agregar')
        print('3)borrar')
        print('-'*100)
        print('0)Inicio.'.center(10,' '),'-1)Salir.'.center(10,' '))
        print('-'*100)
        CRUD_ahorros.total(matriz_ahorros)
        elegir=input("Que desea hacer? ")
        if validaciones.validar(elegir)==1:
            elegir=int(elegir)
            if elegir == 1:
                CRUD_ahorros.imprimir_completo(matriz_ahorros)
                band=0
            if elegir == 2:
                CRUD_ahorros.agregar(matriz_ahorros)
                band=0
            if elegir == 3:
                CRUD_ahorros.borrar(matriz_ahorros)
                band=0
            if elegir == -1:
                print('fin')
                band=1
                return 1
            if elegir== 0:
                return 0
            
            auxiliar=matriz_ahorros
            matriz_ahorros=0
            matriz_ahorros=CRUD_ahorros.ordenar_y_recortar(auxiliar)
        
        else:
            print("Opción no encontrada")