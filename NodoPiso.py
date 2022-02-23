class NodoPiso(): 
    def __init__(self, nombre, filas, columnas, costoVolteo, costoMov):
        self.nombre = nombre
        self.filas = filas
        self.columnas = columnas
        self.costoVolteo = costoVolteo
        self.costoMov = costoMov
        self.siguiente = None
        #self.patrones = ListaPatrones()
        #self.casillas = Matriz() #Matriz