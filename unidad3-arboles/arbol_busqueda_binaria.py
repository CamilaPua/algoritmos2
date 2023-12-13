from arbol_binario import ArbolBinario

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
    def insertar(self, elemento):
        if self.estaVacio():
            self.raiz = ArbolBinario(elemento)
        self.__insertar(self.raiz, elemento)

    def __insertar(self, arbol:ArbolBinario, elemento):
        if elemento == arbol.ciudad:
            return
        if elemento < arbol.ciudad:
            if arbol.hijo_izquierdo is None:
                arbol.hijo_izquierdo = ArbolBinario(elemento)
            else:
                self.__insertar(arbol.hijo_izquierdo, elemento)
        else:
            if arbol.hijo_derecho is None:
                arbol.hijo_derecho = ArbolBinario(elemento)
            else:
                self.__insertar(arbol.hijo_derecho, elemento)

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

    def arriba_mas_cercano(self, elemento) -> ArbolBinario:
        pass

    def menor_y_mayor(self):
        if not self.estaVacio():
            arbol_izquierdo = self.raiz.hijo_izquierdo
            arbol_derecho = self.raiz.hijo_derecho
            return self.__menor_y_mayor(arbol_izquierdo, arbol_derecho)

    def __menor_y_mayor(self, arbol_izquierdo, arbol_derecho):
        while arbol_izquierdo.hijo_izquierdo is not None:
            arbol_izquierdo = arbol_izquierdo.hijo_izquierdo
        while arbol_derecho.hijo_derecho is not None:
            arbol_derecho = arbol_derecho.hijo_derecho
        return arbol_izquierdo, arbol_derecho

    def factor_de_equilibrio(self) -> int:
        sub_arbol_izquierdo = self.raiz.hijo_izquierdo
        sub_arbol_derecho = self.raiz.hijo_derecho
        return sub_arbol_izquierdo.altura_arbol() - sub_arbol_derecho.altura_arbol()
