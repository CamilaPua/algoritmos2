#Clase Nodo Simple
class NodoSimple:
    #Constructor
    def __init__(self, dato_usuario) -> None:
        self.info = dato_usuario
        self.siguiente  = None
    #Str
    def __str__(self) -> str:
        return str(self.info)

#Clase Lista Simple
class ListaSimple:
    def __init__(self) -> None:
        self.nodoInicial = None
        self.longitud = 0    #Atributo de longitud para facilitar excepciones

    #Adicionar al inicio
    def adicionarAlInicio(self, dato_nuevo):
        nodoNuevo = NodoSimple(dato_nuevo)
        if self.nodoInicial == None: #Si la lista esta vacia
            self.nodoInicial = nodoNuevo #Se hace el primer nodo
            self.longitud += 1 # la longitud de la lista aumenta
        else:
            #La lista ya tiene al menos un nodo
            nodoNuevo.siguiente = self.nodoInicial
            self.nodoInicial = nodoNuevo #Actualizar el nodo inicial
            self.longitud += 1

    #Recorrido
    def __str__(self) -> str:
        recorrido = ''
        nodoActual = self.nodoInicial
        while nodoActual != None: #Mientras el nodo exista (lista sin acabar)
            recorrido += str(nodoActual.info) + ' '
            nodoActual = nodoActual.siguiente
        return recorrido


    def indicarPenultimoElemento(self):
        """
        Indica el penultimo elemento de la lista, si existe.
        """
        if self.longitud <= 1:  # Si la lista esta vacia o solo tiene un nodo
            return 'No existe penultimo elemento'
        else:
            nodoActual   = self.nodoInicial
            nodoAnterior = self.nodoInicial
            while nodoActual.siguiente:     # Mientras exista un siguiente nodo se itera la lista
                nodoAnterior    = nodoActual
                nodoActual      = nodoActual.siguiente
            return nodoAnterior     # devuelve nodo anterior al ultimo nodo de la lista) 


    def elementosEntrePosiciones(self, posicionInicial, posicionFinal):
        """
        Indica los elementos entre dos posiciones (inicial y final, siendo inicial < final) de la lista.
        """
        try:
            assert self.longitud > 0, 'La lista esta vacia'
            assert posicionFinal <= self.longitud, 'Indice final fuera de rango.'
            assert posicionInicial >= 0, 'Indice inicial fuera de rango.'
            assert posicionInicial < posicionFinal, 'La posicion inicial debe ser menor que la final.'
            assert posicionFinal >= posicionInicial + 2, 'Debe haber al menos una posicion entre la inicial y la final.'
        except AssertionError as error:
            return error
        
        nodoActual = self.nodoInicial
        posicionActual = 0
        elementosIntermedios = ListaSimple()
        while nodoActual:
            if posicionActual > posicionInicial and posicionActual < posicionFinal:
                elementosIntermedios.adicionarAlInicio(nodoActual)
            nodoActual = nodoActual.siguiente
            posicionActual += 1

        return elementosIntermedios


    def eliminarNodo(self, nodoAnterior: NodoSimple, nodoActual: NodoSimple):
        if nodoActual == self.nodoInicial:
            self.nodoInicial = nodoActual.siguiente
            self.longitud -= 1
        else:
            nodoAnterior.siguiente = nodoActual.siguiente
            self.longitud -= 1
        return nodoActual


    def eliminarCadaElemento(self, elemento: NodoSimple):
        """
        Elimina todas las apariciones de un dato en la lista
        """
        try:
            assert self.longitud > 0, 'La lista esta vacia'
        except AssertionError as error:
            return error

        nodoActual      = self.nodoInicial
        nodoAnterior    = self.nodoInicial

        while nodoActual:
            if nodoActual.info == elemento:
                self.eliminarNodo(nodoAnterior, nodoActual)

            nodoAnterior    = nodoActual
            nodoActual      = nodoActual.siguiente


    def compare(self, otraLista):
        """
        Indica si dos listas son iguales en longitud y contenido (elementos-orden)
        """
        return str(self) == str(otraLista)


    def mover(self, elemento: NodoSimple, posicionFinal):
        """
        Mueve un elemento desde una posición inicial, a una posición final de la lista.
        """
        try:
            assert self.longitud > 0, 'La lista esta vacia'
            assert self.longitud > 2, 'No se puede mover el elemento, solo hay una posicion en la lista'
        except AssertionError as error:
            return error
        
