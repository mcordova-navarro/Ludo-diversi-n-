print("\033[;32m" + "LUDO DIVERTIDO")
import random
def tablero_1(x: str, y: str):
    global p
    print(f"\n## JUEGO ##\n \n# Ludo divertido #\n \n20 Meta \n19 \n18 \n17 \n16 \n15 \n14 Bonus \n13 \n12 \n11 \n10 \n9 \n8 Bonus \n7 \n6 \n5 \n4 \n3 \n2 \n1 \nINICIO {x} {y}")
    positionx = 0
    positiony = 0
    turno = 1
    z = True
    while z == True:
        L22 = "\n## JUEGO ##\n"
        L21 = "\n# Ludo divertido #\n"
        L20 = "\n20 Meta "
        L19 = "\n19 "
        L18 = "\n18 "
        L17 = "\n17 "
        L16 = "\n16 "
        L15 = "\n15 "
        L14 = "\n14 Bonus "
        L13 = "\n13 "
        L12 = "\n12 "
        L11 = "\n11 "
        L10 = "\n10 "
        L9 = "\n9 "
        L8 = "\n8 Bonus "
        L7 = "\n7 "
        L6 = "\n6 "
        L5 = "\n5 "
        L4 = "\n4 "
        L3 = "\n3 "
        L2 = "\n2 "
        L1 = "\n1 "
        L0 = "\nINICIO "

        if turno == 1:
            print("# Turno del jugador 1 #")
            print(" ")

            p = input("Ingrese el tipo de tiro que desea realizar:")
            validez = 0
            while validez == 0:
                if p == "normal":
                    validez += 1
                if p == "debil":
                    validez += 1
                if p == "fuerte":
                    validez += 1
                if validez == 0:
                    p = input("Elija entre el lanzamiento debil, normal o fuerte: ")

            if p == "normal":
                p = random.randint(1, 6)
            if p == "fuerte":
                p = random.randint(4, 6)
            if p == "debil":
                p = random.randint(1, 3)
            positionx += p
            if positionx == positiony:
                positiony = 0
            print(" ")
            print("DADO: Obtuvo el valor de", p)
            if p != 6:
                turno += 1
            if p == 6:
                turno += 0

        elif turno == 2:
            print("# Turno del jugador 2 #")
            print(" ")
            p = input("Ingrese el tipo de tiro que desea realizar:")
            validez = 0
            while validez == 0:
                if p == "normal":
                    validez += 1
                if p == "debil":
                    validez += 1
                if p == "fuerte":
                    validez += 1
                if validez == 0:
                    p = input("Elija entre el lanzamiento debil, normal o fuerte: ")

            if p == "normal":
                p = random.randint(1, 6)
            if p == "fuerte":
                p = random.randint(4, 6)
            if p == "debil":
                p = random.randint(1, 3)
            positiony += p
            if positiony == positionx:
                positionx = 0
            print(" ")
            print("DADO: Obtuvo el valor de", p)
            if p != 6:
                turno -= 1
            if p == 6:
                turno += 0

        if 20 < positionx:
            sobrante = positionx - 20
            positionx = 20 - sobrante
        if 20 < positiony:
            sobrante = positiony - 20
            positiony = 20 - sobrante

        if positionx == 0:
            L0 += x + " "
        if positiony == 0:
            L0 += y + " "

        if positionx == 1:
            L1 += x + " "
        if positiony == 1:
            L1 += y + " "

        if positionx == 2:
            L2 += x + " "
        if positiony == 2:
            L2 += y + " "

        if positionx == 3:
            L3 += x + " "
        if positiony == 3:
            L3 += y + " "

        if positionx == 4:
            L4 += x + " "
        if positiony == 4:
            L4 += y + " "

        if positionx == 5:
            L5 += x + " "
        if positiony == 5:
            L5 += y + " "

        if positionx == 6:
            L6 += x + " "
        if positiony == 6:
            L6 += y + " "

        if positionx == 7:
            L7 += x + " "
        if positiony == 7:
            L7 += y + " "

        if positionx == 8:
            L8 += x + " "
            if p != 6:
                turno -= 1
        if positiony == 8:
            L8 += y + " "
            if p != 6:
                turno += 1
        if positionx == 9:
            L9 += x + " "
        if positiony == 9:
            L9 += y + " "

        if positionx == 10:
            L10 += x + " "
        if positiony == 10:
            L10 += y + " "

        if positionx == 11:
            L11 += x + " "
        if positiony == 11:
            L11 += y + " "

        if positionx == 12:
            L12 += x + " "
        if positiony == 12:
            L12 += y + " "

        if positionx == 13:
            L13 += x + " "
        if positiony == 13:
            L13 += y + " "

        if positionx == 14:
            L14 += x + " "
            if p != 6:
                turno -= 1
        if positiony == 14:
            L14 += y + " "
            if p != 6:
                turno += 1

        if positionx == 15:
            L15 += x + " "
        if positiony == 15:
            L15 += y + " "

        if positionx == 16:
            L16 += x + " "
        if positiony == 16:
            L16 += y + " "

        if positionx == 17:
            L17 += x + " "
        if positiony == 17:
            L17 += y + " "

        if positionx == 18:
            L18 += x + " "
        if positiony == 18:
            L18 += y + " "

        if positionx == 19:
            L19 += x + " "
        if positiony == 19:
            L19 += y + " "

        if positionx == 20:
            L20 += x + " "
        if positiony == 20:
            L20 += y + " "


        print(L22, L21, L20, L19, L18, L17, L16, L15, L14, L13, L12, L11, L10, L9, L8, L7, L6, L5, L4, L3, L2, L1, L0)
        if positionx == 20:
            print("")
            print(f"El ganador es el jugador {x}")
            print("Se termino el Juego, hasta la proxima")
            z = False
        if positiony == 20:
            print("")
            print(f"El ganador es el jugador {y}!")
            print("Se termino el Juego, hasta la proxima")
            z = False
