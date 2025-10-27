###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

from os import system
if system("clear") != 0: system("cls")

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

### -------------
print("Ignacio", end="\n")
print("Cordoba")



### -------------
print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### -------------
print(type(a), type(b), type(c), type(d), type(e))



### -------------

print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### -------------
cadena = "12345"
cadena1 = int(cadena)
cadena2 = float(cadena1)

print(cadena1)
print(cadena2)

num = 3.99
num1 = int(num)

print(num1)

### -------------

print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

nombre = "Ignacio"
edad = 20
altura = 1.80
# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"
print("Hola! Me llamo",nombre, "y tengo", edad, "años, mido", altura, "metros")
### Completa aquí

print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

pi=3.14
pi1=round(pi)
pi2=int(pi1/2)

print(pi, pi1, pi2)