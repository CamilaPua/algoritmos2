from grafos_sinpesos_2023 import GrafoListaSinPesos

def grafo1_diapositiva():
    grafo = GrafoListaSinPesos()
    vertices = ['R', 'D', 'F', 'K', 'L']
    for vertice in vertices:
        grafo.adicionarVertice(vertice)

    grafo.adicionarArcoDirigido('R', 'D')
    grafo.adicionarArcoDirigido('F', 'K')
    grafo.adicionarArco('D', 'F')
    grafo.adicionarArcoDirigido('D', 'K')
    grafo.adicionarArcoDirigido('F', 'K')
    grafo.adicionarArcoDirigido('L', 'K')
    grafo.adicionarArcoDirigido('L', 'F')

    return grafo

# Ejercicio
def grafo2_diapositiva(inicio_recorrido=None, anchura=False):
    grafo = GrafoListaSinPesos()
    vertices = [1, 2, 3, 4, 5, 6]
    for vertice in vertices:
        grafo.adicionarVertice(vertice)
    grafo.adicionarArco(1, 2)
    grafo.adicionarArco(2, 3)
    grafo.adicionarArco(1, 4)
    grafo.adicionarArco(4, 5)

    if inicio_recorrido :
        return grafo.recorridos(inicio_recorrido)
    return grafo

def grafo_9_vertices(inicio_recorrido=None, anchura=False):
    grafo = GrafoListaSinPesos()
    vertices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for vertice in vertices:
        grafo.adicionarVertice(vertice)
    grafo.adicionarArco(1, 2)
    grafo.adicionarArco(2, 3)
    grafo.adicionarArco(3, 4)
    grafo.adicionarArco(3, 5)
    grafo.adicionarArco(4, 5)
    grafo.adicionarArco(2, 6)
    grafo.adicionarArcoDirigido(6, 7)
    grafo.adicionarArcoDirigido(7, 8)
    grafo.adicionarArcoDirigido(8, 9)

if __name__ == '__main__':
    grafo = grafo1_diapositiva()
    print(grafo)
    print(grafo.vertices_terminales())
