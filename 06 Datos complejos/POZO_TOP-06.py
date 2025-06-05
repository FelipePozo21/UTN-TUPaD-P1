## actividad 1

precios_frutas = {'Banana': 1200, "Anana" : 2500, 'Melon': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

## actividad 2

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melon'] = 2800

print(precios_frutas)

## actividad 3

lista = []

for frutas in precios_frutas.keys():
    lista.append(frutas)

print(lista)

## actividad 4

contactos = {}

while len(contactos) < 5 :
    key = input("Ingrese el nombre del contacto: ")
    value = input("Ingrese el numero del contacto: ")
    contactos[key] = value

print(contactos)  

## actividad 5

def frases():
    frase = input("Ingrese la frase: ").split()
    set_frase = set(frase)

    diccionario = {}

    for palabra in frase:
        if palabra in diccionario:
            diccionario[palabra] += 1
        else:
            diccionario[palabra] = 1

    print(f"las palabras unicas son {set_frase} y el diccionario es {diccionario}")
    
# frases()

## actividad 6

alumnos = {}

while len(alumnos) < 3:
    nombre = input("Ingrese el nombre del alumno")
    nota = ()
    while True:
        if len(nota) == 3:
            break

        notas = int(input("Ingrese la nota"))
        nota = nota + (notas, )
    alumnos[nombre] = notas
print(alumnos)

## actividad 7

set_1 = {'geronimo', 'morena', 'tobias', 'mateo', 'brisa'}
set_2 = {'geronimo', 'jazmin', 'felipe', 'julian', 'brisa'}

print(f"{set_1.intersection(set_2)} aprobaron ambos parciales")
print(f"{set_1 - set_2} aprobaron 1 solo parcial")

## actividad 8

stock = {}
while True:
    seleccion = int(input("1. Consultar el stock \n2. Agregar productos \n3. Salir"))


    if seleccion == 3:
        break
    if seleccion == 2:
        nombre_stock = input("Agregue el nombre del producto")
        cantidad_stock = int(input("Ingrese la cantidad del producto"))

        stock[nombre_stock] = cantidad_stock

    if seleccion == 1:
        print(stock)

        while True:
            seleccion_2 = int(input(f"1. Agregar stock \n2. salir"))

            if seleccion_2 == 2:
                break
            else:
                nombre_stock_agregar = input("Agregue el nombre del producto")
                if nombre_stock_agregar in stock:
                    nuevo_stock = int(input("Ingrese la cantidad del producto"))
                    stock[nombre_stock] = nuevo_stock
                else:
                    nombre_stock_agregar = input("Ingrese un nombre valido")

## actividad 9

agenda = {("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés",
    ("miércoles", "18:30"): "Gimnasio"}

dia = input("Ingresá un día: ").lower()
hora = input("Ingresá una hora (formato HH:MM): ")

actividad = agenda.get((dia, hora))

if actividad:
    print(f"A esa hora tenés: {actividad}")
else:
    print("No hay actividades registradas en ese horario.")

## actividad 10

original = {"Argentina": "Buenos Aires", "Chile": "Santiago"}
invertido = {capital: pais for pais, capital in original.items()}
print(invertido)
