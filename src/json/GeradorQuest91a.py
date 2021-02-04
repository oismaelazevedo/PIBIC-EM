import random as rnd
import json

for k in range(200):

    questoes = open('questao{}-91a.json'.format(k+1), 'w')

    a = rnd.randint(-100,100)
    x1 = 7 - rnd.randint(-1000,1000)
    x2 = 7 - rnd.randint(-1000,1000)

    while x1 == x2:
        x2 = 7 - rnd.randint(-1000,1000)

    b = - a * (x1 + x2)
    c = a * (x1 * x2)

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
            listAlternativas[numLetra] = "{} e {}".format(x1, x2)
            isCorrect[numLetra] = "Sim"
            howGenerated[numLetra] = "nenhum"
        elif questaoInvertida == listLetra[numLetra]:
            numRandomTemporario = rnd.randint(0,1)

            if numRandomTemporario == 0:

                listAlternativas[numLetra] = "{} e {}".format(x1 - 14, x2 - 14)
                isCorrect[numLetra] = "Nao"
                howGenerated[numLetra] = "invertida e positiva"
            else:

                listAlternativas[numLetra] = "{} e {}".format(-x1 - 14, -x2 - 14)
                isCorrect[numLetra] = "Nao"
                howGenerated[numLetra] = "invertida e negativa"
        else:
            numRandomTemporario = rnd.randint(0,1)

            if numRandomTemporario == 0:

                x1Aleatorio = rnd.randint(-1000, 1000)
                x2Aleatorio = rnd.randint(-1000, 1000)

                listAlternativas[numLetra] = "{} e {}".format(x1Aleatorio,x2Aleatorio)
                isCorrect[numLetra] = "Nao"
                howGenerated[numLetra] = "gerada aleatoriamente e positiva"
            else:

                x1Aleatorio = rnd.randint(-1000, 1000)
                x2Aleatorio = rnd.randint(-1000, 1000)

                listAlternativas[numLetra] = "{} e {}".format(-x1Aleatorio, -x2Aleatorio)
                isCorrect[numLetra] = "Nao"
                howGenerated[numLetra] = "gerada aleatoriamente e negativa"

    # Cria a variável que será convertida em um arquivo json
    dados = {
        'equacao2Grau' : [
            {
                'a' : a,
                'b' : b,
                'c' : c,
                'x1' : x1,
                'x2' : x2
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
                'enunciado': 'Determine as raízes da equação em IR+: X^({}y² + [{}y] + {}) = 1'.format(a,b,c),
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

