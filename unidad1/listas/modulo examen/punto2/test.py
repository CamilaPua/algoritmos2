from SinglyLinkedList import SinglyLinkedList

enunciado = """Diseñe un método que tome dos listas y elimine de ambas,
sus elementos en común. La eliminación debe hacerse sobre las listas
existentes.
"""
print(enunciado)

data = (1, 2, 3, 5)

lista1 = SinglyLinkedList()
data1 = ('hola', 'si')
for i in data:
    lista1.append(i)
for i in data1:
    lista1.append(i)

lista2 = SinglyLinkedList()
data2 = (5, 'si', 6, 7)
for i in data2:
    lista2.append(i)
for i in data:
    lista2.append(i)
print(f'\tLista 1: {lista1}\tlongitud: {lista1.size}')
print(f'\tLista 2: {lista2}\tlongitud: {lista2.size}')

print('\nEliminar elementos en comun')
lista1.remove_common(lista2)
print(f'\tLista 1: {lista1}\tlongitud: {lista1.size}')
print(f'\tLista 2: {lista2}\tlongitud: {lista2.size}')
