
goleadores=[] 
i=0
nombre=0

while nombre != "SALIR":
    nombre=input("Ingrese un nombre: ")
    nombre=nombre.upper()
    if nombre != "SALIR":    
        goleadores.append([])
        club=input("Ingrese el club correspondiente: ")
        club=club.upper()
        goles=int(input("Ingrese su cantidad de goles: "))
        goleadores[i].extend([club,nombre,goles])
        i=i+1

# Recortar los nombres a un máximo de 10 caracteres
goleadores_recortados = [[club[:7], nombre[:10], goles] for club, nombre, goles in goleadores]

# Ordenar la lista por promedio (descendente) y luego por nombre (ascendente)
goleadores_ordenados = sorted(goleadores_recortados, key=lambda x: (-x[2], x[1]))

# Imprimir la lista ordenada con formato de f-strings
print(f"{'Club':<10} {'Nombre':<10} {'Goles':>10}")
print('-' * 32)
for club, nombre, goles in goleadores_ordenados:
    print(f"{club:<10} {nombre:<10} {goles:>10}")

