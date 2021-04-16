import random as rnd
import math
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

    questoes = open("questao{}.json".format(k+1), 'w')

    # insere um valor aleatório de 2 a 10 para ser a base.
    numBase =  rnd.randint(2,10)

    # insere dois logaritmandos aleatórios em uma lista 
    listNumLogaritmando = [numBase ** rnd.randint(2,10), numBase ** rnd.randint(2,10)]

    # Se os logaritmandos forem iguais, se é gerado novos
    if(listNumLogaritmando[0] == listNumLogaritmando[1]):
        listNumLogaritmando = [numBase ** rnd.randint(2,10), numBase ** rnd.randint(2,10)]

    # O decimais do resultado são reduzidos para 2 casas.
    resposta = str(round(math.log(listNumLogaritmando[0], numBase)/math.log(listNumLogaritmando[1], numBase), 2)).replace(".",",")


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
    while(elementosListaEhDistinta(listAlternativas) == False):
        possuiQuestaoInvertida = rnd.randint(0,1)

        for numLetra in range(0, 5):
            if questaoCerta == listLetra[numLetra]:
                listAlternativas[numLetra] = resposta
                isCorrect[numLetra] = "Sim"
                howGenerated[numLetra] = "nenhum"
            elif questaoInvertida == listLetra[numLetra] and possuiQuestaoInvertida == 1:
                ehNegativoPositivo = rnd.randint(0,1)

                if ehNegativoPositivo == 0:

                    listAlternativas[numLetra] = str(round(math.log(listNumLogaritmando[1], numBase)/math.log(listNumLogaritmando[0], numBase), 2)).replace(".",",")
                    isCorrect[numLetra] = "Nao"
                    howGenerated[numLetra] = "invertida e positiva"
                else:

                    listAlternativas[numLetra] = str(round(-math.log(listNumLogaritmando[1], numBase)/math.log(listNumLogaritmando[0], numBase), 2)).replace(".",",")
                    isCorrect[numLetra] = "Nao"
                    howGenerated[numLetra] = "invertida e negativa"
            else:
                ehNegativoPositivo = rnd.randint(0,1)

                if ehNegativoPositivo == 0:
                    listAlternativas[numLetra] = str(round(math.log(rnd.randint(2,10), rnd.randint(2,9))/math.log(rnd.randint(2,10), rnd.randint(2,9)), 2)).replace(".",",")
                    isCorrect[numLetra] = "Nao"
                    howGenerated[numLetra] = "gerada aleatoriamente e positiva"
                else:
                    listAlternativas[numLetra] = str(round(-math.log(rnd.randint(2,10), rnd.randint(2,9))/math.log(rnd.randint(2,10), rnd.randint(2,9)), 2)).replace(".",",")
                    isCorrect[numLetra] = "Nao"
                    howGenerated[numLetra] = "gerada aleatoriamente e negativa"

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
