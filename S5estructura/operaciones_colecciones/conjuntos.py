emails = {"ana@x.com", "luis@x.com"}

# --- AGREGAR / QUITAR ---
emails.add("sol@x.com")
emails.add("ana@x.com")      # ya existía: no pasa nada, sigue habiendo uno
emails.discard("luis@x.com") # quita sin error aunque no exista
# emails.remove("no@x.com")  # este SÍ lanza error si no existe

# --- LA OPERACIÓN ESTRELLA: pertenencia instantánea ---
if "ana@x.com" in emails:
    print("Ese email ya está registrado")

# --- QUITAR DUPLICADOS DE UNA LISTA ---
ciudades = ["Guayaquil", "Quito", "Guayaquil", "Milagro", "Quito"]
unicas = set(ciudades)            # {'Guayaquil','Quito','Milagro'}
print(len(unicas), "ciudades distintas")
lista_unica = sorted(unicas)      # volver a lista, ordenada

# --- OPERACIONES ENTRE CONJUNTOS ---
matematica = {"Ana", "Luis", "Sol"}
ingles     = {"Luis", "Marco"}

print(matematica | ingles)   # UNIÓN: están en alguna de las dos
print(matematica & ingles)   # INTERSECCIÓN: están en las dos  -> {'Luis'}
print(matematica - ingles)   # DIFERENCIA: solo en matemática   -> {'Ana','Sol'}
print(matematica ^ ingles)   # los que NO comparten

print({"Ana"}.issubset(matematica))       # ¿es subconjunto?
print(matematica.isdisjoint({"Pedro"}))   # ¿no comparten nada?