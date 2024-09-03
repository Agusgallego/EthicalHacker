#Bloque de codigo que encapsula una tarea especifica o grupo de tareas relacionado
#Los argumentos toman sentido a la hora de invocar la variable y pasarle un valor por los parametros
#SINTAXIS
#def <nombre de la funcion> ([parametros]):       ->    DEFINICIÓN DE LA FUNCIÓN
#    <sentencias>                                 ->    CUERPO DE LA FUNCIÓN


def mi_funcion(nombre,apellido):
    print(nombre)
    print(apellido)

mi_funcion("agus", "gallego") #agregamos los argumentos, que deben coincidir con el numero de parametos

#podemos crear la funcion, sin parametros a definir
def sin_arg():
    print("esto es una funcion sin argumentos")

#                                                   TIPOS DE ARGUMENTOS
#IMPORTANTE! -> NO PODEMOS poner un argumento de palabra clave y luego un posicional  => mi_funcion(apellido="Toledo", "Emanuel")
#IMPORTANTE! -> SI PODEMOS poner un argumento posicional y luego uno de palabra clave => mi_funcion("Emanuel", apellido="Toledo")
#           POSICIONALES: proporcionar los valores, en el mismo orden que definimos los parametros
def mi_funcion(nombre,apellido):
    print(nombre)
    print(apellido)
mi_funcion("agus", "gallego")   #Ejemplo de argumentos posicionales 

#           ARGUMENTOS DE PALABRA CLAVE: referenciando el nombre del parametro que colocamos en la definicion de la funcion. 
mi_funcion(apellido="Toledo", nombre="Emanuel") #indicamos explicitamente 


#                                                   TIPOS DE PARAMETROS
#VALOR POR DEFECTO: es decir, si el usuario no introduce uno, utilizar este
def mi_funcion(nombre,apellido="Valor por defecto"):
    print(nombre)
    print(apellido)

mi_funcion("valor1")

# SENTENCIA RETURN: Las funciones pueden retornar un valor, luego de haber ejecutado su cuerpo de la funcion
def mi_funcion(nombre,apellido="Valor por defecto"):
    print(nombre)
    print(apellido)
    return 10    #en el momento que el programa ingresa a esta linea, SE TERMINA la ejecucion de este. 
    print("esta linea no se ejecuta")

valor_final = mi_funcion("agustina", "Gallego")
print(valor_final) #si no colocamos nada luego de return, nos devuelve "None"

def mi_funcion(nombre,apellido="Valor por defecto"):
    print(nombre)
    print(apellido)
    return "valor1", "valor2"    #en el momento que el programa ingresa a esta linea, SE TERMINA la ejecucion de este. 
    print("esta linea no se ejecuta")

valor1 , valor2 = mi_funcion("agustina", "gallego")  
#en estas variables, almacenamos el valor de los return

#                                                 DOCUMENTAR UNA FUNCIÓN 
def mi_funcion(nombre,apellido="Valor por defecto"):
    """ 
    DOCSTRINGS -> guia de estilos -> PEP 257
    """
    print(nombre)
    print(apellido)
    return "valor1", "valor2"    #en el momento que el programa ingresa a esta linea, SE TERMINA la ejecucion de este. 
    print("esta linea no se ejecuta")

    