winners = ''
def tablero_2(x: str):
    global t
    global winners
    y = "CPU"
    print(f"\n## JUEGO ##\n \n# Ludo divertido #\n \n20 Meta \n19 \n18 \n17 \n16 \n15 \n14 Bonus \n13 \n12 \n11 \n10 \n9 \n8 Bonus \n7 \n6 \n5 \n4 \n3 \n2 \n1 \nINICIO {x} {y}")
    positionx = 0
    positiony = 0
    turno = 1
    z = True
    while z == True:
        L22 = "\n## JUEGO ##\n"
        L21 = "\n# Ludo divertido #\n"
        L20 = "\n20 Meta "
        L19 = "\n19 "
        L18 = "\n18 "
        L17 = "\n17 "
        L16 = "\n16 "
        L15 = "\n15 "
        L14 = "\n14 Bonus "
        L13 = "\n13 "
        L12 = "\n12 "
        L11 = "\n11 "
        L10 = "\n10 "
        L9 = "\n9 "
        L8 = "\n8 Bonus "
        L7 = "\n7 "
        L6 = "\n6 "
        L5 = "\n5 "
        L4 = "\n4 "
        L3 = "\n3 "
        L2 = "\n2 "
        L1 = "\n1 "
        L0 = "\nINICIO "

        if turno == 1:
            print("# Turno del jugador #")
            print(" ")
            t = input("Ingrese el tipo de tiro que desea realizar:")
            interfaz_validez = 0
            while interfaz_validez == 0:
                if t == "normal":
                    interfaz_validez +=1
                if t == "debil":
                    interfaz_validez +=1
                if t == "fuerte":
                    interfaz_validez += 1
                if interfaz_validez == 0:
                    t = input("Elija entre el lanzamiento debil, normal o fuerte: ")



            if t == "normal":
                t = random.randint(1, 6)
            if t == "fuerte":
                t = random.randint(4, 6)
            if t == "debil":
                t = random.randint(1, 3)
            positionx += t
            if positionx == positiony:
                positiony = 0
            print(" ")
            print("DADO: Obtuvo el valor de", t)
            if t != 6:
                turno += 1
            if t == 6:
                turno += 0

        elif turno == 2:
            print("# Turno de la CPU #")
            print(" ")
            t = random.randint(1, 6)
            positiony += t
            if positiony == positionx:
                positionx = 0
            print(" ")
            print("DADO: Obtuvo el valor de", t)
            if t != 6:
                turno -= 1
            if t == 6:
                turno += 0
        if 20 < positionx:
            sobrante = positionx - 20
            positionx = 20 - sobrante
        if 20 < positiony:
            sobrante = positiony - 20
            positiony = 20 - sobrante

        if positionx == 0:
            L0 += x + " "
        if positiony == 0:
            L0 += y + " "

        if positionx == 1:
            L1 += x + " "
        if positiony == 1:
            L1 += y + " "

        if positionx == 2:
            L2 += x + " "
        if positiony == 2:
            L2 += y + " "

        if positionx == 3:
            L3 += x + " "
        if positiony == 3:
            L3 += y + " "

        if positionx == 4:
            L4 += x + " "
        if positiony == 4:
            L4 += y + " "

        if positionx == 5:
            L5 += x + " "
        if positiony == 5:
            L5 += y + " "

        if positionx == 6:
            L6 += x + " "
        if positiony == 6:
            L6 += y + " "

        if positionx == 7:
            L7 += x + " "
        if positiony == 7:
            L7 += y + " "

        if positionx == 8:
            L8 += x + " "
            if t != 6:
                turno -= 1
        if positiony == 8:
            L8 += y + " "
            if t != 6:
                turno += 1
        if positionx == 9:
            L9 += x + " "
        if positiony == 9:
            L9 += y + " "

        if positionx == 10:
            L10 += x + " "
        if positiony == 10:
            L10 += y + " "

        if positionx == 11:
            L11 += x + " "
        if positiony == 11:
            L11 += y + " "

        if positionx == 12:
            L12 += x + " "
        if positiony == 12:
            L12 += y + " "

        if positionx == 13:
            L13 += x + " "
        if positiony == 13:
            L13 += y + " "

        if positionx == 14:
            L14 += x + " "
            if t != 6:
                turno -= 1
        if positiony == 14:
            L14 += y + " "
            if t != 6:
                turno += 1

        if positionx == 15:
            L15 += x + " "
        if positiony == 15:
            L15 += y + " "

        if positionx == 16:
            L16 += x + " "
        if positiony == 16:
            L16 += y + " "

        if positionx == 17:
            L17 += x + " "
        if positiony == 17:
            L17 += y + " "

        if positionx == 18:
            L18 += x + " "
        if positiony == 18:
            L18 += y + " "

        if positionx == 19:
            L19 += x + " "
        if positiony == 19:
            L19 += y + " "

        if positionx == 20:
            L20 += x + " "
        if positiony == 20:
            L20 += y + " "

        print(L22, L21, L20, L19, L18, L17, L16, L15, L14, L13, L12, L11, L10, L9, L8, L7, L6, L5, L4, L3, L2, L1, L0)

        if positionx == 20:
            print("")
            print(f"El ganador es el jugador {x}")
            print("Se termino el Juego, hasta la proxima")
            z = False
            winners += f"-{x}\n"
        if positiony == 20:
            print("")
            print("Jaja, te gane!")
            print("Se termino el Juego, hasta la proxima")
            z = False
