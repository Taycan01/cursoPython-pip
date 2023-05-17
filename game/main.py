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
            usu += 1
            print(f"La maquina eligio: {comp}")
            print(f"El usuario eligio: {ipt}")
            print(f"usu: {usu}, mac: {mac}")
            print(f"Gano el usuario")
        elif comp == "Papel" and inp == "Piedra":
            mac += 1
            print(f"La maquina eligio: {comp}")
            print(f"El usuario eligio: {ipt}")
            print(f"usu: {usu}, mac: {mac}")
            print(f"Gano la maquina")
        elif comp == "Piedra" and inp == "Tijera":
            mac += 1
            print(f"La maquina eligio: {comp}")
            print(f"El usuario eligio: {ipt}")
            print(f"usu: {usu}, mac: {mac}")
            print(f"Gano la maquina")
        elif comp == "Tijera" and ipt == "Piedra":
            usu += 1
            print(f"La maquina eligio: {comp}")
            print(f"El usuario eligio: {ipt}")
            print(f"usu: {usu}, mac: {mac}")
            print(f"Gano el usuario")
        elif comp == "Tijera" and ipt == "Papel":
            mac += 1
            print(f"La maquina eligio: {comp}")
            print(f"El usuario eligio: {ipt}")
            print(f"usu: {usu}, mac: {mac}")
            print("Gano la maquina")
        elif comp == "Papel" and ipt == "Tijera":
            usu += 1
            print(f"La maquina eligio: {comp}")
            print(f"El usuario eligio: {ipt}")
            print(f"usu: {usu}, mac: {mac}")
            print(f"Gano el usuario")
        elif comp == inp:
            print(f"La maquina eligio: {comp}")
            print(f"El usuario eligio: {ipt}")
            print(f"usu: {usu}, mac: {mac}")
            print("Es un empate")
        
        n += 1
        
go_playgame()