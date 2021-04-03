import random as rnd
from sympy import pretty, sqrt, cbrt
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

    numBase = rnd.randint(2,1000)
    tipoDenominadorFracao = rnd.randint(2,3)

    if tipoDenominadorFracao == 2:
        # Verifica se o número é primo e, se for, gera um novo.
        qntMultiplos = 0

        while(qntMultiplos < 2):
            for count in range(2,numBase):
                if (numBase % count == 0):
                    qntMultiplos += 1
            if(qntMultiplos < 2):
                numBase = rnd.randint(2,1000)
                qntMultiplos = 0

        resposta = sqrt(numBase)
        resposta = pretty(resposta)   
    else:
        # Verifica se o número é primo e, se for, gera um novo.
        qntMultiplos = 0

        while(qntMultiplos < 3):
            for count in range(2,numBase):
                if (numBase % count == 0):
                    qntMultiplos += 1
            if(qntMultiplos < 3):
                numBase = rnd.randint(2,1000)
                qntMultiplos = 0

        resposta = cbrt(numBase)
        resposta = pretty(resposta)

    listLetra = ["A","B","C","D","E"]
    questaoCerta = rnd.choice(listLetra)
    questaoInvertida = rnd.choice(listLetra)

    while questaoCerta == questaoInvertida:
        questaoInvertida = rnd.choice(listLetra) 

    isCorrect = ['','','','','']
    howGenerated = ['','','','','']
    
    listAlternativas = [0,0,0,0,0]

    # Insere a resposta certa na letra escolhida para ser certa, uma letra recebe a questão invertida e o resto recebe números aleatórios
    while(elementosListaEhDistinta(listAlternativas) == False):
        possuiQuestaoInvertida = rnd.randint(0,1)

        for numLetra in range(0, 5):
            if questaoCerta == listLetra[numLetra]:
                listAlternativas[numLetra] = resposta
                isCorrect[numLetra] = "Sim"
                howGenerated[numLetra] = "nenhum"
            elif questaoInvertida == listLetra[numLetra] and possuiQuestaoInvertida == 1:
                if tipoDenominadorFracao == 2:
                    numRandomTemporario = rnd.randint(0,1)

                    if numRandomTemporario == 0:
                        listAlternativas[numLetra] = cbrt(numBase)
                        listAlternativas[numLetra] = pretty(listAlternativas[numLetra])
                        isCorrect[numLetra] = "Nao"
                        howGenerated[numLetra] = "invertida e positiva"
                    else:
                        listAlternativas[numLetra] = -cbrt(numBase)
                        listAlternativas[numLetra] = pretty(listAlternativas[numLetra])
                        isCorrect[numLetra] = "Nao"
                        howGenerated[numLetra] = "invertida e negativa"
                else:
                    numRandomTemporario = rnd.randint(0,1)

                    if numRandomTemporario == 0:
                        listAlternativas[numLetra] = sqrt(numBase)
                        listAlternativas[numLetra] = pretty(listAlternativas[numLetra])
                        isCorrect[numLetra] = "Nao"
                        howGenerated[numLetra] = "invertida e positiva"
                    else:
                        listAlternativas[numLetra] = -sqrt(numBase)
                        listAlternativas[numLetra] = pretty(listAlternativas[numLetra])
                        isCorrect[numLetra] = "Nao"
                        howGenerated[numLetra] = "invertida e negativa"
            else:
                numRandomTemporario = rnd.randint(2,3)

                if numRandomTemporario == 2:
                    numRandomTemporario = rnd.randint(0,1)

                    if numRandomTemporario == 0:

                        numRandomTemporario = rnd.randint(2,numBase)

                        # Verifica se o número é primo e, se for, gera um novo.
                        qntMultiplos = 0
                        while(qntMultiplos < 2):
                            for count in range(2, numRandomTemporario):
                                if (numRandomTemporario % count == 0):
                                    qntMultiplos += 1
                            if(qntMultiplos < 2):
                                numRandomTemporario = rnd.randint(2,numBase)
                                qntMultiplos = 0

                        listAlternativas[numLetra] = sqrt(numRandomTemporario)
                        listAlternativas[numLetra] = pretty(listAlternativas[numLetra])

                        isCorrect[numLetra] = "Nao"
                        howGenerated[numLetra] = "gerada aleatoriamente e positiva"
                    else:
                        numRandomTemporario = rnd.randint(2,numBase)

                        # Verifica se o número é primo e, se for, gera um novo.
                        qntMultiplos = 0
                        while(qntMultiplos < 2):
                            for count in range(2, numRandomTemporario):
                                if (numRandomTemporario % count == 0):
                                    qntMultiplos += 1
                            if(qntMultiplos < 2):
                                numRandomTemporario = rnd.randint(2,numBase)
                                qntMultiplos = 0

                        listAlternativas[numLetra] = -sqrt(numRandomTemporario)
                        listAlternativas[numLetra] = pretty(listAlternativas[numLetra])

                        isCorrect[numLetra] = "Nao"
                        howGenerated[numLetra] = "gerada aleatoriamente e negativa"
                else:
                    numRandomTemporario = rnd.randint(0,1)

                    if numRandomTemporario == 0:
                        numRandomTemporario = rnd.randint(2,numBase)

                        # Verifica se o número é primo e, se for, gera um novo.
                        qntMultiplos = 0
                        while(qntMultiplos < 3):
                            for count in range(2, numRandomTemporario):
                                if (numRandomTemporario % count == 0):
                                    qntMultiplos += 1
                            if(qntMultiplos < 3):
                                numRandomTemporario = rnd.randint(2,numBase)
                                qntMultiplos = 0

                        listAlternativas[numLetra] = cbrt(numRandomTemporario)
                        listAlternativas[numLetra] = pretty(listAlternativas[numLetra])
                        isCorrect[numLetra] = "Nao"
                        howGenerated[numLetra] = "gerada aleatoriamente e positiva"
                    else:
                        numRandomTemporario = rnd.randint(2,numBase)

                        # Verifica se o número é primo e, se for, gera um novo.
                        qntMultiplos = 0
                        while(qntMultiplos < 3):
                            for count in range(2, numRandomTemporario):
                                if (numRandomTemporario % count == 0):
                                    qntMultiplos += 1
                            if(qntMultiplos < 3):
                                numRandomTemporario = rnd.randint(2,numBase)
                                qntMultiplos = 0

                        listAlternativas[numLetra] = -cbrt(numRandomTemporario)
                        listAlternativas[numLetra] = pretty(listAlternativas[numLetra])
                        isCorrect[numLetra] = "Nao"
                        howGenerated[numLetra] = "gerada aleatoriamente e negativa"


    # Cria a variável que será convertida em um arquivo json
    dados = {
        'logaritmo': [
            {
                'numBase': numBase,
                'tipoDenominadorFracao': tipoDenominadorFracao,
                'resposta': resposta
            }
        ],

        'respostas' : [
            {
                'letra' : 'a)',
                'resposta' : listAlternativas[0],
                'correta' : isCorrect[0],
                'tipoerro' : howGenerated[0]
            },
            {
                'letra' : 'b)',
                'resposta' : listAlternativas[1],
                'correta' : isCorrect[1],
                'tipoerro' : howGenerated[1]
            },
            {
                'letra' : 'c)',
                'resposta' : listAlternativas[2],
                'correta' : isCorrect[2],
                'tipoerro' : howGenerated[2]
            },
            {
                'letra' : 'd)',
                'resposta' : listAlternativas[3],
                'correta' : isCorrect[3],
                'tipoerro' : howGenerated[3]
            },
            {
                'letra' : 'e)',
                'resposta' : listAlternativas[4],
                'correta' : isCorrect[4],
                'tipoerro' : howGenerated[4]
            }
        ],
        'atributosquestao' : [
            {
                'enunciado' : 'A soma dos logaritmos de dois números na base {} é 1/{}. Determine o produto desses números.'.format(numBase,tipoDenominadorFracao),
                'corretaspossiveis' : listAlternativas[isCorrect.index("Sim")],
                'corretas' : isCorrect.count("Sim"),
                'aleatoriapositiva' : howGenerated.count("gerada aleatoriamente e positiva"),
                'aleatorianegativa' : howGenerated.count("gerada aleatoriamente e negativa"),
                'invertidapositiva' : howGenerated.count("invertida e positiva"),
                'invertidanegativa' : howGenerated.count("invertida e negativa"),
                'respostascorretas' : listLetra[isCorrect.index("Sim")]
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
                
            
