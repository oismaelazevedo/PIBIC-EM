# Aumentando a Interatividade no Ensino a Distância via Geração Automática de Questões

## 🗂️ Índice
* [Descrição](#-descrição)
* [Integrantes](#-integrantes)
    * [Professores orientadores](#professores-orientadores)
    * [Orientandos](#orientandos)
* [Atributos do projeto](#%EF%B8%8F-atributos-do-projeto)
    * [Status geral](#Status-geral)
    * [Tecnologias utilizadas](#tecnologias-utilizadas)
    * [Questões base criadas](#questões-base-criadas)
    * [Questões base utilizadas](#questões-base-utilizadas)
    * [Tipos de erro utilizados](#Tipos-de-erro-utilizados)
* [Objetivos](#-objetivos)
    * [Objetivos principais](#objetivos-principais)
    * [Objetivos estimados](#objetivos-estimados)
* [Pré-requisito](#-pré-requisitos)
    * [Python e um editor de código](#python-e-um-editor-de-código)
    * [Biblioteca necessária](#biblioteca-necessária)
    * [Servidor web](#servidor-web)
## 📋 Descrição
O projeto visa criar um banco de questões não-repetidas e aleatórias baseadas em um grupamento de questões-esqueleto que serão alterados a fim de gerar novos itens especificados para cada aluno. Além disto, também é pretendido montar um sistema web online intuitivo para o uso dos itens formulados. O ponto-chave deste trabalho reside na tentativa de criar uma inteligência computacional capaz de avaliar o perfil de acertos e erros do aluno e, com base nisto, enviar uma pergunta mais fácil ou difícil. Na perspectiva de futuros trabalhos acadêmicos, espera-se que este conjunto de soluções possam ser usadas pelos mais diversos profissionais da educação que modularão e expandirão o sistema para outras áreas do conhecimento humano.

Este projeto faz parte do programa de iniciação científica para o ensino médio (PIBIC-EM). Um convênio da Universidade Federal do Rio de Janeiro (UFRJ) com diversas escolas públicas visando fomentar a pesquisa e desenvolvimento tecnológico, bem como formar cidadãos conscientes e futuros profissionais nas diversas áreas que formam a ciência como a conhecemos hoje.

## 🧑‍🤝‍🧑 Integrantes
### Professores orientadores
- Prof. Ph.D. Daniel Sadoc Menasche, Universidade Federal do Rio de Janeiro - [Currículo Lattes](http://lattes.cnpq.br/9931198850020140)
- Profa. M.Sc. Alayne Duarte Amorim, Colégio Pedro II - [Currículo Lattes](http://lattes.cnpq.br/6728091845181284)
- Prof. M.Sc. Marcus Paulo de Q. Amorim, Colégio Pedro II - [Currículo Lattes](http://lattes.cnpq.br/5890334014963199)
### Orientandos
- Estevão Vitor Gregorio Naval - [Currículo Lattes](http://lattes.cnpq.br/3949652173819005)
- Ismael C. S. da Costa de Azevedo - [Currículo Lattes](http://lattes.cnpq.br/2052748666550756)
- Kawan Pereira de Santana - [Currículo Lattes](http://lattes.cnpq.br/8677764261803115)

## 🛠️ Atributos do projeto

### Status geral
#### 🚧  Liberar o sistema web para o público geral com o objetivo deste enviar registros que popularão o banco de dados. O objetivo aqui é permitir o aprendizado de máquina pela avaliação dos dados reunidos.  🚧

### Tecnologias utilizadas
- [Python](https://www.python.org/)
- [Sympy](https://www.sympy.org/pt/index.html)
- [Json](https://json.org/json-pt.html)
- [PHP](https://www.php.net/)
- [HTML](https://developer.mozilla.org/pt-br/docs/Glossario/HTML)
- [CSS](https://developer.mozilla.org/pt-BR/docs/Web/CSS)
- [JavaScript](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript)
- [Bootstrap](https://getbootstrap.com/)
- [MySQL](https://www.mysql.com/)

### Questões base criadas

| Número da questão | Enunciado original | Enunciado adaptado | Fonte |
| :----------: | :----------: | :----------: | :----------: |
| 11 | (UF-RN) Dados os números M = 9,84 x 10<sup>15</sup> e N = 1,23 x 10<sup>16</sup>, pode-se afirmar que: | (UF-RN-modificada) Dados os números M = <número_aleatório> X 10<sup><número_aleatório></sup> e N = <número_aleatório> X 10<sup><número_aleatório></sup>. Pode-se afirmar que: | Vestibular UFRN |
| 14 | (Fuvest) O número x > 1 tal que log<sub>x</sub> 2 = log<sub>4</sub> x é | (Fuvest-modificada) Temos que x > 1 tal que log<sub>x</sub> (<número_aleatório>) = log<sub><número_aleatório></sub> (x). Assim sendo, o logarítmo de x na base 10 é: | Vestibular Fuvest |
| 71 - a | 2<sup>x</sup> = 128 | Resolva a seguinte equação exponencial: <número_aleatório><sup><número_aleatório></sup> = <número_aleatório> | Livro Fundamentos de Matemática Elementar - Vol. 02 |
| 71 - c | 2<sup>x</sup> = 1/16 | Resolva a seguinte equação exponencial: <número_aleatório><sup><número_aleatório></sup> = 1/<número_aleatório> | Livro Fundamentos de Matemática Elementar - Vol. 02 |
| 71 - d | (1/5)<sup>x</sup> = 125 | Resolva a seguinte equação exponencial: (1/<número_aleatório>)<sup>x</sup> = <número_aleatório> | Livro Fundamentos de Matemática Elementar - Vol. 02 |
| 71 - e | (<sup>3</sup>√2)<sup>x</sup> = 8 | Resolva a seguinte equação exponencial: (√<número_aleatório>)<sup>x</sup> = <número_aleatório> | Livro Fundamentos de Matemática Elementar - Vol. 02 |
| 71 - f | (<sup>4</sup>√3)<sup>x</sup> = <sup>3</sup>√9 | Resolva a seguinte equação exponencial: (√<número_aleatório>)<sup>x</sup> = √<número_aleatório> | Livro Fundamentos de Matemática Elementar - Vol. 02 |
| 71 - j | (<sup>5</sup>√4)<sup>x</sup> = 1/√8 | Resolva a seguinte equação exponencial: (√<número_aleatório>)<sup>x</sup> = 1/√<número_aleatório> | Livro Fundamentos de Matemática Elementar - Vol. 02 |
| 79 - a | Resolva as seguintes equações exponenciais: a) 3<sup>x - 1</sup> - 3<sup>x</sup> + 3<sup>x + 1</sup> + 3<sup>x + 2</sup> = 306 | Resolva a seguinte equação exponencial: <express_aleatoria> = <número_aleatório> | Livro Fundamentos de Matemática Elementar - Vol. 02 |
| 79 - e | Resolva as seguintes equações exponenciais: e) 3 x 2<sup>x</sup> - 5 x 2<sup>x + 1</sup> + 5 x 2<sup>x + 3</sup> - 2<sup>x + 5</sup> = 2 | Resolva a seguinte equação exponencial: <express_aleatoria> = <número_aleatório> | Livro Fundamentos de Matemática Elementar - Vol. 02 |
| 79 - f | Resolva as seguintes equações exponenciais: f) 2 x 4<sup>x + 2<sup> - 5 x 4<sup>x + 1</sup> - 3 x 2<sup>2x + 1</sup> - 4<sup>x</sup> = 20 | Resolva a seguinte equação exponencial: <express_aleatoria> = <número_aleatório> | Livro Fundamentos de Matemática Elementar - Vol. 02 |
| 91 - a | Resolva as equações em IR<sub>+</sub>: a) X<sup>x² - 5x + 6</sup> = 1 | Determine as raízes da equação em IR+: X<sup><número_aleatório>y² + <número_aleatório>y + <número_aleatório></sup> = 1 | Livro Fundamentos de Matemática Elementar - Vol. 02 |
| 91 - b | Resolva as equações em IR<sub>+</sub>: b) X<sup>2x² - 7x + 4</sup> = X | Determine as raízes da equação em IR+: X<sup><número_aleatório>y² + <número_aleatório>y + <número_aleatório></sup> = X | Livro Fundamentos de Matemática Elementar - Vol. 02 |
| 135 - a | Calcule pela definição os seguintes logaritmos: a) log<sub>4</sub> 16 | Calcule pela definição os seguintes logaritmos: a) log<sub><número_aleatório></sub> <número_aleatório> | Livro Fundamentos de Matemática Elementar - Vol. 02 |
| 135 - b | Calcule pela definição os seguintes logaritmos: b) log<sub>3</sub> 1/9 | Calcule pela definição os seguintes logaritmos: log<sub><número_aleatório></sub> (1/<número_aleatório>) | Livro Fundamentos de Matemática Elementar - Vol. 02 |
| 135 - c | Calcule pela definição os seguintes logaritmos: c) log<sub>81</sub> 3 | Calcule pela definição os seguintes logaritmos: log<sub><número_aleatório></sub> <número_aleatório> | Livro Fundamentos de Matemática Elementar - Vol. 02 |
| 135 - d | Calcule pela definição os seguintes logaritmos: d) log<sub>1/2</sub> 8 | Calcule pela definição os seguintes logaritmos: log<sub>1/<número_aleatório></sub> <número_aleatório> | Livro Fundamentos de Matemática Elementar - Vol. 02 |
| 135 - f | Calcule pela definição os seguintes logaritmos: f) log<sub>27</sub> 81 | Calcule pela definição os seguintes logaritmos: log<sub><número_aleatório></sub> (<número_aleatório>) | Livro Fundamentos de Matemática Elementar - Vol. 02 |
| 135 - i | Calcule pela definição os seguintes logaritmos: i) log<sub>9</sub> 1/27 | Calcule pela definição os seguintes logaritmos: log<sub><número_aleatório></sub> (1/<número_aleatório>) | Livro Fundamentos de Matemática Elementar - Vol. 02 |
| 163 | O pH de uma solução é definido por pH = log<sub>10</sub>(1/H+), em que H+ é a concentração de hidrogênio em íons-grama por litro de solução. Determine o pH de uma solução tal que H+ = 1,0 x 10<sup>-8</sup>. | O pH de uma solução é definido por pH = log(1/H+), em que H+ é a concentração de hidrogênio em íons-gama por litro de solução. Determine o quadrado sobre três do pH de uma solução tal que H+ = 1,0 x e<sup><número_aleatório></sup>. Admita que e = 10 | Livro Fundamentos de Matemática Elementar - Vol. 02 |
| 166 | Determine a razão entre os logaritmos de 16 e 4 numa base qualquer. | Determine o valor aproximado da razão entre os logaritmos de <número_aleatório> e <número_aleatório> numa base qualquer: | Livro Fundamentos de Matemática Elementar - Vol. 02 |
| 169 | A soma dos logaritmos de dois números na base 9 é 1/2. Determine o produto desses números. | A soma dos logaritmos de dois números na base <número_aleatório> é 1/<2_ou_3>. Determine o produto desses números. | Livro Fundamentos de Matemática Elementar - Vol. 02 |
| 190 | (PUC-PR) Se log (3x + 23) - log (2x - 3) = log 4, encontrar x. | (PUC-PR-modificada) Se log(<express_aleatoria>) - log(<express_aleatoria>) = log <número_aleatório>, então x é igual a: | Vestibular da Pontifícia Universidade Católica do Paraná |
| 226 | O crescimento de uma certa cultura de bactérias obedece à função X(t) = C.e<sup>kt</sup>, em que X(t) é o número de bactérias no tempo t >= 0; C, k são constantes positivas. Verificando que o número inicial de bactérias X(0) duplica em 4 horas, quantas se pode esperar no fim de 6 horas? | O crescimento de uma certa cultura de bactérias obedece à função X(t) = C.<número_aleatório><sup>kt</sup>, em que X(t) é o número de bactérias no tempo t >= 0; C, k são constantes positivas. Verificando que o número inicial de bactérias X(0) é multiplicado por <número_aleatório> em <2_ou_3> horas, quantas se pode esperar no fim de <número_aleatório> horas? | Livro Fundamentos de Matemática Elementar - Vol. 02 |
| 227 | Uma substância radioativa está em processo de desintegração, de modo que no instante t a quantidade não desintegrada é A(t) = A(0) . e<sup>-3t</sup>, em que A(0) indica a quantidade da substância no instante t = 0. Calcule o tempo necessário para que a metade da quantidade inicial se desintegre. | Uma substância radioativa está em processo de desintegração, de modo que no instante t a quantidade não desintegrada é A(t) = A(0).<número_aleatório><sup>-<número_aleatório>t</sup>, em que A(0) indica a quantidade de substância no instante t = 0. Calcule o tempo necessário para que a quantidade inicial dividida por <número_aleatório> se desintegre. | Livro Fundamentos de Matemática Elementar - Vol. 02 |
| 228 | A lei de decomposição do radium no tempo t >= 0 é dada por M(t) = Ce<sup>-kt</sup>, em que M(t) é quantidade de radium no tempo t; C, K são constantes positivas (e é a base do logaritmo neperiano). Se a metade da quantidade primitiva M(0) desaparece em 1600 anos, qual a quantidade perdida em 100 anos? | A lei de decomposição de um elemento X no tempo t >= 0 é dada por M(t) = C<número_aleatório><sup>-kt</sup>, em que M(t) é quantidade de X no tempo t; C, K são constantes positivas. Se a quantidade primitiva M (0), quando dividida por <número_aleatório>, desaparece em <número_aleatório> anos, qual a quantidade perdida em <número_aleatório> anos? | Livro Fundamentos de Matemática Elementar - Vol. 02 |
| 230 - a | Resolva as equações: a) 2<sup>x</sup> = 3<sup>x + 2</sup> | Resolva a equação. Admita que "**" = elevado a: a)<número_aleatório><sup><express_aleatoria></sup> = <número_aleatório><sup><express_aleatoria></sup> | Livro Fundamentos de Matemática Elementar - Vol. 02 |
| 230 - b | Resolva as equações: b) 7<sup>2x - 1</sup> = 3<sup>3x + 4</sup> | Resolva a equação. Admita que "**" = elevado a: b)<número_aleatório><sup><express_aleatoria></sup> = <número_aleatório><sup><express_aleatoria></sup> | Livro Fundamentos de Matemática Elementar - Vol. 02 |
| 230 - c | Resolva as equações: b) 5<sup>x - 1</sup> = 3<sup>4 - 2x</sup> | Resolva a equação. Admita que "**" = elevado a: c)<número_aleatório><sup><express_aleatoria></sup> = <número_aleatório><sup><express_aleatoria></sup> | Livro Fundamentos de Matemática Elementar - Vol. 02 |
| 238 - a | log<sub>4</sub> (3x + 2) = log<sub>4</sub> (2x + 5) | Resolva a equação: a) log<sub><número_aleatório></sub> (<express_aleatoria>) = log<sub><número_aleatório></sub> (<express_aleatoria>) | Livro Fundamentos de Matemática Elementar - Vol. 02 |
| 238 - c | log<sub>2</sub> (5x<sup>2</sup> - 14x + 1) = log<sub>2</sub> (4x<sup>2</sup> - 4x - 20) | Resolva a equação:\nc) log<sub><número_aleatório></sub> (<express_aleatoria>) = log<sub><número_aleatório></sub> (<express_aleatoria>) | Livro Fundamentos de Matemática Elementar - Vol. 02 |
| 401 | O valor de C de um capital (empregado a uma taxa i de juros capitalizados periodicamente ao fim do período), após t períodos, é dado por C = C<sub>0</sub> . (1 + i)<sup>t</sup>, en que C<sub>0</sub> é o valor inicial. Qual é o tempo necessário para que um capital empregado à taxa de 2% ao mês, com juros capitalizados mensamelmente, dobre de valor? | O valor C de um capital (empregado a uma taxa i de juros capitalizados periodicamente ao fim do período), após t períodos, é dado por C = C<sub>0</sub> . (1 + i)<sup>t</sup>, em que C<sub>0</sub> é o valor inicial. Qual é o tempo necessário para que um capital empregado à taxa de <número_aleatório>% ao mês, com juros capitalizados mensalmente, seja multiplicado por <número_aleatório>? Admita que log<número_aleatório> = <log_do_número_aleatório> e log<número_aleatório> = <log_do_número_aleatório> | Livro Fundamentos de Matemática Elementar - Vol. 02 |

### Questões base utilizadas

| Número da questão | Enunciado original | Enunciado adaptado | Fonte |
| :----------: | :----------: | :----------: | :----------: |
| 11 | (UF-RN) Dados os números M = 9,84 x 10<sup>15</sup> e N = 1,23 x 10<sup>16</sup>, pode-se afirmar que: | (UF-RN-modificada) Dados os números M = <número_aleatório> X 10<sup><número_aleatório></sup> e N = <número_aleatório> X 10<sup><número_aleatório></sup>. Pode-se afirmar que: | Vestibular UFRN |
| 14 | (Fuvest) O número x > 1 tal que log<sub>x</sub> 2 = log<sub>4</sub> x é | (Fuvest-modificada) Temos que x > 1 tal que log<sub>x</sub> (<número_aleatório>) = log<sub><número_aleatório></sub> (x). Assim sendo, o logarítmo de x na base 10 é: | Vestibular Fuvest |
| 163 | O pH de uma solução é definido por pH = log<sub>10</sub>(1/H+), em que H+ é a concentração de hidrogênio em íons-grama por litro de solução. Determine o pH de uma solução tal que H+ = 1,0 x 10<sup>-8</sup>. | O pH de uma solução é definido por pH = log(1/H+), em que H+ é a concentração de hidrogênio em íons-gama por litro de solução. Determine o quadrado sobre três do pH de uma solução tal que H+ = 1,0 x e<sup><número_aleatório></sup>. Admita que e = 10 | Livro Fundamentos de Matemática Elementar - Vol. 02 |
| 166 | Determine a razão entre os logaritmos de 16 e 4 numa base qualquer. | Determine o valor aproximado da razão entre os logaritmos de <número_aleatório> e <número_aleatório> numa base qualquer: | Livro Fundamentos de Matemática Elementar - Vol. 02 |
| 169 | A soma dos logaritmos de dois números na base 9 é 1/2. Determine o produto desses números. | A soma dos logaritmos de dois números na base <número_aleatório> é 1/<2_ou_3>. Determine o produto desses números. | Livro Fundamentos de Matemática Elementar - Vol. 02 |
| 71 - a | 2<sup>x</sup> = 128 | Resolva a seguinte equação exponencial: <número_aleatório><sup><número_aleatório></sup> = <número_aleatório> | Livro Fundamentos de Matemática Elementar - Vol. 02 |
| 226 | O crescimento de uma certa cultura de bactérias obedece à função X(t) = C.e<sup>kt</sup>, em que X(t) é o número de bactérias no tempo t >= 0; C, k são constantes positivas. Verificando que o número inicial de bactérias X(0) duplica em 4 horas, quantas se pode esperar no fim de 6 horas? | O crescimento de uma certa cultura de bactérias obedece à função X(t) = C.<número_aleatório><sup>kt</sup>, em que X(t) é o número de bactérias no tempo t >= 0; C, k são constantes positivas. Verificando que o número inicial de bactérias X(0) é multiplicado por <número_aleatório> em <2_ou_3> horas, quantas se pode esperar no fim de <número_aleatório> horas? | Livro Fundamentos de Matemática Elementar - Vol. 02 |
| 227 | Uma substância radioativa está em processo de desintegração, de modo que no instante t a quantidade não desintegrada é A(t) = A(0) . e<sup>-3t</sup>, em que A(0) indica a quantidade da substância no instante t = 0. Calcule o tempo necessário para que a metade da quantidade inicial se desintegre. | Uma substância radioativa está em processo de desintegração, de modo que no instante t a quantidade não desintegrada é A(t) = A(0).<número_aleatório><sup>-<número_aleatório>t</sup>, em que A(0) indica a quantidade de substância no instante t = 0. Calcule o tempo necessário para que a quantidade inicial dividida por <número_aleatório> se desintegre. | Livro Fundamentos de Matemática Elementar - Vol. 02 |
| 79 - f | Resolva as seguintes equações exponenciais: f) 2 x 4<sup>x + 2<sup> - 5 x 4<sup>x + 1</sup> - 3 x 2<sup>2x + 1</sup> - 4<sup>x</sup> = 20 | Resolva a seguinte equação exponencial: <express_aleatoria> = <número_aleatório> | Livro Fundamentos de Matemática Elementar - Vol. 02 |
| 401 | O valor de C de um capital (empregado a uma taxa i de juros capitalizados periodicamente ao fim do período), após t períodos, é dado por C = C<sub>0</sub> . (1 + i)<sup>t</sup>, en que C<sub>0</sub> é o valor inicial. Qual é o tempo necessário para que um capital empregado à taxa de 2% ao mês, com juros capitalizados mensamelmente, dobre de valor? | O valor C de um capital (empregado a uma taxa i de juros capitalizados periodicamente ao fim do período), após t períodos, é dado por C = C<sub>0</sub> . (1 + i)<sup>t</sup>, em que C<sub>0</sub> é o valor inicial. Qual é o tempo necessário para que um capital empregado à taxa de <número_aleatório>% ao mês, com juros capitalizados mensalmente, seja multiplicado por <número_aleatório>? Admita que log<número_aleatório> = <log_do_número_aleatório> e log<número_aleatório> = <log_do_número_aleatório> | Livro Fundamentos de Matemática Elementar - Vol. 02 |


### Tipos de erro utilizados

| Tipo de erro | Descrição |
| :----------: | :----------: |
| Invertida | Erro em que a fórmula para se chegar ao resultado é trocada |
| Aleatória | Um número é gerado por pseudoaleatoriedade, mas dentro dos moldes da fórmula do resultado |
| Sinal trocado | O sinal do resultado final é trocado. Sempre vem acompanhado com os erros anteriores |

## 🎯 Objetivos
### Objetivos principais
- [x] Criar scripts em python para gerar as questões aleatoriamente e em uma grande quantidade
- [x] Formular métodos de erros e aplicá-los em respostas a fim de torná-las falsas.
- [x] Exportar as questões, as possíveis respostas e os atributos desta no formato de troca de dados JSON.
- [x] Desenvolver uma aplicação web capaz de permitir a resolução das questões, além de ser capaz de gerenciá-las.
- [ ] Liberar o sistema web para o público geral com o objetivo deste enviar registros que popularão o banco de dados. O objetivo aqui é permitir o aprendizado de máquina pela avaliação dos dados reunidos.
- [ ] Ter a capacidade de identificar as facilidades e dificuldades daqueles que usarão o sistema por meio do aprendizado de máquina ativo.
- [ ] Aplicar este aprendizado de máquina em uma inteligência artificial que recomendará questões mais fáceis ou difíceis dependendo do desempenho do usuário.

### Objetivos estimados
- [ ] Permitir que estudantes exercitem seu conhecimento na área de logaritmo, fora ajudar professores que possuem uma baixa gama de questões na matéria citada.
- [ ] Servir de base para outros pesquisadores expandirem o projeto para outras áreas de estudo, tais como genética nas ciências biológicas, geometria analítica em exatas, dinâmica dos fluídos na física e assim por diante. 

## 📑 Pré-requisitos
### Python e um editor de código
Antes de tudo, é importante se ter instalado o [interpretador python](https://www.python.org/downloads/), já que os geradores estão baseados na linguagem de programação [python](https://www.python.org/). Além disto, ter um editor de código, tais como o [Visual code](https://code.visualstudio.com/), [Atom](https://atom.io/), [Notepad++](https://notepad-plus-plus.org/), etc, na sua máquina também é importante para a execução dos scripts python.
### Biblioteca necessária
Para executar os scripts python, você deve instalar a biblioteca de código aberto [Sympy](https://www.sympy.org/pt/index.html). Você pode fazer isto via terminal com o seguinte comando:

    pip install sympy

**OBS.:** Caso você tenha pacotes, como o Anaconda, que já instalam a biblioteca Sympy, o pré-requisito acima não é necessário.

### Servidor web
A fim de rodar o sistema web, é necessário possuir um servidor HTTP com suporte a [PHP](https://www.php.net/) e [MySQL](https://www.mysql.com/). Você pode fazer isto manualmente, com a instalação do PHP, MySQL e um servidor qualquer ou pode se utilizar de gerenciadores como o [EasyPHP](https://www.easyphp.org/) ou [XAMPP](https://www.apachefriends.org/pt_br/index.html) que já incluem as tecnologias citadas. Fica ao seu critério.
