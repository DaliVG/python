import os

## mayus indica variable global

CARPETA = 'contactos/'
EXTENSION = '.txt'

class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria
        



def app():

    crearDirectorio()

    mostrarMenu()

    preguntar = True

    while preguntar:
        opcion = input('Seleccione una opcion: \r\n')
        opcion = int(opcion)

    ## NO EXISTEN SWIITCH

        if opcion == 1:
            agregar()
            preguntar = False
        elif opcion == 2:
            editar()
            preguntar = False
        elif opcion == 3:
            mostrar()
            preguntar = False
        elif opcion == 4:
            buscar()
            preguntar = False
        elif opcion == 5:
            eliminar()
            preguntar = False
        else:
            print('Opcion no valida.')


def crearDirectorio():
    if not os.path.exists(CARPETA):
        os.makedirs(CARPETA)
    


def mostrarMenu():
    print('Selecciona del menu que desee:')
    print('1) Agregar')
    print('2) Editar')
    print('3) Ver')
    print('4) Buscar')
    print('5) Eliminar')

def agregar():

    print('Datos...')

    nombre = input('Nombre: \r\n')
    telefono = input('Telefono: \r\n')
    categoria = input('Categoria: \r\n')  

    contacto = Contacto(nombre, telefono, categoria)

    ## Si tiene W significa que el archivo se reescribe si tiene el mismo nombre
    existe = os.path.isfile(CARPETA + contacto.nombre + EXTENSION)

    if not existe:

        with open(CARPETA + contacto.nombre + EXTENSION, 'w') as archivo:
            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Teléfono: ' + contacto.telefono + '\r\n')
            archivo.write('Categoria: ' + contacto.categoria + '\r\n')

        print('\r\n Contacto creado correctamente.')
    else:
       print('Contacto existente.') 
       app()

def editar():
    print('Editar...\r\n')
    nombreAnterior = input('Nombre a editar: ')
    existe = existeContacto(nombreAnterior)

    if existe:
        with open(CARPETA + nombreAnterior + EXTENSION, 'w') as archivo:
            
            nombre = input('Nuevo Nombre: \r\n')
            telefono = input('Nuevo Telefono: \r\n')
            categoria = input('Nuevo Categoria: \r\n')    
        
            contacto = Contacto(nombre, telefono, categoria)           
        
            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Teléfono: ' + contacto.telefono + '\r\n')
            archivo.write('Categoria: ' + contacto.categoria + '\r\n')

            os.rename(CARPETA + nombreAnterior + EXTENSION, CARPETA + contacto.nombre + EXTENSION)

            print('\r\n Contacto editado correctamente.')
    else:
        print('Ese no esta rey.')

def mostrar():
    archivos = os.listdir(CARPETA)

    archivosTxt = [i for i in archivos if i.endswith(EXTENSION)]

    for archivo in archivosTxt:
        with open(CARPETA + archivo) as contacto:
            for linea in contacto:
                print(linea.rstrip())

            print('\r\n')

def buscar():
    nombre = input('A quien buscas?\r\n')

    try:
        with open(CARPETA + nombre + EXTENSION) as contacto:
            print('\r\n Info del contacto: \r\n')
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')
    except IOError:
        print('Diablo, ese no ta.')
        print(IOError)
    
    app()

def eliminar():
    print('ELIMINALOOOO')
    nombre = input('A quien quieres quitar del planeta?\r\n')

    try:
        os.remove(CARPETA + nombre + EXTENSION)
        print('Hecho rey.')
    except IOError:
        print('Diablo, ese no ta.')
        print(IOError)
    
    app()

def existeContacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)

app()