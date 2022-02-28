from ListaAzulejo import ListaAzulejo


class NodoPatron():
    def __init__(self, codigo):
        self.codigo = codigo
        self.listaAzulejos = ListaAzulejo()
        self.siguiente=None
        self.anterior=None
        