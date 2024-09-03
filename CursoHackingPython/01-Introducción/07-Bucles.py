#                                              FOR -> Sentencias en python que se van a repetir un numero finito de veces
# for <variable> in <iterable>:
#     <sentencias>
listaFor = ["Tarea1","Tarea2","Tarea3","Tarea4"]
for tarea in listaFor:
    print("estoy trabajando en la tareas", tarea)
# objetos iterables -> strings, tuplas, diccionarios y listas 

#diccionario
lista_diccionario = {
    "Tarea1":"completada",
    "Tarea2":"en proceso",
    "Tarea3":"terminada",
}

for tarea in lista_diccionario:
    print("estoy trabajando en la tarea:", tarea) #recordemos que SIEMPRE se selecciona la key a exepcion que lo especifiquemos 
    print("su estado es:", lista_diccionario[tarea]) #aqui especificamos que queremos el valor de la key, en cada iteracion 


#                                              WHILE -> Sentencias en python que se van a repetir las veces que querramos
# while <expresion con operadores>:
#     <sentencias>
num = 10
while num > 0:
    num -= 1
    print(num)
#ejecuta la condicion MIENTRAS (while) sea True, cuando esta es False, termina la ejecución
#!!!!!!!!!! Es muy probable que se pueda generar un bucle infinito
# num = 10
# while num > 0:  # esta condicion siempre va a ser True, entonces se ejecuta infinitamente hasta agotar recursos
#     print(num)

# ---> sentencias para controlar el bucle = continue, break
    #BREAK
# while num > 0:  # esta condicion siempre va a ser True, entonces se ejecuta infinitamente hasta agotar recursos
#     print(num)
#     break      #hace que se ejecute el codigo que se encuentra antes, luego del break se corta y sigue con la siguiente linea. 
# print("esto es fuera del bucle")

    #CONTINUE
while num > 0:
    num -= 1
    print(num)
    continue             #despues de esta linea no se ejecuta nada mas, vuelve al punto inicial del bucle.
    print("esta linea nunca se va a ejecutar")
print("fuera del bucle")