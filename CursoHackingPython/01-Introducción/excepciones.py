# print(var) -> es un ERROR ya que no esta definido "var"
# pero podemos manejar este error como una "excepcion"
# tipos de errores ━━━> error de sintaxis(no se pueden manejar, se detiene)
#                  ┗━━> errores "logicos"
#* palabras claves => try:, except: -> para manejar el comportamiento de cuando se porduzca esta excepcion 
#try:
#    print(var) #aca tendriamos todo el cuerpo del codigo, que cuando tenga eun error ejecutaria ┓
#except: #   <━━━━━━━━━━━━ esto no interrumple la ejecución del programa <━━━┏━━━━━━━━━━━━━━━━━━━┛
#    print("la variable no esta definida") #            ┏━━━━━━━━━━━━━━━━━━━━┛
#print("el programa sigue ejecutandose")#    <━━━━━━━━━━┛

#! si quisieramos hace excepciones especificas:
#try:
#    print(estaVarNoExiste)   #en el momento que ocurre una excepcion, salta al siguiente bloque, no importa q haya debajo
#except (NameError, TypeError):
#    print("except especificos")


#! crear excepciones PERSONALIZADAS
#colores = ("verde", "azul", "violeta")
#c = "morado"
#if c not in colores:
#    raise Exception(f"el color {c} no se encuentra entre los colores")
#     ↑      ↑   palabras clave