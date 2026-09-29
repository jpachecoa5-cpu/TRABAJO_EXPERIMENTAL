cliente = {"id": 1, "nombre": "Ana", "email": "ana@x.com"}

# --- LEER ---
print(cliente["nombre"])                  # error si la clave no existe
print(cliente.get("telefono", "sin dato"))# seguro: valor por defecto

# --- ESCRIBIR ---
cliente["telefono"] = "0987654321"        # agrega o reemplaza
cliente.update({"ciudad": "Guayaquil"})

# --- QUITAR ---
del cliente["ciudad"]
telefono = cliente.pop("telefono", None)

# --- RECORRER ---
for clave in cliente:                 print(clave)
for valor in cliente.values():        print(valor)
for clave, valor in cliente.items():  print(f"{clave} = {valor}")

# --- VERIFICAR ---
print("email" in cliente)      # busca en las CLAVES, no en los valores
print(len(cliente))            # cuántos campos tiene

# --- DICCIONARIO DE LISTAS: agrupar ---
notas = {"Matemática": [18, 19], "Inglés": [17]}
notas.setdefault("Historia", []).append(20)   # crea la lista si no existía

# --- COMPRENSIÓN DE DICCIONARIO ---
clientes = [{"id": 1, "nombre": "Ana"}, {"id": 2, "nombre": "Luis"}]
indice = {c["id"]: c["nombre"] for c in clientes}   # {1:'Ana', 2:'Luis'}
print(indice[2])   # búsqueda instantánea por id, sin recorrer nada