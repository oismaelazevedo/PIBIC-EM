import random as rnd
import json

for k in range(200):

    questoes = open('questao{}-227.json'.format(k+1),'w')

    numBase = rnd.randint(2,10000)
    # A variável abaixo multiplicará o valor base
    numMultiplicadorNumBase = rnd.randint(1,10)
    numExpoente = rnd.randint(2,10000)

    while numBase == numExpoente:
        numExpoente = rnd.randint(2,10000)

    resultado = round(numMultiplicadorNumBase/numExpoente, 6)

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

            listAlternativas[numLetra] = resultado
            isCorrect[numLetra] = "Sim"
            howGenerated[numLetra] = "nenhum"
        elif questaoInvertida == listLetra[numLetra]:
            numRandomTemporario = rnd.randint(0,1)

            if numRandomTemporario == 0:
                listAlternativas[numLetra] = round(numMultiplicadorNumBase/numBase, 6)
                isCorrect[numLetra] = "Nao"
                howGenerated[numLetra] = "invertida e positiva"
            else:
                listAlternativas[numLetra] = round(-numMultiplicadorNumBase/numBase, 6)
                isCorrect[numLetra] = "Nao"
                howGenerated[numLetra] = "invertida e negativa"
        else:
            numRandomTemporario = rnd.randint(0,1)

            if numRandomTemporario == 0:
                numRandomTemporario = rnd.randint(2, numExpoente)

                listAlternativas[numLetra] = round(numMultiplicadorNumBase/numRandomTemporario, 6)
                isCorrect[numLetra] = "Nao"
                howGenerated[numLetra] = "gerada aleatoriamente e positiva"
            else:
                numRandomTemporario = rnd.randint(2, numExpoente)

                listAlternativas[numLetra] = round(-numMultiplicadorNumBase/numRandomTemporario, 6)
                isCorrect[numLetra] = "Nao"
                howGenerated[numLetra] = "gerada aleatoriamente e negativa"
    
    # Cria a variável que será convertida em um arquivo json
    dados = {
        'expoente' : [
            {
                'base' : numBase, 
                'numMultiplicadorNumBase': numMultiplicadorNumBase,
                'expoente': numExpoente,
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
                'enunciado': 'Uma substância radioativa está em processo de desintegração, de modo que no instante t a quantidade não desintegrada é A(t) = A(0).{}^-{}t, em que A(0) indica a quantidade de substância no instante t = 0. Calcule o tempo necessário para que a quantidade inicial dividida por {} se desintegre.'.format(numBase, numExpoente, numBase * numMultiplicadorNumBase),
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



