import random as rnd
from sympy import symbols, pretty
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

    questoes = open("./src/json/Gerador11/questao{}.json".format(k+1), 'w')

    numBaseLogaritmo = rnd.randint(2,1000)

    a2 = rnd.randint(2,100)
    a1 = rnd.randint(2,100)

    x1 = 7 - rnd.randint(-100,100)
    x2 = 7 - rnd.randint(-100,100)

    while x1 == x2 or a1 == 0:
        x2 = 7 - rnd.randint(-100,100)

        a2 = rnd.randint(2,100)
        a1 = rnd.randint(2,100)

    b2 = rnd.randint(2,100)
    b1 = -a1 * (x1 + x2)

    c2 = rnd.randint(2,100)
    c1 = a1 * (x1 * x2)

    resposta = "S = [x ∈ IR/ x = {} ou x = {}]".format(x1,x2)

    x = symbols('x')

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

                    listAlternativas[numLetra] = "S = [x ∈ IR/ x = {} ou x = {}]".format(x1 - 14, x2 - 14)
                    isCorrect[numLetra] = "Nao"
                    howGenerated[numLetra] = "invertida e positiva"
                else:
                    listAlternativas[numLetra] = "S = [x ∈ IR/ x = {} ou x = {}]".format(-x1 - 14, -x2 - 14)
                    isCorrect[numLetra] = "Nao"
                    howGenerated[numLetra] = "invertida e negativa"
            else:
                numRandomTemporario = rnd.randint(0,1)

                if numRandomTemporario == 0:

                    listAlternativas[numLetra] = "S = [x ∈ IR/ x = {} ou x = {}]".format(rnd.randint(-100, 100), rnd.randint(-100, 100))
                    isCorrect[numLetra] = "Nao"
                    howGenerated[numLetra] = "gerada aleatoriamente e positiva"
                else:

                    listAlternativas[numLetra] = "S = [x ∈ IR/ x = {} ou x = {}]".format(-rnd.randint(-100, 100), -rnd.randint(-100, 100))
                    isCorrect[numLetra] = "Nao"
                    howGenerated[numLetra] = "gerada aleatoriamente e negativa"

    # Cria a variável que será convertida em um arquivo json
    dados = {
        'logaritmo' : [
            {
                'a': a1,
                'b': b1,
                'c': c1,
                'x1': x1,
                'x2': x2,
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
                'enunciado': 'Resolva a equação:\nc) log<sub>{}</sub>({}x² + {}x + {}) = log<sub/>{}</sub>({}x² + {}x + {})'.format(numBaseLogaritmo,(a1+a2),(b1+b2),(c1+c2), numBaseLogaritmo, a2, b2, c2),
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
        print('Resolva a equação:\nc) log<sub>{}</sub>({}x² + {}x + {}) = log<sub/>{}</sub>({}x² + {}x + {})'.format(numBaseLogaritmo,(a1+a2),(b1+b2),(c1+c2), numBaseLogaritmo, a2, b2, c2))
        
    # Armazena os enunciados
        enunciado[k] = dados['atributosquestao'][0]['enunciado']
        
    # Cria o arquivo JSON
        print("\nquestao {}\n".format(k+1),json.dumps(dados))
        json.dump(dados, questoes, indent=4)
        k = k + 1

questoes.close()
