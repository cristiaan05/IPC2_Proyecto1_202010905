from NodoPiso import NodoPiso
from os import startfile, system
class ListaPisos():
    def __init__(self):
        self.inicio=None
        self.fin=None
        self.dimension=0

    def insertarPiso(self,nombre,filas,columnas,costoVolteo,costoMov):
        nuevoPiso=NodoPiso(nombre,filas,columnas,costoVolteo,costoMov)
        self.dimension+=1
        if self.inicio is None:
            self.inicio=nuevoPiso
            self.fin=nuevoPiso
        else:
            # actual=self.inicio
            # while actual.siguiente is not None:
            #     actual=actual.siguiente
            # actual.siguiente=nuevoPiso
            
            self.fin.siguiente=nuevoPiso
            self.fin=nuevoPiso
            # nuevoPiso.anterior=actual
            # self.fin=nuevoPiso
        return nuevoPiso
    
    def mostarPisos(self):
        actual = self.inicio
        for i in range(self.dimension):
            print('Nombre:', actual.nombre, 'Filas:', actual.filas, 'Columnas: ',actual.columnas
                  ,'Costo Volteo:',actual.costoVolteo,'Costo Mov: ',actual.costoMov,'Patrones: ')
            actual.patrones.mostrarPatrones()
            actual = actual.siguiente
    def mostarNombrePisos(self):
        actual = self.inicio
        for i in range(self.dimension):
            print('***',i+1,'***  Nombre:', actual.nombre)
            actual = actual.siguiente
        return self.dimension
    
    # def recorrer(self,posicion):
    #     actual= self.inicio
    #     while actual != None:
    #         x=1
    #         while x <= int(self.dimension):
    #             if posicion==x:
    #                 print("Nombre: ",actual.nombre)
    #                 # print("Nombre",actual.terreno.nombre,"Dimension:",actual.terreno.filas,", ",actual.terreno.columnas,"Posicion Inical:",actual.terreno.xPosInicio,", ",actual.terreno.yPosInicio,"Posicion Final: ",actual.terreno.xPosFinal,", ",actual.terreno.yPosFinal)
    #         # actual.terreno.posiciones.getPosiciones()
    #         actual=actual.siguiente
    
    def buscarPiso(self,nombrePiso):
        actual = self.inicio
        while actual != None:
            if actual and actual.nombre==nombrePiso:
                return actual.patrones
                print("Nombre",actual.terreno.nombre,"Dimension:",actual.terreno.filas,", ",actual.terreno.columnas,"Posicion Inical:",actual.terreno.xPosInicio,", ",actual.terreno.yPosInicio,"Posicion Final: ",actual.terreno.xPosFinal,", ",actual.terreno.yPosFinal)
                # print(f"Carne {actual.estudiante.carne} Nombre: {actual.estudiante.nombre} Correo{actual.estudiante.carne} Professión: {actual.estudiante.carrera}")
            actual = actual.siguiente
            
    # def getPosiciones(self):
    #     actual=self.inicio
    #     while actual is not None:
    #         print('x: ',actual.x,'y: ',actual.y,'Combustible: ',actual.cantidad)
    #         actual=actual.siguiente
    
    # def generarGraphviz(posiciones,nombre,m,n):
#         print("posiciones",posiciones)
#         m=int(m)+1
#         n=int(n)+1
#         x="hola"
#         graphviz='''
#         digraph L{
#             node[shape=box fillcolor="#FFEDBB" style=filled]
            
#             subgraph cluster_p{
#                 label ="Nombre Terreno: '''+nombre+'"'
#         graphviz=graphviz+'''
#                 bgcolor="#398D9C"
#                 raiz[label="0,0"]
#                 edge[dir="both"]//permite poner flechas para ambos lados
#                 /*AQUI CREAMOS LAS CABECERAS
#                 DE LAS FILAS*/'''
#         for fi in range(1,int(m)):
#             graphviz=graphviz+'''
#                 Fila'''+str(fi)+'''[label="'''+str(fi)+'''",group='''+str(1)+'''];'''
#         auxFi=1
#         for fi in range(1,int(m)):
#             if auxFi<int(m-1): 
#                 graphviz=graphviz+'''
#                 Fila'''+str(auxFi)+'''->Fila'''+str(auxFi+1)+''';
#                 '''
#             auxFi=auxFi+1
#         aux=2
#         for col in range(1,int(n)):
#             graphviz=graphviz+'''
#                 Columna'''+str(col)+'''[label="'''+str(col)+'''",group='''+str(aux)+''',fillcolor=yellow];'''
#             aux=aux+1
#         auxcol=1
#         for col in range(1,int(n)):
#             if auxcol<int(n-1): 
#                 graphviz=graphviz+'''
#                 Columna'''+str(auxcol)+'''->Columna'''+str(auxcol+1)+''';
#                 '''
#             auxcol=auxcol+1
            
