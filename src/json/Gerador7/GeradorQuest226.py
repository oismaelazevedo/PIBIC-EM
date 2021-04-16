import random as rnd
from sympy import pretty, sqrt, symbols
import json
from math import log10

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

    qntHoraDada = 2
    qntHoraEsperada = rnd.randint(3,10)

    while(qntHoraEsperada % 2 == 0):
        qntHoraEsperada = rnd.randint(3,10)
    
    resposta =  round(log10(sqrt(numBase ** qntHoraEsperada)),2)
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
                
                numRandomTemporario = rnd.randint(0,1)

                if numRandomTemporario == 0:

                    listAlternativas[numLetra] = round(log10(numBase),2)
                    listAlternativas[numLetra] = pretty(listAlternativas[numLetra]) 
                    isCorrect[numLetra] = "Nao"
                    howGenerated[numLetra] = "invertida e positiva"
                else:
                    listAlternativas[numLetra] = -round(log10(numBase),2)
                    listAlternativas[numLetra] = pretty(listAlternativas[numLetra])
                    isCorrect[numLetra] = "Nao"
                    howGenerated[numLetra] = "invertida e negativa"
            else:
                numRandomTemporario = rnd.randint(0,1)

                if numRandomTemporario == 0:
                    numRandomTemporario = rnd.randint(2, numBase)
                    listAlternativas[numLetra] = round(log10(sqrt(numRandomTemporario)),2)
                    listAlternativas[numLetra] = pretty(listAlternativas[numLetra])
                    isCorrect[numLetra] = "Nao"
                    howGenerated[numLetra] = "gerada aleatoriamente e positiva"
                else:
                    numRandomTemporario = rnd.randint(2, numBase)
                    listAlternativas[numLetra] = -round(log10(sqrt(numRandomTemporario)),2)
                    listAlternativas[numLetra] = pretty(listAlternativas[numLetra])
                    isCorrect[numLetra] = "Nao"
                    howGenerated[numLetra] = "gerada aleatoriamente e negativa"
                    
    # Cria a variável que será convertida em um arquivo json
    dados = {
        'equacaoExponencial' : [
            {
                'radicando' : numBase, 
                'indice': qntHoraDada,
                'expoente': 2,
                'qntHoraEsperada': qntHoraEsperada,
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
<<<<<<< HEAD
                'enunciado': 'O crescimento de uma certa cultura de bactérias obedece à função X(t) = C.{}^(p.t), em que X(t) é o número de bactérias no tempo t ≥ 0; C, p são constantes positivas. Verificando que o número inicial de bactérias X(0) é multiplicado por {} em {} horas, quantas vezes do valor inicial de bactérias se pode esperar no fim de {} horas? Admita que a resposta será o resultado do logarítmo da quantidade de vezes na base 10.'.format(numBase,numBase,qntHoraDada, qntHoraEsperada),
=======
                'enunciado': 'O crescimento de uma certa cultura de bactérias obedece à função X(t) = C.{}<sup>(p.t)</sup>, em que X(t) é o número de bactérias no tempo t ≥ 0; C, p são constantes positivas. Verificando que o número inicial de bactérias X(0) é multiplicado por {} em {} horas, quantas se pode esperar no fim de 2 horas?'.format(numBase,numBase,qntHoraDada),
>>>>>>> d9874bfb4769deccbef0a28629920e62cec7ccf9
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

