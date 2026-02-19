# Cuando se le añade __init__ es el constructor.
# Cuando a los atributos se le pone un _X se vuelven PROTECTED, por default esta public.
# Cuando se pone __X (doble guion bajo) es un PRIVATE

class Restaurante:

    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    def mostrarInfo(self):
        print(f'Nombre: {self.__nombre}, Categoria: {self.__categoria}, Precio: {self.__precio}.')

## GETTERS SETTERS

    def getPrecio(self):
        return self.precio
    def getNombre(self):
        return self.nombre
    def getCategoria(self):
        return self.categoria

    def setPrecio(self, precio):
        self.precio = precio
    def setNombre(self, nombre):
        self.nombre = nombre
    def setCategoria(self, categoria):
        self.categoria = categoria

## HERENCIA

class Hotel(Restaurante):
    def __init__(self, nombre, categoria, precio, piscina):
        super().__init__(nombre, categoria, precio)
        self.__piscina = piscina

    def mostrarInfo(self):
        print(f'Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.precio}, Piscina: {self.__piscina}')


    def getPiscina(self):
        return self.__piscina

    def setPiscina(self, piscina):
        self.__piscina = piscina

hotel = Hotel('Hotel POO', '5 Estrellas', '200', 'Si')
hotel.mostrarInfo()

