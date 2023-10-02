#Clase Grafo
class GrafoListaSinPesos:
    def __init__(self) -> None:
        self.__lista_vertices = dict()

    def __str__(self) -> str:
        return str(self.__lista_vertices)

    def __buscarVertice(self, dato_buscar):
        return self.__lista_vertices.get(dato_buscar)

    def verAdyacentes(self, dato_buscar):
        # solo se ejecuta si el vertice esta en el grafo
        if self.__buscarVertice(dato_buscar) != None:
            return list(self.__buscarVertice(dato_buscar))

    def adicionarVertice(self, dato_nuevo_vertice):
        if self.__buscarVertice(dato_nuevo_vertice) is None:
            lista_adyacentes = set()
            self.__lista_vertices[dato_nuevo_vertice] = lista_adyacentes

    def verVertices(self):
        return list(self.__lista_vertices.keys())

    def adicionarArcoDirigido(self, vertice_inicial, vertice_final):
        busqueda_inicial = self.__buscarVertice(vertice_inicial)
        busqueda_final = self.__buscarVertice(vertice_final)
        if busqueda_inicial is None or busqueda_final is None:
            return False
        busqueda_inicial.add(vertice_final)

    def adicionarArco(self, vertice_a, vertice_b):
        busqueda_a = self.__buscarVertice(vertice_a)
        busqueda_b = self.__buscarVertice(vertice_b)
        if busqueda_a is None or busqueda_b is None:
            return False
        busqueda_a.add(vertice_b)
        busqueda_b.add(vertice_a)

    def sonAdyacentes(self, vertice_inicial, vertice_final):
        busqueda_inicial = self.__buscarVertice(vertice_inicial)
        busqueda_final = self.__buscarVertice(vertice_final)
        if busqueda_inicial is None or busqueda_final is None:
            return False
        return vertice_final in busqueda_inicial

    #RECORRIDOS
    #RECORRIDO EN PROFUNDIDAD DFS
    def __dfs(self, list_recorrido:list, set_visitados:set, vertice_actual):
        list_recorrido.append(vertice_actual)
        set_visitados.add(vertice_actual)
        adyacentes_actual = self.__buscarVertice(vertice_actual)
        for ady_actual in adyacentes_actual:
            if ady_actual not in set_visitados:
                list_recorrido, set_visitados = self.__dfs(list_recorrido, set_visitados, ady_actual)
        return list_recorrido, set_visitados

    def recorrerProfundidad(self, vertice_inicial):        
        if self.__buscarVertice(vertice_inicial) is None:
            return None
        recorrido, visitados = self.__dfs(list(), set(), vertice_inicial)
        return recorrido

    #RECORRIDO EN ANCHURA BFS    
    def __bfs(self, list_recorrido:list, set_visitados:set, vertice_actual):
        list_recorrido.append(vertice_actual)
        set_visitados.add(vertice_actual)
        cola_ady = [vertice_actual]
        while cola_ady:
            vertice_cola = cola_ady.pop(0)        
            adyacentes_actual_cola = self.__buscarVertice(vertice_cola)
            for ady_actual in adyacentes_actual_cola:
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

    def recorrido(self, inicio_recorrido, anchura=False):
        if anchura:
            recorrido = self.recorrerAnchura(inicio_recorrido)
        else:
            recorrido = self.recorrerProfundidad(inicio_recorrido)
        return recorrido

    def grado_salida(self, vertice) -> int:
        return len(self.verAdyacentes(vertice))

    def grado_entrada(self, vertice):
        if self.__buscarVertice(vertice):
            grado_entrada = 0
            # recorrer grafo
            for vertice_actual in self.__lista_vertices:
                if vertice in self.verAdyacentes(vertice_actual):
                    grado_entrada += 1
            return grado_entrada

    def eliminar_arco(self, vertice1, vertice2, dirigido=True) -> None:
        # solo se ejecuta si ambos vertices estan en el grafo
        if self.__buscarVertice(vertice1) and self.__buscarVertice(vertice2):
            if dirigido:
                # borrar vertice 2 de los adyacentes de vertice 1
                    self.__lista_vertices[vertice1].discard(vertice2)
            else:
                # borrar ambos adyacentes en los sets de cada vertice    
                    self.__lista_vertices[vertice1].discard(vertice2)
                    self.__lista_vertices[vertice2].discard(vertice1)

    def eliminar_vertice(self, vertice_a_eliminar) -> None:
        if self.__buscarVertice(vertice_a_eliminar):
            for vertice_actual in self.__lista_vertices:
                if vertice_a_eliminar in self.verAdyacentes(vertice_actual):
                    self.eliminar_arco(vertice_actual, vertice_a_eliminar)
            self.__lista_vertices.pop(vertice_a_eliminar)

    def es_adyacente_de(self, vertice):
        if self.__buscarVertice(vertice):
            lo_tienen_como_adyacente = []
            for vertice_actual in self.__lista_vertices:
                if vertice in self.verAdyacentes(vertice_actual):
                    lo_tienen_como_adyacente.append(vertice_actual)
            return lo_tienen_como_adyacente

    def vertices_terminales(self) -> list:
        vertices_terminales = []
        for vertice_actual in self.__lista_vertices:
            if len(self.verAdyacentes(vertice_actual)) == 0:
                vertices_terminales.append(vertice_actual)
        return vertices_terminales
