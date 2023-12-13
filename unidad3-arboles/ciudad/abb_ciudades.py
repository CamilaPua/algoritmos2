from ab_ciudades import ArbolBinario
from ciudad import Ciudad

#Clase Arbol Binario de Búsqueda (ABB)
class ArbolBinarioBusqueda:
    def __init__(self) -> None:
        self.raiz = None

    def estaVacio(self) -> bool:
        return self.raiz == None

    def __str__(self) -> str:
        if not self.estaVacio():
            return self.raiz.verArbol()
        return ""

    def __repr__(self) -> str:
        return self.__str__()

    #Recorrido
    def enOrden(self):
        if not self.estaVacio():
            return self.raiz.enOrden()
        return None
        
    #Visualización Arbol      
    def verArbol(self):
        if not self.estaVacio():
            return self.raiz.verArbol()
        return None

    #Insercion
    def insertar(self, ciudad:Ciudad):
        if self.estaVacio():
            self.raiz = ArbolBinario(ciudad)
        self.__insertar(self.raiz, ciudad)

    def __insertar(self, arbol:ArbolBinario, ciudad):
        if ciudad == arbol.ciudad:
            return
        if ciudad < arbol.ciudad:
            if arbol.hijo_izquierdo is None:
                arbol.hijo_izquierdo = ArbolBinario(ciudad)
            else:
                self.__insertar(arbol.hijo_izquierdo, ciudad)
        else:
            if arbol.hijo_derecho is None:
                arbol.hijo_derecho = ArbolBinario(ciudad)
            else:
                self.__insertar(arbol.hijo_derecho, ciudad)

    #Búsqueda
    def buscar(self, elemento) -> ArbolBinario:
        if not self.estaVacio():
            return self.__buscar(self.raiz, elemento)
        return None

    def __buscar(self, arbol:ArbolBinario, elemento):
        if elemento == arbol.ciudad:
            return arbol
        if elemento < arbol.ciudad:
            if arbol.hijo_izquierdo is not None:
                return self.__buscar(arbol.hijo_izquierdo, elemento)
            else:
                return None
        else:
            if arbol.hijo_derecho is not None:
                return self.__buscar(arbol.hijo_derecho, elemento)
            else:
                return None

    #Eliminar
    def eliminar(self, elemento):
        if not self.estaVacio():
            return self.__eliminar(self.raiz, elemento, None)
        return False

    def __eliminar(self, arbol:ArbolBinario, elemento, padre:ArbolBinario):
        if arbol is None:
            return False
        if elemento < arbol.ciudad:
            return self.__eliminar(arbol.hijo_izquierdo, elemento, padre=arbol)
        elif elemento > arbol.ciudad:
            return self.__eliminar(arbol.hijo_derecho, elemento, padre=arbol)
        else:
            #Caso Nodo hoja
            if arbol.esHoja():
                #Caso Nodo Hoja y Raiz
                if arbol == self.raiz:
                    self.raiz = None
                    return True
                #Actualizacion enlace nodo padre
                if padre.hijo_izquierdo == arbol:
                    padre.hijo_izquierdo = None
                else:
                    padre.hijo_derecho = None
                return True
            #Caso Nodo con un hijo
            if arbol.hijo_izquierdo is None and arbol.hijo_derecho is not None:
                #Nodo con hijo derecho únicamente
                #Caso Raiz
                if arbol == self.raiz:
                    self.raiz = arbol.hijo_derecho
                    return True
                #Actualizacion enlace nodo padre
                if padre.hijo_izquierdo is not None and padre.hijo_izquierdo == arbol:
                    padre.hijo_izquierdo = arbol.hijo_derecho
                else:
                    padre.hijo_derecho = arbol.hijo_derecho
                return True
            if arbol.hijo_izquierdo is not None and arbol.hijo_derecho is None:
                #Nodo con hijo izquierdo únicamente
                #Caso Raiz
                if arbol == self.raiz:
                    self.raiz = arbol.hijo_izquierdo
                    return True
                #Actualizacion enlace nodo padre
                if padre.hijo_izquierdo is not None and padre.hijo_izquierdo == arbol:
                    padre.hijo_izquierdo = arbol.hijo_izquierdo
                else:
                    padre.hijo_derecho = arbol.hijo_izquierdo
                return True
            #Caso Nodo interno
            nodo_izquierdo:ArbolBinario = arbol.hijo_izquierdo
            nodo_temporal:ArbolBinario = None            
            while nodo_izquierdo.hijo_derecho is not None: # busca el mayor de los menores
                nodo_temporal = nodo_izquierdo
                nodo_izquierdo = nodo_izquierdo.hijo_derecho
            arbol.ciudad = nodo_izquierdo.ciudad
            if nodo_temporal is None:
                arbol.hijo_izquierdo = nodo_izquierdo.hijo_izquierdo
            elif nodo_temporal.hijo_izquierdo == nodo_izquierdo:
                nodo_temporal.hijo_izquierdo = nodo_izquierdo.hijo_izquierdo
            elif nodo_temporal.hijo_derecho == nodo_izquierdo:
                nodo_temporal.hijo_derecho = nodo_izquierdo.hijo_izquierdo
            return True

    def zona_influencia(self, ciudad:Ciudad) -> list:
        ciudad = self.buscar(ciudad)
        if ciudad is not None:
            return ciudad.descendencia()

    def mayor_influente(self) -> ArbolBinario:
        if not self.estaVacio():
            arbol_izquierdo = self.raiz.hijo_izquierdo
            arbol_derecho = self.raiz.hijo_derecho
            if len(arbol_izquierdo.descendencia()) > len(arbol_derecho.descendencia()):
                return arbol_izquierdo
            return arbol_derecho

    def menor_y_mayor_poblacion(self):
        if not self.estaVacio():
            arbol_izquierdo = self.raiz.hijo_izquierdo
            arbol_derecho = self.raiz.hijo_derecho
            return self.__menor_y_mayor_poblacion(arbol_izquierdo, arbol_derecho)

    def __menor_y_mayor_poblacion(self, arbol_izquierdo, arbol_derecho):
        while arbol_izquierdo.hijo_izquierdo is not None:
            arbol_izquierdo = arbol_izquierdo.hijo_izquierdo
        while arbol_derecho.hijo_derecho is not None:
            arbol_derecho = arbol_derecho.hijo_derecho
        return arbol_izquierdo, arbol_derecho

    def mayor_poblacion(self) -> ArbolBinario:
        return self.menor_y_mayor_poblacion()[1]

    def promedio_poblacion_ciudades(self) -> float:
        if not self.estaVacio():
            poblaciones = list()
            for nodo in self.enOrden():
                poblaciones.append(nodo.ciudad.poblacion)
            return round(sum(poblaciones)/len(poblaciones), 2)

    def ciudades_poblacion_mayor_promedio(self) -> list:
        if not self.estaVacio():
            ciudades = list()
            for nodo in self.enOrden():
                if nodo.ciudad.poblacion > self.promedio_poblacion_ciudades():
                    ciudades.append(nodo)
            return ciudades
