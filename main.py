
from xml.dom import minidom
from ListaAzulejo import ListaAzulejo
from ListaPatron import ListaPatron

from ListaPisos import ListaPisos
from NodoAzulejo import NodoAzulejo
from NodoPatron import NodoPatron
from Grafica import generarGraphviz

def cargarArchivo():
    global path
    path = input("Ingrese la ruta del archivo: ")
    try:
        file = open(path)
        global text
        parsear=file.read()
        text = parsear.lower()
    except:
        print("Ruta invalida")

def procesarArchivo():
    global pisos
    global listaP
    global filas,columnas
    listaP=ListaPisos()
    listaPatrones=ListaPatron()
    archivo=str(path)
    mydoc = minidom.parse(archivo) 
    pisos = mydoc.getElementsByTagName('piso') # pisps = mydoc.getElementsByTagName('piso')
    # print()
    for x in pisos: # for piso in pisos
        global nombre
        nombre=x.attributes['nombre'].value
        filas=x.getElementsByTagName('R')[0].firstChild.data
        columnas=x.getElementsByTagName('C')[0].firstChild.data
        costoVolteo=x.getElementsByTagName('F')[0].firstChild.data
        costoMov=x.getElementsByTagName('S')[0].firstChild.data
        nuevoPiso=listaP.insertarPiso(nombre,filas,columnas,costoVolteo,costoMov)
        patrones = x.getElementsByTagName('patron')
        
        for item in patrones:
            nuevoPatronPiso=item.attributes['codigo'].value
            piso=nuevoPiso.patrones.insertarPatron(nuevoPatronPiso)
            azulejos=item.firstChild.data.replace('\n','')
            azulejos=azulejos.replace(' ','')
            # print('****************','Patron:',nuevoPatronPiso,'Piso:',nombre)
            contadoA=0
            listaA=ListaAzulejo()
            for c in range(int(filas)):
                for d in range(int(columnas)):
                    # nuevoAzulejo=NodoAzulejo(c+1,d+1,azulejos[contadoA])
                    # az=listaA.insertarAzulejoPatron(c+1,d+1,azulejos[contadoA])
                    piso.listaAzulejos.insertarAzulejoPatron(c+1,d+1,azulejos[contadoA])
                    contadoA+=1
                    # print(nuevoAzulejo.posX,nuevoAzulejo.posY,nuevoAzulejo.color)
            # print(azulejos)

            #NodoPatron.listaPatrones.insertarPatron(nuevoPatronPiso)
            #nuevoPiso.patrones.insertarPatrones(nuevoPatronPiso)
            #print(item.attributes['codigo'].value)
        # listaP.insertarPiso(x.attributes['nombre'].value, x.firstChild.data)
            #cursos = e.getElementsByTagName('curso') #patrones = piso.getElementsByTagName('patron')
            #for c in cursos:
            #    print('-',c.firstChild.data)
        #ListaPisos.mostarPisos()
    print("\n")
    print("Exito agregando pisos!!!")
    #listaP.mostarPisos()

    

def mostrarPisos():
    try:
        global listaP,p,opcionPiso,s
        print('*************PISOS CARGADOS*********************')
        # listaP.mostarNombrePisos()
        s=listaP.mostarNombrePisos()
        print("*** Ingrese "+str(s+1)+" Para Volver al Menu Anterior")
        opcionPiso=input("Ingrese el nombre del piso que desea ver: ")
        if opcionPiso==str(s+1):
            menuPrincipal()
        else: 
            p=listaP.buscarPiso(str(opcionPiso))
            if p==None:
                print("\n")
                print("El piso que selecciono no existe, por favor intente de nuevo")
                mostrarPisos()
            elif p!=None:
                menuXPiso(p)
    except NameError:
        print("Ocurrio un error, cargue un archivo nuevo e intentelo de nuevo!")
        menuPrincipal()
            #mostrarPisos()
            # mostrarPisos()
