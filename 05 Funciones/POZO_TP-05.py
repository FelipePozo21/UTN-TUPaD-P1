from math import pi

## actividad 1 

def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()

## actividad 2

nombre = input("Ingrese su nombre")

def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

saludar_usuario(nombre)
## actividad 3

apellido = input("Ingrese su apellido")
edad = input("Ingrese su edad")
residencia = input("Ingrese donde vive")

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

informacion_personal(nombre, apellido, edad, residencia)

## actividad 4

radio = int(input("Ingrese el radio"))

def calcular_area_circulo(radio):
    print(f"El area es: {pi * radio ** 2}")

def calcular_perimetro_circulo(radio):
    print(f"El perimetro es: {(radio * 2) * pi}")

calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)

## actividad 5

segundos = int(input("Ingrese los segundos"))

def segundos_a_horas(segundos):
    print(f"{segundos} segundos es igual a: {segundos/3600} horas.")

segundos_a_horas(segundos)

## actividad 6

multi = int(input("Ingrese el numero a multiplicar"))

def tabla_multiplicar(numero):
    for i in range(1,11):
        print(f"{i} * {numero} = {i * numero}")

tabla_multiplicar(multi)

## actividad 7

num_a = int(input("Ingrese el primer numero"))
num_b = int(input("Ingrese el segundo numero"))

def opearciones_basicas(a,b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b

    tupla = (suma, resta, multiplicacion, division)

    print(f"La suma de {a} + {b} es: {tupla[0]}")
    print(f"La resta de {a} - {b} es: {tupla[1]}")
    print(f"La multiplicacion de {a} * {b} es: {tupla[2]}")
    print(f"La division de {a} / {b} es: {tupla[3]}")

opearciones_basicas(num_a, num_b)

## actividad 8

peso = int(input("Ingrese su peso"))
altura = int(input("Ingrese su altura en metros"))

def calcular_imc(peso, altura):
    print(f"Tu IMC es: {peso / (altura ** 2)}")

calcular_imc(peso, altura)
## actividad 9

celsius = int(input("Ingrese los grados celsius"))

def celsius_a_fahrenheit(celsius):
    print(f"La temperatura fahrenheit es: {(celsius * 9 / 5) + 32}")

celsius_a_fahrenheit(celsius)
## actividad 10

promedio_a = int(input("Ingrese el primer numero para calcular el promedio"))
promedio_b = int(input("Ingrese el segundo numero para calcular el promedio"))
promedio_c = int(input("Ingrese el tercer numero para calcular el promedio"))

def calcular_promedio(a, b, c):
    print(f"El promedio es: {(a + b + c) / 3}")

calcular_promedio(promedio_a, promedio_b, promedio_c)