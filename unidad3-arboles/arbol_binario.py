#Clase Arbol
class ArbolBinario:
    def __init__(self, dato, arbol_izquierdo=None, arbol_derecho=None) -> None:
        self.valor_nodo = dato
        self.hijo_izquierdo = arbol_izquierdo
        self.hijo_derecho = arbol_derecho     

    def esHoja(self):
        return self.hijo_izquierdo == None and self.hijo_derecho == None
    
    def __str__(self) -> str:
        return str(self.valor_nodo)
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def __eq__(self, otro: object) -> bool:
        if not isinstance(otro, ArbolBinario):
            return False
        return self.valor_nodo == otro.valor_nodo

    #Visualización Arbol      
    def verArbol(self) -> str: 
        return self.__verArbol(self,"")
    
    def __verArbol(self, arbol:"ArbolBinario", recorrido:str, nivel=0) -> str:
        espaciado = "\t" * nivel        
        if arbol is None:
            return ""
        recorrido =  espaciado + str(arbol.valor_nodo) + "\n" \
            + str(self.__verArbol(arbol.hijo_izquierdo, recorrido, nivel+1)) + \
            str(self.__verArbol(arbol.hijo_derecho, recorrido, nivel + 1)) + recorrido
        return recorrido        
    
    #RECORRIDOS
    #Preorden o profundidad
    def preOrden(self):
        visitados = list()
        self.__preOrden(self, visitados)
        return visitados
    
    def __preOrden(self, arbol:"ArbolBinario", visitados:list):
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
    
    def __enOrden(self, arbol:"ArbolBinario", visitados:list):
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
    
    def __posOrden(self, arbol:"ArbolBinario", visitados:list):
        if arbol is not None:
            visitados = self.__posOrden(arbol.hijo_izquierdo, visitados)
            visitados = self.__posOrden(arbol.hijo_derecho, visitados)
            visitados.append(arbol)
        return visitados

    def nodos_hoja(self) -> list:
        hojas = list()
        self.__nodos_hoja(self, hojas)
        return hojas

    def __nodos_hoja(self, arbol:"ArbolBinario", hojas:list) -> list:
        if arbol is not None:
            hojas = self.__nodos_hoja(arbol.hijo_izquierdo, hojas)
            hojas = self.__nodos_hoja(arbol.hijo_derecho, hojas)
            if arbol.esHoja(): hojas.append(arbol)
        return hojas
    
    def numero_nodos(self) -> int:
        return len(self.enOrden())

    def altura_arbol(self) -> int:
        return self.__altura_arbol(self)

    def __altura_arbol(self, arbol:"ArbolBinario") -> int:
        if arbol is None:
            altura = 0
        else:
            altura = 1 + max(self.__altura_arbol(arbol.hijo_izquierdo), self.__altura_arbol(arbol.hijo_derecho))
        return altura

    def nodos_de_un_nivel(self, nivel:int) -> list:
        nodos = list()
        self.__nodos_de_un_nivel(self, nivel, nodos)
        return nodos

    def __nodos_de_un_nivel(self, arbol:"ArbolBinario", nivel:int, nodos:list, nivel_actual=-1) -> list:
        if arbol is not None:
            nivel_actual += 1
            if nivel_actual == nivel:
                nodos.append(arbol)
            self.__nodos_de_un_nivel(arbol.hijo_izquierdo, nivel, nodos, nivel_actual)
            self.__nodos_de_un_nivel(arbol.hijo_derecho, nivel, nodos, nivel_actual)
        return nodos

    def numero_nodos_en_un_nivel(self, nivel:int):
        return len(self.nodos_de_un_nivel(nivel))

    def es_completo(self) -> bool:
        for nivel in range(self.altura_arbol()):
            if self.numero_nodos_en_un_nivel(nivel) != 2**nivel:
                return False
        return True

    def papaelemento(self, elemento):
        papanodo = self.__papaelemento(self, [], elemento)
        return papanodo

    def __papaelemento(self, arbol:"ArbolBinario", papanodo:list, elemento):
        if arbol is not None:
            if arbol.hijo_derecho is not None:
                if  arbol.hijo_derecho.valor_nodo == elemento:
                    papanodo.append(arbol)
            if arbol.hijo_izquierdo is not None:
                if arbol.hijo_izquierdo.valor_nodo == elemento:
                    papanodo.append(arbol)
            papanodo = self.__papaelemento(arbol.hijo_izquierdo, papanodo, elemento)
            papanodo = self.__papaelemento(arbol.hijo_derecho, papanodo, elemento)
        return papanodo

    def nodos_mas_profundos(self) -> list:
        mayor_profundidad = self.altura_arbol() - 1
        return self.nodos_de_un_nivel(mayor_profundidad)