def menuXPiso(p):
    global opcionPiso
    print('\t','---------MENU PISO '+opcionPiso+'--------')
    print('\t','1----Graficar Piso')
    print('\t','2----Cambiar Por Un Nuevo Patron')
    print('\t','3----Volver a Menu Anterior')
    oP=input("Ingrese la opción que desea: ")
    if oP=="1":
        cod=p[0].getPatronDefecto()
        graficarPiso(cod)
    elif oP=="2":
        menuCambiarPatron()
    elif oP=="3":
        mostrarPisos()
    else:
        print("Opción inválida, intentelo de nuevo !")             

# def patronesPisoS():
#     global p,opcionPiso,a
#     print('\t','------PATRONES DEL PISO: '+opcionPiso+'------')
#     p[0].mostrarNombrePatron()
#     print('\t','\t','***  Presione V para volver al menu anterior')
#     opcion=input('\t'+"Ingrese el nombre del patron que desea: ")
#     if opcion.lower()=="v" or opcion.lower()=="volver":
#         mostrarPisos()
#     else:
#         mostrarMenuPatrones(opcion)
        # a=p[0].buscarPatron(opcion)
        

# def mostrarMenuPatrones(codigo):
#         global p,a,opcionPiso
#     # print('\t','----Menú Patron--',codigo+'---')
#     # print('\t','1----Mostrar Patron')
#     # print('\t','2----Cambiar Por Un Nuevo Patron')
#     # print('\t','3----Volver a Menu Anterior')
#     # opcion=input("---Ingresa la Opcion que desea: ")
#     # if opcion=="1":
#         # p[0].buscarPatron(codigo).mostrarAzulejosPatron()
#         filasP=p[1]
#         columnasP=p[2]
#         generarGraphviz(p[0].buscarPatron(codigo),opcionPiso,filasP,columnasP)
#         # patronSelect=listaPa.buscarPatron(codigo)
#         # patronSelect.mostrarAzulejosPatron()
#         # mostrarMenuPatrones(codigo)
#         menuXPiso(p)
        
    # elif opcion=="2":
    #     print("Instrucciones")
    # elif opcion=="3":
    #     patronesPisoS()
    # else:
    #     print("Opcion no valida por favor intente de nuevo")
    #     mostrarMenuPatrones()
def menuCambiarPatron():
    global p,opcionPiso,a
    print('\t','------PATRONES DEL PISO: '+opcionPiso+'------')
    large=p[0].mostrarNombrePatron()
    print('\t','\t',str(large+1)+'---Volver al menu anterior')
    opcion=input('\t'+"Ingrese el codigo del nuevo patron: ")
    if opcion==str(large+1):
        menuXPiso(p)
    else:
        patronNuevo=p[0].buscarPatron(opcion)
        if patronNuevo!=None:
            patronDefecto=p[0].getPatronDefecto()
            cambiarPatron(patronDefecto,opcion)
        else:
            print("El patron no existe intentelo de nuevo")
            menuCambiarPatron()
            
        

def graficarPiso(codigo):
    global p,a,opcionPiso
    filasP=p[1]
    columnasP=p[2]
    generarGraphviz(p[0].buscarPatron(codigo),opcionPiso,filasP,columnasP)
    menuXPiso(p)
    
def cambiarPatron(codPatronDefecto,codPatronNuevo):
    global p,Total,instrucciones
    patronDefecto=p[0].buscarPatron(codPatronDefecto)
    patronN=p[0].buscarPatron(codPatronNuevo)
    filas=p[1]
    columnas=p[2]
    costoM=p[3]
    costoV=p[4]
    Total=0
    # for x in filas:
    #     patronN=p[0].buscarPatron(codPatronNuevo)
    # patronDefecto.listaAzulejoPatron()
    # print("--------------------------------------")
    # patronN.listaAzulejoPatron()
    contador=0
    aux=0
    instrucciones=""
    for x in range(int(filas)):
        for y in range(int(columnas)):
            # print("recorrido--",y)
            X=patronDefecto.compararXCuadrito(contador)
            Y=patronN.compararXCuadrito(contador)
            # print(X[2]+"----"+Y[2])
            if Y[2]==X[2]:
                print("")
                # patronDefecto.modificarAzulejo(aux,X[0],X[1])
            elif X[2]!=Y[2]:
                costo=patronDefecto.modificarAzulejo(Y[2],X[0],X[1],contador,columnas)
                if costo[0]=="M":
                    # print(costo[1])
                    instrucciones=instrucciones+"Se intercambio la casilla en la posicion "+str(X[0])+"_"+str(X[1])+" con la casilla "+str(costo[1])+"_"+str(costo[2])+"* Costo: Q "+costoM+"\n"
                    Total+=int(costoM)
                elif costo[0]=="V":
                    instrucciones=instrucciones+"Se Volteo el color de la casilla en la posicion "+str(X[0])+"_"+str(X[1])+"* Costo: Q "+costoV+"\n"
                    Total+=int(costoV)
                aux+=1
                if aux>=(int(filas)*int(columnas)):
                    break
            contador+=1
            if contador>=(int(filas)*int(columnas)):
                break
        if contador>=(int(filas)*int(columnas)):
            break
    Instrucciones()
    # print("----------------PATRON CAMBIADO------------")
    # patronDefecto.listaAzulejoPatron()        
    # print("--azulejos distintos",aux)
    
