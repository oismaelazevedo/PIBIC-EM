import random as rnd
from sympy import pretty, sqrt, cbrt, Symbol
import json

def elementosListaEhDistinta(lista):
    for indiceLista in range(len(lista)):
        for indiceListaComparacao in range(len(lista)):
            if indiceLista == 4:
                return True
            elif lista[indiceLista] == lista[indiceListaComparacao] and indiceLista != indiceListaComparacao:
                return False

for k in range(200):

    questoes = open("questoes{}-71f.json".format(k+1), 'w')

    numBase = rnd.randint(2,1000)
    numExpoente = rnd.randint(2,5)

    # Mostra que tipo de raíz (sqrt ou cbrt) o número base será sujeitado
    tipoRadiciacaoNumBase = rnd.randint(2,3)
    tipoRadiciacaoNumBaseComExpoente = 2

    while numExpoente % tipoRadiciacaoNumBaseComExpoente == 0:
        numExpoente = rnd.randint(2,5)
    while numBase % tipoRadiciacaoNumBase == 0:
        numBase = rnd.randint(2,1000)

    x = Symbol('x')

    if tipoRadiciacaoNumBase == 2:
        
        resposta = round((numExpoente/2)/(1/2), 2)
        expressRaizNumBase = sqrt(numBase) ** x
        expressRaizNumBaseComExpoente = sqrt(numBase ** numExpoente)
    else:
        
        resposta = round((numExpoente/2)/(1/3), 2)
        expressRaizNumBase = cbrt(numBase) ** x
        expressRaizNumBaseComExpoente = sqrt(numBase ** numExpoente)

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
        for numLetra in range(0,5):
            if questaoCerta == listLetra[numLetra]:
                listAlternativas[numLetra] = resposta
                isCorrect[numLetra] = "Sim"
                howGenerated[numLetra] = "nenhum"
            elif questaoInvertida == listLetra[numLetra]:

                numRandomTemporario = rnd.randint(0,1)

                if numRandomTemporario == 0:
                    if tipoRadiciacaoNumBase == 2:
                        listAlternativas[numLetra] = round((numExpoente/2)/(1/3), 2)
                        isCorrect[numLetra] = "Nao"
                        howGenerated[numLetra] = "invertida e positiva"
                    else:
                        listAlternativas[numLetra] = round((numExpoente/2)/(1/2), 2)
                        isCorrect[numLetra] = "Nao"
                        howGenerated[numLetra] = "invertida e positiva"
                else:
                    if tipoRadiciacaoNumBase == 2:
                        
                        listAlternativas[numLetra] = round(-((numExpoente/2)/(1/3)), 2)
                        isCorrect[numLetra] = "Nao"
                        howGenerated[numLetra] = "invertida e negativa"
                    else:
                        
                        listAlternativas[numLetra] = round(-((numExpoente/2)/(1/2)), 2)
                        isCorrect[numLetra] = "Nao"
                        howGenerated[numLetra] = "invertida e negativa"
            else:
                numRandomTemporario = rnd.randint(0,1)
                tipoRadiciacaoNumBaseTemporario = rnd.randint(2,3)

                if numRandomTemporario == 0:
                    if tipoRadiciacaoNumBaseTemporario == 2:
                        
                        listAlternativas[numLetra] = round((rnd.randint(1,15)/2)/(1/2),2)
                        isCorrect[numLetra] = "Nao"
                        howGenerated[numLetra] = "gerada aleatoriamente e positiva"
                    else:
                        
                        listAlternativas[numLetra] = round((rnd.randint(1,15)/2)/(1/3),2)
                        isCorrect[numLetra] = "Nao"
                        howGenerated[numLetra] = "gerada aleatoriamente e positiva"  
                else:
                    if tipoRadiciacaoNumBaseTemporario == 2:
                        
                        listAlternativas[numLetra] = round(-((rnd.randint(1,15)/2))/(1/2),2)
                        isCorrect[numLetra] = "Nao"
                        howGenerated[numLetra] = "gerada aleatoriamente e negativa"
                        
                    else:
                        
                        listAlternativas[numLetra] = round(-((rnd.randint(1,15)/2))/(1/3),2)
                        isCorrect[numLetra] = "Nao"
                        howGenerated[numLetra] = "gerada aleatoriamente e negativa"
                    


    # Cria a variável que será convertida em um arquivo json
    dados = {
        'equacaoExponencial' : [
            {
                'numBase' : numBase,
                'numExpoente': numExpoente,
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
                'enunciado': 'Resolva a seguinte equação exponencial:\n{} =    {}'.format(pretty(expressRaizNumBase),pretty(expressRaizNumBaseComExpoente)),
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

    print('Resolva a seguinte equação exponencial:\n{} = {}'.format(pretty(expressRaizNumBase),pretty(expressRaizNumBaseComExpoente)))

    # Cria o arquivo JSON
    print("\nquestao {}\n".format(k+1),json.dumps(dados))
    json.dump(dados, questoes, indent=4)

questoes.close()