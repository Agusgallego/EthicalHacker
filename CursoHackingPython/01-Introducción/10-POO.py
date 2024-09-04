
# POO => Programación Orientada a Objetos: paradigma de programacion que proporciona objetos, que nos permiten estructurar programas con propiedades y comportamientos se agrupen
# si nosotros instanciamos una estructura, pero no queremos definirle nada, la instanciamos con "pass"

#! CLASES => estructura principal en la orientación a objetos. (proporciona medio para agrupar), cuando creamos una clase, se crea un nuevo tipo de dato "class"
# cuando nosotros instanciamos una FUNCIÓN dentro de una clase, se denomina MÉTODO (funciona igual)
# Parametro Self: cuando nosotros definimos un método en una clase, es necesario proporcionarles un parametro a estos metodos #! (Self)
#* Crear clase
class Coche:
    def __init__(self):
        pass
    atributo_clase = 100
    def velocidad_maxima(self):                    
        print("velocidad maxima:", self.atributo_clase) #ejemplo de la usabilidad de self

#* parametro self -> debe situarse como PRIMER parametro, referenciamos el contenido de la propia clase
#* Instanciar clase
coche1 = Coche() #coche1 HEREDA todos los datos y funcionalidades de Coche()

#* Invocación de método
#funcion instanciada en una clase => MÉTODO

coche1.velocidad_maxima()
print(coche1.atributo_clase) #podemos desde la propia instancia REFERENCIAR la clase
#* Almacenar datos dentro de la clase
#variable instanciada en una clase => ATRIBUTO

#! IMPORTANTE -> lo normal, es que querramos partir de una estructura => "Coche()" e irle definiendo atributos 
# Como lo hacemos? ATRIBUTOS DE INSTANCIA: variables que pertenecen a un objeto en particular
#? def __init__(self) -> se va a ejecutar automaticamente cada vez que nosotros ejecitemos una INSTANCIA de esta clase
#? def __init__(self) = "constructor" asigna valores especificos y comportamientos especificos para el objeto que instanciamos 

class CocheEjemplo(): 
    def __init__(self, vel_max):           #vel_max recibe el valor de  ──────────────────────────────────────────────┐
        self.max_vel = vel_max # self.max_vel -> crea un atributo de instancia y se le asigna el valor de vel_max   ╻─┘ 
        print("velocidad maxima:", self.max_vel)# utilizamos el atributo de instancia, almacena = valor de vel_max  ┃
corola = CocheEjemplo(100)# ─────────────────────────────────────────y lo almacena ─────────────────────────────────┛
                #     ↑ aca le pasamos los valores epecificos de esta instancia con el "esqueleto" de la clase coche
ford = CocheEjemplo(200)
mercedes = CocheEjemplo(300)   #definimos los distintos tipos de coches, partiendo del mismo "esqueleto"
amarok = CocheEjemplo(350)


# !!! De esta manera, agrupamos datos y funcionalidades, que despues podemos instanciar con diferentes valores. funcion: es reutilizable.