enunciado = """Diseñe un método que adicione un dato ingresado por el
usuario, teniendo en cuenta que, si ya existe el dato en la lista, se
adiciona de último en la lista, si no existe, se adiciona de primero en
la lista."""
print(enunciado)

from SinglyLinkedList import SinglyLinkedList

print('----- Pruebas -----')
lista1 = SinglyLinkedList()
data = (1, 2, 3, 'hola', 'Python')
for i in data:
    lista1.append(i)

lista2 = SinglyLinkedList()
data2 = (4, 5, 6, 'chao', 'javascript')
for i in data2:
    lista2.append(i)

print(f'Lista 1: {lista1}\tlongitud: {lista1.size}')
print(f'Lista 2: {lista2}\tlongitud: {lista2.size}')

print('Supongamos que el usuario quiere ingresar "Python" en la lista 1')
lista1.append_or_preppend('Python')
print('Como ya existe lo agrega al final')
print(f'Lista 1: {lista1}\tlongitud: {lista1.size}\n')

print('Ahora el usuario quiere ingresar "Python" en la lista 2')
print(f'Lista 2: {lista2}\tlongitud: {lista2.size}')
lista2.append_or_preppend('Python')
print('Como no existe lo agrega al inicio')
print(f'Lista 2: {lista2}\tlongitud: {lista2.size}')
