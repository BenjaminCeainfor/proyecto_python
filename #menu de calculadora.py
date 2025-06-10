#menu de calculadora

#funciones def

#ciclos de repeticion menu

#validcacion con try except

import time

#paso 1 - creacion de funciones def 



#las variables num1 y num2 que se encuenteran dentro de los parentesis,

#son los argumentos que recibe desde afuera de la funcion sumar

def sumar (num1, num2):

  #expresion sumar

  resultado_suma = num1 + num2

  return(resultado_suma)



def restar (num1,num2):

  resultado_resta = num1 - num2

  return (resultado_resta)



def dividir (num1,num2):

  try:

    resultado_division = num1 / num2

    return (resultado_division)

  except ZeroDivisionError:

    print("no se puede dividir por cero\n")

    time.sleep(3)



def multiplicar (num1, num2):

  resultado_multiplicacion = num1 * num2

  return(resultado_multiplicacion)



def mostrar_menu():

  print("========================================")

  print("Menu de calculadora en python:")

  print("========================================")

  print("1- sumar.")

  print("2- restar.")

  print("3- multiplicar")

  print("4- dividir.")

  print("5- salir.")



def obtener_numeros():

  while True:

    try:

      num1 = int(input("ingrese el primer numero a operar:"))

      num2 = int(input("ingrese el segundo numero a operar:"))

      return(num1,num2)



    except ValueError:

      print("error se ha ingresado un numero no valido:")

      time.sleep(3)



def main():

  while True:

    mostrar_menu()



    try:

      op = int(input("ingrese una opcion de 1 a 5:"))

    except ValueError:

      print("error, ingrese un valor valido.")

      time.sleep(3)

    #validar que la opcion este entre 1 y 5

    if op < 1 or op > 5:

      print("error, ha ingresado una opcion no valida")

      time.sleep(3)

    #cunado la opcion ingresada sea entre las 4 opciones de la lista 

    #ingresa al codigo interno if 

    if op in [1,2,3,4]:

      #guardar en la variables num1 y num2 las lo que me esta retornando es la funcion obtener_numeros()

      num1,num2 = obtener_numeros()

      if op == 1 :

        resultado = sumar(num1,num2)

        print(f"el resultado de la suma es {resultado}\n")

        time.sleep(2)

      if op == 2 :

        resultado = restar(num1,num2)

        print(f"el resiltado de la resta es {restar}\n")

        time.sleep(2)

      if op == 3 :

        resultado = multiplicar(num1,num2)

        print(f"el resultado de la multiplicacion es {resultado}\n")

        time.sleep(2)

      if op == 4 :

        resultado = dividir(num1,num2)

        print(f"el resultado de la division {resultado}\n")

        time.sleep(2)

    if op == 5 :

      print("muchas gracias por utilizar el programa")

      exit()

main()