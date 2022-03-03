from turtle import pos
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
    
    def listaAzulejoPatron(self):
        actual = self.inicio
        for i in range(self.dimension):
            print('PosX:', actual.posX,'PosY:',actual.posY,'Color:',actual.color)
            actual = actual.siguiente
    
    def recorrer(self,m,n):
        actual= self.inicio
        graphviz=''''''
        while actual != None:
            for fi in range(1,int(m)):
                grupo=2
                for col in range(1,int(n)):
                    if actual.color=="W":
                        graphviz=graphviz+'''
                        nodo'''+str(fi)+'''_'''+str(col)+'''[label="",fillcolor=white,group='''+str(0)+''']'''
                        grupo=grupo+1
                    elif actual.color=="B":
                        graphviz=graphviz+'''
                        nodo'''+str(fi)+'''_'''+str(col)+'''[label="",fillcolor=black,group='''+str(0)+''']'''
                        grupo=grupo+1
                    actual=actual.siguiente
        return graphviz
    
    
    def compararXCuadrito(self,x):
        if x==0:
            actual=self.inicio
            return actual.posX,actual.posY,actual.color
        elif x>=1:
            y=0
            actual=self.inicio
            while y!=x:
                actual = actual.siguiente
                y+=1
            #print('PosX:', actual.posX,'PosY:',actual.posY,'Color:',actual.color)
            return actual.posX,actual.posY,actual.color
    
    def modificarAzulejo(self,color,posx,posy,contador):
        if contador==0:
            actual = self.inicio
        elif contador>=1:
            y=0
            actual=self.inicio
            while y<contador:
                actual = actual.siguiente
                y+=1
        if actual != None:
            # if actual and actual.posX == posx and actual.posY==posy:
            actualC=actual.siguiente
            if actualC!=None:
                if actualC.color==color:
                    aux=actual.color
                    actualC.color=aux
                    actual.color=color
                    actual=actual.siguiente
                    print("mov")
                    return "M"
                else:   
                    while posx!=actual.posX and actual.posY!=(str(posy+1)):
                        actualD=actual.siguiente
                    if actual.color==color:
                        aux=actual.color
                        actualD.color=aux
                        actual.color=color
                        actual=actual.siguiente
                        
                    else:
                        print("volteo")
                        actual.color=color
                        actual = actual.siguiente
                        return "V"
            else:
                actualC=actual
                if actual.color==color:
                    aux=actual.color
                    actualC.color=aux
                    actual.color=color
                    actual=actual.siguiente
                    print("mov")
                    return "M"
                else:
                    while posx!=actual.posX and actual.posY!=(str(posy+1)):
                        actualD=actual.siguiente
                    if actual.color==color:
                        aux=actual.color
                        actualD.color=aux
                        actual.color=color
                        actual=actual.siguiente
                    else:
                        print("volteo")
                        actual.color=color
                        actual = actual.siguiente
                        return "V"
    
            
    # def buscarAxulejoPatron(self,nombrePiso):
    #     actual = self.inicio
    #     while actual != None:
    #         if actual and actual.nombre==nombrePiso:
    #             return actual.patrones
    #             print("Nombre",actual.terreno.nombre,"Dimension:",actual.terreno.filas,", ",actual.terreno.columnas,"Posicion Inical:",actual.terreno.xPosInicio,", ",actual.terreno.yPosInicio,"Posicion Final: ",actual.terreno.xPosFinal,", ",actual.terreno.yPosFinal)
    #             # print(f"Carne {actual.estudiante.carne} Nombre: {actual.estudiante.nombre} Correo{actual.estudiante.carne} Professión: {actual.estudiante.carrera}")
    #         actual = actual.siguiente