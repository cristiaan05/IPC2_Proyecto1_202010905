
from xml.dom import minidom

from ListaPisos import ListaPisos

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
    listaP=ListaPisos()
    archivo=str(path)
    mydoc = minidom.parse(archivo) 
    pisos = mydoc.getElementsByTagName('piso') # pisps = mydoc.getElementsByTagName('piso')
    print()
    for x in pisos: # for piso in pisos
        nombre=x.attributes['nombre'].value
        filas=x.getElementsByTagName('R')[0].firstChild.data
        columnas=x.getElementsByTagName('C')[0].firstChild.data
        costoVolteo=x.getElementsByTagName('F')[0].firstChild.data
        costoMov=x.getElementsByTagName('S')[0].firstChild.data
        listaP.insertarPiso(nombre,filas,columnas,costoVolteo,costoMov)
        # listaP.insertarPiso(x.attributes['nombre'].value, x.firstChild.data)
            #cursos = e.getElementsByTagName('curso') #patrones = piso.getElementsByTagName('patron')
            #for c in cursos:
            #    print('-',c.firstChild.data)
        #ListaPisos.mostarPisos()
    print("Exito agregando pisos!!!")
    listaP.mostarPisos()

    



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
    elif opcion=="2":
        print("gg")
        #mostrarPisos()
    elif opcion=="3":
        print("**************Gracias,Vuelva Pronto***********")
    else:
        print("**Error, Escoja una opcion valida**")
        menuPrincipal()
menuPrincipal()
    