jugador = {}

jugador['nombre'] = 'Dali'
jugador['puntaje'] = 1000
jugador['posicion'] = 'Centro campista'

print(jugador)

print(jugador.get('consola', 'No existe valor.'))

for llave, valor in jugador.items():
    print(llave, valor)