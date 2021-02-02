# Aumentando a Interatividade no Ensino a Distância via Geração Automática de Questões

## Descrição
Este projeto faz parte do programa de iniciação científica para o ensino médio (PIBIC-EM). Um convênio da Universidade Federal do Rio de Janeiro (UFRJ) com diversas escolas públicas visando fomentar a pesquisa e desenvolvimento tecnológico, bem como formar cidadãos conscientes e futuros profissionais nas diversas áreas que formam a ciência como a conhecemos hoje.

## Integrantes
### Professores orientadores
- Profa. Alayne Duarte Amorim, Colégio Pedro II ![Badge](https://img.shields.io/static/v1?label=Lattes&message=Alayne%20Duarte&color=blue&style=flat)
- Prof. Daniel Sadoc Menasche, Universidade Federal do Rio de Janeiro ![Badge](https://img.shields.io/static/v1?label=Lattes&message=Daniel%20Sadoc&color=blue&style=flat)
- Prof. Marcus Paulo de Q. Amorim, Colégio Pedro II ![Badge](https://img.shields.io/static/v1?label=Lattes&message=Marcus%20Amorim&color=blue&style=flat)
### Orientandos
- Estevão Vitor Gregorio Naval, Colégio Pedro II ![Badge](https://img.shields.io/static/v1?url=http%3A%2F%2Flattes.cnpq.br%2F3949652173819005
&label=Lattes&message=Estev%C3%A3o%20Naval&color=blue&style=flat)
- Ismael C. S. da Costa de Azevedo, Colégio Pedro II ![Badge](https://img.shields.io/static/v1?label=Lattes&message=Ismael%20Azevedo&color=blue&style=flat)
- Kawan Pereira de Santana, Colégio Pedro II ![Badge](https://img.shields.io/static/v1?label=Lattes&message=Kawan%20Santana&color=blue&style=flat)

## Objetivos principais
- [ ] Criar scripts em python para gerar as questões aleatoriamente e em uma grande quantidade
- [ ] Formular métodos de erros e aplicá-los em respostas a fim de torná-las falsas.
- [ ] Exportar as questões, as possíveis respostas e os atributos desta no formato de troca de dados JSON.
- [ ] Desenvolver uma aplicação web capaz de permitir a resolução das questões, além de ser capaz de gerenciá-las.
- [ ] Ter a capacidade de identificar as facilidades e dificuldades daqueles que usarão o sistema por meio do aprendizado de máquina ativo.
- [ ] Aplicar este aprendizado de máquina em uma inteligência artificial que poderá recomendar questões mais fáceis ou difíceis dependendo do desempenho do usuário.

## Objetivos estimados
- [ ] Permitir que estudantes exercitem seu conhecimento na área de logaritmo, fora ajudar professores que possuem uma baixa gama de questões na matéria citada.
- [ ] Servir de base para outros pesquisadores expandirem o projeto para outras áreas de estudo, tais como genética nas ciências biológicas, geometria analítica em exatas, dinâmica dos fluídos na física e assim por diante. 

## Pré-requisitos
### Biblioteca necessária
Primeiramente, para executar os scripts python, você deve instalar a biblioteca de código aberto [Sympy](https://www.sympy.org/pt/index.html). Você pode fazer isto via terminal com o seguinte comando:

    pip install sympy

**OBS.:** Caso você tenha pacotes, como o Anaconda, que já instalam a biblioteca Sympy, o pré-requisito acima não é necessário.

### Servidor web
A fim de rodar o sistema web, é necessário possuir um servidor HTTP com suporte a [PHP](https://www.php.net/) e [MySQL](https://www.mysql.com/). Você pode fazer isto manualmente, com a instalação do PHP, MySQL e um servidor qualquer ou pode se utilizar de gerenciadores como o [EasyPHP](https://www.easyphp.org/) ou [XAMPP](https://www.apachefriends.org/pt_br/index.html) que já incluem as tecnologias citadas. Fica ao seu critério.
