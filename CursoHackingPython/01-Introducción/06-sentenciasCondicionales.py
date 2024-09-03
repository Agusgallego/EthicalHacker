#IF - ELSE: estructura
 
edad = int(input("introduzca su edad:"))
if edad in [10, 19, 30]:
    print(f"puede ingresar ya que su edad es {edad}") #todo lo que se encuentre en esta indentacion, se ejecuta si la condicion de if es True
else: #opcion por defecto
    print(f"no puede ingresar ya que su edad es {edad}")#todo lo que se encuentre en esta indentacion, se ejecuta si la condicion de if es False
#en python es muy importante mantener la indentacion 

#IF - ELIF - ELSE
if edad >= 18 and edad < 21:
    print("el usuario es mayor de edad en España")
elif edad >= 21:
    print("el usuario es mayor de edad en eeuu")
else:
    print("el usuario NO es mayor de edad")