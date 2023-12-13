from estudiante import Estudiante

class ArbolBinarioEstudiantes:
    def __init__(self, estudiante:Estudiante, arbol_izquierdo=None, arbol_derecho=None) -> None:
        self.estudiante = estudiante
        self.hijo_izquierdo = arbol_izquierdo
        self.hijo_derecho = arbol_derecho     

    def esHoja(self):
        return self.hijo_izquierdo == None and self.hijo_derecho == None
    
    def __str__(self) -> str:
        return str(self.estudiante)
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def __eq__(self, otro: object) -> bool:
        if not isinstance(otro, ArbolBinarioEstudiantes):
            return False
        return self.estudiante == otro.estudiante

    #Visualización Arbol
    def verArbol(self) -> str: 
        return self.__verArbol(self,"")

    def __verArbol(self, arbol:"ArbolBinarioEstudiantes", recorrido:str, nivel=0) -> str:
        espaciado = "\t" * nivel   
        if arbol is None:
            return ""
        recorrido =  espaciado + str(arbol.estudiante) + "\n" \
            + str(self.__verArbol(arbol.hijo_izquierdo, recorrido, nivel+1)) + \
            str(self.__verArbol(arbol.hijo_derecho, recorrido, nivel + 1)) + recorrido
        return recorrido

#RECORRIDOS
    #Preorden o profundidad
    def preOrden(self):
        visitados = list()
        self.__preOrden(self, visitados)
        return visitados
    
    def __preOrden(self, arbol:"ArbolBinarioEstudiantes", visitados:list):
        if arbol is not None:
            visitados.append(arbol)
            visitados = self.__preOrden(arbol.hijo_izquierdo, visitados)
            visitados = self.__preOrden(arbol.hijo_derecho, visitados)
        return visitados
    #EnOrden
    def enOrden(self):
        visitados = list()
        self.__enOrden(self, visitados)
        return visitados
    
    def __enOrden(self, arbol:"ArbolBinarioEstudiantes", visitados:list):
        if arbol is not None:
            visitados = self.__enOrden(arbol.hijo_izquierdo, visitados)
            visitados.append(arbol)
            visitados = self.__enOrden(arbol.hijo_derecho, visitados)
        return visitados
    #PosOrden
    def posOrden(self):
        visitados = list()
        self.__posOrden(self, visitados)
        return visitados
    
    def __posOrden(self, arbol:"ArbolBinarioEstudiantes", visitados:list):
        if arbol is not None:
            visitados = self.__posOrden(arbol.hijo_izquierdo, visitados)
            visitados = self.__posOrden(arbol.hijo_derecho, visitados)
            visitados.append(arbol)
        return visitados

    def estudiantes_hoja_aprobados(self) -> list:
        hojas_aprobadas = list()
        self.__nodos_hoja(self, hojas_aprobadas)
        return hojas_aprobadas

    def __nodos_hoja(self, arbol:"ArbolBinarioEstudiantes", hojas_aprobadas:list) -> list:
        if arbol is not None:
            hojas_aprobadas = self.__nodos_hoja(arbol.hijo_izquierdo, hojas_aprobadas)
            hojas_aprobadas = self.__nodos_hoja(arbol.hijo_derecho, hojas_aprobadas)
            if arbol.esHoja() and arbol.estudiante.aprobado:
                hojas_aprobadas.append(arbol)
        return hojas_aprobadas

    def estudiantes_de_un_nivel(self, nivel:int) -> list:
        estudiantes = list()
        self.__estudiantes_de_un_nivel(self, nivel, estudiantes)
        return estudiantes

    def __estudiantes_de_un_nivel(self, arbol:"ArbolBinarioEstudiantes", nivel:int, estudiantes:list, nivel_actual=-1) -> list:
        if arbol is not None:
            nivel_actual += 1
            if nivel_actual == nivel:
                estudiantes.append(arbol)
            self.__estudiantes_de_un_nivel(arbol.hijo_izquierdo, nivel, estudiantes, nivel_actual)
            self.__estudiantes_de_un_nivel(arbol.hijo_derecho, nivel, estudiantes, nivel_actual)
        return estudiantes

    def numero_estudiantes_en_un_nivel(self, nivel:int):
        return len(self.estudiantes_de_un_nivel(nivel))

    def estudiantes_con_nota(self, nota) -> list:
        estudiantes = list()
        self.__estudiantes_con_nota(self, estudiantes, nota)
        return estudiantes

    def __estudiantes_con_nota(self, arbol, estudiantes, nota) -> list:
        if arbol is not None and type(self.estudiante) == Estudiante:
            if arbol.estudiante.tiene_nota(nota):
                estudiantes.append(arbol)
            estudiantes = self.__estudiantes_con_nota(arbol.hijo_izquierdo, estudiantes, nota)
            estudiantes = self.__estudiantes_con_nota(arbol.hijo_derecho, estudiantes, nota)
        return estudiantes
