n = int( input( "Digite um número: " ) )

soma = 0

while ( n != 0 ):
    resto_n = n % 10
    n = n // 10
    soma = soma + resto_n

print( soma )