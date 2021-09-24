#def computador_escolhe_jogada(n, m)

#def usuario_escolhe_jogada(n, m)

cpu = computador_escolhe_jogada(n, m)
user = usuario_escolhe_jogada(n, m)
defnm = def_nm(n, m)

def main(x):
    x = 0
    while x == 1 or x == 2:
        x = int(input("Bem-vindo ao jogo do NIM! Escolha: /n/n 1 - para jogar uma partida isolada /n 2 - para jogar um campeonato"))
        if x == 1:
            return partida()
        else: 
            return campeonato()

def def_nm(n, m):
    n = int(input("Quantas peças?"))
    m = int(input("Limite de peças por jogada?"))
    if main(1):
        return partida
    else:
        return campeonato

def partida():
    print("Você escolheu uma partida!")
    return def_nm
    if n * m + 1:
        print("Você começa!")
        return user
    else:
        print("Computador começa!")
        return cpu
    
def campeonato():
    print("Você escolheu uma partida!")
    return def_nm
