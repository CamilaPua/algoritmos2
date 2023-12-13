class Estudiante:
    def __init__(self, id:int, nombre:str, fecha_nacimiento:str, notas=[]):
        self.id = id
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.notas = notas
        self.promedio = round(sum(self.notas)/len(self.notas), 2)
        self.aprobado = self.promedio >= 3

    def __str__(self) -> str:
        return str(self.nombre)

    def __repr__(self) -> str:
        return self.__str__()

    def tiene_nota(self, nota):
        return nota in self.notas
