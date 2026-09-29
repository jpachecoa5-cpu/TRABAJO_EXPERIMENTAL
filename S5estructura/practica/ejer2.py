conteo = {}
for ciudad in ciudades:
    conteo[ciudad] = conteo.get(ciudad, 0) + 1     # .get evita el KeyError la primera vez

print(conteo)

# El más repetido:
mas_repetida = max(conteo, key=conteo.get)
print(mas_repetida)