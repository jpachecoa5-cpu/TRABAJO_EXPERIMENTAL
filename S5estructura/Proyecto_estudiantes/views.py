from models import Estudiante, CAMPOS_ESTUDIANTE
from shared.json_manager import GestorJSON
from shared.herramientas import es_email_valido


gestor = GestorJSON("data/estudiantes.json")


# TUPLA de campos obligatorios
CAMPOS_OBLIGATORIOS = ("nombre", "apellido", "email", "carnet")

# TUPLA de campos que podremos buscar
CAMPOS_BUSCABLES = ("nombre", "apellido", "email", "carnet")


# AYUDAS INTERNAS 

def carnets_registrados(excepto_id=None):
    """CONJUNTO con los carnets ya utilizados."""
    return {
        registro["carnet"].lower()
        for registro in gestor.leer()
        if registro["id"] != excepto_id
    }


def siguiente_id():
    """Obtiene el siguiente ID disponible."""
    ids = [registro["id"] for registro in gestor.leer()]
    return max(ids) + 1 if ids else 1

# CREATE
def crear_estudiante(datos):
    """Crea un estudiante y lo guarda en el archivo JSON."""
    try:
        # 1) Normalizo los datos
        valores = {
            campo: str(datos.get(campo, "")).strip()
            for campo in CAMPOS_ESTUDIANTE
        }

        # 2) Reviso los campos obligatorios
        faltantes = [
            campo
            for campo in CAMPOS_OBLIGATORIOS
            if not valores[campo]
        ]

        if faltantes:
            return False, f"Faltan campos obligatorios: {', '.join(faltantes)}"

        # 3) Reviso que el email tenga un formato válido
        if not es_email_valido(valores["email"]):
            return False, f"El email '{valores['email']}' no tiene un formato válido"

        # 4) Reviso que el carnet no esté repetido
        if valores["carnet"].lower() in carnets_registrados():
            return False, "Ese carnet ya está registrado"

        # 5) Creo el objeto Estudiante
        estudiante = Estudiante(siguiente_id(), **valores)

        # 6) Lo agrego a la LISTA y guardo
        registros = gestor.leer()
        registros.append(estudiante.a_diccionario())

        if not gestor.guardar(registros):
            return False, "No se pudo escribir el archivo"

        return True, (
            f"Estudiante {estudiante.obtener_nombre_completo()} "
            f"creado con id {estudiante.id}"
        )

    except Exception as error:
        return False, f"Error inesperado: {error}"
    
    # READ
def obtener_todos():
    """Devuelve una LISTA de objetos Estudiante."""
    return [
        Estudiante.desde_diccionario(registro)
        for registro in gestor.leer()
    ]


def obtener_por_id(id_estudiante):
    """Busca un estudiante por su ID."""
    for estudiante in obtener_todos():
        if estudiante.id == id_estudiante:
            return estudiante

    return None

# SEARCH 

def buscar_estudiantes(termino):
    """Busca estudiantes por nombre, apellido, email o carnet."""
    termino = termino.strip().lower()

    if not termino:
        return []

    encontrados = []

    for registro in gestor.leer():
        for campo in CAMPOS_BUSCABLES:
            if termino in str(registro.get(campo, "")).lower():
                encontrados.append(
                    Estudiante.desde_diccionario(registro)
                )
                break

    return encontrados

# UPDATE 

def actualizar_estudiante(id_estudiante, cambios):
    """Actualiza los campos indicados de un estudiante."""
    try:
        # Revisamos que los campos existan
        desconocidos = set(cambios) - set(CAMPOS_ESTUDIANTE)

        if desconocidos:
            return False, f"Campos no válidos: {', '.join(sorted(desconocidos))}"

        if not cambios:
            return False, "No se indicó ningún cambio"

        # Si se cambia el email, lo validamos
        if "email" in cambios:
            cambios["email"] = cambios["email"].strip()

            if not es_email_valido(cambios["email"]):
                return False, "El email no tiene un formato válido"

        # Si se cambia el carnet, revisamos que no esté repetido
        if "carnet" in cambios:
            cambios["carnet"] = cambios["carnet"].strip()

            if cambios["carnet"].lower() in carnets_registrados(
                excepto_id=id_estudiante
            ):
                return False, "Ese carnet ya lo usa otro estudiante"

        registros = gestor.leer()

        posicion = None

        for indice, registro in enumerate(registros):
            if registro["id"] == id_estudiante:
                posicion = indice
                break

        if posicion is None:
            return False, f"No existe un estudiante con id {id_estudiante}"

        registros[posicion].update(cambios)

        if not gestor.guardar(registros):
            return False, "No se pudo escribir el archivo"

        return True, (
            f"Estudiante {id_estudiante} actualizado "
            f"({len(cambios)} campo/s)"
        )

    except Exception as error:
        return False, f"Error inesperado: {error}"
    
# DELETE

def eliminar_estudiante(id_estudiante):
    """Elimina un estudiante por su ID."""
    registros = gestor.leer()

    # Creamos una LISTA nueva sin el estudiante indicado
    quedan = [
        registro
        for registro in registros
        if registro["id"] != id_estudiante
    ]

    # Si las listas tienen el mismo tamaño, no se encontró
    if len(quedan) == len(registros):
        return False, f"No existe un estudiante con id {id_estudiante}"

    # Guardamos la nueva lista
    if not gestor.guardar(quedan):
        return False, "No se pudo escribir el archivo"

    return True, f"Estudiante {id_estudiante} eliminado"


# FUNCIONES ESPECIALES 

def agregar_nota(id_estudiante, materia, nota):
    """Agrega una nota a un estudiante."""

    # La nota debe estar entre 0 y 20
    if nota < 0 or nota > 20:
        return False, "La nota debe estar entre 0 y 20"

    estudiante = obtener_por_id(id_estudiante)

    if estudiante is None:
        return False, f"No existe un estudiante con id {id_estudiante}"

    materia = materia.strip()

    if not materia:
        return False, "La materia no puede estar vacía"

    estudiante.agregar_nota(materia, nota)

    registros = gestor.leer()

    for registro in registros:
        if registro["id"] == id_estudiante:
            registro.update(estudiante.a_diccionario())
            break

    if not gestor.guardar(registros):
        return False, "No se pudo guardar la nota"

    return True, "Nota agregada correctamente"

def materias_ofertadas():
    """Devuelve un CONJUNTO con todas las materias inscritas."""

    materias = set()

    for estudiante in obtener_todos():
        materias.update(estudiante.materias)

    return materias

def estudiantes_en_comun(id_a, id_b):
    """Devuelve las materias que comparten dos estudiantes."""

    estudiante_a = obtener_por_id(id_a)
    estudiante_b = obtener_por_id(id_b)

    if estudiante_a is None:
        return set()

    if estudiante_b is None:
        return set()

    # INTERSECCIÓN de conjuntos
    return estudiante_a.materias & estudiante_b.materias
