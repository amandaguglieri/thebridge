recintos=[]
def mostrar_recinto():
	if len(recintos) == 0:
		print("Primero tienes que añadir un recinto. ")
	else:
		print("Recintos disponibles: ")
		ini=0
		for rec in recintos:
			print(ini,"-",rec['nombre'])
			ini += 1

def mostrar_asistentes():
	recinto_elegido = elige_recinto()
	indice = 1
	if len(recintos) != 0:
		for i in recintos[recinto_elegido]["asistentes"]:
			print("Asistente ", indice, ":" , i)
			indice+=1

def elige_recinto():
	mostrar_recinto()
	if len(recintos) > 0:
		elige=int(input("Elige el recinto (teclea el numero): "))
		return elige

def anadir_recinto():
	nombre=str(input("Introduce el nombre del recinto: "))
	aforo=int(input("Introduce su aforo máximo: "))
	recinto={'nombre': nombre, "aforo": aforo, "asistentes":[] }
	recintos.append(recinto)

def anadir_asistente():
	while len(recintos) == 0:
		print("Primero tienes que añadir un recinto. ")
		anadir_recinto()
	elige = elige_recinto()
	while elige > len(recintos):
		print("Ese recinto no existe")
		elige = int(input("Elige el recinto (teclea el número): "))
	asistente=str(input("Nombre de asistente: "))
	if len(recintos[elige]["asistentes"]) < recintos[elige]["aforo"]:
		recintos[elige]["asistentes"].append(asistente)
	else:
		print("Aforo maximo alcanzado")

def menu():
	print('''
	[1] Mostrar recinto  \n
	[2] Anadir recinto  \n
	[3] Mostrar asistentes \n
	[4] Añadir un asistente \n
	[5] Salir del programa \n ''')

menu()
escoger = int(input("Escoge un numero: "))

while escoger != 5:
	if escoger == 1:
		mostrar_recinto()
	elif escoger == 2:
		anadir_recinto()
	elif escoger == 3:
		mostrar_asistentes()
	elif escoger == 4:
		anadir_asistente()
	elif escoger == 5:
		print("Hasta luego!!")
		quit()
	else:
		print("Opcion no valida")
	menu()
	escoger=int(input("Escoge un numero: "))
