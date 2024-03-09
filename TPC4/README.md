# TPC4

Neste trabalho foram desenvolvidos 4 ficheiros html com o objetivo de construir uma página sobre o meu hobby: o voleibol.

A página inicial (**home.html**) apresenta uma barra de navegação (*navigation bar*) com 7 ligações possíveis:
<ul>
<li><strong>Home</strong>: a página atual;</li>
<li><strong>Regras</strong>: uma página com as regras do voleibol;</li>
<li><strong>Posições</strong>: uma página dedicada às posições e papeis de cada um dos jogadores do voleibol;</li>
<li><strong>FCA</strong>: contém informação acerca do clube onde jogo atualmente, o Futebol Clube "Os Académicos";</li>
<li><strong>FPV</strong>: este link redireciona diretamente para a página oficial da Federação Portuguesa de Voleibol:</li>
<li><strong>FIVB</strong>: redireciona para a página da Federação Internacional de Voleibol;</li>
<li><strong>GitHub</strong>: redireciona para a página de GitHub da Unidade Curricular de Processamento de Linguagem Natural em Engenharia Biomédica.
</ul>

Os *icons* utilizados nesta página (nos links para a página inicial e para o github foram retirados da ferramenta e biblioteca **FontAwesome**). Para além disso, as letras da palavra "VOLEIBOL" são também *icons* retirados da mesma biblioteca.

O atributo **title** foi utilizado para que o utilizador saiba o que cada um destes links aborda. 
Foram ainda adicionador efeitos **hover** para tornar a experiência mais intuitiva.

![home](https://github.com/monicaccmartins/pln-2324/assets/91961697/3e104e93-1360-4570-9ec4-7bc4cab15a6d)


A página **regras.html**, para além da barra de navegação, tem as regras básicas do voleibol acompanhadas de alguns aspetos gráficos para uma melhor compreensão das mesmas.


https://github.com/monicaccmartins/pln-2324/assets/91961697/fb95cf3a-cbc4-4d72-9efe-b9e7ed3bbf26


Na página **posicoes.html** pode ver-se um campo de voleibol e os diferentes papéis ou funções que um jogador pode ter durante um jogo.
Ao passar o rato por cima das posições, pode verificar-se uma breve explicação sobre as mesmas (nome da posição e funções/características do jogador). Esta funcionalidade foi possível com a utilização do atributo **visibility: visible** e **visibility: hidden**, conforme o efeito *hover* se verifiva ou não, respetivamente.
Para esta página, foi utilizada a propriedade CSS **cursor** para que o cursor fosse uma bola de voleibol.
Para conseguir uma disposição adequada dos itens no campo de voleibol, foi contruída uma grelha (*grid*).


https://github.com/monicaccmartins/pln-2324/assets/91961697/8a54127b-fb8a-4c17-bd34-53e937c86ec2


Por fim, a página **fca.html** contém informação sobre o clube onde jogo e, para além disso, inclui duas funções simples em *JavaScript*, para fazer uma espécie de carrossel com imagens (para recuar e avançar imagens), com o auxílio do atributo *onclick*.



https://github.com/monicaccmartins/pln-2324/assets/91961697/dc62c36f-a3e5-4554-b481-73a8c40a7645


A maior dificuldade durante a realização deste trabalho, foi a disposição dos elementos na página html, nomeadamente na página que contém as **posições**, uma vez que o campo é uma imagem de fundo. Este problema tornou-se mais fácil de resolver através da construção da grelha. 
Para além disso, nessa página, foi difícil garantir a consistência da página entre ecrãs de tamanhos diferentes.
