class Restaurante:

    def agregarRestaurante(self, nombre):
        print('Agregando...')
        self.nombre = nombre

    def mostrarInfo(self):
        print(f'Nombre: {self.nombre}')

restaurante = Restaurante()
restaurante.agregarRestaurante('Pizzeria Mexico')
restaurante.mostrarInfo()

restauranteDos = Restaurante()
restauranteDos.agregarRestaurante('Pizzeria Gran Tarajal')
restauranteDos.mostrarInfo()

print(f'Nombre restaurante: {restaurante.nombre}')
print(f'Nombre restaurante: {restauranteDos.nombre}')
