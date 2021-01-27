import random as rnd
import math
import json

# insere um valor aleatório de 2 a 9 para ser a base.
numBase =  rnd.randint(2,9)

# insere dois logaritmandos aleatórios em uma lista 
listNumLogaritmando = [numBase ** rnd.randint(2,10), numBase ** rnd.randint(2,10)]

# Se os logaritmandos forem iguais, se é gerado novos
while(listNumLogaritmando[0] == listNumLogaritmando[1]):
    listNumLogaritmando = [numBase ** rnd.randint(2,10), numBase ** rnd.randint(2,10)]

# O decimais do resultado são reduzidos para 2 casas.
resultado = round(math.log(listNumLogaritmando[0], numBase)/math.log(listNumLogaritmando[1], numBase), 2)


listLetra = ["A","B","C","D","E"]
questaoCerta = rnd.choice(listLetra)
questaoInvertida = rnd.choice(listLetra)

# Verifica se a letra com a resposta certa e invertida são iguais 
repetida = True
while repetida == True: 
    if questaoCerta == questaoInvertida:
        questaoCerta = rnd.choice(listLetra)
        questaoInvertida = rnd.choice(listLetra)
    else: repetida = False
 
listAlternativas = [0,0,0,0,0]

# Insere a resposta certa na letra escolhida para ser certa, uma letra recebe a questão invertida e o resto recebe números aleatórios
for numLetra in range(0, 5):
    if questaoCerta == listLetra[numLetra]:
        listAlternativas[numLetra] += resultado
    elif questaoInvertida == listLetra[numLetra]:
        listAlternativas[numLetra] += round(math.log(listNumLogaritmando[1], numBase)/math.log(listNumLogaritmando[0], numBase), 2)
    else:
        listAlternativas[numLetra] += round(math.log(rnd.randint(2,10), rnd.randint(2,9))/math.log(rnd.randint(2,10), rnd.randint(2,9)), 2)

# Dá duas tentativas para o indivíduo acertar
for numTentativa in range(2):
    print(f"Determine o valor aproximado da razão entre os logaritmos de {listNumLogaritmando[0]} e {listNumLogaritmando[1]} numa base qualquer: ")
    print(f"a) {listAlternativas[0]}")
    print(f"b) {listAlternativas[1]}")
    print(f"c) {listAlternativas[2]}")
    print(f"d) {listAlternativas[3]}")
    print(f"e) {listAlternativas[4]}")
    respAluno = input()

    if(respAluno.upper() == questaoCerta):
        print("Parabéns!!! Acertou miserável!!!")
        break
    else:
        print("Resposta errada. Tente novamente")