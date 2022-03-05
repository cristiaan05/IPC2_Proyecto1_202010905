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
    
    def modificarAzulejo(self,color,posx,posy,contador,columnas):
        if contador==0:
            actual = self.inicio
        elif contador>=1:
            y=0
            actual=self.inicio
            while y<contador:
                actual = actual.siguiente
                y+=1
        if actual != None:
            # if actual and actual.posX == posx and actual.posY==posy: W     W b
            actualC=actual.siguiente
            actualA=actual
            if actualC!=None:
                if actualC.color==color:
                    for i in range(int(columnas)):
                            if actualA.siguiente != None:
                                actualA = actualA.siguiente
                    if actualA.color==color:
                        aux=actual.color
                        actualA.color=aux
                        actual.color=color
                        actual=actual.siguiente
                        i=""+str(actualA.posX)
                        j=""+str(actualA.posY)
                        print("mov")
                        print("no debio entrar aca")
                        return "M",i,j
                    else: 
                        aux=actual.color
                        actualC.color=aux
                        actual.color=color
                        actual=actual.siguiente
                        # casilla=actualC.color
                        i=""+str(actualC.posX)
                        j=""+str(actualC.posY)
                        print("mov")
                        return "M",i,j
                else:
                    actualAbajo=actual
                    # for i in range(int(columnas)):
                    #     if actualC.siguiente!=None:
                    #         print(actualC.siguiente)
                    for i in range(int(columnas)):
                            if actualAbajo.siguiente != None:
                                actualAbajo = actualAbajo.siguiente
                    if actualAbajo.color==color:
                        aux=actual.color
                        actualAbajo.color=aux
                        actual.color=color
                        actual=actual.siguiente
                        i=""+str(actualAbajo.posX)
                        j=""+str(actualAbajo.posY)
                        print("mov")
                        return "M",i,j
                    else:
                        actualAbajo=actual
                        actualN=actual
                        for i in range(int(columnas)):
                            if actualAbajo.siguiente != None:
                                actualAbajo = actualAbajo.siguiente
                        # print("------------"+actualAbajo.color)
                        # actual=actualN
                        # print("abajo",actualAbajo.posX,actualAbajo.posY)
                        # print("POSICION",actual.posX,actual.posY)
                        if actualAbajo.color==color:
                            aux=actual.color
                            actualAbajo.color=aux
                            actual.color=color
                            actual=actual.siguiente
                            i=""+str(actualAbajo.posX)
                            j=""+str(actualAbajo.posY)
                            print("mov")
                            return "M",i,j
                        else:    
                            print("volteo")
                            actual.color=color
                            i=""+str(actual.posX)
                            j=""+str(actual.posY)
                            actual = actual.siguiente
                            return "V",i,j
            else:
                actualC=actual
                if actual.color==color:
                    aux=actual.color
                    actualC.color=aux
                    actual.color=color
                    actual=actual.siguiente
                    i=""+str(actualC.posX)
                    j=""+str(actualC.posY)
                    print("mov")
                    return "M",i,j
                else:
                    actualAbajo=actual
                    for i in range(int(columnas)):
                            if actualAbajo.siguiente != None:
                                actualAbajo = actualAbajo.siguiente
                    if actual.color==color:
                        aux=actual.color
                        actualAbajo.color=aux
                        actual.color=color
                        actual=actual.siguiente
                        i=""+str(actualAbajo.posX)
                        j=""+str(actualAbajo.posY)
                        print("mov")
                        return "M",i,j
                    else:
                        actual.color=color
                        i=""+str(actual.posX)
                        j=""+str(actual.posY)
                        actual = actual.siguiente
                        print("volteo")
                        return "V",i,j