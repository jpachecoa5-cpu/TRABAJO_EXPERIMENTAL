CAMPOS_CLIENTE = ("nombre", "apellido", "email", "telefono", "direccion")

print(len(CAMPOS_CLIENTE))        # 5
print(CAMPOS_CLIENTE[0])          # 'nombre'
print("email" in CAMPOS_CLIENTE)  # True

# CAMPOS_CLIENTE.append("ciudad")  ->  AttributeError: no existe append
# CAMPOS_CLIENTE[0] = "nombres"    ->  TypeError: no se puede asignar

# 1) Devolver dos valores a la vez: el retorno es una tupla
def crear_cliente(nombre):
    if not nombre:
        return (False, "El nombre es obligatorio")
    return (True, "Cliente creado")

exito, mensaje = crear_cliente("Ana")   # desempaquetado
print(exito, mensaje)

# 2) Recorrer pares con zip()
campos  = ("nombre", "email")
valores = ("Ana", "ana@x.com")
for campo, valor in zip(campos, valores):
    print(f"{campo}: {valor}")

# 3) Intercambiar sin variable auxiliar
a, b = 1, 2
a, b = b, a

# 4) Una tupla SÍ puede ser clave de un diccionario; una lista NO
ventas = {("2026", "enero"): 1500, ("2026", "febrero"): 1800}
print(ventas[("2026", "enero")])