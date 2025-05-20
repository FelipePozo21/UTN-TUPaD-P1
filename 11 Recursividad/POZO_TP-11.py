## actividad 1

## funcion que calcula el factorial de un numero dado
def act_1(n):
    if n == 1:
        return 1
    else:
        return n * act_1(n - 1)
    
# actividad_1_input = int(input("Ingrese el numero que quieras calcular el factorial: "))

# print(act_1(actividad_1_input))

## actividad 2

def act_2(n):
    if n == 0 or n == 1:
        return n
    else:
        return act_2(n - 2) + act_2(n - 1)
    

# actividad_2_input = int(input("Ingrese la posicion de fibonacci: "))

## bucle que muestra cada numero de la secuencia fibo
# for i in range(actividad_2_input):
#     print(act_2(i))

## actividad 3

def act_3(n,m):
    print(n,m)
    if m == 0:
        return 1
    else:
        return n * act_3(n, m - 1)
    
# print(act_3(16,12))

## actividad 4

def act_4(n, cadena=""):
    if n == 1:
        return "1" + cadena
    else:
        cadena = str(n % 2) + cadena
        return act_4(int(n/2), cadena)
    
# print(act_4(8))

## actividad 5

def es_palindromo(cadena):
    if len(cadena) <= 1:
        return True

    if cadena[0] == cadena[-1]:
        return es_palindromo(cadena[1:-1])
    else:
        return False
    

# print(es_palindromo("abccba"))

## actividad 6

def suma_digitos(n):
    if n == 0:
        return n
    else:
        ## verifica el ultimo digito de n con el % y con // lo saca
        return n % 10 + suma_digitos(n // 10)

# print(suma_digitos(1234))

## actividad 7

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)
    
# print(contar_bloques(4))

## actividad 8

def contar_digito(numero, digito, contador=0):
    if numero == 0:
        return contador
    else:
        ## verifica si el ultimo numero es igual al digito, si lo es suma 1 a contador, sino se llama a si misma sin sumarlo
        if numero % 10 == digito:
            return contar_digito(numero // 10, digito, contador + 1)
        else:
            return contar_digito(numero // 10, digito, contador)
        
print(contar_digito(5555,5))