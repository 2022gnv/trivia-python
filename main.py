#crearemos una constante (es como variables pero no cambia su valor),escribiremos en mayuscula para no escribir los codigos del color, (color a lo que escribimos)
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET= '\033[38m'
#importaremos una libreria de python,para usar funciones avanzadas
import random #libreria importada random
import time

#para implementar puntos,crearemos una variable llamada puntaje la comenzara en 2
puntaje=random.randint(0,20)#numeros al azar del 2 al 50.
#para contar las respuestas correctas y incorrectas realizaremos las siguientes variables
correcta=0
incorrecta=0

#va a aparecer el numero de veces que juguemos 
iniciar_trivia = True #iniciamos con la variable True 
intentos = 0 # es la variable que guaradara el numero de veces que el jugador intenta nuestra trivia
jugador_turno = []

#mensaje de bienvenida
print(BLUE+"Bienvenido a mi trivia sobre los *SIMPSON*")
time.sleep(1)
print("pondremos a prueva tus conocimientos simpsonianos"+RESET)
time.sleep(1)
print(GREEN+"comensaras con:",puntaje,"puntos"+RESET)
time.sleep(1)
#preguntaremos el nombre del jugador
nombre=input("ingresa tu nombre:")
edad=input("ingresa tu edad:")
if edad.isnumeric():
   print("esa edad me tomare en cervesas en la taberna de Moe")
else:
  print("no es un numero")
  time.sleep(2)
  edad=input("ingresa de nuevo tu edad o eres una rosquilla flandirijillo:")


#instrucciones
print(YELLOW+"Hola", nombre,"escribe la alternativa correcta y da enter,recuerda que cada pregunta tiene un puntaje:\n"+RESET)

# EL \n al final de la linea 27 es para dar un salto de linea

#va a aparecer el numero de veces que juguemos la trivia
while iniciar_trivia==True:
  correcta=0
  incorrecta=0
  intentos+=1
  puntaje=0
  a=0
  b=0
  c=0
  d=0
  print("\nintento numero: ",intentos)
  input("presione enter para continuar")

  #crearemos un siclo para mostrar una carga inicial de 6 segundos
  for numero_carga in range(3,0,-1):
    print(numero_carga)
    time.sleep(1)
  # pregunta 1
  print(BLUE+"\n1) ¿Quien tenia una taberna?"+RESET)
  listaa=["a) Marge simpson","b) Moe szyslak","c) Ralph wiggum", "d) Barney gumble"]
  for element in listaa:
    print(element)

  #almacenamos ñas respuestar del jugador en la variable respuesta_1
  respuesta_1=input(GREEN+"\ntu respuesta:"+RESET).lower()
  #aplicaremos un ciclo de validacion
  while respuesta_1 not in ("a","b","c","d"):
   respuesta_1=input("debes responder a,b,c,d. ingresa tu respuesta:").lower()
  #utilizaremos la condicional para ver si tu respuesta es correcta o incorrecta
  if respuesta_1=="b":
    a+=random.randint(5,20)
    correcta+=1
    print("muy bien",nombre,"!")
  else:
    a-=random.randint(1,5)
    incorrecta+=1
    print("incorrecto",nombre,"!")
  time.sleep(1)
  print(GREEN+nombre,"ganaste",a,"puntos."+RESET)
  time.sleep(2)
  #pregunta 2
  print(BLUE+"\n2) ¿Cuantos hijos tenia homero simpson?"+RESET)
  listab=[BLUE+"a) 1","b) 3","c) 5","d) 8"+RESET]
  for element in listab:
    print(element)


  respuesta_2=input(YELLOW+"\ntu respuesta:"+RESET)

  while respuesta_2 not in ("a","b","c","d","x"):
    respuesta_2=input("debes responder a,b,c,d. ingresa nuevamente tu respuesta:").lower()
    
  if respuesta_2=="x":
    b+=random.randint(1,6)
    incorrecta+=1
    print("este es un mensaje secreto")
  elif respuesta_2=="a":
   b-=random.randint(1,6)
   incorrecta+=1
   print("incorrecto!",nombre, "son mas hijos")
  elif respuesta_2=="b":
   b+=random.randint(5,10)
   correcta+=1
   print(nombre,"si pareces un simpson","!")
  elif respuesta_2=="c":
   b-=random.randint(1,6)
   incorrecta+=1
   print("incorrecto!", nombre,"son menos hijos")
  else:
    b-=random.randint(1,6)
    incorrecta+=1
    print("incorrecto!",nombre,"son mas hijos")
  time.sleep(1)
  print(GREEN+nombre,"ganastes",b,"puntos."+RESET)
  time.sleep(2)
  #PREGUNTA 3
  print(GREEN+"\n3) ¿Donde trabajaba homero simpson?"+RESET)
  listac=("a) en una planta nuclear","b) en un bar","c) en un taxi","d) en mcdonalds")
  for element in listac:
    print(element)
    
  respuesta_3=input(YELLOW+"\n tu respuesta:"+RESET)

  while respuesta_3 not in ("a","b","c","d","x"):
    respuesta_3=input("debes responder a,b.c,d. flanders ingresa nuevamente tu respuesta o me comere tu rosquilla: ")
  if respuesta_3=="a":
    c+=random.randint(8,20)
    correcta+=1
    print("muy bien", nombre,"!")
  elif respuesta_3=="b":
    c-=random.randint(1,5)
    incorrecta+=1
  elif respuesta_3=="c":
    c-=random.randint(1,5)
    incorrecta+=1
    print("incorrecto!",nombre, "no trabajaba ahi")
  elif respuesta_3=="d":
    c-=random.randint(1,5)
    incorrecta+=1
    print("incorrecto!",nombre, " no trabajaba ahi")
  else:
    c-=random,randint(1,5)
    incorrecta+=1
    print("incorrecto!", nombre,"no tabajaba ahi")
  print(WHITE+nombre,"ganaste",c,"puntos."+RESET)
  time.sleep(2)
  #RULETA DE PUNTAJE FINAL
  print("\njugaremos la ruleta de puntaje final")
  numero_carga2=int(input("\n¿cuantas veces deseas girar la ruleta? "))
  for ruleta in range(1,numero_carga2+1):
    d=random.randint(1,20)
    if ruleta==numero_carga2:
      print("a tu ultima puntuacion se le sumara: ",d)
    else:
      print("intento N°",ruleta,"resultado: ",d)

    time.sleep(1)
  #agragamos un mensaje final donde se mostrara el puntaje total
  print("cantidad de respuestas correctas:",correcta)
  time.sleep(1)

  lista1=[a,b,c,d]
  print("estos puntajes fueron obtenidos por cada pregunta: ",lista1)

  print(BLUE+"gracias",nombre,"por jugar mi trivia, alcanzastes",sum(lista1),"puntos."+RESET)

  jugador_turno.append(sum(lista1))
  
  #si deseamos seguir jugando aqui se decide
  print("\n¿deseamos intentar la trivia nuevamente?")
  repetir_trivia = input("ingresa 'si' para repetir, o cualquier tecla para finalizar:").lower()

  if repetir_trivia != "si": # != sifnifica distinto
   print("\nespero",nombre,"que ayas pasado un buen momento,asta pronto!")
    
   iniciar_trivia = False # cambiamos el valor de iniciar_trivia a false para evitar que se repita.