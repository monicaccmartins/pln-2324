# TPC5

O trabalho do dia 11 de março consistia na conclusão de um etiquetador que começou a ser desenvolvido na aula. Após a conclusão do etiquetador, deve ser construída uma página html com o conteúdo do ficheiro "<strong>LIVRO-Doenças-do-Aparelho-Digestivo.txt</strong>", com etiquetação de alguns termos médicos.

Para além do etiquetador, foi também desenvolvido um tradutor (ficheiro <strong>tradutor.py</strong>). Neste ficheiro pode ser encontrado:
<ul>
<li>Abertura do ficheiro <strong>conceitos.json</strong>: este ficheiro <i>json</i> contém vários termos médicos e a respetiva descrição (uma espécie de dicionário médico);</li>
<li>Tradução dos termos: com recurso à bilioteca <i>deep_translator</i>;</li>
<li>Construção de uma estrutura de dados json (<strong>conceitos_v2.json</strong>): esta estrutura de dados consiste em várias chaves (termos) cujo valor corresponde é um dicionário com as chaves "desc" e "en" (que correspondem, respetivamente, à descrição e tradução do termo);</li>
</ul>

Por se tratar de um programa extenso e demorado, foi fornecido o ficheiro <strong>termos_traduzidos.txt</strong> que consiste num ficheiro com vários termos médicos e respetiva tradução da seguinte forma: termo em português @ tradução. 

![image](https://github.com/monicaccmartins/pln-2324/assets/91961697/9bdf731c-c1ed-4d13-a96c-9550a8b0ae00)

Posto isto, o ficheiro <strong>etiquetador.py</strong> é responsável por:
<ul>
<li>Abrir e ler o ficheiro <strong>LIVRO-Doenças-do-Aparelho-Digestivo.txt</strong>;</li>
<li>Abrir e carregar o dicionário médico disponível em <strong>conceitos.json</strong>;</li>
<li>Abrir e ler o ficheiro <strong>termos_traduzidos.txt</strong>. Nesta fase é importante utilizar uma expressão regular para criar uma lista de tuplos do tipo [(termo, tradução)] e de seguida, transformar essa lista num dicionário do tipo {"termo": tradução};</li>

![image](https://github.com/monicaccmartins/pln-2324/assets/91961697/74d9539a-8b79-4968-827f-12acabdce636)

<li>Percorrer todos os termos do dicionário que contém as descrições e, caso o termo esteja presente no dicionário que contém as traduções, adiciona a uma estrutura de dados do tipo: {termo: {"en": tradução do termo, "descricao": descricao do termo}}, ou seja, um dicionário de dicionários. Caso o termo não tenha tradução, o valor da chave "en" é definido como "Tradução indisponível";</li>

![image](https://github.com/monicaccmartins/pln-2324/assets/91961697/87ee789d-8921-44a4-bf6f-1539ee2902c9)

<li>Construção de um ficheiro html (<strong>livro.html</strong>) com o conteúdo do livro acima referido e "etiquetação" dos termos com descrição no dicionário médico, com recurso ao parâmetro "title" do html.</li>
</ul>

O resultado da página html desenvolvida foi o seguinte:
