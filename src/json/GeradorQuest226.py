import random as rnd
from sympy import pretty, sqrt, cbrt, symbols
import json


for k in range(200):

    questoes = open('questao{}-226.json'.format(k+1), 'w')
    numBase = rnd.randint(2,1000)

    qntHoraDada = rnd.randint(2,3)
    qntHoraEsperada = rnd.randint(2,10)

    while(qntHoraDada == qntHoraEsperada):
        qntHoraEsperada = rnd.randint(2,10)

    if(qntHoraDada == 2):
        resultado = sqrt(numBase ** qntHoraEsperada)
        resultado = pretty(resultado)
    else:
        resultado = cbrt(numBase ** qntHoraEsperada)
        resultado = pretty(resultado)

    C, k, t = symbols("C k t")

    listLetra = ["A","B","C","D","E"]
    questaoCerta = rnd.choice(listLetra)
    questaoInvertida = rnd.choice(listLetra)

    while(questaoCerta == questaoInvertida):
        questaoInvertida = rnd.choice(listLetra)
    
    listAlternativas = [0,0,0,0,0]
    isCorrect = ['','','','','']
    howGenerated = ['','','','','']

    # Insere a resposta certa na letra escolhida para ser certa, uma letra recebe a questão invertida e o resto recebe números aleatórios
    for numLetra in range(0, 5):
        if questaoCerta == listLetra[numLetra]:
            listAlternativas[numLetra] = resultado
            isCorrect[numLetra] = "Sim"
            howGenerated[numLetra] = "nenhum"
        elif questaoInvertida == listLetra[numLetra]:
            if(qntHoraDada == 2):
                numRandomTemporario = rnd.randint(0,1)

                if numRandomTemporario == 0:

                    listAlternativas[numLetra] = cbrt(numBase ** qntHoraEsperada)
                    listAlternativas[numLetra] = pretty(listAlternativas[numLetra])
                    isCorrect[numLetra] = "Nao"
                    howGenerated[numLetra] = "invertida e positiva"
                else:
                    listAlternativas[numLetra] = -cbrt(numBase ** qntHoraEsperada)
                    listAlternativas[numLetra] = pretty(listAlternativas[numLetra])
                    isCorrect[numLetra] = "Nao"
                    howGenerated[numLetra] = "invertida e negativa"
            else:
                numRandomTemporario = rnd.randint(0,1)

                if numRandomTemporario == 0:

                    listAlternativas[numLetra] = sqrt(numBase ** qntHoraEsperada)
                    listAlternativas[numLetra] = pretty(listAlternativas[numLetra]) 
                    isCorrect[numLetra] = "Nao"
                    howGenerated[numLetra] = "invertida e positiva"
                else:
                    listAlternativas[numLetra] = -sqrt(numBase ** qntHoraEsperada)
                    listAlternativas[numLetra] = pretty(listAlternativas[numLetra]) 
                    isCorrect[numLetra] = "Nao"
                    howGenerated[numLetra] = "invertida e negativa"
        else:
            numRandomTemporario = rnd.randint(2,3)

            if numRandomTemporario == 2:
                numRandomTemporario = rnd.randint(0,1)

                if numRandomTemporario == 0:
                    numRandomTemporario = rnd.randint(2, numBase)
                    listAlternativas[numLetra] = sqrt(numRandomTemporario)
                    listAlternativas[numLetra] = pretty(listAlternativas[numLetra])
                    isCorrect[numLetra] = "Nao"
                    howGenerated[numLetra] = "gerada aleatoriamente e positiva"
                else:
                    numRandomTemporario = rnd.randint(2, numBase)
                    listAlternativas[numLetra] = -sqrt(numRandomTemporario)
                    listAlternativas[numLetra] = pretty(listAlternativas[numLetra])
                    isCorrect[numLetra] = "Nao"
                    howGenerated[numLetra] = "gerada aleatoriamente e negativa"
            else:
                numRandomTemporario = rnd.randint(0,1)

                if numRandomTemporario == 0:
                    numRandomTemporario = rnd.randint(2, numBase)
                    listAlternativas[numLetra] = cbrt(numRandomTemporario)
                    listAlternativas[numLetra] = pretty(listAlternativas[numLetra])
                    isCorrect[numLetra] = "Nao"
                    howGenerated[numLetra] = "gerada aleatoriamente e positiva"
                else:
                    numRandomTemporario = rnd.randint(2, numBase)
                    listAlternativas[numLetra] = -cbrt(numRandomTemporario)
                    listAlternativas[numLetra] = pretty(listAlternativas[numLetra])
                    isCorrect[numLetra] = "Nao"
                    howGenerated[numLetra] = "gerada aleatoriamente e negativa"
                    
    # Cria a variável que será convertida em um arquivo json
    dados = {
        'raiz' : [
            {
                'radicando' : numBase, 
                'indice': qntHoraDada,
                'expoente': qntHoraEsperada,
                'resultado' : resultado
            }
        ],
        'respostas': [
            {
                'letra': 'a)',
                'resposta': listAlternativas[0],
                'correta': isCorrect[0],
                'tipoerro': howGenerated[0]
            },
            {
                'letra': 'b)',
                'resposta': listAlternativas[1],
                'correta': isCorrect[1],
                'tipoerro': howGenerated[1]
            },
            {
                'letra': 'c)',
                'resposta': listAlternativas[2],
                'correta': isCorrect[2],
                'tipoerro': howGenerated[2]
            },{
                'letra': 'd)',
                'resposta': listAlternativas[3],
                'correta': isCorrect[3],
                'tipoerro': howGenerated[3]
            },{
                'letra': 'e)',
                'resposta': listAlternativas[4],
                'correta': isCorrect[4],
                'tipoerro': howGenerated[4]
            }
        ],
        'atributosquestao': [
            {
                'enunciado': 'O crescimento de uma certa cultura de bactérias obedece à função X(t) = {}, em que X(t) é o número de bactérias no tempo t >= 0; C, k são constantes positivas. Verificando que o número inicial de bactérias X(0) é multiplicado por {} em {} horas, quantas se pode esperar no fim de {} horas?'.format(pretty(C*(numBase**(k*t))),numBase,qntHoraDada,qntHoraEsperada),
                'corretaspossiveis': listAlternativas[isCorrect.index("Sim")],
                'corretas': isCorrect.count("Sim"),
                'aleatoriapositiva': howGenerated.count("gerada aleatoriamente e positiva"),
                'aleatorianegativa': howGenerated.count("gerada aleatoriamente e negativa"),
                'invertidapositiva': howGenerated.count("invertida e positiva"),
                'invertidanegativa': howGenerated.count("invertida e negativa"),
                'respostascorretas': listLetra[isCorrect.index("Sim")]
            }
        ]
    }

    # Cria o arquivo JSON
    print("\nquestao {}\n".format(k+1),json.dumps(dados))
    json.dump(dados, questoes, indent=4)

questoes.close()

