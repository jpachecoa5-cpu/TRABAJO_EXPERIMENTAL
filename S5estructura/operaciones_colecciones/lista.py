clientes = [ "Ana", "Luis", "Sol"]

# __agregar__
clientes.append("Marco") # al final ['Ana','Luis',' Sol', 'Maria']
clientes.insert(1, "Beeto") # en la posicion 1
clientes.extend(["Ivan","Ruth2"]) # agrega varios de una vez

#__quitar__
clientes.remove("Beto")   # por valor (error si no existe)
ultimo = clientes.pop()   # saca y devuelve el ultimo - es una pila
primero = clientes.pop(0) # saca el primero - es una cola
  
#__consultar__
print(len(clientes))      # cuantos hay
print(clientes[0], clientes[-1])# primero y ultimo
print("Ana" in clientes)  #true/false
print(clientes.index("Sol")) #en que posicion esta
print(clientes.count("Ana")) # cuantas veces aparece

#__recorrer__
for nombre in clientes:
    print(nombre)

for posicion, nombre in enumerate(clientes):  # cuando necesito el índice
    print(posicion, nombre)

#__ordenar__
clientes.sort()                       # modifica la lista original
copia_ordenada = sorted(clientes)     # deja la original intacta
clientes.sort(reverse=True)           # de z a A

#__transformar__
mayusculas = [n.upper() for n in clientes]
con_a      = [n for n in clientes if n.startswith("A")]   # filtrar
longitudes = [len(n) for n in clientes]
  
  #__acumular__
notas = [18, 15, 20, 12]
print(sum(notas), max(notas), min(notas), sum(notas) / len(notas))