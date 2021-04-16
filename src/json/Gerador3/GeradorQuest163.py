import random as rnd
import json
from sympy import pretty, Symbol
import math

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
    questoes = open("./src/json/Gerador3/questao{}.json".format(k+1), 'w')

    expoenteConcentracao = rnd.randint(1,1000)
    resposta = round((expoenteConcentracao ** 2)/3, 2)

    e = Symbol('e')

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

                    listAlternativas[numLetra] = str(round((expoenteConcentracao ** 3)/2, 2)).replace(".",",")
                    isCorrect[numLetra] = "Nao"
                    howGenerated[numLetra] = "invertida e positiva"
                else:
                    
                    listAlternativas[numLetra] = str(round(-(expoenteConcentracao ** 3)/2, 2)).replace(".",",")
                    isCorrect[numLetra] = "Nao"
                    howGenerated[numLetra] = "invertida e negativa"
            else:
                ehNegativoPositivo = rnd.randint(0,1)

                if (ehNegativoPositivo == 0): 
                    listAlternativas[numLetra] = str(round((rnd.randint(1,expoenteConcentracao) ** 2)/3, 2)).replace(".",",") 
                    isCorrect[numLetra] = "Nao"
                    howGenerated[numLetra] = "gerada aleatoriamente e positiva"
                else: 
                    listAlternativas[numLetra] = str(round(-(rnd.randint(1,expoenteConcentracao) ** 2)/3, 2)).replace(".",",")
                    isCorrect[numLetra] = "Nao"
                    howGenerated[numLetra] = "gerada aleatoriamente e negativa"


    # Cria a variável que será convertida em um arquivo json
    dados = {
        'logaritmo' : [
            {
                'base' : 10,
                'logaritmando' : 1 / 10 ** expoenteConcentracao,
                'expoente' : expoenteConcentracao,
                'resultado' : resposta 
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
                'enunciado': 'O pH de uma solução é definido por pH = log(1&frasl;<sub>H+</sub>), em que H+ é a concentração de hidrogênio em íons-gama por litro de solução. Determine o quadrado sobre três do pH de uma solução tal que H+ = 1,0 × 10<sup>{}</sup>.'.format(expoenteConcentracao),
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
