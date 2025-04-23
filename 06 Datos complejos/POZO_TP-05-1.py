## actividad 1

## una lista de los multiplos de 4 desde el 0 hasta el 100
actividad_1 = range(0,101, 4)

# for x in actividad_1:
#     print(x)

## actividad 2

actividad_2 = [0,1,2,3,4]

print(actividad_2[-2])

## actividad 3

actividad_3 = []

## usando el metodo append, le agrego 3 palabras
actividad_3.append("primera_palabra")
print(actividad_3)
actividad_3.append("segunda_palabra")
print(actividad_3)
actividad_3.append("tercera_palabra")
print(actividad_3)

## actividad 4

animales = ["perro", "gato", "conejo", "pez"]

print(animales)

## muto el array mediante el uso del index

animales[0] = "loro"

print(animales)

animales[-1] = "oso"

print(animales)

## actividad 5

## numeros = [8, 15, 3, 22, 7]
## numeros.remove(max(numeros))
## print numeros

## este codigo crea una lista de 5 elementos, despues con el metodo max, itera sobre la lista, buscando el elemento mas grande, una ves que lo encuentra, lo borra de la lista

## actividad 6

actividad_6 = range(10, 31, 5)

for i in actividad_6:
    print(i)

## actividad 7

autos = ["sedan", "polo", "suran", "gol"]

print(autos) 
autos[1] = "toyota"

print(autos) 

autos[2] = "audi"

print(autos) 

## actividad 8

dobles = []

dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)

print(dobles)

## actividad 9

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

## 9.a)

compras[-1].append("jugo")

## 9.b)

compras[1][1] = "tallarines"

## 9.c)

compras[0].remove("pan")

## 9.d)

print(compras)


## actividad 10

lista_anidada = [15, True, [25.5, 57.9, 30.6], False]

print(lista_anidada)