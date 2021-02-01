import random as rnd
from sympy import pretty, sqrt, cbrt
import json

numBase = rnd.randint(2,1000)
tipoDenominadorFracao = 2

if tipoDenominadorFracao == 2:
    # Verifica se o número é primo e, se for, gera um novo.
    qntMultiplos = 0

    while(qntMultiplos < 2):
        for count in range(2,numBase):
            if (numBase % count == 0):
                qntMultiplos += 1
        if(qntMultiplos < 2):
            numBase = rnd.randint(2,1000)
            qntMultiplos = 0

    resultado = sqrt(numBase)
    resultado = pretty(resultado)
    
else:
    # Verifica se o número é primo e, se for, gera um novo.
    qntMultiplos = 0

    while(qntMultiplos < 3):
        for count in range(2,numBase):
            if (numBase % count == 0):
                qntMultiplos += 1
        if(qntMultiplos < 3):
            numBase = rnd.randint(2,1000)
            qntMultiplos = 0

    resultado = cbrt(numBase)
    resultado = pretty(resultado)

listLetra = ["A","B","C","D","E"]
questaoCerta = rnd.choice(listLetra)
 
listAlternativas = [0,0,0,0,0]

# Insere a resposta certa na letra escolhida para ser certa, uma letra recebe a questão invertida e o resto recebe números aleatórios
for numLetra in range(0, 5):
    if questaoCerta == listLetra[numLetra]:
        listAlternativas[numLetra] = resultado
    else:
        numRandomTemporario = rnd.randint(2,3)

        if numRandomTemporario == 2:
            numRandomTemporario = rnd.randint(2,numBase)

            # Verifica se o número é primo e, se for, gera um novo.
            qntMultiplos = 0
            while(qntMultiplos < 2):
                for count in range(2, numRandomTemporario):
                    if (numRandomTemporario % count == 0):
                        qntMultiplos += 1
                if(qntMultiplos < 2):
                    numRandomTemporario = rnd.randint(2,numBase)
                    qntMultiplos = 0

            listAlternativas[numLetra] = sqrt(numRandomTemporario)
            listAlternativas[numLetra] = pretty(listAlternativas[numLetra])
        else:
            numRandomTemporario = rnd.randint(2,numBase)

            # Verifica se o número é primo e, se for, gera um novo.
            qntMultiplos = 0
            while(qntMultiplos < 3):
                for count in range(2, numRandomTemporario):
                    if (numRandomTemporario % count == 0):
                        qntMultiplos += 1
                if(qntMultiplos < 3):
                    numRandomTemporario = rnd.randint(2,numBase)
                    qntMultiplos = 0

            listAlternativas[numLetra] = cbrt(numRandomTemporario)
            listAlternativas[numLetra] = pretty(listAlternativas[numLetra])

# Dá duas tentativas para o indivíduo acertar
for numTentativa in range(2):
    print(f"A soma dos logaritmos de dois números na base {numBase} é 1/{tipoDenominadorFracao}. Determine o produto desses números.")
    print(f"a)\n{pretty(listAlternativas[0])}\n")
    print(f"b)\n{pretty(listAlternativas[1])}\n")
    print(f"c)\n{pretty(listAlternativas[2])}\n")
    print(f"d)\n{pretty(listAlternativas[3])}\n")
    print(f"e)\n{pretty(listAlternativas[4])}\n")
    respAluno = input()

    if(respAluno.upper() == questaoCerta):
        print("Parabéns!!! Acertou miserável!!!")
        break
    else:
        print("Resposta errada. Tente novamente")
            
        