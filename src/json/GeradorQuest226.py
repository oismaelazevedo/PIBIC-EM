import random as rnd
from sympy import pretty, sqrt, cbrt
import json

numBase = rnd.randint(2,250)

qntHoraDada = rnd.randint(2,3)
qntHoraEsperada = rnd.randint(2,10)

while(qntHoraDada == qntHoraEsperada):
    qntHoraEsperada = rnd.randint(2,10)

if(qntHoraDada == 2):
    resultado = sqrt(numBase ** qntHoraEsperada)
else:
    resultado = cbrt(numBase ** qntHoraEsperada)

listLetra = ["A","B","C","D","E"]
questaoCerta = rnd.choice(listLetra)
questaoInvertida = rnd.choice(listLetra)

while(questaoCerta == questaoInvertida):
    questaoInvertida = rnd.choice(listLetra)
 
listAlternativas = [0,0,0,0,0]

# Insere a resposta certa na letra escolhida para ser certa, uma letra recebe a questão invertida e o resto recebe números aleatórios
for numLetra in range(0, 5):
    if questaoCerta == listLetra[numLetra]:
        listAlternativas[numLetra] = resultado
    elif questaoInvertida == listLetra[numLetra]:
        if(qntHoraDada == 2):
            listAlternativas[numLetra] = cbrt(numBase ** qntHoraEsperada)
        else:
            listAlternativas[numLetra] = sqrt(numBase ** qntHoraEsperada)  
    else:
        numRandomTemporario = rnd.randint(2,3)

        if numRandomTemporario == 2:
            numRandomTemporario = rnd.randint(0,1)

            if numRandomTemporario == 0:
                numRandomTemporario = rnd.randint(2, numBase)
                listAlternativas[numLetra] = sqrt(numRandomTemporario)
            else:
                numRandomTemporario = rnd.randint(2, numBase)
                listAlternativas[numLetra] = -sqrt(numRandomTemporario)
        else:
            numRandomTemporario = rnd.randint(0,1)

            if numRandomTemporario == 0:
                numRandomTemporario = rnd.randint(2, numBase)
                listAlternativas[numLetra] = cbrt(numRandomTemporario)
            else:
                numRandomTemporario = rnd.randint(2, numBase)
                listAlternativas[numLetra] = -cbrt(numRandomTemporario)

# Dá duas tentativas para o indivíduo acertar
for numTentativa in range(2):
    print(f'''O crescimento de uma certa cultura de bactérias obedece à função X(t) = C.{numBase}^kt, em que X(t) é o número de bactérias no tempo t >= 0; C, k são constantes positivas. 
    Verificando que o número inicial de bactérias X(0) é multiplicado por {numBase} em {qntHoraDada} horas, quantas se pode esperar no fim de {qntHoraEsperada} horas?''')
    print(f"a)\n{pretty(listAlternativas[0])} vezes o valor inicial\n")
    print(f"b)\n{pretty(listAlternativas[1])} vezes o valor inicial\n")
    print(f"c)\n{pretty(listAlternativas[2])} vezes o valor inicial\n")
    print(f"d)\n{pretty(listAlternativas[3])} vezes o valor inicial\n")
    print(f"e)\n{pretty(listAlternativas[4])} vezes o valor inicial\n")
    respAluno = input()

    if(respAluno.upper() == questaoCerta):
        print("Parabéns!!! Acertou miserável!!!")
        break
    else:
        print("Resposta errada. Tente novamente")