#         graphviz=graphviz+'''
#                 /*AQUI ENLAZAMOS LOS NODOS DE LAS FILAS*/
#                 raiz->Fila1;
#                  raiz->Columna1;
                 
#             /*aqui vamos al alinear cada nodo cabecera de las columnas*/
#             {rank=same;raiz;Columna1;'''
#         for col in range(1,int(n)):
#             graphviz=graphviz+'''Columna'''+str(col)+''';
#         '''
#         graphviz=graphviz+'''         
#                 }'''
#        ## /*aqui vamos al alinear cada nodo cabecera de las columnas*/
#         for fi in range(1,int(m)):
#             grupo=2
#             for col in range(1,int(n)):
#                 graphviz=graphviz+'''
#             nodo'''+str(fi)+'''_'''+str(col)+'''[label="a",fillcolor=green,group='''+str(grupo)+''']'''
#                 grupo=grupo+1
                
#         ##/* AHORA ALINEAMOS FILA POR FILA */        
#         for fi in range(1,int(m)):
#             graphviz=graphviz+'''
#                 Fila'''+str(fi)+'''->nodo'''+str(fi)+'''_1;
#             '''
#         ##ALINEAMOS POR FILA CADA NODO
#         for fi in range(1,int(m)):
#             grupo=2
#             for col in range(1,int(n)):
#                 if int(grupo)<int(n):  
#                     graphviz=graphviz+'''
#                         nodo'''+str(fi)+'''_'''+str(col)+'''->nodo'''+str(fi)+'''_'''+str(grupo)+'''
#                     '''
#                     grupo=grupo+1
#         for fi in range(1,int(m)):
#             graphviz=graphviz+'''
#                 {rank=same;Fila'''+str(fi)+''';'''
#             grupo=2
#             for col in range(1,int(n)):
#                 if int(col)<int(n-1): 
#                     graphviz=graphviz+'''
#                     nodo'''+str(fi)+'''_'''+str(col)+''','''
#                     grupo=grupo+1
#                 else:
#                     graphviz=graphviz+'''
#                     nodo'''+str(fi)+'''_'''+str(col)
#             graphviz=graphviz+'''
#                 }    
#             '''
            
#         ##/*AQUI ENLZAMOS LAS COLUMNAS*/
#         for col in range(1,int(n)):
#             graphviz=graphviz+'''
#                 Columna'''+str(col)+'''->nodo1_'''+str(col)+''';
#             '''
        
#         ## AQUI ENLAZAMOS LAS COLUMNAS
#         for col in range(1,int(n)):
#             fila=2
#             for fi in range(1,int(m-1)):
#                 graphviz=graphviz+'''
#                     nodo'''+str(fi)+'''_'''+str(col)+'''->nodo'''+str(fila)+'''_'''+str(col)+''';
#                 '''
#                 fila=fila+1
            
#         # for col in range(1,int(n)):
#         #     # grupo=2
#         #     for fi in range(1,int(m)):
#         #         grupo=2
#         #         if int(grupo)<int(m-1):  
#         #             graphviz=graphviz+'''
#         #                 nodo'''+str(fi)+'''_'''+str(col)+'''->nodo'''+str(grupo)+'''_'''+str(col)+'''
#         #             '''
#         #             grupo=grupo+1
        
               
                
                
                
#         graphviz=graphviz+'''
        
#     }
# }
#             '''
    
        # miarchivo=open('graphviz.dot','w')
        # miarchivo.write(graphviz)
        # miarchivo.close()
        
        # system('dot -Tpng graphviz.dot -o graphviz.png')
        # system('cd ./graphviz.png')
        # startfile('graphviz.png')
     
    
    
    
    # def insertarPosicion(self,x,y,cantidad):
    # nuevo=Posi