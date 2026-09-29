indice = {cliente["id"]: cliente for cliente in clientes}
print(indice[2]["nombre"])       # 'Luis'

# Diferencia de costo:
# recorrer la lista  -> revisa hasta N registros
# indice[2]          -> una sola operación, sin importar cuántos haya
