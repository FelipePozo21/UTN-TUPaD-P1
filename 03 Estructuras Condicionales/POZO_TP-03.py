
from statistics import mode, median, mean
import random 

## actividad 1

edad_usuario = int(input("Ingrese su edad: "))

## verifica si el usuario es mayor de edad
if edad_usuario >= 18:
    print("Eres mayor de edad")

## actividad 2

nota_usuario = int(input("Ingrese su nota: "))

## verifica la nota del usuario y devuelve si esta aprobado o no
if nota_usuario >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

## actividad 3

par_inpar = int(input("Ingrese un numero: "))

## usando la ternaria y el modulo, verifico si es par o inpar  
print("Es numero par") if par_inpar % 2 == 0 else print("Por favor, ingrese un numero par")

## actividad 4 

verificar_edad = int(input("Ingrese su edad: "))

## Se concatenan condicionales para verificar la edad del usuario
if verificar_edad > 0 and verificar_edad < 12:
    print("Niño")
elif verificar_edad >= 12 and verificar_edad < 18:
    print("Adolescente")
elif verificar_edad >= 18 and verificar_edad < 30:
    print("Adulto/a joven")
elif verificar_edad >= 30 and verificar_edad < 100:
    print("Adulto/a")
else:
    print("Ingrese una edad validad")

## actividad 5

contrasenia_usuario = input("Ingrese su contraseña: ")

## se usa el metodo len para verificar el tamaño de la contraseña
len_contrasenia = len(contrasenia_usuario)

## se verifica si la contraseña mide entre 8 y 14, si lo es le avisa al usuario que ingreso la contraseña correcta, sino se le pide al usuario que ingrese una contraseña correcta
if len_contrasenia >= 8 and len_contrasenia <= 14:
    print("Ha ingreasdo una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

## actividad 6

## se crea una lista de 50 numeros aleatorios entre el 1 y el 100
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

## mediante el modulo statistics, se usan sus metodos para sacar la mediana, la moda y la media
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

## se verifica si se consigue que entren en algun sesgo y se devuelve el resultado
if media > mediana and mediana > moda:
    print("Sesgo positivo")
elif media < mediana and mediana < moda:
    print("Sesgo negativo")
elif media == mediana and mediana == moda:
    print("Sin sesgo")
else:
    print("No entro en ningun sesgo")

## actividad 7

frase_usuario = input("Ingrese una frase o palabra")

## se crea una lista con las vocales
vocales = ["a", "e", "i", "o", "u"]

## se crea un ciclo con el tamaño de las vocales, y verifica si el index de vocales es igual al ultimo index de frase_usuario, si lo es devuelve frase_usuario + !, sino devuelve frase_usuario
for i in range(len(vocales)):
    if frase_usuario[-1] == vocales[i]:
        print(f'{frase_usuario}!')
        break
    else:
        print(frase_usuario)
        break

## actividad 8:

## se le pide el nombre al usuario y que opcion quiere
nombre_usuario_8 = input("Ingrese su nombre: ")
numero = int(input("Ingrese alguno de estos numeros: 1, 2 o 3 "))

## verifica si el numero elegido es una opcion valida, si lo es hace lo que se pidio, sino se le dice al usuario que el numero es invalido
if numero == 1:
    print(nombre_usuario_8.upper())
elif numero == 2:
    print(nombre_usuario_8.lower())
elif numero == 3:
    print(nombre_usuario_8.title())
else:
    print("Ingrese un numero valido ")

## actividad 9

terremoto = int(input("Ingrese la magnitud del terremoto: "))

## se verifica la magnitud del terremoto
if terremoto > 0 and terremoto < 3:
    print("Muy leve")
elif terremoto >= 3 and terremoto < 4:
    print("Leve")
elif terremoto >= 4 and terremoto < 5:
    print("Moderado")
elif terremoto >= 5 and terremoto < 6:
    print("Fuerte")
elif terremoto >= 6 and terremoto < 7:
    print("Muy fuerte")
elif terremoto >= 7 and terremoto < 10:
    print("Extremo")
else:
    print("Se ingreso magnitud incorrecta")

## actividad 10

## se le preguntan datos al usuario
emisferio_usuario = input("Ingrese en que emisferio vives (N/S): ")
dia = int(input("Ingrese el dia: "))
mes = input("Ingrese que mes es (nombre): ")

## se genera una lista de los meses, por si a futuro se necesita agregar los dias limites de cada ems
calendario = ["enero", "febrero", "marzo", "abril","mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
index = 0

## se busca el index del calendario
for i in range(len(calendario)):
    if calendario[i] == mes:
        index = i
        break

## verifica que periodo del año es
if index >= 11 or (index <= 2 and index >= 0):
    if dia < 21 and index == 11 or index == 2:
        pass
    else:
        if emisferio_usuario == 'N':
            print("Invierno")
        else:
            print("Verano")
if index >= 2 and index <= 5:
    if dia < 21 and index == 2 or index == 5:
        pass
    else:
        if emisferio_usuario == 'N':
            print("Primavera")
        else:
            print("Otoño")
if index >= 5 and index <= 8:
    if dia < 21 and index == 5 or index == 8:
        pass
    else:
        if emisferio_usuario == 'N':
            print("Verano")
        else:
            print("Invierno")
if index >= 8 and index <= 11:
    if dia < 21 and index == 8 or index == 11:
        pass
    else:
        if emisferio_usuario == 'N':
            print("Otoño")
        else:
            print("Primavera")
