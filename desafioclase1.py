from random import randint

estudiantes=randint(1,10)
materias=5
matriz=[]

def mostrar_matriz(matriz,filas,columnas):
    filas = len(matriz)
    columnas = len(matriz[0])
    for i in range(filas):
        h=i+1
        print("%3d" % h,"° estudiante",end="")
        for j in range(columnas):
            print("%4d" % matriz[i][j], end="")
        print()


def calcular_promedio_estudiantes(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    suma_filas = [0] * filas

    
    for i in range(filas):
        for j in range(columnas):
            suma_filas[i] += matriz[i][j]

    for i in range(len(suma_filas)):
        print("El promedio del",i+1,"° estudiante es:",suma_filas[i]/columnas)


def calcular_promedio_materias(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    suma_columnas = [0] * columnas

    for i in range(filas):
        for j in range(columnas):
            suma_columnas[j] += matriz[i][j]

    for i in range(len(suma_columnas)):
        print("El promedio del",i+1,"° materia es:",suma_columnas[i]/filas)


for i in range(estudiantes):
    matriz.append([])
    for j in range(materias):
        matriz[i].append(randint(1,10))

mostrar_matriz(matriz,estudiantes,materias)
print()
calcular_promedio_estudiantes(matriz)
print()
calcular_promedio_materias(matriz)