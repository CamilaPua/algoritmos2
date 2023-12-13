class Ciudad:
    def __init__(self, nombre, anio_creacion, poblacion) -> None:
        self.nombre = nombre
        self.anio_creacion = anio_creacion
        self.poblacion = poblacion

    def __str__(self) -> str:
        return str(self.nombre) + ' - Población: ' + str(self.poblacion)

    def __lt__(self, otra_ciudad):
        return self.poblacion < otra_ciudad.poblacion

    def __gt__(self, otra_ciudad):
        return self.poblacion > otra_ciudad.poblacion
