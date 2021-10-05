clear = lambda: os.system('cls')
recintos = [] #para guardar todos los recintos que se creen
nombre = "" # global para saludarte y despedirnos al final del programa

class Recinto:
    def __init__(self, n, a, p):
        self.nombre = n # str
        self.aforo = a #int
        self.asistentes = p #en def anadir_recinto se define como {diccionario}.

def line():
    print('─' * 50)

def saludo():
    global nombre
    nombre=input("¿Cuál es tu nombre? \n")
    line()
    print("¡Te damos la bienvenida,", nombre, "!")
    line()

def anadir_recinto():
    #Añade recintos, comprueba antes si ya existen. Si existe, actualiza sus datos.
    n = input("Nombre del recinto que quieres añadir: ")
    a = int(input("Aforo maximo permitido: "))
    p = {} #Definimos la lista de asistentes como un diccionario
    existerecinto = 0 # 0, no existe recinto || 1, existe el recinto
    for rec in recintos: #recorre los recintos existentes para comprobar si ya existía
        if n == rec.nombre: #comprueba si ya existe el nombre de recinto introducido
            existerecinto += 1
            rec.aforo = a
            #no actualizamos la lista de asistentes porque en el momento de crear,
            #asignamos una lista vacía. De esta manera, no pisamos posibles listas de
            #asistentes cargadas anteriormente.
            line()
            print("Este recinto ya existe. Hemos actualizado sus datos. ")
            line()
    if existerecinto == 0:
        r= Recinto(n, a, p) #creamos un objeto Recinto
        recintos.append(r) #añade el objeto recinto a la lista de recintos[]
        line()
        print("Has creado el recinto",r.nombre,"con aforo de",r.aforo,"personas")
        line()
        return r

def anadir_asistente():
    mostrar_recinto()
    recinto = int(input("Elige el recinto al que añadir asistentes: "))
    while recinto > len(recintos): # si el user teclea un número no incluido
        print("Ese recinto no existe")
        recinto = int(input("Elige el recinto al que añadir asistentes: "))
    # Mientras nuestra lista sea menor que el aforo, pediremos que introduzca asistentes
    index = 1 # Para añadir keys diferentes al diccionario de asistentes
    while len(recintos[recinto].asistentes) < recintos[recinto].aforo:
        line()
        key="Asistente " + str(index)
        print("Recinto seleccionado: ", recintos[recinto].nombre)
        value = str(input("Nombre de asistente: "))
        recintos[recinto].asistentes.update({key:value})
        index += 1
        line()
        seguir = int(input('''¿Qué quieres hacer?\n[1] Añadir otro asistente\n[2] Salir\n '''))
        if seguir == 2:
            line()
            break
    if len(recintos[recinto].asistentes) == recintos[recinto].aforo:
        line()
        print("Aforo máximo alcanzado: ", recintos[recinto].aforo)
        print("Lista de asistentes registrados en", recintos[recinto].nombre)
        for key in recintos[recinto].asistentes:
            print(key, ":", recintos[recinto].asistentes[key])
        line()

def mostrar_recinto():
    #si no hay recinto, le pedimos que dé de alta uno
    if len(recintos) == 0:
        line()
        print("Añade primero algún recinto.")
        line()

    else:
        line()
        print("Recintos registrados: ")
        ini=0
        for rec in recintos:
            print("[",ini,"] ", rec.nombre, "(aforo: ", rec.aforo, ")." )
            ini += 1
        line()


def mostrar_asistentes():
    mostrar_recinto()
    recinto = int(input("Selecciona primero el recinto: "))
    while recinto > len(recintos): # si el user teclea un número no incluido
        print("Ese recinto no existe")
        recinto = int(input("Elige el recinto: "))

    if len(recintos[recinto].asistentes) == 0:
        print("Aún no hay asistentes registrados en el recinto", recintos[recinto].nombre)
        line()
    else:
        print("Lista de asistentes al recinto", recintos[recinto].nombre)
        ini=0
        for key in recintos[recinto].asistentes:
            print("[",ini,"]",key, ":", recintos[recinto].asistentes[key])
            ini += 1
        line()


def borrar_recinto():
    mostrar_recinto()
    recinto = int(input("Elige el recinto que quieres borrar: "))
    while recinto > len(recintos): # si el user teclea un número no incluido
        print("Ese recinto no existe")
        recinto = int(input("Elige el recinto que quieres borrar: "))
    borrado = recintos.pop(recinto)
    print("Recinto ",borrado.nombre, "eliminado con exito. ")
    line()

def borrar_asistente():
    recinto=0
    mostrar_asistentes()
    elige = int(input("Indica que asistente quieres eliminar: "))
    # if len(recintos[recinto].asistentes) == 0:
    #     print("Aún no hay asistentes registrados en el recinto", recintos[recinto].nombre)
    # else:
    ini = 0
    for key in recintos[recinto].asistentes:
        if ini == elige:
            key_to_remove = key
        ini += 1
    borrado = recintos[recinto].asistentes.pop(key_to_remove)
    print("Has borrado con éxito a", key_to_remove, ":", borrado)
    line()


def mostrar_estadisticas():
    #si no hay recinto, le pedimos que dé de alta uno
    while len(recintos) == 0:
        line()
        print("No hay ningún recinto aún.")

    line()
    print("Estadísticas: ")
    line()
    for rec in recintos:
        n = rec.nombre #nombre del recinto
        a = rec.aforo #aforo
        asis = len(rec.asistentes) #numero de asistentes
        pl = a - asis #plazas libres
        print("Recinto",n, "\n Aforo: ", a, "\n Asistentes: ", asis, "\n Plazas libres: ", pl )
        line()
    line()

def menu():
    print(''' Menu de usuario:\n
    [1] Mostrar los recintos que tenemos registrados \n
    [2] Añadir recintos \n
    [3] Mostrar los asistentes de un recinto \n
    [4] Añadir un asistente a un recinto \n
    [5] Borrar un recinto \n
    [6] Borrar un asistente \n
    [7] Mostrar estadisticas \n
    [8] Salir del programa\n''')


# EJECUTANDO EL PROGRAMA
saludo()

exit=0
while exit != 8:
    menu()
    exit=(int(input("Selecciona una opcion (1-5): ")))
    if exit == 1:
        mostrar_recinto()
    elif exit == 2:
        anadir_recinto()
    elif exit == 3:
        mostrar_asistentes()
    elif exit == 4:
        anadir_asistente()
    elif exit == 5:
        borrar_recinto()
    elif exit == 6:
        borrar_asistente()
    elif exit == 7:
        mostrar_estadisticas()
    elif exit == 8:
        print("¡Hasta pronto,", nombre, "!")
        quit()
    else:
        print("Opción no válida.")
        exit=(int(input("Selecciona una opcion (1-5): ")))
