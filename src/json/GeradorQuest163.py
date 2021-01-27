import random as rnd
import json

expoenteConcentracao = rnd.randint(1,70)
resposta = round((expoenteConcentracao ** 2)/3, 2)

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

# Insere a resposta certa na letra escolhida para ser certa, uma letra recebe a questão invertida e o resto recebe números aleatórios
for numLetra in range(0, 5):
    if questaoCerta == listLetra[numLetra]:
        listAlternativas[numLetra] = resposta
    elif questaoInvertida == listLetra[numLetra]:
        listAlternativas[numLetra] = round(-(expoenteConcentracao ** 3)/2, 2)
    else:
        EhNegativoPositivo = rnd.randint(0,1)
        if (EhNegativoPositivo == 0): 
            listAlternativas[numLetra] = round((rnd.randint(1,expoenteConcentracao) ** 2)/3, 2) 
        else: 
            listAlternativas[numLetra] = round(-(rnd.randint(1,expoenteConcentracao) ** 2)/3, 2)

# Dá duas tentativas para o indivíduo acertar
for numTentativa in range(2):
    print(f"O pH de uma solução é definido por pH = log(1/H+), em que H+ é a concentração de hidrogênio em íons-gama por litro de solução. Determine o quadrado sobre três do pH de uma solução tal que H+ = 1,0 x e{expoenteConcentracao}. Admita que e = 10")
    print(f"a) {listAlternativas[0]}")
    print(f"b) {listAlternativas[1]}")
    print(f"c) {listAlternativas[2]}")
    print(f"d) {listAlternativas[3]}")
    print(f"e) {listAlternativas[4]}")
    respAluno = input()

    if(respAluno.upper() == questaoCerta):
        print("Parabéns!!! Acertou miserável!!!")
        break
    else:
        print("Resposta errada. Tente novamente")

