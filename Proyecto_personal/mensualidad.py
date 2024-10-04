import validaciones
import CRUD_mensualidad
import load_upload




def interfaz_mensualidad(gastos, ahorros):
    band = 0
    
    while band == 0:
        print('-'*100)
        print('1) Imprimir matriz')
        print('2) Agregar')
        print('3) Borrar')
        print('4) Sumatoria de un mes')
        print('-'*100)
        print('0) Inicio'.center(10, ' '), '-1) Salir'.center(10, ' '))
        print('-'*100)
        elegir = input("¿Qué desea hacer? ")
        
        if validaciones.validar(elegir) == 1:
            elegir = int(elegir)
            
            if elegir == 1:
                CRUD_mensualidad.imprimir_fecha(gastos)
                        
                # Aquí no necesitamos reiniciar band, ya que estamos dentro de un bucle
            
            elif elegir == 2:
                CRUD_mensualidad.agregar(gastos)
            
            elif elegir == 3:
                CRUD_mensualidad.borrar(gastos)
            
            elif elegir == 4:
                CRUD_mensualidad.sumatoria(gastos)
            
            elif elegir == 0:
                return 0  # Regresa a la pantalla de inicio
            
            elif elegir == -1:
                print('Fin')
                return 1  # Salida del programa
            
            # Llamar a agregar_ahorros después de una modificación en los gastos
            CRUD_mensualidad.agregar_ahorros(gastos, ahorros)

        else:
            print("Opción no encontrada")





