import random as rnd
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

    numFloatAleatorio01 = round(rnd.uniform(1,1000), 2)
    numFloatAleatorio02 = round(rnd.uniform(1,100), 2)
    ordemDez01 = rnd.randint(10,100)
    ordemDez02 = ordemDez01 + 1

    if(numFloatAleatorio01 * (10 ** ordemDez01) >= numFloatAleatorio02 * (10 ** ordemDez02)):
        resposta = "M ≥ N"
    else:
        resposta = "M < N"

    listLetra = ["A","B","C","D","E"]

    questaoCerta = rnd.choice(listLetra)
    questaoInvertida = rnd.choice(listLetra)

    while(questaoCerta == questaoInvertida):
        questaoInvertida = rnd.choice(listLetra)
        
    listAlternativas = [0,0,0,0,0]
    isCorrect = ['','','','','']
    howGenerated = ['','','','','']

    # Insere a resposta certa na letra escolhida para ser certa, uma letra recebe a questão invertida e o resto recebe números aleatórios
    numRandomTemporario = 0

    for numLetra in range(0,5):
        if questaoCerta == listLetra[numLetra]:
            listAlternativas[numLetra] = resposta
            isCorrect[numLetra] = "Sim"
            howGenerated[numLetra] = "nenhum"
        elif questaoInvertida == listLetra[numLetra]:
            if resposta == "M ≥ N":
                listAlternativas[numLetra] = "M < N" 
                isCorrect[numLetra] = "Nao"
                howGenerated[numLetra] = "invertida e positiva"
            else:
                listAlternativas[numLetra] = "M ≥ N" 
                isCorrect[numLetra] = "Nao"
                howGenerated[numLetra] = "invertida e positiva"
        else:

            if numRandomTemporario == 0:

                listAlternativas[numLetra] = "M + N = {} . 10<sup>{}</sup>".format(str(round(numFloatAleatorio01+ numFloatAleatorio02, 2)).replace('.', ','), ordemDez01 + ordemDez02)
                isCorrect[numLetra] = "Nao"
                howGenerated[numLetra] = "gerada aleatoriamente e positiva"
                numRandomTemporario += 1
            elif numRandomTemporario == 1:

                listAlternativas[numLetra] = "M . N = {} . 10<sup>{}</sup>".format(str(round(numFloatAleatorio01 * numFloatAleatorio02, 2)).replace('.', ','), ordemDez01 + ordemDez02)
                isCorrect[numLetra] = "Nao"
                howGenerated[numLetra] = "gerada aleatoriamente e positiva"
                numRandomTemporario += 1
            else:
                listAlternativas[numLetra] = "M ÷ N = {} . 10<sup>{}</sup>".format(str(round(numFloatAleatorio01 / numFloatAleatorio02, 2)).replace('.', ','), ordemDez01 - ordemDez02)
                isCorrect[numLetra] = "Nao"
                howGenerated[numLetra] = "gerada aleatoriamente e positiva"




    # Cria a variável que será convertida em um arquivo json
    dados = {
        'equacaoExponencial' : [
            {
                'numFloatAleatorio01':numFloatAleatorio01,
                'numFloatAleatorio02':numFloatAleatorio02,
                'ordemDez01':ordemDez01,
                'ordemDez02':ordemDez02,
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
                # str(numero_com_ponto).replace('.', ',')
                'enunciado': '(UF-RN-modificada) Dados os números M = {} . 10<sup>{}</sup> e N = {} . 10<sup>{}</sup>. Pode-se afirmar que:'.format(str(numFloatAleatorio01).replace('.', ','), ordemDez01, str(numFloatAleatorio02).replace('.', ','), ordemDez02),
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

