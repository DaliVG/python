#nombre = input('Cual es tu nombre: \r\n')

#print(f'Hola {nombre}')
preguntar = True;

while preguntar:
# con if else etc

    edad = input('Cual es tu edad: \r\n')
    edad = int(edad)   
    print(f'Tienes {edad} años')    

    if edad >= 18:
        print('Votas')
    else:
        preguntar = False
        print('No votas')