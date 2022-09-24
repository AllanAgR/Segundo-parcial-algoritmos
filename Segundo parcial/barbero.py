import os
espera = []
sillon = []
silla = []

def error23():
    print("No hay suficientes sillas")
    input()

def ordenado():
    print(" \nIngresa tu nombre \n ")
    x = input()

    if len(silla) == 0:
        silla.append(x)
    elif len(sillon) == 3:
        espera.append(x)
    elif len(sillon) < 3:
        sillon.append(x)

    print(" \n El Cliente fué registrado de manera exitosa! ")
    input()

def corte():
    if len(silla) == 1:
        a = silla.pop()
        print(" \n--Barbero: Adios " + a + " ! Gracias por venir!")
        print("--" + a + ": Adios!!")
        input()

        if len(sillon) > 0:
            y = sillon.pop(0)
            silla.append(y)
            print("--Barbero: Pasa adelante " + y + " sientate ")
            print("--" + y + ": Lo mismo de siempre")
            input()

        if len(espera) > 0:
            w = espera.pop(0)
            print(" \n--Barbero: Pasa adentro " + w + " ya hay un lugar libre en el sillon para ti! Sientate! ya te tocará tu turno...")
            sillon.append(w)
        input()
    else:
        print(" \n--Barbero: Ningun cliente por atender! Hora de una siesta... \n zZZ zZZ zZZ ...")
        input()
def estado():
    if len(silla) == 1:
        x = str(len(silla))
        print(" \nEl Barbero se encuentra cortandole el cabello a " + x + " cliente")
        input()
    elif len(silla) == 0:
        print(" \nEl Barbero no tiene clientes! Se encuentra tomando una siesta...")
        input()
    elif len(silla) > 1:
        error23()

def clientess():
    a = len(silla)
    b = len(sillon)
    c = str(a + b)
    a = str(a)
    b = str(b)

    print(" \nEn la Barberia en este momento se encuentran " +  c  + " clientes " + a + " cliente en la silla y " + b + " clientes en el sillon de espera")
    input()

def  esperaa():
    a = str(len(espera))

    print(" \n hay un total de " + a + " esperando su turno fuera de la Barberia...")
    input()

while True: 
    os.system('cls')
    print("Barberia DonFigaro \n \nQue deseas hacer? \n  ")
    print("1. Ingresar Cliente")
    print("2. Despertar al Barbero")
    print("3. Revisar Estado del Barbero")
    print("4. Clientes sentados")
    print("5. Lista de Espera")
    print("6. SALIR")

    opcion = int(input())

    if opcion == 1:
        ordenado()
    elif opcion == 2:
        corte()
    elif opcion == 3:
        estado()
    elif opcion == 4:
        clientess()
    elif opcion == 5:
        esperaa()
    elif opcion == 6:
        print(" \ngracias-")
        input()
        break
    else:
        print(" ")
        input("Presione tecla e Intentelo nuevamente")