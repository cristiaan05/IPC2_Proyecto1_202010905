
from importlib.metadata import FileHash
from xml.dom import minidom
from ListaAzulejo import ListaAzulejo
from ListaPatron import ListaPatron

from ListaPisos import ListaPisos
from NodoAzulejo import NodoAzulejo
from NodoPatron import NodoPatron

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
    print("Exito agregando pisos!!!")
    #listaP.mostarPisos()

    

def mostrarPatronesPiso():
    global listaP
    print('*************PISOS CARGADOS*********************')
    # listaP.mostarNombrePisos()
    s=listaP.mostarNombrePisos()
    opcion=input("Ingrese el nombre del piso que desea ver: ")
    p=listaP.buscarPiso(str(opcion))
    if p==None:
        mostrarPatronesPiso()
    elif p!=None:
        print('\t','------PATRONES DEL PISO:',opcion+'------')
        p.mostrarNombrePatron()
        # mostrarPisos()

def mostrarMenuPatrones(codigo):
    print('\t','1----Mostrar Patron-----')
    print('\t','1----Mostrar Patron-----')
def menuPrincipal():
    print("******************MENÚ*********PRINCIPAL****************")
    print("**  1--Cargar Archivo")
    print("**  2--Mostrar Pisos Cargados")
    print("**  3--Salir")
    print("********************************************************")
    print("Ingrese la opcion: ")
    opcion=input()
    if opcion =="1":
        cargarArchivo()
        procesarArchivo()
        menuPrincipal()
    elif opcion=="2":
        mostrarPatronesPiso()
        
    elif opcion=="3":
        print("**************Gracias,Vuelva Pronto***********")
        exit()
    else:
        print("**Error, Escoja una opcion valida**")
        menuPrincipal()
        
if __name__ == '__main__':        
    menuPrincipal()
    