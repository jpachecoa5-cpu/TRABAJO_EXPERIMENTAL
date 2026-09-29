CAMPOS_ESTUDIANTE = (
    "nombre",
    "apellido",
    "email",
    "carnet",
)

class Estudiante:
    """MODELO: representa a un estudiante. Usa las cuatro colecciones."""

    def __init__(self, id_estudiante, nombre, apellido, email, carnet, notas=None, materias=None):
        self.id = id_estudiante
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.carnet = carnet

        # DICCIONARIO DE LISTAS:
        # {"Matemática": [18, 19], "Inglés": [17]}
        self.notas = notas if notas else {}

        # CONJUNTO: materias en las que está inscrito, sin repetidos
        self.materias = set(materias) if materias else set()

    def obtener_nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    def inscribir_materia(self, materia):
        # add() no duplica
        self.materias.add(materia)

    def agregar_nota(self, materia, nota):
        self.inscribir_materia(materia)

        # Crea la lista si la materia todavía no existe
        self.notas.setdefault(materia, []).append(nota)

    def obtener_promedio(self):
        todas = []

        for lista_notas in self.notas.values():
            todas.extend(lista_notas)

        if not todas:
            return 0

        return round(sum(todas) / len(todas), 2)

    def materias_en_comun(self, otro_estudiante):
        # INTERSECCIÓN de conjuntos
        return self.materias & otro_estudiante.materias

    def a_diccionario(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "email": self.email,
            "carnet": self.carnet,
            "notas": self.notas,

            # JSON no guarda set directamente,
            # por eso lo convertimos en lista.
            "materias": sorted(self.materias),
        }

    @classmethod
    def desde_diccionario(cls, datos):
        return cls(
            datos["id"],
            datos["nombre"],
            datos["apellido"],
            datos["email"],
            datos["carnet"],
            notas=datos.get("notas", {}),
            materias=set(datos.get("materias", [])),
        )

    def __str__(self):
        return f"[{self.carnet}] {self.obtener_nombre_completo()} - Promedio: {self.obtener_promedio()}"