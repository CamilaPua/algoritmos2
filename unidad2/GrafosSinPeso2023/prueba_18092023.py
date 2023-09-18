from grafos_sinpesos_2023 import GrafoListaSinPesos

def prueba():
    grafo = GrafoListaSinPesos()

    grafo.adicionarVertice('a')
    grafo.adicionarVertice('b')
    grafo.adicionarVertice('c')
    grafo.adicionarVertice('d')
    print('Grafo:', grafo)

    grafo.adicionarArcoDirigido('a', 'b')
    grafo.adicionarArcoDirigido('b', 'a')
    grafo.adicionarArcoDirigido('c', 'b')
    grafo.adicionarArcoDirigido('d', 'c')
    print('Grafo:', grafo)

# Ejercicio
def ejercicio():
    grafo = GrafoListaSinPesos()
    vertices = [1, 2, 3, 4, 5, 6]
    for vertice in vertices:
        grafo.adicionarVertice(vertice)
    grafo.adicionarArco(1, 2)
    grafo.adicionarArco(2, 3)
    grafo.adicionarArco(1, 4)
    grafo.adicionarArco(4, 5)
    print(grafo)

if __name__ == '__main__':
    ejercicio()
