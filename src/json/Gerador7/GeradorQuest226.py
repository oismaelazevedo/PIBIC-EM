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

enunciado = [None]*200
k = 0
while k < 200:

    questoes = open("./src/json/Gerador7/questao{}.json".format(k+1), 'w')
    numBase = rnd.randint(2,1000)

    qntHoraDada = rnd.randint(2,3)
    qntHoraEsperada = rnd.randint(2,10)

    while(qntHoraDada == qntHoraEsperada):
        qntHoraEsperada = rnd.randint(2,10)

    if(qntHoraDada == 2):
        resposta = sqrt(numBase ** qntHoraEsperada)
        resposta = pretty(resposta)
    else:
        resposta = cbrt(numBase ** qntHoraEsperada)
        resposta = pretty(resposta)

    C, p, t = symbols("C p t")

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
                listAlternativas[numLetra] = resposta
                isCorrect[numLetra] = "Sim"
                howGenerated[numLetra] = "nenhum"
            elif questaoInvertida == listLetra[numLetra] and possuiQuestaoInvertida == 1:
                if(qntHoraDada == 2):
                    numRandomTemporario = rnd.randint(0,1)

                    if numRandomTemporario == 0:

                        listAlternativas[numLetra] = cbrt(numBase ** qntHoraEsperada)
                        listAlternativas[numLetra] = pretty(listAlternativas[numLetra])
                        isCorrect[numLetra] = "Nao"
                        howGenerated[numLetra] = "invertida e positiva"
                    else:
                        listAlternativas[numLetra] = -cbrt(numBase ** qntHoraEsperada)
                        listAlternativas[numLetra] = pretty(listAlternativas[numLetra])
                        isCorrect[numLetra] = "Nao"
                        howGenerated[numLetra] = "invertida e negativa"
                else:
                    numRandomTemporario = rnd.randint(0,1)

                    if numRandomTemporario == 0:

                        listAlternativas[numLetra] = sqrt(numBase ** qntHoraEsperada)
                        listAlternativas[numLetra] = pretty(listAlternativas[numLetra]) 
                        isCorrect[numLetra] = "Nao"
                        howGenerated[numLetra] = "invertida e positiva"
                    else:
                        listAlternativas[numLetra] = -sqrt(numBase ** qntHoraEsperada)
                        listAlternativas[numLetra] = pretty(listAlternativas[numLetra]) 
                        isCorrect[numLetra] = "Nao"
                        howGenerated[numLetra] = "invertida e negativa"
            else:
                numRandomTemporario = rnd.randint(2,3)

                if numRandomTemporario == 2:
                    numRandomTemporario = rnd.randint(0,1)

                    if numRandomTemporario == 0:
                        numRandomTemporario = rnd.randint(2, numBase)
                        listAlternativas[numLetra] = sqrt(numRandomTemporario)
                        listAlternativas[numLetra] = pretty(listAlternativas[numLetra])
                        isCorrect[numLetra] = "Nao"
                        howGenerated[numLetra] = "gerada aleatoriamente e positiva"
                    else:
                        numRandomTemporario = rnd.randint(2, numBase)
                        listAlternativas[numLetra] = -sqrt(numRandomTemporario)
                        listAlternativas[numLetra] = pretty(listAlternativas[numLetra])
                        isCorrect[numLetra] = "Nao"
                        howGenerated[numLetra] = "gerada aleatoriamente e negativa"
                else:
                    numRandomTemporario = rnd.randint(0,1)

                    if numRandomTemporario == 0:
                        numRandomTemporario = rnd.randint(2, numBase)
                        listAlternativas[numLetra] = cbrt(numRandomTemporario)
                        listAlternativas[numLetra] = pretty(listAlternativas[numLetra])
                        isCorrect[numLetra] = "Nao"
                        howGenerated[numLetra] = "gerada aleatoriamente e positiva"
                    else:
                        numRandomTemporario = rnd.randint(2, numBase)
                        listAlternativas[numLetra] = -cbrt(numRandomTemporario)
                        listAlternativas[numLetra] = pretty(listAlternativas[numLetra])
                        isCorrect[numLetra] = "Nao"
                        howGenerated[numLetra] = "gerada aleatoriamente e negativa"
                    
    # Cria a variável que será convertida em um arquivo json
    dados = {
        'equacaoExponencial' : [
            {
                'radicando' : numBase, 
                'indice': qntHoraDada,
                'expoente': qntHoraEsperada,
                'resposta' : resposta
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
                'enunciado': 'O crescimento de uma certa cultura de bactérias obedece à função X(t) = {}, em que X(t) é o número de bactérias no tempo t ≥ 0; C, p são constantes positivas. Verificando que o número inicial de bactérias X(0) é multiplicado por {} em {} horas, quantas se pode esperar no fim de {} horas?'.format(pretty(C*(numBase**(p*t))),numBase,qntHoraDada,qntHoraEsperada),
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
        k += 1
        

questoes.close()

