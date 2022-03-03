from os import startfile, system


def generarGraphviz(posiciones,nombre,m,n):
        # print("m",m,n)
        m=int(m)+1
        n=int(n)+1
        x="hola"
        
        # print(posiciones.mostrarAzulejosPatron())
        # print("hola")
        
        graphviz='''
        digraph L{
            node[shape=box fillcolor="#FFEDBB" style=filled]
            nodesep=0.02;
            ranksep=0.02;
            subgraph cluster_p{
                label ="Nombre Piso: '''+nombre+'"'
        graphviz=graphviz+'''
                bgcolor="#398D9C"
                edge[dir="none"]//permite poner flechas para ambos lados
                '''            
        
        g=posiciones.recorrer(m,n)
        graphviz=graphviz+g
        for fi in range(1,int(m)):
            grupo=2
            for col in range(1,int(n)):
                if int(grupo)<int(n):  
                    graphviz=graphviz+'''
                        nodo'''+str(fi)+'''_'''+str(col)+'''->nodo'''+str(fi)+'''_'''+str(grupo)+'''[dir=none color="#398D9C"]
                    '''
                    grupo=grupo+1
        for fi in range(1,int(m)):
            graphviz=graphviz+'''
                {rank=same;'''
            grupo=2
            for col in range(1,int(n)):
                if int(col)<int(n-1): 
                    graphviz=graphviz+'''
                    nodo'''+str(fi)+'''_'''+str(col)+''','''
                    grupo=grupo+1
                else:
                    graphviz=graphviz+'''
                    nodo'''+str(fi)+'''_'''+str(col)
            graphviz=graphviz+'''
                }    
            '''
        
        ## AQUI ENLAZAMOS LAS COLUMNAS
        for col in range(1,int(n)):
            fila=2
            for fi in range(1,int(m-1)):
                graphviz=graphviz+'''
                    nodo'''+str(fi)+'''_'''+str(col)+'''->nodo'''+str(fila)+'''_'''+str(col)+'''[dir=none color="#398D9C"];
                '''
                fila=fila+1
            
        # for col in range(1,int(n)):
        #     # grupo=2
        #     for fi in range(1,int(m)):
        #         grupo=2
        #         if int(grupo)<int(m-1):  
        #             graphviz=graphviz+'''
        #                 nodo'''+str(fi)+'''_'''+str(col)+'''->nodo'''+str(grupo)+'''_'''+str(col)+'''[dir=none color="#398D9C"]
        #             '''
        #             grupo=grupo+1
        
               
                
                
                
        graphviz=graphviz+'''
        
    }
}
            '''
    
        miarchivo=open('graphviz.dot','w')
        miarchivo.write(graphviz)
        miarchivo.close()
        
        system('dot -Tpng graphviz.dot -o graphviz.png')
        system('cd ./graphviz.png')
        startfile('graphviz.png')