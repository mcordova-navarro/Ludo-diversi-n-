import random
import re
winners_total = ''
winners1 = ''
winners2 = ''
winners3 = ''
winners4 = ''
winners5 = ''
winners6 = ''
winners7 = ''
winners8 = ''
winners9 = ''
winners10 = ''
winners11 = ''
winners12= ''
print("\033[;32m" + "LUDO DIVERTIDO")
def juego():
    def validar_nombre(nombre: str) -> bool:
        if len(nombre) < 3:
            return False
        if not nombre.isalpha():
            return False
        return True

    def validar_correo(correo: str) -> bool:
        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(patron, correo) is not None

    def validar_fecha(fecha: str) -> bool:
        patron = r"^\d{2}-\d{4}$"
        return bool(re.match(patron, fecha))

    def rendirse():
        print("\nSe termino el Juego, hasta la proxima\n")
        z = False
        interfaz()

    def tablero_1(x: str, winners_total=''):
        global t
        global winners1
        global winners2
        global winners3
        global winners4
        global winners5
        global winners6
        global winners7
        global winners8
        global winners9
        global winners10
        global winners11
        global winners12
        y = "Yarascabot"
        print(
            f"\n## JUEGO ##\n \n# Ludo divertido #\n \n20 Meta \n19 \n18 \n17 \n16 \n15 \n14 Bonus \n13 \n12 \n11 \n10 \n9 \n8 Bonus \n7 \n6 \n5 \n4 \n3 \n2 \n1 \nINICIO {x} {y}")
        positionx = 0
        positiony = 0
        turno = 1
        pasos = 0
        z = True
        while z:
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
                t = input("Ingrese el tipo de tiro que desea realizar: ")
                while t not in ["normal", "debil", "fuerte", "rendirse", "empezar de nuevo"]:
                    t = input("Elija entre el lanzamiento debil, normal o fuerte: ")

                if t == "normal":
                    t = random.randint(1, 6)
                elif t == "fuerte":
                    t = random.randint(4, 6)
                elif t == "debil":
                    t = random.randint(1, 3)
                elif t == "rendirse":
                    rendirse()
                elif t == "empezar de nuevo":
                    print("Se termino el Juego, ahora se empieza uno nuevo...")
                    tablero_1(jugador1)
                pasos = pasos + 1
                positionx += t
                if positionx == positiony:
                    positiony = 0
                print(" ")
                print("DADO: Obtuvo el valor de", t)
                if t != 6:
                    turno += 1

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

            if positionx > 20:
                sobrante = positionx - 20
                positionx = 20 - sobrante
            if positiony > 20:
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

            print(L22, L21, L20, L19, L18, L17, L16, L15, L14, L13, L12, L11, L10, L9, L8, L7, L6, L5, L4, L3, L2, L1,
                  L0)

            if positionx == 20:
                print("")
                print(f"馃コEl ganador es el jugador {x}馃コ")
                print("Se termino el Juego, hasta la pro2xima")
                z = False
                if 1 >0:
                    winners_total += f"-Nombre: {x}\aFecha: {fecha}\aPasos: {pasos}\n"
                if fecha[0:2] == "01":
                    winners1 += f"-Nombre: {x}\aFecha: {fecha}\aPasos: {pasos}\n"
                if fecha[0:2] == "02":
                    winners2 += f"-Nombre: {x}\aFecha: {fecha}\aPasos: {pasos}\n"
                if fecha[0:2] == "03":
                    winners3 += f"-Nombre: {x}\aFecha: {fecha}\aPasos: {pasos}\n"
                if fecha[0:2] == "04":
                    winners4 += f"-Nombre: {x}\aFecha: {fecha}\aPasos: {pasos}\n"
                if fecha[0:2] == "05":
                    winners5 += f"-Nombre: {x}\aFecha: {fecha}\aPasos: {pasos}\n"
                if fecha[0:2] == "06":
                    winners6 += f"-Nombre: {x}\aFecha: {fecha}\aPasos: {pasos}\n"
                if fecha[0:2] == "07":
                    winners7 += f"-Nombre: {x}\aFecha: {fecha}\aPasos: {pasos}\n"
                if fecha[0:2] == "08":
                    winners8 += f"-Nombre: {x}\aFecha: {fecha}\aPasos: {pasos}\n"
                if fecha[0:2] == "09":
                    winners9 += f"-Nombre: {x}\aFecha: {fecha}\aPasos: {pasos}\n"
                if fecha[0:2] == "10":
                    winners10 += f"-Nombre: {x}\aFecha: {fecha}\aPasos: {pasos}\n"
                if fecha[0:2] == "11":
                    winners11 += f"-Nombre: {x}\aFecha: {fecha}\aPasos: {pasos}\n"
                if fecha[0:2] == "12":
                    winners12 += f"-Nombre: {x}\aFecha: {fecha}\aPasos: {pasos}\n"
            if positiony == 20:
                print("")
                print("Jaja, te gane, el Yarascabot nunca pierde!")
                print("Se termino el Juego, hasta la proxima")
                z = False

    def interfaz():
        opcion_menu_str = input(
            "## MENU DE INICIO ##  \n \n 1. Empezar el juego \n 2. Record \n 3. Info de jugadores \n 4. Salir \n \n ###################### \n \n Seleccione una opcion: ")

        while opcion_menu_str not in ["1", "2", "3", "4"]:
            opcion_menu_str = input("Elija entre las opciones 1, 2, 3 y 4: ")

        opcion_menu = int(opcion_menu_str)

        if opcion_menu == 1:
            global jugador1
            global fecha
            jugador1 = input("\n## Registro de jugador ## \n\nIngrese su nombre: ")
            while not validar_nombre(jugador1):
                print("El nombre debe tener al menos 3 caracteres y solo contener letras.")
                jugador1 = input("Ingrese su nombre: ")

            correo = input("Ingrese su correo: ")
            while not validar_correo(correo):
                print("Correo inválido. Inténtelo nuevamente.")
                correo = input("Ingrese su correo: ")

            fecha = input("Ingrese la fecha (mm-yyyy): ")
            while not validar_fecha(fecha):
                print("Fecha inválida. Ingrese la fecha nuevamente.")
                fecha = input("Ingrese la fecha: ")

            tablero_1(jugador1)

            return False
        elif opcion_menu == 2:
            print("## RECORD ##")
            menu_record_str = input("\n 1. Lista de ganadores \n 2. Ganadores del mes \n \n ############################ \n \n Seleccione una opcion: ")
            while menu_record_str not in ["1", "2"]:
                menu_record_str = input("Elija entre las opciones 1 y 2: ")

            menu_record = int(opcion_menu_str)
            if menu_record == 1:
                print("####Lista de ganadores:####")
                print(winners_total)
            elif menu_record == 2:
                print("Ingrese el mes a buscar (mm):")
                mes = input("M:")
                if mes == "Enero".lower():
                    print("Los ganadores anteriores contra la CPU en el mes 1 fueron:")
                    print(winners1)
                elif mes == "Febrero".lower():
                    print("Los ganadores anteriores contra la CPU en el mes 2 fueron:")
                    print(winners2)
                elif mes == "Marzo".lower():
                    print("Los ganadores anteriores contra la CPU mes 3 fueron:")
                    print(winners3)
                elif mes == "Abril".lower():
                    print("Los ganadores anteriores contra la CPU en el mes 4 fueron:")
                    print(winners4)
                elif mes == "Mayo".lower():
                    print("Los ganadores anteriores contra la CPU en el mes 5 fueron:")
                    print(winners5)
                elif mes == "Junio".lower():
                    print("Los ganadores anteriores contra la CPU en el mes 6 fueron:")
                    print(winners6)
                elif mes == "Julio".lower():
                    print("Los ganadores anteriores contra la CPU en el mes 7 fueron:")
                    print(winners7)
                elif mes == "Agosto".lower():
                    print("Los ganadores anteriores contra la CPU en el mes 8 fueron:")
                    print(winners8)
                elif mes == "Septiembre".lower():
                    print("Los ganadores anteriores contra la CPU en el mes 9 fueron:")
                    print(winners9)
                elif mes == "Octubre".lower():
                    print("Los ganadores anteriores contra la CPU en el mes 10 fueron:")
                    print(winners10)
                elif mes == "Noviembre".lower():
                    print("Los ganadores anteriores contra la CPU en el mes 11 fueron:")
                    print(winners11)
                elif mes == "Diciembre".lower():
                    print("Los ganadores anteriores contra la CPU en el mes 12 fueron:")
                    print(winners12)
                elif mes == "Total".lower():
                    print("Los ganadores anteriores contra la CPU en total fueron:")
                    print(winners_total)
        elif opcion_menu == 3:
            print("#### Info de jugadores ####")
            input("")
        elif opcion_menu == 4:
            print("Por qué cierras el videojuego 😭😭😭😭😭")
            return True

    l = False
    while not l:
        l = interfaz()


juego()