class _IteradorListaEnlazada(object):
    " Iterador para la clase ListaEnlazada "
    def __init__(self, prim):
        """ Constructor del iterador.
            prim es el primer elemento de la lista. """
        self.actual = prim

    def next(self):
        """ Devuelve uno a uno los elementos de la lista. """
        if self.actual == None:
            raise StopIteration("No hay más elementos en la lista")

        # Guarda el dato
        dato = self.actual.dato
        # Avanza en la lista
        self.actual = self.actual.prox
        # Devuelve el dato
        return dato

    def __iter__(self):
        " Devuelve el iterador de la lista. "
        return _IteradorListaEnlazada(self.prim)

    def iterReverse(self):
        iter = _IteradorListaEnlazada(self.prim)
        iter.pr

def main():


if __name__ == "__main__":
    main()

