playlist = {}

playlist['canciones'] = []

def app():
    agregarPlaylist = True

    while agregarPlaylist:
        nombrePlaylist = input('¿Cómo desdeas llamarla? \r\n')

        if nombrePlaylist:
            playlist['nombre'] = nombrePlaylist
            agregarPlaylist = False
            agregarCanciones()

def agregarCanciones():
    print('Agregar canciones...')
    agregarCancion = True

    while agregarCancion:
        nombrePlaylist = playlist['nombre']
        pregunta = f'Agrega caciones para la playlist {nombrePlaylist}: \r\n'
        pregunta += 'Escribe "X" para dejar de agregar canciones...'

        cancion = input(pregunta)

        if cancion == 'X':
            mostrarLista()
            print('Esta es tu lista. Muchas graciaaaas')
            agregarCancion = False
        else:
            playlist['canciones'].append(cancion)

def mostrarLista():
    nombrePlaylist = playlist['nombre']
    print(f'Playlist: {nombrePlaylist}\r\n')
    print(f'Canciones: \r\n')
    for cancion in playlist['canciones']:
        print(cancion)


app()