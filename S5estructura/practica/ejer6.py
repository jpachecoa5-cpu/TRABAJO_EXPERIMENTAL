def clientes_por_ciudad():
    agrupados = {}
    for registro in gestor.leer():
        ciudad = registro.get("ciudad", "").title() or "Sin ciudad"
        # setdefault: si la ciudad no estaba, crea la lista vacía y luego agrega
        agrupados.setdefault(ciudad, []).append(registro["nombre"])
    return agrupados