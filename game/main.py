import random

mq = ("Piedra", "Tijera", "Papel")
def go_playgame():
    n = 0
    while n < 5:
        ipt = input("Cual sera su movimiento en esta ronda: ")
        usu = 0
        mac = 0
        comp = random.choice(mq)
        if comp == "Piedra" and ipt == "Papel":
            n += 1
            usu += 1
            print(f"La maquina eligio: {comp}")
            print(f"El usuario eligio: {ipt}")
            print(f"usu: {usu}, mac: {mac}")
            print(f"Gano el usuario")
        elif comp == "Papel" and inp == "Piedra":
            n += 1
            mac += 1
            print(f"La maquina eligio: {comp}")
            print(f"El usuario eligio: {ipt}")
            print(f"usu: {usu}, mac: {mac}")
            print(f"Gano la maquina")
        elif comp == "Piedra" and inp == "Tijera":
            n += 1
            mac += 1
            print(f"La maquina eligio: {comp}")
            print(f"El usuario eligio: {ipt}")
            print(f"usu: {usu}, mac: {mac}")
            print(f"Gano la maquina")
        elif comp == "Tijera" and ipt == "Piedra":
            n += 1
            usu += 1
            print(f"La maquina eligio: {comp}")
            print(f"El usuario eligio: {ipt}")
            print(f"usu: {usu}, mac: {mac}")
            print(f"Gano el usuario")
        elif comp == "Tijera" and ipt == "Papel":
            n += 1
            mac += 1
            print(f"La maquina eligio: {comp}")
            print(f"El usuario eligio: {ipt}")
            print(f"usu: {usu}, mac: {mac}")
            print("Gano la maquina")
        elif comp == "Papel" and ipt == "Tijera":
            n += 1
            usu += 1
            print(f"La maquina eligio: {comp}")
            print(f"El usuario eligio: {ipt}")
            print(f"usu: {usu}, mac: {mac}")
            print(f"Gano el usuario")
        elif comp == inp:
            n += 1
            print(f"La maquina eligio: {comp}")
            print(f"El usuario eligio: {ipt}")
            print(f"usu: {usu}, mac: {mac}")
            print("Es un empate")
        else:
            print("Algo salio mal")
            
    return "Se termino el juego"
        
go_playgame()