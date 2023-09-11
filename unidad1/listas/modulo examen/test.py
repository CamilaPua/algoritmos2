from SinglyLinkedList import SinglyLinkedList

def pruebas_agregar():
    print(' ----- Metodos agregar al final y al princio -----')
    lista1 = SinglyLinkedList()
    print(f'\tLista 1: {lista1}\tlongitud: {lista1.size}\n')

    print('  | En la lista vacia 1 agregaremos al final el numero 1 y el 2')
    lista1.append(1)
    lista1.append(2)
    print(f'  | Lista 1: {lista1}\tlongitud: {lista1.size}\n')
    
    print('  | Ahora agregamos al inicio')
    lista1.prepend(0)
    print(f'  | Lista 1: {lista1}\tlongitud: {lista1.size}\n')

    print('  | El metodo prepend tambien funciona cuando la lista esta vacia')
    lista2 = SinglyLinkedList()
    print(f'  | Lista 2: {lista2}\tlongitud: {lista2.size}')
    lista2.prepend('porsiaca')
    print(f'  | Lista 2: {lista2}\tlongitud: {lista2.size}\n')


def pruebas_eliminar_por_indice():
    lista = SinglyLinkedList()
    print('\n ----- Metodos eliminar por indice -----')
    
    print('  - Con la lista vacia')
    print('  | Intentemos eliminar una posicion (0) que no existe')
    lista.delete_index(0)
    print(f'  | Lista: {lista}\tlongitud: {lista.size}\n')

    lista.append(0)
    print('  - Eliminar una unica posicion (0) en la lista')
    print(f'  | Lista: {lista}\tlongitud: {lista.size}')
    lista.delete_index(0)
    print(f'  | Resultado: {lista}\tlongitud: {lista.size}\n')

    print('  - Eliminar una posicion media (1) de la lista')
    lista.append(1)
    lista.append(2)
    lista.append(3)
    lista.append(4)
    print(f'  | Lista: {lista}\tlongitud: {lista.size}')
    lista.delete_index(1)
    print(f'  | Resultado: {lista}\tlongitud: {lista.size}\n')
    
    print('  | Eliminamos la ultima posicion (2) por su indice')
    print(f'  | Lista: {lista}\tlongitud: {lista.size}')
    lista.delete_index(2)
    print(f'  | Resultado: {lista}\tlongitud: {lista.size}\n')

    print('  | Eliminamos la primera posicion (0) por su indice')
    print(f'  | Lista: {lista}\tlongitud: {lista.size}')
    lista.delete_index(0)
    print(f'  | Resultado: {lista}\tlongitud: {lista.size}\n')


def pruebas_eliminar_primer_elemento():
    print('\n ----- Metodos eliminar primer elemento -----')

    print('\n  - Con la lista vacia')
    lista = SinglyLinkedList()
    print(f'  | Lista: {lista}\tlongitud: {lista.size}')
    lista.delete_first()
    print(f'  | Resultado: {lista}\tlongitud: {lista.size}')

    print('\n  - Con un solo elemento')
    lista.append('hola')
    print(f'  | Lista: {lista}\tlongitud: {lista.size}')
    lista.delete_first()
    print(f'  | Resultado: {lista}\tlongitud: {lista.size}')
    
    print('\n  - Con varios elementos')
    data = ('hola', 1, 2, 'Python')
    for i in data:
        lista.append(i)
    print(f'  | Lista: {lista}\tlongitud: {lista.size}')
    lista.delete_first()
    print(f'  | Resultado: {lista}\tlongitud: {lista.size}\n')


def pruebas_eliminar_ultimo_elemento():
    print('\n ----- Metodos eliminar ultimo elemento -----')
    print('\n  - Con la lista vacia')
    lista = SinglyLinkedList()
    print(f'  | Lista: {lista}\tlongitud: {lista.size}')
    lista.delete_last()
    print(f'  | Resultado: {lista}\tlongitud: {lista.size}')

    print('\n  - Con un solo elemento')
    lista.append('hola')
    print(f'  | Lista: {lista}\tlongitud: {lista.size}')
    lista.delete_last()
    print(f'  | Resultado: {lista}\tlongitud: {lista.size}')
    
    print('\n  - Con varios elementos')
    data = ('hola', 1, 2, 'Python')
    for i in data:
        lista.append(i)
    print(f'  | Lista: {lista}\tlongitud: {lista.size}')
    lista.delete_last()
    print(f'  | Resultado: {lista}\tlongitud: {lista.size}\n')


def pruebas_contar():
    print('\n ---------- Contar un elemento ----------')
    lista1 = SinglyLinkedList()
    print('\n  - Con la lista vacia')
    print(f'  | Lista 1: {lista1}\tlongitud: {lista1.size}\n')
    print(f'  | Ocurrencias de "hola": {lista1.count("hola")}')

    data = (1, 2, 3, 'hola', 'hola')
    for i in data:
        lista1.append(i)
    print('\n  - Con la lista llena')
    print(f'  | Lista 1: {lista1}\tlongitud: {lista1.size}\n')

    print(f'  | Ocurrencias de "hola": {lista1.count("hola")}')
    print(f'  | Ocurrencias de "Camila": {lista1.count("Camila")}\n')


