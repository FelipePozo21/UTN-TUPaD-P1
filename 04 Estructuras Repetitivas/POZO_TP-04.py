from random import randrange

## actividad 1

## pongo 101 en vez de 100 por que sino imprime hasta el 99
for i in range (0,101):
    print(i)

## actividad 2

entero = input("Ingrese un numero entero: ")
digito = 0

for i in range(0,len(entero)):
    digito += 1

print(digito)

## actividad 3

numero_1 = int(input("Ingrese el primer numero: "))
numero_2 = int(input("Ingrese el segundo numero: "))

for i in range(numero_1 + 1, numero_2):
    print(i)

## actividad 4

sumatoria = int(input("Ingrese el numero a sumar(si deseas terminar, ingrese 0) "))
sum = 0

while sumatoria != 0:
    sum = sum + sumatoria
    sumatoria = int(input("Ingrese el numero a sumar(si deseas terminar, ingrese 0) "))

print(sum)

## actividad 5

intentos = 0
numero_secreto = randrange(0, 10,1)

while True:
    intento = int(input("Ingrese un numero entre 0 y 9 "))
    if intento == numero_secreto:
        break

print(f"intentos: {intentos}")

## actividad 6

num = 100
while True:
    if num == 0:
        break
    num -= 1
    print(num)

## actividad 7

sumatoria_1 = int(input("Ingrese un numero: "))
suma = 0

for i in range(0, sumatoria_1 + 1):
    suma += i
print(suma)

## actividad 8

for i in range(0, 101):
    num = int(input("Ingrese un numero: "))
    if num > 0:
        print("Par y positivo") if num % 2 == 0 else print("Impar y positivo")
    else:
        print("Par y negativo") if +num % 2 == 0 else print("Impar y negativo")

## actividad 9

suma = 0
for i in range(0,101):
    num = int(input("Ingrese un numero: "))
    suma += num
print(suma / 100)

## actividad 10

string_1 = input("Ingrese un numero: ")
string_2 = ""

for i in range(0, len(string_1)):
    string_2 = string_1[i] + string_2
print(string_2)