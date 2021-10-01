def computador_escolhe_jogada(n, m):
    jogada = m
    while jogada > 0:
        if (n - jogada) % (m+1) == 0:
            return jogada
        else:
            jogada -= 1
    return m

def usuario_escolhe_jogada(n, m):
    jogada = int(input('\nQuantas peças você vai tirar? \n'))
    while jogada <= 0 or jogada > m or jogada > n:
        print('\nOops! Jogada inválida! Tente de novo.\n')
        jogada = 0
        jogada = int(input('\nQuantas peças você vai tirar? \n'))
    return jogada


def partida():
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))
    
    if n % (m+1) == 0:
        print('\nVocê começa!\n')
        cpu_win = False
        while cpu_win != True:
            jogada = usuario_escolhe_jogada(n, m)
            n = n - jogada
            print('\nVoce tirou', jogada, "peças.")
            print('Agora restam', n, 'peças no tabuleiro.\n')
            jogada = computador_escolhe_jogada(n, m)
            n = n - jogada
            print('\nO computador tirou', jogada, "peças.")
            if n == 0:
                cpu_win == True
                break
            else:
                print('Agora restam', n, 'peças no tabuleiro.\n')
                print('\nÉ a sua vez!\n')
        print('\nFim do jogo! O computador ganhou!\n')
    
    else:
        print('\nComputador começa!\n')
        while n != 0:
            jogada = computador_escolhe_jogada(n, m)
            n = n - jogada
            print('\nO computador tirou', jogada, "peças.")
            print('Agora restam', n, 'peças no tabuleiro.\n')
            if n == 0:
                break
            elif n > 0:    
                print('\nÉ a sua vez!\n')
                jogada = usuario_escolhe_jogada(n, m)
                n = n - jogada
                print('\nVoce tirou', jogada, "peças.")
                print('Agora restam', n, 'peças no tabuleiro.\n')
            print('\nAgora é a vez do computador!\n')
        print('\nFim do jogo! O computador ganhou!\n')


def campeonato():
    n_partida = 1
    while n_partida < 4:
        print('\n**** Rodada', n_partida, '****\n')
        partida()
        n_partida +=1
    print('\n**** Final do campeonato! ****')
    print('Placar: Você 0 X 3 Computador\n')
        

print('Bem-vindo ao jogo do NIM!\n')
print('\n1 - para jogar uma partida isolada')
print('2 - para jogar um campeonato\n')
x = 0
while x != 1 or x != 2:
    x = int(input('Escolha modo de jogo: '))
    if x == 1:
        partida()
        break
    elif x == 2:
        campeonato()
        break