def pruebas_eliminar_todos_estos_elementos():
    print('\n ----- Eliminar todas las apariciones de un dato en la lista -----')
    lista = SinglyLinkedList()
    print('\n  - Con la lista vacia (eliminar "hola")')
    print(f'  | Lista: {lista}\tlongitud: {lista.size}')
    lista.clean_this_data('hola')
    print(f'  | Resultado: {lista}\tlongitud: {lista.size}\n')

    data = ('hola', 1, 2, 'hola', 3, 'hola')
    for i in data:
        lista.append(i)
    print('\n  - Con la lista llena')
    print(f'  | Lista: {lista}\tlongitud: {lista.size}')
    lista.clean_this_data('hola')
    print(f'  | Resultado: {lista}\tlongitud: {lista.size}\n')


def pruebas_encontrar():
    print('\n ---------- Encontrar un elemento ----------')
    lista1 = SinglyLinkedList()
    lista2 = SinglyLinkedList()
    data = (1, 2, 2, 'hola', 'Camila')
    for i in data:
        lista2.append(i)
    print(f'\tLista 1: {lista1}\t\t\tlongitud: {lista1.size}')
    print(f'\tLista 2: {lista2}\tlongitud: {lista2.size}\n')

    print('  | Encontrar un elemento por su indice')
    print('  | * En la lista 2')
    print(f'  | *    Elemento en la posicion 0: {lista2.find(0)}')
    print(f'  | *    Elemento en posicion inexistente 64: {lista2.find(64)}')
    print(f'  | *    Elemento en posicion inexistente -5: {lista2.find(-5)}')
    print('  |')
    print('  | * En la lista 1 vacia')
    print(f'  | *    Elemento en la posicion 0: {lista1.find(0)}')
    print(f'  | *    Elemento en la posicion 5: {lista1.find(5)}\n')

    print('  | Encontrar indice dado un elemento')
    print('  | * En la lista 2')
    print(f'  | *    Posiciones del elemento 3: {lista2.where_is(3)}')
    print(f'  | *    Posiciones del elemento hola: {lista2.where_is("hola")}')
    print(f'  | *    Posiciones del elemento 2: {lista2.where_is(2)}')
    print('  |')
    print('  | * En la lista 1 vacia')
    print(f'  | *    Posiciones del elemento Python: {lista1.where_is("Python")}')
    print(f'  | *    Posiciones del elemento 6: {lista1.where_is(6)}')


    print('\n ---------- Encontrar un penultimo elemento ----------')
    print(f'\tLista 1: {lista1}\t\t\tlongitud: {lista1.size}')
    print(f'\tLista 2: {lista2}\tlongitud: {lista2.size}')
    lista3 = SinglyLinkedList()
    lista3.append('UnicoElemento')
    print(f'\tLista 3: {lista3}\tlongitud: {lista3.size}\n')
    print(f'  | En la lista 1: {lista1.find_penultimate()}')
    print(f'  | En la lista 2: {lista2.find_penultimate()}')
    print(f'  | En la lista 3: {lista3.find_penultimate()}')


    print('\n ----- Encontrar elementos entre dos posiciones -----')
    print(f'\tLista 1: {lista1}\t\t\tlongitud: {lista1.size}')
    print(f'\tLista 2: {lista2}\tlongitud: {lista2.size}')
    print(f'\tLista 3: {lista3}\tlongitud: {lista3.size}\n')
    print(f'  | En lista 1, elementos entre la posicion 1 y 3: {lista1.slice_between(1, 3)}')
    print(f'  | En lista 2, elementos entre la posicion 1 y 4: {lista2.slice_between(1, 4)}')
    print(f'  | En lista 3. elementos entre la posicion 1 y 1: {lista3.slice_between(1, 1)}')


def pruebas_comparar_dos_listas():
    lista1 = SinglyLinkedList()
    lista2 = SinglyLinkedList()
    lista3 = SinglyLinkedList()
    data = (1, 'hola', 2, 'estas?')
    for i in data:
        lista1.append(i)
        lista2.append(i)
    print(f'\tLista 1: {lista1}\t\t\tlongitud: {lista1.size}')
    print(f'\tLista 2: {lista2}\tlongitud: {lista2.size}')
    print(f'\tLista 3: {lista3}\tlongitud: {lista3.size}\n')
    
    lista1.compare(lista2)
    print(f'  | La lista 1 es igual a la 2?: {lista1.compare(lista2)}')
    print(f'  | La lista 2 es igual a la 3?: {lista2.compare(lista3)}')


if __name__ == '__main__':
    # pruebas_agregar()
    # pruebas_eliminar_por_indice()
    # pruebas_eliminar_todos_estos_elementos()
    # pruebas_eliminar_primer_elemento()
    # pruebas_eliminar_ultimo_elemento()
    # pruebas_contar()
    # pruebas_encontrar()
    pruebas_comparar_dos_listas()

