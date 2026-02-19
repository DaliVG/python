# Cuando se le añade __init__ es el constructor.
# Cuando a los atributos se le pone un _X se vuelven PROTECTED, por default esta public.
# Cuando se pone __X (doble guion bajo) es un PRIVATE

class Restaurante:

    def __init__(self, nombre, categoria, precio):
        self.__nombre = nombre
        self.__categoria = categoria
        self.__precio = precio

    def mostrarInfo(self):
        print(f'Nombre: {self.__nombre}, Categoria: {self.__categoria}, Precio: {self.__precio}.')

## GETTERS SETTERS

    def getPrecio(self):
        return self.__precio
    def getNombre(self):
        return self.__nombre
    def getCategoria(self):
        return self.__categoria

    def setPrecio(self, precio):
        self.__precio = precio
    def setNombre(self, nombre):
        self.__nombre = nombre
    def setCategoria(self, categoria):
        self.__categoria = categoria

restaurante = Restaurante('Pizzeria Mexico', 'Napolitano', '€€')
restauranteDos = Restaurante('Pizzeria Gran Tarajal', 'Independiente', '€€€')



restaurante.mostrarInfo()
restauranteDos.mostrarInfo()
