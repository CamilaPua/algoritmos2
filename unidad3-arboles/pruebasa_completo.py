from arbol_binario import ArbolBinario
# Arbol incompleto
#Creacion de Nodos
raizA = ArbolBinario("A")
nodoB = ArbolBinario("B")
nodoC = ArbolBinario("C")
nodoD = ArbolBinario("D")
nodoE = ArbolBinario("E")
nodo1 = ArbolBinario(1)
nodo2 = ArbolBinario(2)

#Conexion de nodos
raizA.hijo_izquierdo = nodoB
raizA.hijo_derecho = nodoC
nodoB.hijo_izquierdo = nodo1
nodoB.hijo_derecho = nodo2
nodoC.hijo_izquierdo = nodoD
nodoC.hijo_derecho = nodoE

#Visualización
print("Arbol incompleto:\n",raizA.verArbol())
print("Recorridos")
print("PreOrden:",raizA.preOrden())
print("EnOrden:",raizA.enOrden())
print("PosOrden:",raizA.posOrden())
print('Nodos hoja:', raizA.nodos_hoja())
print('Numero de nodos:', raizA.numero_nodos())
print('Altura:', raizA.altura_arbol())
print('Nodos en nivel 2:', raizA.nodos_de_un_nivel(2), '- Cantidad:', raizA.numero_nodos_en_un_nivel(2))
print('¿El arbol es completo?:', raizA.es_completo())
print('Padre de D:', raizA.papaelemento('D'))
print('Nodos en el nivel mas profundo:', raizA.nodos_mas_profundos())
