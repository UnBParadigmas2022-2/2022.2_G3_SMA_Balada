# Simulação de Balada

**Disciplina**: FGA0210 - PARADIGMAS DE PROGRAMAÇÃO - T02 <br>
**Nro do Grupo**: 03<br>
**Paradigma**: Sistema Multiagentes<br>

## Alunos

|Matrícula  |  Aluno |
| --------- | ------------------------------------------------------ |
| 170161897 | [Eduarda Servidio Claudino](https://github.com/ServidioEC)| 
| 190046091 | [Gustave Augusto Persijn](https://github.com/gpersijn) |
| 170034992 | [Gustavo Afonso Pires](https://github.com/GustavoAPS)  |
| 180113992 | [Lorrany Oliveira](https://github.com/Lorranyoliveira) |
| 190032863 | [Lorrayne Alves](https://github.com/LorrayneCardozo)   |
| 190036435 | [Pedro Henrique Carvalho](https://github.com/peh099)   |
| 180130889 | [Sávio Cunha de Carvalho](https://github.com/savioc2)  |
| 170164357 | [Ugor Marcilio Brandão](https://github.com/ubrando)    |

## Sobre 
O projeto é voltado para a prática da programação de multiagentes. O tema consiste na modelagem de uma balada onde o comportamento das pessoas é modelado a fim desse agente poder tomar decisões ou não tomar. Tendo isso em vista, alguns dos comportamentos do agente são:
* Movimento aleatório 
* Movimento em direção ao centro da balada
* Movimento em direção ao bar
* Movimento de volta ao centro
* Movimento para saída da balada

## Screenshots
Adicione 2 ou mais screenshots do projeto em termos de interface e/ou funcionamento.

## Instalação 
**Linguagens**: Python<br>
**Tecnologias**: mesa<br>
Após clonar o repositório, instale o requerimentos com seguinte comando no terminal:
```
pip install requirements.txt
```

## Uso 
O passo a passo para rodar o projeto é:
```
1. No diretório do projeto digite a python server.py no terminal e espero a interface carregar por completa ( quando os botôes aparecerem).
2. Aperte o botão "Iniciar balada" e divirta-se com a simulação da balada.
3. Lembre que também é possível adicionar mais participantes a simulação pressionando o botão "Adicionar Pessoas"
4. Caso queira saber o comportamento do agente em números, aperte "Check todo mundo" e observe o terminal.
5. Também é possível obter o histórico do comportamento da simulação no arquivo utils/log.txt 
```

## Vídeo
Adicione 1 ou mais vídeos com a execução do projeto.
Procure: 
(i) Introduzir o projeto;
(ii) Mostrar passo a passo o código, explicando-o, e deixando claro o que é de terceiros, e o que é contribuição real da equipe;
(iii) Apresentar particularidades do Paradigma, da Linguagem, e das Tecnologias, e
(iV) Apresentar lições aprendidas, contribuições, pendências, e ideias para trabalhos futuros.
OBS: TODOS DEVEM PARTICIPAR, CONFERINDO PONTOS DE VISTA.
TEMPO: +/- 15min

## Participações
|Nome do Membro | Contribuição | Significância da Contribuição para o Projeto (Excelente/Boa/Regular/Ruim/Nula) |
| -- | -- | -- |
| Eduarda Servídio  | Criação do log com nome dos agentes e seus comportamentos; criação da interface e adição de gifs no frontend. | Excelente |
| Gustave Augusto Persijn  | Implementação do comportamento do agente, funções gotobebida, gotosaida, gotocenter, backtocenter. | Excelente |
| Gustavo Afonso Pires  | Desacoplamento do mesa core e da interface gráfica nativa do mesa, integração gráfica do tkinter com o turtle, suporte com o código dos colegas, refatoração do código.| Execelente |
| Lorrany Oliveira  |  Desacoplamento do mesa core e da interface gráfica nativa do mesa, integração gráfica do tkinter com o turtle, refatoração do código. | Excelente |
| Lorrayne Alves  | Criação do log com nome dos agentes e seus comportamentos; criação da interface e adição de gifs no frontend. | Excelente |
| Pedro Henrique Carvalho  | implementação do comportamento do agente, construção da Balada Model, Implementação do painel e botões.  | Excelente |
| Sávio Cunha de Carvalho  | Implementação do comportamento do agente, funções gotobebida, gotosaida, gotocenter. | Excelente |
| Ugor Marcilio Brandão  | implementação do comportamento do agente, construção da Balada Model, Implementação do painel e botões. | Excelente  |

## Outros 
### Lições Aprendidas
|Nome do Membro | Lições Aprendidas | 
| -------- | -- | 
| Eduarda Servídio  |  com a realização do projeto foi possível entender o funcionamento dos sistemas multiagentes e seus comportamentos. Além de como personalizar a aplicação para construção da interface no nosso projeto. Foi de grande valia as tentativas para realizar esse trabalho.|  
| Gustave Augusto Persijn  | Aprendi muito sobre sistemas multiagentes através da aplicação prática da proposta do nosso projeto, em que pude pesquisar e estudar mais sobre como funciona o Mesa, além de entender mais sobre os atributos e comportamentos que vão compor cada agente, além das interações entre eles. |  
| Gustavo Afonso Pires  | É muito importante conhecer bem a plataforma de código, no caso do Mesa apesar de algumas facilitações da ferramenta, foi muito difícil personalizar alguns aspectos.| 
| Lorrany Oliveira  |  Achei bastante interessante e gostei muito do nosso projeto, acredito que ficou mais claro como funciona o sistema de multiagentes.|  
| Lorrayne Alves  | Realizando o projeto ficou muito mais claro sobre o funcionamento de  Sistemas Multiagentes e seus comportamentos, principalmente devido a cooperação da equipe, visto que todos se ajudaram e compartilharam diversos conhecimentos. | 
| Pedro Henrique Carvalho  | O aprendizado com sistema Multiagentes foi satisfatório. Foi possível aprender como modelar comportamentos para o Agente, como integrar diferentes bibliotecas para uma interação completa dentro do escopo definido. |
| Sávio Cunha de Carvalho  |Consegui entender o Paradigma de Sistemas Multiagente de forma prática. Gostei do paradigma e da sua aplicação no projeto, evidenciando vários comportamentos dos agentes. | 
| Ugor Marcilio Brandão  | A Programação Multiagente foi bastante interessante. A gente vai aprendendo a programar sempre com comportamentos de causa e efeito e pensar multiagente é pensar que ao modelar um ambiente os agente envolvidos podem ter decisões diferentes aos estímulos (até mesmo não reagir) e ter um comportamento mesmo que não esteja interagindo. Enfim, o projeto foi divertido e deu pra perceber que dá pra ir bem mais longe.|  
### Percepções;
|Nome do Membro | Percepções | 
| -- | -- | 
| Eduarda Servídio  |  Não é tão trivial mexer com sistemas multiagentes, não estamos acostumados com esse tipo de programação, foge da convencional. E como decidimos utilizar o mesa, sentimos um pouco de dificuldade em estabelecer as funções de comportamento, precisamos até mesmo mudar a temática do trabalho para conseguir entregar algo.|  
| Gustave Augusto Persijn  | Achei extremamente interessante o sistema de multiagentes, mas confesso que no início foi difícil entender a lógica que se passava na interação entre eles, mas no final entendi melhor a lógica por trás disso. |  
| Gustavo Afonso Pires  | Acho que o paradigma é muito interessante, certamente é base para muitas tecnologias acopladas em linguagens de uso corriqueiro, apenas senti falta de maior desacoplamento nas bibliotecas do Mesa.| 
| Lorrany Oliveira  |  Achei o paradigma interessante, mas achei complicado de entender a lógica dele inicialmente.|  
| Lorrayne Alves  | O paradigma SMA trouxe uma visão diferente da programação convencional, o que não foi uma tarefa fácil devido às nossas limitações de conhecimento sobre o mesa. | 
| Pedro Henrique Carvalho  | O paradigma de Sistemas Multiagentes trouxe uma visão diferente, mostrando que pode ser útil ou ideal para diferentes tipos de aplicação. Também foi possível perceber que o Mesa abstrai muito do que pode ser feito com Sistemas MultiAgentes, e mesmo que facilite o uso para alguns objetivos, possui fragilidades. |
| Sávio Cunha de Carvalho  |osso projeto evidenciou bem o uso do paradigma de Sistemas Multiagentes e entendeu como funciona o mesa e suas limitações, possibilitando a criação da nossa balada. | 
| Ugor Marcilio Brandão  | A biblioteca do Mesa facilita algumas coisas mas deixa a programação engessada. A gente tinha bastante vontade de produzir um front end bonito e foi trabalhoso de fazer. O mais importante na minha visão foi a modelagem do comportamento do agente.|  

### Fragilidades
|Nome do Membro | Fragilidades | 
| -- | -- | 
| Eduarda Servídio  |  |  
| Gustave Augusto Persijn  |  |  
| Gustavo Afonso Pires  |  O projeto tem alguns bugs e problemas de desempenho, talvez algoritmos mais eficientes podem ajudar com os problemas de desempenho.| 
| Lorrany Oliveira  |  |  
| Lorrayne Alves  | É possível encontrar uma fragilidade do sistema nos agentes que possuem poucos comportamentos. | 
| Pedro Henrique Carvalho  | Os agentes poderiam ter outros comportamentos (alguns foram traçados, mas não implementados). |
| Sávio Cunha de Carvalho  |osso projeto evidenciou bem o uso do paradigma de Sistemas Multiagentes e entendeu como funciona o mesa e suas limitações, possibilitando a criação da nossa balada. | 
| Ugor Marcilio Brandão  | O movimento aleatório dos agentes ainda faz com que eles fiquem mais em uma determinada área. A interface poderia ser maior. Os agentes poderiam ser deletados e realmente apagados da memória. | 

### Trabalhos Futuros.
|Nome do Membro | Ideias para trabalhos futuros | 
| -- | -- | 
| Eduarda Servídio  | Criação de mais comportamentos para os agentes da balada, quanto mais comportamentos mais interessante e mais próximo da situação real vai ficando a aplicação. |  
| Gustave Augusto Persijn  |  |  
| Gustavo Afonso Pires  |  Acredito que o stack de bibliotecas e o desacoplamento usado para a interface visual pode vir a ser útil para projetos futuros que não queriam usar a interface genérica do Mesa.| 
| Lorrany Oliveira  |  |  
| Lorrayne Alves  |Criação de novos comportamentos para os agentes.
| Pedro Henrique Carvalho  | Os agentes poderiam ter outros comportamentos (alguns foram traçados, mas não implementados). |
| Sávio Cunha de Carvalho  |Adição de novos comportamentos para os agentes. | 
| Ugor Marcilio Brandão  | O projeto conta com alguns gifs não utilizados como flerte, briga e passando mal que não foram implementados como comportamentos. Poderia acrescentar um botão de troca de música e com essa troca o comportamento dos agentes também mudariam. Movimento aleatório dos agentes mais fluidos no mapa.  | 
<br>
## Fontes
* tkinker: <https://docs.python.org/3/library/tkinter.html>
* mesa: <https://mesa.readthedocs.io/en/latest/tutorials/intro_tutorial.html>
* Turtle: <https://docs.python.org/3/library/turtle.html>
* Pygame: <https://www.pygame.org/news>
