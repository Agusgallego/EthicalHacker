#                                              OPERADORES ARITMÉTICOS, COMPARACIÓN Y ASIGNACIÓN 
numero_1 = 10
numero_2 = 10

string_1 = "texto1"
string_2 = "texto2"

lista_1 = ["lista1", "lista2", "lista3"]
lista_2 = ["lista4", "lista5", "lista6"]

tupla1 = ("tupla1", "tupla2" , "tupla3")

dic_1 = {"clave1": "valor1", "clave2": "valor2"}
dic_1 = {"clave3": "valor3", "clave4": "valor4"}

#OPERADORES ARITMETICOS
# + - / // * ** %
sum = numero_1 + numero_2 
res = numero_1 - numero_2 
div = numero_1 / numero_2 
mult = numero_1 * numero_2 
modulo = numero_1 % numero_2 
exponencial = numero_1 ** numero_2 
divEnteros = numero_1 // numero_2 


#OPERADORES COMPARACION
# == != >= <= < >
igualdad = numero_1 == numero_2 
desigual = numero_1 != numero_2 
mayorQue = numero_1 < numero_2
menorQue =  numero_1 > numero_2
mayorIgual =  numero_1 <= numero_2
menorIgual = numero_1 >= numero_2


#OPERADORES DE ASIGNACIÓN
# a += 5 equivalente a = a + 5
# a /= 10 equivalente a = a / 10
# a *= 7 equivalente a = a * 7



#                                              OPERADORES PERTENENCIA, LÓGICOS E IDENTIDAD
#OPERADORES DE PERTENENCIA -> IN , NOT IN
#!!!!!!!!!! SE APLICA UNICAMENTE EN SECUENCIAS !!!!!!!!!!!!!!!!!!!!!!

print('c' in string_1) # in => nos indica si un elemento se encunetra 
                       #dentro de otro ( en este caso si el char 'c' se encuentra en el string string_1)

print('c' not in string_1)# not in => nos indica si un elemento NO SE encuentra dentro de otro
                          # en este caso si el char 'c' no se encuentra en el string string_1

#Aplicado a diccionarios 
print('clave1' in dic_1)  #solo podemos aplicar este operador en las KEY's         
#Aplicado a listas 
print('lista1' in lista_1) 
#Aplicado a listas 
print('tupla1' in tupla1)

#OPERADORES DE LÓGICOS -> NOT, AND, OR
#OR -> al menos una expresion debe ser verdadera
print(numero_1 >= numero_2 or 'c' in string_1)
#AND -> ambas expresiones deben ser verdaderas
print(numero_1 >= numero_2 and 'c' in string_1)
#NOT -> NIEGA LA OPERACION 
print(not(numero_1 >= numero_2))

#OPERADORES DE IDENTIDAD -> IS, IS NOT
#comparan si son EL MISMO OBJETO, es decir no funciona igual que "==" 
print(type(string_1) is str) #aqui comparamos si string_1 es de tipo str(string)
print(type(lista_1) is not list) #aqui comparamos si NO SON el mismo tipo de dato

