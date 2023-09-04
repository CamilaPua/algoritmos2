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

def pruebas_metodos_eliminar():
    lista1 = SinglyLinkedList()
    lista1.append(0)
    lista1.append(1)
    lista1.append(2)
    print('\n ----- Metodos eliminar -----')
    print(f'\tLista 1: {lista1}\tlongitud: {lista1.size}\n')

    print('  | Intentemos eliminar una posicion que no existe (159)')
    lista1.delete_index(159)
    print(f'  | Lista 1: {lista1}\tlongitud: {lista1.size}\n')

    print('  | Nada paso, intentemos con un decimal (1.59)')
    lista1.delete_index(1.59)
    print(f'  | Lista 1: {lista1}\tlongitud: {lista1.size}\n')

    print('  | Con un numero negativo (-2)')
    lista1.delete_index(-2)
    print(f'  | Lista 1: {lista1}\tlongitud: {lista1.size}\n')

    print('  | Eliminamos la segunda posicion por su indice (los indices van desde 0)')
    lista1.delete_index(1)
    print(f'  | Lista 1: {lista1}\tlongitud: {lista1.size}\n')

    print('  * Eliminamos el primer elemento')
    lista1.delete_first()
    print(f'  * Lista 1: {lista1}\tlongitud: {lista1.size}\n')

    print('  - Eliminamos el ultimo elemento')
    lista1.delete_last()
    print(f'  - Lista 1: {lista1}\tlongitud: {lista1.size}\n')
    
    print('  | Intentamos eliminar ahora que esta vacia (eliminar primero)')
    lista1.delete_first()
    print(f'  | Lista 1: {lista1}\tlongitud: {lista1.size}\n')
    
    print('  | No pasa nada, se manejaron las excepciones (eliminar ultimo)')
    lista1.delete_last()
    print(f'  | Lista 1: {lista1}\tlongitud: {lista1.size}\n')

    print('  | En los tres metodos (eliminar por indice)')
    lista1.delete_index(5)
    print(f'  | Lista 1: {lista1}\tlongitud: {lista1.size}\n')

def pruebas_contar():
    print('\n ---------- Contar un elemento ----------')
    lista1 = SinglyLinkedList()
    data = (1, 2, 3, 'hola', 'hola')
    for i in data:
        lista1.append(i)
    print(f'\tLista 1: {lista1}\tlongitud: {lista1.size}\n')

    print(f'  | Ocurrencias de "hola": {lista1.count("hola")}')
    print(f'  | Ocurrencias de "Camila": {lista1.count("Camila")}\n')

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


if __name__ == '__main__':
    # pruebas_agregar()
    # pruebas_metodos_eliminar()
    # pruebas_contar()
    pruebas_encontrar()
