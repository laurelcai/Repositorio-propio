import re

def validar(entrada):
      if re.match(r"^-?\d+$",entrada):
             return 1
      else:
           return 0
      
def validar_fecha():
    band=0
    
    while band == 0:
        fecha=input("Ingrese una fecha (en formato:año-mes): ")
        if re.match(r"^\d{4}-\d{2}$",fecha):
            band=1
            return fecha
        
def filtrar_fecha(fecha,gastos):
    filtrados = [fila for fila in gastos if fila[0] == fecha]
    return filtrados