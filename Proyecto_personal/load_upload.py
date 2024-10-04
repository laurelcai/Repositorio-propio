import pickle

def cargar():
    try:
        with open("datos.pkl", "rb") as archivo:
            datos = pickle.load(archivo)
            gastos=datos["gastos"]
            ahorros = datos["ahorros"]
            ventas=datos["ventas"]
            print("Se cargaron {} registros de gastos y {} de ingresos del documento externo.".format(len(gastos), len(ahorros),len(ventas)))
            return gastos, ahorros,ventas
    except FileNotFoundError:
        print("El archivo no existe. Se comenzará con listas vacías.")
        return {}, [['0.Total Pesos',0,'1.Total Dolares',0]],[]
    except EOFError:
        print("El archivo está vacío. Se comenzará con listas vacías.")
        return {}, [],[]
    except Exception as e:
        print(f"Ocurrió un error al cargar el archivo: {e}")
        return {}, [],[]


def guardar(gastos, ahorros,ventas):
    try:
        with open("datos.pkl", "wb") as archivo:
            # Serializar ambos objetos en un diccionario
            datos = {"gastos": gastos, "ahorros": ahorros,"ventas":ventas}
            pickle.dump(datos, archivo)
        print("Datos guardados exitosamente.")
    except Exception as e:
        print(f"Error al guardar los datos: {e}")

