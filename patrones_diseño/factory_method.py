'''
Las clases anteriormente creadas se queda igual sin modificaciones y se crea una subclase "Factory" que se encarga de
convertir en subclases a las clases ya creadas para facilitar el ingreso de codigo nuevo.

Usando este metodo es factible usar herencia, un ejemplo sería en transportes, donde Motocicleta y carro pueden compartir
elementos mecanicos como Motor, valvulas, etc. o fisicos como velocidad, aceleración, etc.

Utilizando este metodo se hace herencia entre los vehiculos y en caso de querer agregar más, se usa este metodo para no modificar el ya creado.

Ejemplo código:
{https://www.geeksforgeeks.org/factory-method-python-design-patterns/}
'''

# Python Code for factory method 
# it comes under the creational 
# Design Pattern
 
class FrenchLocalizer:
 
    """ it simply returns the french version """
 
    def __init__(self):
 
        self.translations = {"car": "voiture", "bike": "bicyclette",
                             "cycle":"cyclette"}
 
    def localize(self, msg):
 
        """change the message using translations"""
        return self.translations.get(msg, msg)
 
class SpanishLocalizer:
    """it simply returns the spanish version"""
 
    def __init__(self):
        self.translations = {"car": "coche", "bike": "bicicleta",
                             "cycle":"ciclo"}
 
    def localize(self, msg):
 
        """change the message using translations"""
        return self.translations.get(msg, msg)
 
class EnglishLocalizer:
    """Simply return the same message"""
 
    def localize(self, msg):
        return msg
 
def Factory(language ="English"):
 
    """Factory Method"""
    localizers = {
        "French": FrenchLocalizer,
        "English": EnglishLocalizer,
        "Spanish": SpanishLocalizer,
    }
 
    return localizers[language]()
 
if __name__ == "__main__":
 
    f = Factory("French")
    e = Factory("English")
    s = Factory("Spanish")
 
    message = ["car", "bike", "cycle"]
 
    for msg in message:
        print(f.localize(msg))
        print(e.localize(msg))
        print(s.localize(msg))