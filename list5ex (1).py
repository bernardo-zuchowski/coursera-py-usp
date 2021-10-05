l = int(input("Digite a largura: "))
a = int(input("Digite a altura: "))
aux = l

while a > 0:
    while aux > 0:
        print('#', end="")
        aux -= 1
    print('')
    aux = l
    a -= 1