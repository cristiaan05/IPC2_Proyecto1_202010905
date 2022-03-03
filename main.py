
from importlib.metadata import FileHash
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
    global p
    patronDefecto=p[0].buscarPatron(codPatronDefecto)
    patronN=p[0].buscarPatron(codPatronNuevo)
    filas=p[1]
    columnas=p[2]
    costoM=p[3]
    costoV=p[4]
    Total=0
    # for x in filas:
    #     patronN=p[0].buscarPatron(codPatronNuevo)
    patronDefecto.listaAzulejoPatron()
    print("--------------------------------------")
    patronN.listaAzulejoPatron()
    contador=0
    aux=0
    for x in range(int(filas)):
        for y in range(int(columnas)):
            print("recorrido--",y)
            X=patronDefecto.compararXCuadrito(contador)
            Y=patronN.compararXCuadrito(contador)
            print(X[2]+"----"+Y[2])
            if Y[2]==X[2]:
                print("")
                # patronDefecto.modificarAzulejo(aux,X[0],X[1])
            elif X[2]!=Y[2]:
                costo=patronDefecto.modificarAzulejo(Y[2],X[0],X[1],contador)
                if costo=="M":
                    Total+=int(costoM)
                elif costo=="V":
                    Total+=int(costoV)
                aux+=1
                if aux>=(int(filas)*int(columnas)):
                    break
            contador+=1
            if contador>=(int(filas)*int(columnas)):
                break
        if contador>=(int(filas)*int(columnas)):
            break
    print("----------------PATRON CAMBIADO------------")
    patronDefecto.listaAzulejoPatron()        
    print("--azulejos distintos",aux)
    print("---Costo Operacion---",Total)           
        # comparacion=patronDefecto.compararXCuadrito()
    menuXPiso(p)
        
    
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
    