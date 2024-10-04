import load_upload
import CRUD_ahorros
import CRUD_mensualidad
import validaciones
import Ahorros
import mensualidad
import Ventas
import CRUD_ventas

carga_gastos,carga_ahorros,carga_ventas=load_upload.cargar()


if carga_ahorros != None:
    ahorros=CRUD_ahorros.ordenar_y_recortar(carga_ahorros)
else:
    ahorros=[]

if carga_ventas != None:
    ventas=CRUD_ventas.ordenar_y_recortar(carga_ventas)
else:
    ventas=[]

band=0  
while band == 0:
    print('-'*100)
    print('1)Gastos')
    print('2)Ventas')
    print('3)Ahorros')
    print('4)salir')
    print('-'*100)
    elegir=input("Que desea hacer? ")
    if validaciones.validar(elegir)==1:
        elegir=int(elegir)
        if elegir == 1:
            band=mensualidad.interfaz_mensualidad(carga_gastos,ahorros)
            load_upload.guardar(carga_gastos,ahorros,ventas)
            
        if elegir == 2:
            band=Ventas.interfaz_ventas(ventas,ahorros)
            load_upload.guardar(carga_gastos,ahorros,ventas)
        
        if elegir == 3:
            band=Ahorros.interfaz_ahorros(ahorros)
            load_upload.guardar(carga_gastos,ahorros,ventas)
        
        if elegir == 4:
            print('fin')
            band=1
            load_upload.guardar(carga_gastos,ahorros,ventas)

        
    else:
        print("Opción no encontrada")
