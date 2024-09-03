#                                              MANIPULACIÓN DE DATOS
#lista de tareas 
lista_tareas = ["tarea1", "tarea2", "tarea3", "tarea4", "tarea5" ]

#tupla de tareas 
tupla_tareas = ("tarea1", "tarea2", "tarea3", "tarea4", "tarea5" )

#diccionario de tareas
diccionario_tareas = {
    "tarea1":"termianda",
    "tarea2":"pendiente",
    "tarea3":"termianda",
    "tarea4":"en proceso",
    "tarea5":"pendiente"
}

#                                                    INDEXING
#lista de tareas
print(lista_tareas[0]) #INDICAMOS INDICE DE EL VALOR AL QUE QUEREMOS ACCEDER. inicia con 0

#tupla de tareas
print(tupla_tareas[1]) #INDICAMOS INDICE DE EL VALOR AL QUE QUEREMOS ACCEDER. inicia con 0

#diccionario de tareas
print(diccionario_tareas["tarea1"])

#                                            modificación - INDEXING
#lista de tareas
lista_tareas[2] = "modificamos valor" 
#diccionario de tareas
diccionario_tareas["tarea1"] = "en proceso"


#                                                    SLICING
#lista de tareas
print(lista_tareas[1:4]) #incluye el primer elemento, pero el ultimo no.

#tupla de tareas
print(tupla_tareas[1:4]) #incluye el primer elemento, pero el ultimo no.

#diccionario de tareas  -> NO SE PUEDE

#SI PODEMOS APLICARLO A CADENAS DE TEXTO 
cadena = "texto"
cadena[2] = "g"
print(cadena[1])

#                                                    STRIDE
print(lista_tareas[3:]) #indicamos que inicie en tres, hasta el final de la lista
print(lista_tareas[:4]) #inicie en la lista y termine en la posicion 4 
print(lista_tareas[0::2]) #decimos que empiece en cero, que termine, cuando se termina la tarea y con el 2, que imprima cada 2 elementos