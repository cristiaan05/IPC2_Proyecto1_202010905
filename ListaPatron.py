from NodoPatron import NodoPatron


class ListaPatron():
    def __init__(self):
        self.inicio=None
        self.fin=None
        self.dimension=0
    
    def insertarPatron(self,codigo):
        nuevoPatron=NodoPatron(codigo)
        self.dimension+=1
        if self.inicio is None:
            self.inicio=nuevoPatron
            self.fin=nuevoPatron
        else:
            # actual=self.inicio
            # while actual.siguiente is not None:
            #     actual=actual.siguiente
            # actual.siguiente=nuevoPiso
            
            self.fin.siguiente=nuevoPatron
            nuevoPatron.anterior=self.fin   
            self.fin=nuevoPatron
            # nuevoPiso.anterior=actual
            # self.fin=nuevoPiso
        return nuevoPatron
    
    def mostrarPatrones(self):
        actual = self.inicio
        for i in range(self.dimension):
            print('Codigo:', actual.codigo)
            actual.listaAzulejos.mostrarAzulejosPatron()
            actual = actual.siguiente
            
    def mostrarNombrePatron(self):
        actual = self.inicio
        for i in range(self.dimension):
            print('\t','\t','***',i+1,'***  Codigo:', actual.codigo)
            actual = actual.siguiente
        return self.dimension