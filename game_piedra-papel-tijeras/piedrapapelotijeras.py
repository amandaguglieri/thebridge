#modules to import
import random

#variables
diccionario={"Piedra":0, "Papel":1, "Tijeras":2}
count= 0
machine = 0
human = 0
score_machine = 0
score_human = 0
matches = int(input("Numero de partidas que quieres jugar: "))
nombre = str(input("Tu nombre: "))

#function definitions
def play():
	global machine, human
	machine = random.randint(0,2)
	human = int(input('''
	[0] Piedra \n
	[1] Papel \n
	[2] Tijeras \n
	Introduce tu opción: '''))
	print("-" * 50)
	print("Partida numero", count)
	print("\n\tElegiste", number_to_name(human))
	print("\tLa maquina eligio", number_to_name(machine))

def number_to_name(x):
	for key in diccionario:
		if x == diccionario[key]:
			return key

def print_winner(x):
	print("\tGana", x)
	print("\nPuntuacion general: La maquina (",score_machine,") - ", nombre, "(",score_human,")")
	print("-" * 50)



#game logic
while count < matches:
	count += 1
	play()
	# Con la operación +n %n evitamos valores negativos cuando restamos:
	# 0 - piedra, 1 - Papel, 2 - Tijeras ---de manera que:
	# Si la diferencia es 1, gana el lado izquierdo
	# 	(tijeras-papel+3) %3 = 1 (con o sin +3 %3 ),
	# 	(papel-piedra+3) %3 = (con o sin +3 %3),
	# 	(piedra-tijeras+3) %3 = 1 (CON operación +3 %3)
	# Si la diferencia es 2, gana el lado derecho
	#	(tijeras-piedra+3) %3 = 2
	#	(piedra-papel+3) %3 = 2
	# 	(papel-tijeras+3) % 3 = 2
	# Y si la diferencia es 0, empate
	diferencia = (human-machine +3)%3

	if diferencia == 0:
		score_machine +=1
		score_human += 1
		print("\tEmpate, un punto para", nombre, "y otro para la máquina")
		print("\nPuntuacion general: La maquina(",score_machine,") - ", nombre, "(", score_human, ")")
		print("-" *50)
	elif diferencia == 1:
		score_human += 1
		print_winner(nombre)
	else:
		score_machine += 1
		print_winner("la maquina")


print("PUNTUACION GLOBAL \n", "La maquina:", score_machine, "\n", nombre, ": ", score_human)
