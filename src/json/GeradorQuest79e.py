import random as rnd
from sympy import pretty, Symbol
import json

def elementosListaEhDistinta(lista):
    for indiceLista in range(len(lista)):
        for indiceListaComparacao in range(len(lista)):
            if indiceLista == 4:
                return True
            elif lista[indiceLista] == lista[indiceListaComparacao] and indiceLista != indiceListaComparacao:
                return False

for k in range(50):

    questoes = open("questoes{}-79e.json".format(k+1),'w')

    numBase = rnd.randint(2,20)
    numExpoenteNumBase = rnd.randint(1,10)
    numMultiplicadorIncognitaAlternativa = (3 * 1) - (5 * numBase) + (5 * (numBase ** 3)) - (numBase ** 5)

    resposta = numExpoenteNumBase

    x = Symbol('x')
    express = 3 * numBase ** x - 5 * numBase ** (x + 1) + 5 * numBase ** (x + 3) - numBase ** (x + 5)

    listLetra = ["A","B","C","D","E"]

    questaoCerta = rnd.choice(listLetra)
    questaoInvertida = rnd.choice(listLetra)

    while(questaoCerta == questaoInvertida):
        questaoInvertida = rnd.choice(listLetra)
        
    listAlternativas = [0,0,0,0,0]
    isCorrect = ['','','','','']
    howGenerated = ['','','','','']

    # Insere a resposta certa na letra escolhida para ser certa, uma letra recebe a questão invertida e o resto recebe números aleatórios
    while(elementosListaEhDistinta(listAlternativas) == False):
        possuiQuestaoInvertida = rnd.randint(0,1)

        for numLetra in range(0,5):
            if questaoCerta == listLetra[numLetra]:
                listAlternativas[numLetra] = resposta
                isCorrect[numLetra] = "Sim"
                howGenerated[numLetra] = "nenhum"
            elif questaoInvertida == listLetra[numLetra] and possuiQuestaoInvertida == 1:
                
                numRandomTemporario = rnd.randint(0,1)

                if numRandomTemporario == 0:
                    listAlternativas[numLetra] = numExpoenteNumBase - 1
                    isCorrect[numLetra] = "Nao"
                    howGenerated[numLetra] = "invertida e positiva"
                else:
                    listAlternativas[numLetra] = -numExpoenteNumBase + 1
                    isCorrect[numLetra] = "Nao"
                    howGenerated[numLetra] = "invertida e negativa"
            else:
                numRandomTemporario = rnd.randint(0,1)

                if numRandomTemporario == 0:
                    listAlternativas[numLetra] = rnd.randint(2,20) + 1
                    isCorrect[numLetra] = "Nao"
                    howGenerated[numLetra] = "gerada aleatoriamente e positiva"
                else:
                    listAlternativas[numLetra] = -rnd.randint(2,20) + 1
                    isCorrect[numLetra] = "Nao"
                    howGenerated[numLetra] = "gerada aleatoriamente e negativa"
    
    # Cria a variável que será convertida em um arquivo json
    dados = {
        'equacaoExponencial' : [
            {
                'numBase': numBase,
                'numExpoenteNumBase': numExpoenteNumBase,
                'numMultiplicadorIncognitaAlternativa': numMultiplicadorIncognitaAlternativa,
                'express': pretty(express),
                'resposta': resposta

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
                'enunciado': 'Resolva a seguinte equação exponencial:\n{} = {}'.format(pretty(express), numMultiplicadorIncognitaAlternativa * (numBase ** numExpoenteNumBase)),
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

    print('Resolva a seguinte equação exponencial:\n{} = {}'.format(pretty(express), numMultiplicadorIncognitaAlternativa * (numBase ** numExpoenteNumBase)))

    # Cria o arquivo JSON
    print("\nquestao {}\n".format(k+1),json.dumps(dados))
    json.dump(dados, questoes, indent=4)

questoes.close()