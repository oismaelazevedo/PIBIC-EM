import random as rnd
from sympy import pretty, Eq, solve, symbols
import json

for k in range(200):

    questoes = open("questao{}-190-PUCPR.json".format(k+1),'w')

    x = symbols('x')

    valX01 = rnd.randint(2,1000)
    valX02 = rnd.randint(2,1000)
    num01 = rnd.randint(2,1000)
    num02 = rnd.randint(2,1000)
    numResposta = rnd.randint(2,20)

    express = valX01*x + num01 + numResposta*(-valX02*x + num02)
    resp = solve(express)
    resp = pretty(resp)

    listLetra = ["A","B","C","D","E"]

    questaoCerta = rnd.choice(listLetra)
    questaoInvertida = rnd.choice(listLetra)

    while(questaoCerta == questaoInvertida):
        questaoInvertida = rnd.choice(listLetra)
        
    listAlternativas = [0,0,0,0,0]
    isCorrect = ['','','','','']
    howGenerated = ['','','','','']

    # Insere a resposta certa na letra escolhida para ser certa, uma letra recebe a questão invertida e o resto recebe números aleatórios
    for numLetra in range(0,5):
        if questaoCerta == listLetra[numLetra]:
            listAlternativas[numLetra] = resp
            isCorrect[numLetra] = "Sim"
            howGenerated[numLetra] = "nenhum"
        elif questaoInvertida == listLetra[numLetra]:
            
            numRandomTemporario = rnd.randint(0,1)

            if numRandomTemporario == 0:

                listAlternativas[numLetra] = solve(numResposta*(-valX01*x + num01) + valX02 + num02)
                listAlternativas[numLetra] = pretty(listAlternativas[numLetra])
                isCorrect[numLetra] = "Nao"
                howGenerated[numLetra] = "invertida e positiva"
            else:
                listAlternativas[numLetra] = solve(-(numResposta*(-valX01*x + num01) + valX02 + num02))
                listAlternativas[numLetra] = pretty(listAlternativas[numLetra])
                isCorrect[numLetra] = "Nao"
                howGenerated[numLetra] = "invertida e negativa"
        else:
            numRandomTemporario = rnd.randint(0,1)

            if numRandomTemporario == 0:

                listAlternativas[numLetra] = solve(rnd.randint(2,1000)*x + rnd.randint(2,1000) + rnd.randint(2,20)*(-rnd.randint(2,1000)*x + rnd.randint(2,1000)))
                listAlternativas[numLetra] = pretty(listAlternativas[numLetra])
                isCorrect[numLetra] = "Nao"
                howGenerated[numLetra] = "gerada aleatoriamente e positiva"
            else:

                listAlternativas[numLetra] = solve(-(rnd.randint(2,1000)*x + rnd.randint(2,1000) + rnd.randint(2,20)*(-rnd.randint(2,1000)*x + rnd.randint(2,1000))))
                listAlternativas[numLetra] = pretty(listAlternativas[numLetra])
                isCorrect[numLetra] = "Nao"
                howGenerated[numLetra] = "gerada aleatoriamente e negativa"

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
                'resp': resp
                
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
                'enunciado': '(PUC-PR-modificada) Se log({}x + {}) - log({}x - {}) = log {}, então x é igual a:'.format(valX01,num01,valX02,num02,numResposta),
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

    print('(PUC-PR-modificada) Se log({}x + {}) - log({}x - {}) = log {}, então x é igual a:'.format(valX01,num01,valX02,num02,numResposta))

    # Cria o arquivo JSON
    print("\nquestao {}\n".format(k+1),json.dumps(dados))
    json.dump(dados, questoes, indent=4)

questoes.close()