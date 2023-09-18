import sys
#Clase Arco
class Arco:
    def __init__(self, vertice_inicial, vertice_final, peso:int) -> None:
        self.vertice_inicial = vertice_inicial
        self.vertice_final = vertice_final
        self.peso = peso
    
    def __repr__(self) -> str:
        return "["+str(self.vertice_inicial)+", "+str(self.vertice_final)+"]: "+str(self.peso)
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __eq__(self, otro: object) -> bool:
        if not isinstance(otro, Arco):
            return False
        return self.vertice_inicial == otro.vertice_inicial and \
               self.vertice_final == otro.vertice_final and self.peso == otro.peso
    
    def __hash__(self) -> int:
        return hash(str(self))
#Clase Grafo
class GrafoListaConPesos:
    def __init__(self) -> None:
        self.__lista_vertices = dict()
    
    def __str__(self) -> str:
        return str(self.__lista_vertices)
    
    def __buscarVertice(self, dato_buscar):
        return self.__lista_vertices.get(dato_buscar)
    
    def adicionarVertice(self, dato_nuevo_vertice):
        if self.__buscarVertice(dato_nuevo_vertice) is None:
            lista_adyacentes = set()
            self.__lista_vertices[dato_nuevo_vertice] = lista_adyacentes
    
    def verVertices(self):
        return list(self.__lista_vertices.keys())
    
    def verAdyacentes(self, dato_buscar):
        return list(self.__lista_vertices.get(dato_buscar))

    def adicionarArco(self, vertice_inicial, vertice_final, peso:int = 0):
        busqueda_inicial = self.__buscarVertice(vertice_inicial)
        busqueda_final = self.__buscarVertice(vertice_final)        
        if busqueda_inicial is None or busqueda_final is None:
            return False
        #Creacion de arco
        arco_nuevo = Arco(vertice_inicial, vertice_final, peso)
        busqueda_inicial.add(arco_nuevo)
    
    def sonAdyacentes(self, vertice_inicial, vertice_final):
        busqueda_inicial = self.__buscarVertice(vertice_inicial)
        busqueda_final = self.__buscarVertice(vertice_final)
        if busqueda_inicial is None or busqueda_final is None:
            return False
        for arco in busqueda_inicial:
            if arco.vertice_final == vertice_final:
                return True
        return False   
    
    #RECORRIDOS
    #RECORRIDO EN PROFUNDIDAD DFS
    def __dfs(self, list_recorrido:list, set_visitados:set, vertice_actual):
        list_recorrido.append(vertice_actual)
        set_visitados.add(vertice_actual)
        adyacentes_actual = self.__buscarVertice(vertice_actual)
        for arco_ady_actual in adyacentes_actual:
            ady_actual = arco_ady_actual.vertice_final
            if ady_actual not in set_visitados:
                list_recorrido, set_visitados = self.__dfs(list_recorrido, set_visitados, ady_actual)
        return list_recorrido, set_visitados

    def recorrerProfundidad(self, vertice_inicial):        
        if self.__buscarVertice(vertice_inicial) is None:
            return None        
        recorrido, visitados = self.__dfs(list(), set(), vertice_inicial)
        for vertice in self.verVertices():
            if vertice not in visitados:
                recorrido, visitados = self.__dfs(recorrido, visitados, vertice)
        return recorrido
    
    #RECORRIDO EN ANCHURA BFS    
    def __bfs(self, list_recorrido:list, set_visitados:set, vertice_actual):
        list_recorrido.append(vertice_actual)
        set_visitados.add(vertice_actual)
        cola_ady = [vertice_actual]
        while cola_ady:
            vertice_cola = cola_ady.pop(0)        
            adyacentes_actual_cola = self.__buscarVertice(vertice_cola)
            for arco_ady_actual in adyacentes_actual_cola:
                ady_actual = arco_ady_actual.vertice_final
                if ady_actual not in set_visitados:
                    list_recorrido.append(ady_actual)
                    set_visitados.add(ady_actual)
                    cola_ady.append(ady_actual)
        return list_recorrido, set_visitados

    def recorrerAnchura(self, vertice_inicial):
        if self.__buscarVertice(vertice_inicial) is None:
            return None        
        recorrido, visitados = self.__bfs(list(), set(), vertice_inicial)
        for vertice in self.verVertices():
            if vertice not in visitados:
                recorrido, visitados = self.__bfs(recorrido, visitados, vertice)
        return recorrido
    