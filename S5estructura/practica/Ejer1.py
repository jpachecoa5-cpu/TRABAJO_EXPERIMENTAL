ciudades = ["Quito", "Guayaquil", "Quito", "Cuenca", "Guayaquil"]

vistas = set()      # conjunto de control: para preguntar rápido si ya apareció
unicas = []         # lista de resultado: conserva el orden
for ciudad in ciudades:
    if ciudad not in vistas:
        vistas.add(ciudad)
        unicas.append(ciudad)

print(unicas)   