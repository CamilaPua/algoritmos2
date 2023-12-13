from ciudad import Ciudad
from abb_ciudades import ArbolBinarioBusqueda

madrid = Ciudad('Madrid', 1234, 3300000)
barcelona = Ciudad('Barcelona', 1234, 1600000)
valencia = Ciudad('Valencia', 1234, 790000)
sevilla = Ciudad('Sevilla', 1234, 690000)
zaragoza = Ciudad('Zaragoza', 1234, 650000)
malaga = Ciudad('Málaga', 1234, 590000)
murcia = Ciudad('Murcia', 1234, 440000)
palma = Ciudad('Palma', 1234, 400000)
alicante = Ciudad('Alicante', 1234, 340000)
valladolid = Ciudad('Valladolid', 1234, 330000)

# Crear una instancia del árbol binario de búsqueda
arbol = ArbolBinarioBusqueda()

# Insertar las ciudades en el árbol
arbol.insertar(malaga)
arbol.insertar(valladolid)
arbol.insertar(sevilla)
arbol.insertar(zaragoza)
arbol.insertar(murcia)
arbol.insertar(alicante)
arbol.insertar(valencia)
arbol.insertar(madrid)
arbol.insertar(barcelona)
arbol.insertar(palma)

print(arbol.verArbol())
print('Zona de influencia de Sevilla:', arbol.zona_influencia(sevilla))
print('Mayor influente:', arbol.mayor_influente())
print('Ciudad con mayor población:', arbol.mayor_poblacion())
print('Promedio de población de las ciudades:', arbol.promedio_poblacion_ciudades())
print('Ciudades con población mayor al promedio:', arbol.ciudades_poblacion_mayor_promedio())
