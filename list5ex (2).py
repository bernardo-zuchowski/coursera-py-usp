l = int(input("Digite a largura: "))
a = int(input("Digite a altura: "))
aux_l = l
aux_a = a

while aux_a > 0:
    while aux_l > 0:
        if aux_a == a or aux_a == 1:
            print("#", end="")
        else:
            if aux_l == l or aux_l == 1:
                print("#", end="")
            else:
                print(" ", end="")
        aux_l -= 1
    print('')
    aux_l = l
    aux_a -= 1