import random as rnd
from sympy import pretty, sqrt, cbrt
import json

for k in range(200):

    questoes = open("questao{}-71d.json".format(k+1), 'w')

    numBase = rnd.randint(2,1000)
    resposta = -rnd.randint(2,5)

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
            listAlternativas[numLetra] = resposta
            isCorrect[numLetra] = "Sim"
            howGenerated[numLetra] = "nenhum"
        elif questaoInvertida == listLetra[numLetra]:
            
            numRandomTemporario = rnd.randint(0,1)

            if numRandomTemporario == 0:

                listAlternativas[numLetra] = rnd.randint(1,15) - resposta
                isCorrect[numLetra] = "Nao"
                howGenerated[numLetra] = "invertida e positiva"
            else:
                listAlternativas[numLetra] = -rnd.randint(1,15) + resposta
                isCorrect[numLetra] = "Nao"
                howGenerated[numLetra] = "invertida e negativa"
        else:
            numRandomTemporario = rnd.randint(0,1)

            if numRandomTemporario == 0:

                listAlternativas[numLetra] = rnd.randint(-resposta + 1, 15)
                isCorrect[numLetra] = "Nao"
                howGenerated[numLetra] = "gerada aleatoriamente e positiva"
            else:

                listAlternativas[numLetra] = -rnd.randint(-resposta + 1, 15)
                isCorrect[numLetra] = "Nao"
                howGenerated[numLetra] = "gerada aleatoriamente e negativa"

    # Cria a variável que será convertida em um arquivo json
    dados = {
        'equacaoExponencial' : [
            {
                'numBase' : numBase,
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
                'enunciado': 'Resolva a seguinte equação exponencial: (1/{})^x = {}'.format(numBase, numBase ** -resposta),
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