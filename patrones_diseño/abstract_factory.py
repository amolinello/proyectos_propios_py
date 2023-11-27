from abc import ABC, abstractmethod

'''
Busca implementar una fabrica para crear familias de productos o clases que comparten elementos pero son distintos
ejemplo: Animales, estilos de muebles, etc.
En animales: Todos Comen, Todos duermen, pero algunos vuelan, algunos nada, etc. de manera abstracta se 
especifican las diferencias en las clases
'''

# Python tiene la libreria ABC para la creación de clases abstractas

# Productos Abstractos
class Silla(ABC):
    @abstractmethod
    def sentar(self):
        print('Metodo en Silla')

class Mueble(ABC):
    @abstractmethod
    def sentar(self):
        print('Metodo en Mueble')

# Productos
class SillaMadera(Silla):
    def sentar(self):
        print('Metodo en SillaMadera')

class MuebleCuero(Mueble):
    def sentar(self):
        print('Metodo en MuebleCuero')

# Fabrica abstracta
class FrabricaAbs(ABC):
    @abstractmethod
    def crear_silla(self):
        print('Metodo en crear silla')

    @abstractmethod
    def crear_mueble(self):
        print('Metodo en crear mueble')

# Fabrica de productos
class FabricaMadera(FrabricaAbs):
    def crear_silla(self):
        return SillaMadera
    
    # No tenemos muebles de madera en los productos
    def crear_mueble(self):
        print('- No tiene mueble de madera')
        return None

class FabricaCuero(FrabricaAbs):
    # No tenemos Sillas de cuero
    def crear_silla(self):
        print('- No tiene silla de cuero')
        return None
    
    def crear_mueble(self):
        return MuebleCuero

if __name__ == '__main__':
    fabricar_m = FabricaMadera()
    fabricar_c = FabricaCuero()

    silla_madera = fabricar_m.crear_silla()
    silla_cuero = fabricar_c.crear_silla()
    print(f'Silla de madera: {silla_madera}')
    print(f'Silla de cuero: {silla_cuero}')
    print('*'*20)

    mueble_madera = fabricar_m.crear_mueble()
    mueble_cuero = fabricar_c.crear_mueble()
    print(f'mueble de madera: {mueble_madera}')
    print(f'mueble de cuero: {mueble_cuero}')
    print('*'*20)

    silla_madera().sentar()
    mueble_cuero().sentar()
