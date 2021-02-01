import random as rnd
import json
import math



for k in range(200):

    questoes = open('questao{}-163.json'.format(k+1), 'w')

    expoenteConcentracao = rnd.randint(1,70)
    resposta = round((expoenteConcentracao ** 2)/3, 2)

    listLetra = ["A","B","C","D","E"]
    questaoCerta = rnd.choice(listLetra)
    questaoInvertida = rnd.choice(listLetra)

    # Verifica se a letra com a resposta certa e invertida são iguais 
    repetida = True
    while repetida == True: 
        if questaoCerta == questaoInvertida:
            questaoCerta = rnd.choice(listLetra)
            questaoInvertida = rnd.choice(listLetra)
        else: repetida = False
    
    listAlternativas = [0,0,0,0,0]
    isCorrect = ['','','','','']
    howGenerated = ['','','','','']

    # Insere a resposta certa na letra escolhida para ser certa, uma letra recebe a questão invertida e o resto recebe números aleatórios
    for numLetra in range(0, 5):
        if questaoCerta == listLetra[numLetra]:
            listAlternativas[numLetra] = resposta
            isCorrect[numLetra] = "Sim"
            howGenerated[numLetra] = "nenhum"
        elif questaoInvertida == listLetra[numLetra]:
            listAlternativas[numLetra] = round(-(expoenteConcentracao ** 3)/2, 2)
            isCorrect[numLetra] = "Nao"
            howGenerated[numLetra] = "invertida"
        else:
            EhNegativoPositivo = rnd.randint(0,1)
            if (EhNegativoPositivo == 0): 
                listAlternativas[numLetra] = round((rnd.randint(1,expoenteConcentracao) ** 2)/3, 2) 
                isCorrect[numLetra] = "Nao"
                howGenerated[numLetra] = "gerada aleatoriamente e positiva"
            else: 
                listAlternativas[numLetra] = round(-(rnd.randint(1,expoenteConcentracao) ** 2)/3, 2)
                isCorrect[numLetra] = "Nao"
                howGenerated[numLetra] = "gerada aleatoriamente e negativa"


    # Cria a variável que será convertida em um arquivo json
    dados = {
        'logaritmo' : [
            {
                'base' : 10,
                'logaritmando' : 1 / 10 ** expoenteConcentracao,
                'resultado' : round(math.log(1 / 10 ** expoenteConcentracao, 10),2)    
            }
        ],
        'respostas' : [
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
                'enunciado': 'O pH de uma solução é definido por pH = log(1/H+), em que H+ é a concentração de hidrogênio em íons-gama por litro de solução. Determine o quadrado sobre três do pH de uma solução tal que H+ = 1,0 x e{}. Admita que e = 10'.format(expoenteConcentracao),
                'corretaspossiveis': listAlternativas[isCorrect.index("Sim")],
                'corretas': isCorrect.count("Sim"),
                'aleatoriapositiva': howGenerated.count("gerada aleatoriamente e positiva"),
                'aleatorianegativa': howGenerated.count("gerada aleatoriamente e negativa"),
                'invertida': howGenerated.count("invertida"),
                'respostascorretas': listLetra[isCorrect.index("Sim")]
            }
        ]
    }

    # Cria o arquivo JSON
    print("\nquestao {}\n".format(k+1),json.dumps(dados))
    json.dump(dados, questoes, indent=4)

questoes.close()
