import random as rnd
from sympy import simplify, Symbol, pretty
import json

def elementosListaEhDistinta(lista):
    for indiceLista in range(len(lista)):
        for indiceListaComparacao in range(len(lista)):
            if indiceLista == 4:
                return True
            elif lista[indiceLista] == lista[indiceListaComparacao] and indiceLista != indiceListaComparacao:
                return False
            
enunciado = [None]*100
k = 0
while k < 100:

    questoes = open("questao{}-230c.json".format(k+1),'w')

    numBaseEsqrdEq = rnd.randint(2,1000)
    numBaseDireitaEq = rnd.randint(2,500)
    numExpoenteNumBaseDireitaEq = rnd.randint(2,3)

    while numBaseEsqrdEq % numBaseDireitaEq == 0 or numBaseDireitaEq % numBaseEsqrdEq == 0:
        numBaseEsqrdEq = rnd.randint(2,1000)
        numBaseDireitaEq = rnd.randint(2,500)

    resposta = "log{} ({})".format(numBaseEsqrdEq * (numBaseDireitaEq ** 2), (numBaseDireitaEq ** numExpoenteNumBaseDireitaEq) * numBaseEsqrdEq)

    x = Symbol('x')

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
                    if numExpoenteNumBaseDireitaEq == 2:
                        listAlternativas[numLetra] = "log{} ({})".format(numBaseDireitaEq * (numBaseEsqrdEq ** 2), (numBaseEsqrdEq ** 3) * numBaseDireitaEq)
                        isCorrect[numLetra] = "Nao"
                        howGenerated[numLetra] = "invertida e positiva"
                    else:
                        listAlternativas[numLetra] = "log{} ({})".format(numBaseDireitaEq * (numBaseEsqrdEq ** 2), (numBaseEsqrdEq ** 2) * numBaseDireitaEq)
                        isCorrect[numLetra] = "Nao"
                        howGenerated[numLetra] = "invertida e positiva"
                else:
                    if numExpoenteNumBaseDireitaEq == 2:
                        listAlternativas[numLetra] = "log{} (-{})".format(numBaseDireitaEq * (numBaseEsqrdEq ** 2), (numBaseEsqrdEq ** 3) * numBaseDireitaEq)
                        isCorrect[numLetra] = "Nao"
                        howGenerated[numLetra] = "invertida e negativa"
                    else:
                        listAlternativas[numLetra] = "log{} (-{})".format(numBaseDireitaEq * (numBaseEsqrdEq ** 2), (numBaseEsqrdEq ** 2) * numBaseDireitaEq)
                        isCorrect[numLetra] = "Nao"
                        howGenerated[numLetra] = "invertida e negativa"
            else:
                numRandomTemporario = rnd.randint(0,1)

                if numRandomTemporario == 0:
                    numRandomTemporario = rnd.randint(2,3)

                    if numRandomTemporario == 2:
                        listAlternativas[numLetra] = "log{} ({})".format(rnd.randint(2,500) * (rnd.randint(2,1000) ** 2), (rnd.randint(2,1000) ** 2) * rnd.randint(2,500)) 
                        isCorrect[numLetra] = "Nao"
                        howGenerated[numLetra] = "gerada aleatoriamente e positiva"
                    else:
                        listAlternativas[numLetra] = "log{} ({})".format(rnd.randint(2,500) * (rnd.randint(2,1000) ** 2), (rnd.randint(2,1000) ** 3) * rnd.randint(2,500))
                        isCorrect[numLetra] = "Nao"
                        howGenerated[numLetra] = "gerada aleatoriamente e positiva"
                else:

                    numRandomTemporario = rnd.randint(2,3)

                    if numRandomTemporario == 2:
                        listAlternativas[numLetra] = "log{} (-{})".format(rnd.randint(2,500) * (rnd.randint(2,1000) ** 2), (rnd.randint(2,1000) ** 2) * rnd.randint(2,500))
                        isCorrect[numLetra] = "Nao"
                        howGenerated[numLetra] = "gerada aleatoriamente e negativa"
                    else:
                        listAlternativas[numLetra] = "log{} (-{})".format(rnd.randint(2,500) * (rnd.randint(2,1000) ** 2), (rnd.randint(2,1000) ** 3) * rnd.randint(2,500))
                        isCorrect[numLetra] = "Nao"
                        howGenerated[numLetra] = "gerada aleatoriamente e negativa"

    # Cria a variável que será convertida em um arquivo json
    dados = {
        'equacaoExponencial' : [
            {
                'numBaseEsqrdEq': numBaseEsqrdEq,
                'numBaseDireitaEq': numBaseDireitaEq,
                'numExpoenteNumBaseDireitaEq': numExpoenteNumBaseDireitaEq,
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
                'enunciado': 'Resolva a equação. Admita que "**" = elevado a:\nc){} = {}'.format(simplify(numBaseDireitaEq ** (x-1)),simplify(numBaseEsqrdEq ** (numExpoenteNumBaseDireitaEq - 2*x))),
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
                   