def Instrucciones():
        global instrucciones,Total
        print("¿Como desea ver las instrucciones?")
        print("1---En consola")
        print("2---Un archivo HTML")
        print("3---No deseo verlas, volver al menu anterior")
        opcion=input("Ingrese la opcion: ")
        if opcion=="1":
            print("----------------INSTRUCCIONES------------")
            print(instrucciones)
            print("---Costo Operacion---",Total)
                # comparacion=patronDefecto.compararXCuadrito()
            menuXPiso(p)
        elif opcion=="2":
            instruccionesHTML()
        elif opcion=="3":
            menuCambiarPatron()
        else:
            print("Error, intentelo de nuevo")
            Instrucciones()


def instruccionesHTML():
    global instrucciones,Total
    try:
        print("Su reporte fue generado, verificar".center(50, "-"))
        file = open("Reporte.html", "w")
        imprimir = f"""
                <!DOCTYPE html>
                <html lang="en">
                <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <link rel="stylesheet" href="main.css" type="text/css" />
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">
                <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
                <title>INSTRUCCIONES CAMBIO DE PATRON</title>
                </head>
                <body>
                    <h2 id="Titulosecundario" align="center">Cristian Fernando Hernandez Tello 202010905</h2>
                    <div class="titulo">
                       <li class="curso">Instrucciones Cambio de Patron</li>
                    </div>
                    <div class="container">
                    <div class="table table-striped centered">
                        <table class="tabla centered">
                            <tr>
                                <th>Instruccion</th>
                                <th>Costo</th>
                            </tr>
                """
        # Tabla Alumnos asignados
        file.write(imprimir)
        instru=instrucciones.split('\n')
        # i=""
        # c=""
        # for x in range(len(instru)-1):
        #     p=instru[x].split('*')
        #     i=i+p[0]
        #     c=c+p[1]
        #     print("--",instru[x])
        
        for x in range(len(instru)-1):
            p=instru[x].split('*')
            fila = f"""
                <tr>
                    <td>{p[0]}</td>
                    <td>{p[1]}</td>
                </tr>
                    """
            valor = fila
            file.write(valor)
        t=f"""
            <tr>
                <td>TOTAL</td>
                <td>Q.{Total}</td>
            </tr>
        """
        file.write(t)
        file.close()
        Instrucciones()
    except:
        print(f"Algo malo paso".center(50, "!"))
    
        
    
def menuPrincipal():
    print("******************MENÚ*********PRINCIPAL****************")
    print("**  1--Cargar Archivo")
    print("**  2--Mostrar Pisos Cargados")
    print("**  3--Salir")
    print("********************************************************")
    opcion=input("Ingrese la opcion: ")
    print("\n")
    if opcion =="1":
        cargarArchivo()
        procesarArchivo()
        menuPrincipal()
    elif opcion=="2":
        mostrarPisos()
    elif opcion=="3":
        print("**************Gracias,Vuelva Pronto***********")
        exit()
    else:
        print("**Error, Escoja una opcion valida**")
        menuPrincipal()
        
if __name__ == '__main__':        
    menuPrincipal()
    