import random as rnd
from math import log10
import json


def elementosListaEhDistinta(lista):
    for indiceLista in range(len(lista)):
        for indiceListaComparacao in range(len(lista)):
            if indiceLista == 4:
                return True
            elif lista[indiceLista] == lista[indiceListaComparacao] and indiceLista != indiceListaComparacao:
                return False

enunciado = [None]*100
k = 0
while k < 100:

    questoes = open("questao{}-401.json".format(k+1), 'w')

    taxaMes = rnd.randint(2,100)
    valMultiplicadorMonteInicial = rnd.randint(2,1000)

    while taxaMes > valMultiplicadorMonteInicial:
        taxaMes = rnd.randint(2,100)
        valMultiplicadorMonteInicial = rnd.randint(2,1000)

    logTaxaMes = round(log10((taxaMes/100) + 1),2)
    logValMultiplicadorMonteInicial = round(log10(valMultiplicadorMonteInicial), 2)

    resposta = int(logValMultiplicadorMonteInicial/logTaxaMes)

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

                    listAlternativas[numLetra] = int((logTaxaMes/logValMultiplicadorMonteInicial) * 1000)
                    isCorrect[numLetra] = "Nao"
                    howGenerated[numLetra] = "invertida e positiva"
                else:
                    listAlternativas[numLetra] = -int((logTaxaMes/logValMultiplicadorMonteInicial) * 1000)
                    isCorrect[numLetra] = "Nao"
                    howGenerated[numLetra] = "invertida e negativa"
            else:
                numRandomTemporario = rnd.randint(0,1)

                if numRandomTemporario == 0:

                    listAlternativas[numLetra] = int(log10(rnd.randint(2,1000))/log10(1 + (rnd.randint(2,100)/100)))
                    isCorrect[numLetra] = "Nao"
                    howGenerated[numLetra] = "gerada aleatoriamente e positiva"
                else:

                    listAlternativas[numLetra] = -int(log10(rnd.randint(2,1000))/log10(1 + (rnd.randint(2,100)/100)))
                    isCorrect[numLetra] = "Nao"
                    howGenerated[numLetra] = "gerada aleatoriamente e negativa"

    # Cria a variável que será convertida em um arquivo json
    dados = {
        'logaritmo' : [
            {
                'taxaMes':taxaMes,
                'valMultiplicadorMonteInicial':valMultiplicadorMonteInicial,
                'logTaxaMes':logTaxaMes,
                'logValMultiplicadorMonteInicial':logValMultiplicadorMonteInicial,
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
                'enunciado': 'O valor C de um capital (empregado a uma taxa i de juros capitalizados periodicamente ao fim do período), após t períodos, é dado por C = C0.(1 + i)^t, em que C0 é o valor inicial.\nQual é o tempo necessário para que um capital empregado à taxa de {}% ao mês, com juros capitalizados mensalmente, seja multiplicado por {}?\nAdmita que log{} = {} e log{} = {}'.format(taxaMes, valMultiplicadorMonteInicial,(taxaMes/100) + 1, logTaxaMes, valMultiplicadorMonteInicial, logValMultiplicadorMonteInicial),
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

    # Verifica os enunciados
    if dados['atributosquestao'][0]['enunciado'] in enunciado:
        continue
    else:

        print('O valor C de um capital (empregado a uma taxa i de juros capitalizados periodicamente ao fim do período), após t períodos, é dado por C = C0.(1 + i)^t, em que C0 é o valor inicial.\nQual é o tempo necessário para que um capital empregado à taxa de {}% ao mês, com juros capitalizados mensalmente, seja multiplicado por {}?\nAdmita que log{} = {} e log{} = {}'.format(taxaMes, valMultiplicadorMonteInicial,(taxaMes/100) + 1, logTaxaMes, valMultiplicadorMonteInicial, logValMultiplicadorMonteInicial))
        
    # Armazena os enunciados
        enunciado[k] = dados['atributosquestao'][0]['enunciado']
        
    # Cria o arquivo JSON
        print("\nquestao {}\n".format(k+1),json.dumps(dados))
        json.dump(dados, questoes, indent=4)
        k = k + 1

questoes.close()