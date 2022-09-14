# Colores
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'



import random 

import time

# Ejemplo 1
print (YELLOW +"Hola, nos vemos en 2 segundos"+RESET)

time.sleep(2) # Espera 2 segundos antes de continuar.
print (MAGENTA + "Bienvenido a mi trivia sobre computación" + RESET)



# Para implementar puntajes, crearemos una nueva variable llamada "puntaje", la que inicializamos en 0.
puntaje = random.randint(0, 10)


iniciar_trivia = True  # Iniciamos la variable en True
intentos = 0  # variable que almacenará el número de veces que el usuario intenta nuestra trivia.


while iniciar_trivia == True: #  Mientras iniciar_trivia sea True, repite:
  intentos += 1
  puntaje = 0

  print(BLUE+"\nIntento número:"+RESET, intentos)
  input(GREEN+"Presiona Enter para continuar"+RESET)

  print ("Pondremos a prueba tus conocimientos")
  print (CYAN+"Tienes", puntaje, "puntos"+RESET)

  nombre = input ("Ingresa tu nombre: ")
  print (GREEN+"\nHola",nombre, "responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n"+RESET)

  
  
 # Pregunta 1
  print (YELLOW +"1) ¿Quién fue el creador de windows?")
  print ("a) Linus Torvalds")
  print ("b) Bill Gates")
  print ("c) Mark Zuckerberg")
  print ("d) Dennis Ritchie"+RESET)

  # Almacenamos la respuesta del usuario en la variable "respuesta_1"
  respuesta_1 = input("\nTu respuesta: ")
  while respuesta_1 not in ("a", "b", "c", "d"):
    respuesta_1 = input ("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  if respuesta_1 == "b":
    puntaje += 10
    print ("Muy bien", nombre, "!")
  else:
    print ("Incorrecto", nombre, "!")
  print(RED + nombre, "llevas", puntaje, "puntos" + RESET)
  # Pregunta 2
  print (YELLOW+"\n2) ¿Cual de estos lenguajes de programación es de más bajo nivel?")
  print ("a) Python")
  print ("b) Java")
  print ("c) PHP")
  print ("d) Assembly"+RESET)
  # Almacenamos la respuesta del usuario en la variable "respuesta_2"
  respuesta_2 = input("\nTu respuesta: ")
  while respuesta_2 not in ("a", "b", "c", "d"):
    respuesta_2 = input ("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  
    # Ahora, verificamos su respuesta para mandar un mensaje de acierto o de error
  if respuesta_2 == "a":
    print ("Incorrecto!", nombre, "Python es un lenguaje de alto nivel")
  elif respuesta_2 == "b":
      print ("Incorrecto!", nombre, "Java es un lenguaje de alto nivel")
  elif respuesta_2 == "c":
    print ("Incorrecto!", nombre, "PHP es un lenguaje de alto nivel")
  else:
    puntaje += 10
    print ("Muy bien", nombre, "!")
  print(nombre, "llevas", puntaje, "puntos")


  # Pregunta 3
  print (YELLOW +"\n3) ¿Quién fue el creador de FACEBOOK?")
  print ("a) Linus Torvalds")
  print ("b) Bill Gates")
  print ("c) Mark Zuckerberg")
  print ("d) Dennis Ritchie"+RESET)

  # Almacenamos la respuesta del usuario en la variable "respuesta_1"
  respuesta_1 = input("\nTu respuesta: ")
  while respuesta_1 not in ("a", "b", "c", "d"):
    respuesta_1 = input ("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  if respuesta_1 == "c":
    puntaje += 10
    print ("Muy bien", nombre, "!")
  else:
    print ("Incorrecto", nombre, "!")
  print(nombre, "llevas", puntaje, "puntos")


  # Pregunta 4
  print (YELLOW+"\n4)¿En que lenguaje se progamo Minecraft?")
  print ("a) Python")
  print ("b) Java")
  print ("c) PHP")
  print ("d) Assembly"+RESET)

  # Almacenamos la respuesta del usuario en la variable "respuesta_3"
  respuesta_3 = input("\nTu respuesta: ")
  while respuesta_3 not in ("a", "b", "c", "d"):
    respuesta_3 = input ("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  if respuesta_3 == "a":
    print ("Totalmente incorrecto! ...")
    puntaje = puntaje / 2
  elif respuesta_3 == "d":
    print ("...")
    puntaje = puntaje + 5
  elif respuesta_3 == "c":
    print ("Incorrecto! ...")
    puntaje = puntaje - 5
  else:
    print ("Correcto! ...")
    puntaje = puntaje * 2

  print (RED+"Gracias", nombre, "por jugar mi trivia, alcanzaste", puntaje, "puntos"+RESET)
  
  print(BLUE+"\n¿Deseas intentar la trivia nuevamente?"+RESET)
  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()
  if repetir_trivia != "si":  # != significa "distinto"
   print(MAGENTA+"\nEspero",nombre ,"que lo hayas pasado bien, hasta pronto!"+RESET)
   iniciar_trivia = False  # Cambiamos el valor de iniciar_trivia a False para evitar que se repita.