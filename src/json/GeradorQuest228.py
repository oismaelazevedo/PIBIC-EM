import random as rnd
from sympy import pretty, sqrt, cbrt, symbols
import json

def elementosListaEhDistinta(lista):
    for indiceLista in range(len(lista)):
        for indiceListaComparacao in range(len(lista)):
            if indiceLista == 4:
                return True
            elif lista[indiceLista] == lista[indiceListaComparacao] and indiceLista != indiceListaComparacao:
                return False

for k in range(200):

    questoes = open('questao{}-228.json'.format(k+1), 'w')

    numBase = rnd.randint(2,10000)

    qntHoraDecaimentoDado = rnd.randint(2, 3)
    qntHoraDecaimentoEsperado = rnd.randint(2, 5)

    while qntHoraDecaimentoDado == qntHoraDecaimentoEsperado:
        qntHoraDecaimentoEsperado = rnd.randint(2, 5)

    if qntHoraDecaimentoDado == 2:
        resultado = 1 - sqrt(numBase ** qntHoraDecaimentoEsperado)
        resultado = pretty(resultado)
    else:
        resultado = 1 - cbrt(numBase ** qntHoraDecaimentoEsperado)
        resultado = pretty(resultado)

    k, t = symbols("k t")

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

        for numLetra in range(0, 5):
            if questaoCerta == listLetra[numLetra]:
                listAlternativas[numLetra] = resultado
                isCorrect[numLetra] = "Sim"
                howGenerated[numLetra] = "nenhum"
            elif questaoInvertida == listLetra[numLetra] and possuiQuestaoInvertida == 1:
                if(qntHoraDecaimentoDado == 2):
                    numRandomTemporario = rnd.randint(0,1)

                    if numRandomTemporario == 0:

                        listAlternativas[numLetra] = 1 - cbrt(numBase ** qntHoraDecaimentoEsperado)
                        listAlternativas[numLetra] = pretty(listAlternativas[numLetra])
                        isCorrect[numLetra] = "Nao"
                        howGenerated[numLetra] = "invertida e positiva"
                    else:
                        listAlternativas[numLetra] = 1 + cbrt(numBase ** qntHoraDecaimentoEsperado)
                        listAlternativas[numLetra] = pretty(listAlternativas[numLetra])
                        isCorrect[numLetra] = "Nao"
                        howGenerated[numLetra] = "invertida e negativa"
                else:
                    numRandomTemporario = rnd.randint(0,1)

                    if numRandomTemporario == 0:

                        listAlternativas[numLetra] = 1 - sqrt(numBase ** qntHoraDecaimentoEsperado)
                        listAlternativas[numLetra] = pretty(listAlternativas[numLetra]) 
                        isCorrect[numLetra] = "Nao"
                        howGenerated[numLetra] = "invertida e positiva"
                    else:
                        listAlternativas[numLetra] = 1 + sqrt(numBase ** qntHoraDecaimentoEsperado)
                        listAlternativas[numLetra] = pretty(listAlternativas[numLetra]) 
                        isCorrect[numLetra] = "Nao"
                        howGenerated[numLetra] = "invertida e negativa"
            else:
                numRandomTemporario = rnd.randint(2,3)

                if numRandomTemporario == 2:
                    numRandomTemporario = rnd.randint(0,1)

                    if numRandomTemporario == 0:
                        numRandomTemporario = rnd.randint(2, numBase)
                        listAlternativas[numLetra] = 1 - sqrt(numRandomTemporario ** qntHoraDecaimentoEsperado)
                        listAlternativas[numLetra] = pretty(listAlternativas[numLetra])
                        isCorrect[numLetra] = "Nao"
                        howGenerated[numLetra] = "gerada aleatoriamente e positiva"
                    else:
                        numRandomTemporario = rnd.randint(2, numBase)
                        listAlternativas[numLetra] = 1 + sqrt(numRandomTemporario ** qntHoraDecaimentoEsperado)
                        listAlternativas[numLetra] = pretty(listAlternativas[numLetra])
                        isCorrect[numLetra] = "Nao"
                        howGenerated[numLetra] = "gerada aleatoriamente e negativa"
                else:
                    numRandomTemporario = rnd.randint(0,1)

                    if numRandomTemporario == 0:
                        numRandomTemporario = rnd.randint(2, numBase)
                        listAlternativas[numLetra] = 1 - cbrt(numRandomTemporario ** qntHoraDecaimentoEsperado)
                        listAlternativas[numLetra] = pretty(listAlternativas[numLetra])
                        isCorrect[numLetra] = "Nao"
                        howGenerated[numLetra] = "gerada aleatoriamente e positiva"
                    else:
                        numRandomTemporario = rnd.randint(2, numBase)
                        listAlternativas[numLetra] = 1 + cbrt(numRandomTemporario ** qntHoraDecaimentoEsperado)
                        listAlternativas[numLetra] = pretty(listAlternativas[numLetra])
                        isCorrect[numLetra] = "Nao"
                        howGenerated[numLetra] = "gerada aleatoriamente e negativa"
    
    # Cria a variável que será convertida em um arquivo json
    dados = {
        'equacaoExponencial' : [
            {
                'radicando' : numBase, 
                'indice': qntHoraDecaimentoDado,
                'expoente': qntHoraDecaimentoEsperado,
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
                'enunciado': 'A lei de decomposição de um elemento X no tempo t >= 0 é dada por M(t) = C.{}, em que M(t) é quantidade de X no tempo t; C, K são constantes positivas. Se a quantidade primitiva M(0), quando dividida por {}, desaparece em {} anos, qual a quantidade perdida em {} anos?'.format(pretty(numBase ** (k*t)),numBase,qntHoraDecaimentoDado,qntHoraDecaimentoEsperado),
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



    