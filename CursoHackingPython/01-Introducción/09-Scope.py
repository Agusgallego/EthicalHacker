
# ! SCOPE LOCAL => variables, que tienen un alcance local, es decir, -dentro de una etructura de datos, fuera de esta no la podemos utulizar-
def func():
    num = 10        #num funciona dentro de esta función 
    def fun2():     #tiene su propio scope local
        num2 = 14
        print(num)  # ↑
        print(num2)
func()
#ACLARACION -> func() tiene aclace al scope de func2(), pero no al reves 
#podemos ir de afuera hacia dentro ↓ pero no de dentro hacia afuera ↑

# ! SCOPE GLOBAL => elementos de los que podemos acceder desde cualquier estructra de datos
variableGlobal = "valor global"
def funGlobal():
    print(variableGlobal)

# ! SCOPE POR DEFECTO => ambito especial de python, que se carga cada vez que se ejecuta
# * palabras clave, funciones por defecto, excepciones,  etc

#si nosotros queremos ver lo que esta definido de forma local y global 
print(locals()) #local 
print(globals()) #global