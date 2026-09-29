datos = ["a", "b", "a", "c"]

list(datos)      # ['a','b','a','c']
tuple(datos)     # ('a','b','a','c')   -> la sello, ya no cambia
set(datos)       # {'a','b','c'}       -> pierdo orden y repetidos
sorted(set(datos))                     # ['a','b','c'] sin repetidos y ordenado

dict(zip(("id", "nombre"), (1, "Ana")))   # {'id':1, 'nombre':'Ana'}
list({"id": 1, "nombre": "Ana"}.items())  # [('id',1), ('nombre','Ana')]