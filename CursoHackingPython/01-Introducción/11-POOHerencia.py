class Coche ():
    """esta clase representa un coche"""
    def __init__(self, modelo, potencia, consumo):
        """Inicializa los atributos de instancia.
        Argumentos posicionales 
        modelo ->  string que representa el modelo del coche
        potencia -> int que representa la potencia en cv
        consumo -> int que representa el consumo en litros/100km
        """
        self.modelo = modelo
        self.potencia = potencia 
        self.consumo = consumo 
        self.km_actuales = 0 

    def especificaciones(self): 
        """Muestra las especifciaciones del coche"""  
        print("modelo:", self.modelo ,                
            f"\n Potencia: {self.potencia} cv",     
            f"\n Consumo: {self.consumo} l/100km",   
            f"\n Kilometros actuales:", self.km_actuales)    
    def actualizar_kilometros(self, kilometros):
        """ Actualiza los km actuales del coche"""
        if kilometros > self.km_actuales:
            self.km_actuales = kilometros
        else:
            print("ERROR")


#con la funcion #!help(Coche) -> podemos ver como se utiliza #   
#help(Coche) # muestra todas las especificaciones que """ escribimos dentro de"""           

#? INSTANCIAMOS LA CLASE Y LE PASAMOS VALORES                                               
mercedes = Coche("mercedes", 1, 200)                                                       
#? si nosotros queremos modificar el valor de "mercedes"                                    
mercedes.km_actuales = 2500 #modificamos el atributo de instancia                           
mercedes.especificaciones()                                                              

#* GETTER: Y SETTER                                                                        
# atributos que se deben modificar o es posible q se modifique en el futuro                                                                              
#* getter -> obtener un valor en concreto sin tener que invocar directamente el nombre del atributo
#* setter -> ponerle un nuevo valor a un atributo de instancia sin invocar directamente el nombre del atributo
mercedes.actualizar_kilometros(20000)
mercedes.actualizar_kilometros(2000) #ERROR, porque no se pueden tener menos km q ↑

#* si nosotros queremos saber la cantidad de METODOS asociados a una clase utilizamos ↓
print(dir(Coche))
#obtenemos nuestros metodos y los indicados con "__init__" estos son creados por defecto


#!    HERENCIA
#Mecanismos que se utilizan para crear jerarquias de #* clases que estan relacionadas
# comparten una interfaz comun "clase padre" y le hereda a las "clases hijo"

class CocheElectrico(Coche):  # HEREDA LA FUNCIONALIDAD DE COCHE, AL INDICARLO ENTRE (Coche)
    """esta clase representa un coche electrico"""
    def __init__(self, modelo, potencia, consumo):          #como hereda la funcionalidad de la clase coche, nosotros debemos modificarlo o agregarle. 
        super().__init__(modelo, potencia, consumo)
    def especificaciones(self): 
        """Muestra las especifciaciones del coche"""  
        print("modelo:", self.modelo ,                
            f"\n Potencia: {self.potencia} cv",     
            f"\n Consumo: {self.consumo} kWh /100km",       #ya que es un coche electrico es necesaria esta aclaración 
            f"\n Kilometros actuales:", self.km_actuales)    
        
tesla = CocheElectrico("tesla", "15", "200")