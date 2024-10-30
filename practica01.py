while ejecutar:
print (" Hola este es un cajero ")
#variable nombre
nombre = input(" ¿Cuál es tu nombre? ")
ahorro = int(input(" ¿Cuál es tu ahorrro"))
print(" Muy bien " + nombre)
ejecutar = True
print( " ** selecciona una opción ** ")
print(nombre + " presiona 1 para connsultar saldo")
print(nombre + " presiona 2 para hacer un retiro")
print(nombre + " presiona 3 para hacer un abono")
print("****")
pcion= int(input("Escribe la opcion que deseas usar "))
#Opcion 1 Consultar tu saldo 
if opcion== 1:
print("Tu saldo es de ", ahorro  , "mxn")
opcion_uno=input("¿Deseas hacer otra cosa otra operacion")
if opcion_uno=="si":
print("tend´rás que regresar al menu principal")
ejecutar=True
elif opcion_uno=="no":
 print("Gracias por visitarnos , hasta luego.")
 ejecutar=False
 else:
   print("opcion no valida")