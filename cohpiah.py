import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    sab = 0
    for i in range(0,6):
        sab = sab + (abs(as_a[i] - as_b[i]))
    return sab / 6

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    # Tamanho médio de palavra é a soma dos tamanhos das palavras dividida pelo número total de palavras.
    sentencas = separa_sentencas(texto)
    frases = []
    palavras = []
    lista_palavras = []
    soma_tam_p = 0
    soma_caract_sent = 0
    soma_caract_frase = 0

    for sentenca in sentencas:
        soma_caract_sent = soma_caract_sent + len(sentenca) ##
        lista_frases = separa_frases(sentenca)
        for f in lista_frases:
            frases.append(f)
    
    for f in frases:
        soma_caract_frase = soma_caract_frase + len(f) ##
        lista_palavras = separa_palavras(f)
        for p in lista_palavras:
            palavras.append(p)

    for p in palavras:
        soma_tam_p = soma_tam_p + len(p)

    media_tam_p = soma_tam_p / len(palavras)
    rel_tt = n_palavras_diferentes(lista_palavras) / len(lista_palavras)
    raz_hapax = n_palavras_unicas(lista_palavras) / len(lista_palavras)
    tam_medio_sent = soma_caract_sent / len(sentencas)
    complex_sent = len(frases) / len(sentencas)
    tam_medio_f = soma_caract_frase / len(frases)

    ass = [media_tam_p, rel_tt, raz_hapax,
           tam_medio_sent, complex_sent, tam_medio_f]
    
    return ass


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    x = []

    for texto in textos:
        as_a = calcula_assinatura(texto)
        x.append(compara_assinatura(as_a, ass_cp))

    menor = x[0]
    cohpiah = 1

    for i in range(1, len(x)):
        if (menor > x[i]):
            cohpiah = i
    return cohpiah

def main():        
    assinatura = le_assinatura()
    textos = le_textos()
    cohpiah = avalia_textos(textos, assinatura)
    print("O autor do texto", cohpiah, "está infectado com COH-PIAH")

main()