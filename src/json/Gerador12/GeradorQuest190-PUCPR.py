import random as rnd
from sympy import pretty, Eq, solve, symbols
import json

def elementosListaEhDistinta(lista):
    for indiceLista in range(len(lista)):
        for indiceListaComparacao in range(len(lista)):
            if indiceLista == 4:
                return True
            elif lista[indiceLista] == lista[indiceListaComparacao] and indiceLista != indiceListaComparacao:
                return False

enunciado = [None]*200
k = 0
while k < 200:

    questoes = open("./src/json/Gerador12/questao{}.json".format(k+1), 'w')

    x = symbols('x')

    valX01 = rnd.randint(2,100)
    valX02 = rnd.randint(2,100)
    num01 = rnd.randint(2,100)
    num02 = rnd.randint(2,100)
    numResposta = rnd.randint(2,20)

    express = valX01*x + num01 + numResposta*(-valX02*x + num02)
    resposta = solve(express)
    resposta = pretty(resposta)

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

                    listAlternativas[numLetra] = solve(numResposta*(-valX01*x + num01) + valX02 + num02)
                    listAlternativas[numLetra] = pretty(listAlternativas[numLetra])
                    isCorrect[numLetra] = "Nao"
                    howGenerated[numLetra] = "invertida e negativa"
                else:
                    listAlternativas[numLetra] = solve(-(numResposta*(-valX01*x + num01) + valX02 + num02))
                    listAlternativas[numLetra] = pretty(listAlternativas[numLetra])
                    isCorrect[numLetra] = "Nao"
                    howGenerated[numLetra] = "invertida e positiva"
            else:
                numRandomTemporario = rnd.randint(0,1)

                if numRandomTemporario == 0:

                    listAlternativas[numLetra] = solve(rnd.randint(2,100)*x + rnd.randint(2,100) + rnd.randint(2,20)*(-rnd.randint(2,100)*x + rnd.randint(2,100)))
                    listAlternativas[numLetra] = pretty(listAlternativas[numLetra])
                    isCorrect[numLetra] = "Nao"
                    howGenerated[numLetra] = "gerada aleatoriamente e negativa"
                else:

                    listAlternativas[numLetra] = solve(-(rnd.randint(2,100)*x + rnd.randint(2,100) + rnd.randint(2,20)*(-rnd.randint(2,100)*x + rnd.randint(2,100))))
                    listAlternativas[numLetra] = pretty(listAlternativas[numLetra])
                    isCorrect[numLetra] = "Nao"
                    howGenerated[numLetra] = "gerada aleatoriamente e positiva"

    # Cria a variável que será convertida em um arquivo json
    dados = {
        'equacaoExponencial' : [
            {
                'valX01': valX01,
                'valX02': valX02,
                'num01': num01,
                'num02': num02,
                'numResposta': numResposta,
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
                'enunciado': '(PUC-PR-modificada) Se log({}𝑥 + {}) - log({}𝑥 - {}) = log {}, então 𝑥 é igual a:'.format(valX01,num01,valX02,num02,numResposta),
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
        
    # Armazena os enunciados
        enunciado[k] = dados['atributosquestao'][0]['enunciado']
        
    # Cria o arquivo JSON
        print("\nquestao {}\n".format(k+1),json.dumps(dados))
        json.dump(dados, questoes, indent=4)
        k = k + 1

questoes.close()
