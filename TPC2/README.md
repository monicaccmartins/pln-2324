# TPC2

No ficheiro TPC2.ipynb, encontram-se as resoluções para os exercícios propostos na aula de Processamento de Linguagem Natural em Engenharia Biomédica do dia 19 de fevereiro de 2024.

O objetivo principal desta ficha de exercícios foi a consolidação dos conhecimentos relacionados com Expressões Regulares, nomeadamente a utilização do módulo *re* e das suas funções *search*, *match*, *findall*, *sub* e *split*.

No que diz respeito ao **Exercício 1**, destaca-se a utilização do parâmetro "*flags=re.IGNORECASE*" nas alíneas 1.3 e 1.4 para que seja ignorado o facto de as letras estarem escritas em minúscula ou maiúscula.

Quanto ao **Exercício 2**, deve notar-se que foram considerados como "sinais válidos de pontuação" os seguintes: ".", "?", "!". Caso se queira considerar outros sinais de pontuação (por exemplo ";" ou ","), os mesmos devem ser adicionados à Expressão Regular (<strong>re.findall(r"por favor[.?!,;]$", frase, flags=re.IGNORECASE)</strong>). 
O uso do símbolo "**$**" nesta expressão regular foi fundamental para garantir que o sinal de pontuação se encontrava no final da frase.

Nos **Exercícios 3 e 4** foram utilizadas as funções *findall* e *sub*, respetivamente.

Para resolver o **Exercício 5** utilizou-se a função *split* para a criação de uma lista cujos elementos seriam os elementos da string recebida, separados por "**,**". De seguida, com um ciclo *for* foi possível calcular a soma desses elementos.

No **Exercício 6** foram criadas 3 possibilidades para o utilizador:
<ul>
<li>Encontrar os pronomes todos, quer eles estivessem escritos em maiúscula ou minúscula;</li>
<li>Encontrar os pronomes escritos em maiúscula;</li>
<li>Encontrar os pronomes escritos em minúscula.</li>
</ul>

Deste modo, teve-se em atenção a capitalização das letras.


No **Exercício 7 e 8** foram criadas expressões regulares mais complexas. No Exercício 7 foi fundamental a utilização dos símbolos "**^**" e "**$**" para definir os caracteres com que a frase iniciava e terminava, respetivamente. Já no Exercício 8, o símbolo "**?**" antes de "**[-]**" permite considerar os casos em que se trata de um número positivo ou negativo.

Por fim, quanto aos **Exercícios 9 e 10**, utilizaram-se as funções *sub* e *split*, respetivamente. Assume-se que, como referido no enunciado, no caso do Exercício 10, a lista fornecida é composta por **códigos postais válidos**. Se não fosse o caso, deveria ser feita uma verificação dos elementos da string (com uma REGEX, do tipo "[0-9]{4}-[0-9]{3}").


