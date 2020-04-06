CUOTA_X_MINUTO_NACIONAL_LOCAL = 0.03
CUOTA_X_MINUTO_NACIONAL_LARGA_DISTANCIA = 0.06
CUOTA_X_MINUTO_INTERNACIONAL_LARGA_DISTANCIA = 0.1

def get_total(minutos, tipo_de_llamada, turno, total = 0):
    total_actual = 0

    if tipo_de_llamada == 1:
        minutos = minutos - 10

        if minutos < 0: 
            minutos = 0

        total_actual = CUOTA_X_MINUTO_NACIONAL_LOCAL * minutos

        if turno == 1 and not total_actual == 0:
            total_actual = total_actual * 2

        return total + total_actual
    elif tipo_de_llamada == 2:
        total_actual = CUOTA_X_MINUTO_NACIONAL_LARGA_DISTANCIA * minutos

        if turno == 1:
            total_actual = total_actual * 2

        return total + total_actual
    elif tipo_de_llamada == 3:
        total_actual = CUOTA_X_MINUTO_INTERNACIONAL_LARGA_DISTANCIA * minutos

        if turno == 1:
            total_actual = total_actual * 2

        return total + total_actual
    else:
        print("ERROR: Introdujo un tipo de llamada invalida.")

def run():
    total = 0
    nuevo_usuario = 1

    while True:
        if nuevo_usuario == 1:
            input("Ingrese su usuario: ")

        minutos = int(input("Cuantos minutos uso en esta llamda?"))
        tipo_de_llamada = int(input("""
        S E L E C C I O N E  E L  T I P O  D E  L L A M A D A
        [1] Llamada nacional local 
        [2] Llamada nacional larga distancia
        [3] Llamada internacional larga distancia
        """))
        turno = int(input("""
        S E L E C C I O N E  E L  T U R N O
        [1] Manana 
        [2] Tarde
        [3] Noche
        """))

        total = round(get_total(minutos, tipo_de_llamada, turno, total), 2)
        print(f"El total actual de su cuenta es {total}$")
        condicional = int(input("""

        Desea ingresar mas llamadas?
        [1] Si
        [2] No
        """))

        if condicional == 2:
            nuevo_usuario = int(input("""

            Desea ingresar otro usuario?
            [1] Si
            [2] No
            """))

            if nuevo_usuario == 2: 
                break
            else:
                total = 0
        elif condicional == 1:
            nuevo_usuario = 2

if __name__ == "__main__":
    print("B I E N V E N I D O")
    run()
