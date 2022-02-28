from NodoAzulejo import NodoAzulejo

class ListaAzulejo():
    def __init__(self):
        self.inicio=None
        self.fin=None
        self.dimension=0
    
    def insertarAzulejoPatron(self,posX,posY,color):
        nuevoAzulejo=NodoAzulejo(posX,posY,color)
        self.dimension+=1
        if self.inicio is None:
            self.inicio=nuevoAzulejo
            self.fin=nuevoAzulejo
        else:
            # actual=self.inicio
            # while actual.siguiente is not None:
            #     actual=actual.siguiente
            # actual.siguiente=nuevoPiso
            
            self.fin.siguiente=nuevoAzulejo
            nuevoAzulejo.anterior=self.fin   
            self.fin=nuevoAzulejo
            # nuevoPiso.anterior=actual
            # self.fin=nuevoPiso
        return nuevoAzulejo
    
    def mostrarAzulejosPatron(self):
        actual = self.inicio
        for i in range(self.dimension):
            print('PosX:', actual.posX,'PosY:',actual.posY,'Color:',actual.color)
            actual = actual.siguiente