def interfaz():
    opcion_menu_str = input("## MENU DE INICIO ##  \n \n 1. Empezar el juego \n 2. Record \n 3. Salir \n \n ###################### \n \n Seleccione una opcion: ")

    interfaz_validez = False
    while interfaz_validez == False:
        if opcion_menu_str == "1":
            interfaz_validez = True
        if opcion_menu_str == "2":
            interfaz_validez = True
        if opcion_menu_str == "3":
            interfaz_validez = True
        if interfaz_validez == False:
            opcion_menu_str = input("Elija entre las opciones 1, 2 y 3: ")

    opcion_menu = int(opcion_menu_str)

    if opcion_menu == 1:

        tipo_juego_str = input("\n## TIPO DE JUEGO ## \n \n 1. 1 VS 1 \n \n 2. 1 VS CPU \n \n ###################### \n \n Seleccione una opcion: ")

        interfaz_validez = False
        while interfaz_validez == False:
            if tipo_juego_str == "1":
                interfaz_validez = True
            if tipo_juego_str == "2":
                interfaz_validez = True
            if interfaz_validez == False:
                tipo_juego_str = input("Elija entre las opciones 1 y 2: ")
        tipo_juego = int(tipo_juego_str)
        if tipo_juego == 1:

            jugador1 = input("\n## Jugadores  ## \n \n Ingrese el nombre del jugador 1: ")
            jugador2 = input(" Ingrese el nombre del jugador 2: ")

            print("\n ######################")
            tablero_1(jugador1, jugador2)

        elif tipo_juego == 2:

            jugador1 = input("\n## Jugadores  ## \n \n Ingrese el nombre del jugador 1: ")
            print("\n ######################")
            tablero_2(jugador1)
        return False
    elif opcion_menu == 2:
        print("## RECORD ##")
        print("Los ganadores anteriores contra la CPU fueron:")
        print(winners)
        return False
    elif opcion_menu == 3:
        print("Por que cierras el videojuego 😭😭😭😭😭")
        return True

l = False
while l == False:
    interfaz()
    if interfaz() == True:
        l = True