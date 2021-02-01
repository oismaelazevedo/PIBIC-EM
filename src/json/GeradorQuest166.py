import random as rnd
import math
import json


for k in range(200):

    questoes = open('questao{}-166.json'.format(k+1), 'w')

    # insere um valor aleatório de 2 a 9 para ser a base.
    numBase =  rnd.randint(2,9)

    # insere dois logaritmandos aleatórios em uma lista 
    listNumLogaritmando = [numBase ** rnd.randint(2,10), numBase ** rnd.randint(2,10)]

    # Se os logaritmandos forem iguais, se é gerado novos
    if(listNumLogaritmando[0] == listNumLogaritmando[1]):
        listNumLogaritmando = [numBase ** rnd.randint(2,10), numBase ** rnd.randint(2,10)]

    # O decimais do resultado são reduzidos para 2 casas.
    resultado = round(math.log(listNumLogaritmando[0], numBase)/math.log(listNumLogaritmando[1], numBase), 2)


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
            listAlternativas[numLetra] += resultado
            isCorrect[numLetra] = "Sim"
            howGenerated[numLetra] = "nenhum"
        elif questaoInvertida == listLetra[numLetra]:
            listAlternativas[numLetra] += round(math.log(listNumLogaritmando[1], numBase)/math.log(listNumLogaritmando[0], numBase), 2)
            isCorrect[numLetra] = "Nao"
            howGenerated[numLetra] = "invertida"
        else:
            listAlternativas[numLetra] += round(math.log(rnd.randint(2,10), rnd.randint(2,9))/math.log(rnd.randint(2,10), rnd.randint(2,9)), 2)
            isCorrect[numLetra] = "Nao"
            howGenerated[numLetra] = "gerada aleatoriamente"

    # Cria a variável que será convertida em um arquivo json
    dados = {
        'logaritmo1' : [
            {
                'base' : numBase, 
                'logaritmando' : listNumLogaritmando[0], 
                'resultado' : round(math.log(listNumLogaritmando[0], numBase),2)
            }
        ],
        'logaritmo2' : [
            {
                'base' : numBase,
                'logaritmando' : listNumLogaritmando[1],
                'resultado' : round(math.log(listNumLogaritmando[1], numBase),2)
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
                'enunciado': 'Determine o valor aproximado da razão entre os logaritmos de {} e {} numa base qualquer:'.format(listNumLogaritmando[0],listNumLogaritmando[1]),
                'corretaspossiveis': listAlternativas[isCorrect.index("Sim")],
                'corretas': isCorrect.count("Sim"),
                'aleatoria': howGenerated.count("gerada aleatoriamente"),
                'invertida': howGenerated.count("invertida"),
                'respostascorretas': listLetra[isCorrect.index("Sim")]
            }
        ]
    }

    # Cria o arquivo JSON
    print("\nquestao {}\n".format(k+1),json.dumps(dados))
    json.dump(dados, questoes, indent=4)

questoes.close()
