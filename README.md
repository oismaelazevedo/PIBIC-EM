# Aumentando a Interatividade no Ensino a Distância via Geração Automática de Questões

## 🗂️ Índice
* [Descrição](#-descrição)
* [Integrantes](#-integrantes)
    * [Professores orientadores](#professores-orientadores)
    * [Orientandos](#orientandos)
* [Atributos do projeto](#%EF%B8%8F-atributos-do-projeto)
    * [Tecnologias utilizadas](#tecnologias-utilizadas)
    * [Questões base utilizadas](#questões-base-utilizadas)
* [Objetivos](#-objetivos)
    * [Objetivos principais](#objetivos-principais)
    * [Objetivos estimados](#objetivos-estimados)
* [Pré-requisito](#-pré-requisitos)
    * [Python e um editor de código](#python-e-um-editor-de-código)
    * [Biblioteca necessária](#biblioteca-necessária)
    * [Servidor web](#servidor-web)
## 📋 Descrição
Este projeto faz parte do programa de iniciação científica para o ensino médio (PIBIC-EM). Um convênio da Universidade Federal do Rio de Janeiro (UFRJ) com diversas escolas públicas visando fomentar a pesquisa e desenvolvimento tecnológico, bem como formar cidadãos conscientes e futuros profissionais nas diversas áreas que formam a ciência como a conhecemos hoje.

## 🧑‍🤝‍🧑 Integrantes
### Professores orientadores
- Profa. Alayne Duarte Amorim, Colégio Pedro II - [Lattes](http://lattes.cnpq.br/6728091845181284)
- Prof. Daniel Sadoc Menasche, Universidade Federal do Rio de Janeiro - [Lattes](http://lattes.cnpq.br/9931198850020140)
- Prof. Marcus Paulo de Q. Amorim, Colégio Pedro II - [Lattes](http://lattes.cnpq.br/5890334014963199)
### Orientandos
- Estevão Vitor Gregorio Naval, Colégio Pedro II - [Lattes](http://lattes.cnpq.br/3949652173819005)
- Ismael C. S. da Costa de Azevedo, Colégio Pedro II - [Lattes](http://lattes.cnpq.br/2052748666550756)
- Kawan Pereira de Santana, Colégio Pedro II - [Lattes](http://lattes.cnpq.br/8677764261803115)

## 🛠️ Atributos do projeto
#### 🚧  Em construção...  🚧

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
### Questões base utilizadas

| Número da questão | Enunciado original | Fonte |
| :----------: | :----------: | :----------: |
| 163 | O pH de uma solução é definido por pH = log (1/H+), em que H+ é a concentração de hidrogênio em íons-grama por litro de solução. Determine o pH de uma solução tal que H+ = 1,0 x 10^-8. | Livro Fundamentos de Matemática Elementar - Vol. 02 |
| 166 | Determine a razão entre os logaritmos de 16 e 4 numa base qualquer. | Livro Fundamentos de Matemática Elementar - Vol. 02 |
| 169 | A soma dos logaritmos de dois números na base 9 é 1/2. Determine o produto desses números. | Livro Fundamentos de Matemática Elementar - Vol. 02 |
| 226 | O crescimento de uma certa cultura de bactérias obedece à função X(t) = C.e^kt, em que X(t) é o número de bactérias no tempo t >= 0; C, k são constantes positivas. Verificando que o número inicial de bactérias X(0) duplica em 4 horas, quantas se pode esperar no fim de 6 horas? | Livro Fundamentos de Matemática Elementar - Vol. 02 |  

## 🎯 Objetivos
### Objetivos principais
- [ ] Criar scripts em python para gerar as questões aleatoriamente e em uma grande quantidade
- [ ] Formular métodos de erros e aplicá-los em respostas a fim de torná-las falsas.
- [ ] Exportar as questões, as possíveis respostas e os atributos desta no formato de troca de dados JSON.
- [ ] Desenvolver uma aplicação web capaz de permitir a resolução das questões, além de ser capaz de gerenciá-las.
- [ ] Ter a capacidade de identificar as facilidades e dificuldades daqueles que usarão o sistema por meio do aprendizado de máquina ativo.
- [ ] Aplicar este aprendizado de máquina em uma inteligência artificial que poderá recomendar questões mais fáceis ou difíceis dependendo do desempenho do usuário.

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
