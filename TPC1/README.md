# TPC1

No ficheiro TPC1.py, encontram-se as resoluções para os exercícios propostos na aula de Processamento de Linguagem Natural em Engenharia Biomédica do dia 12 de fevereiro de 2024.

Como desafio principal, foi proposto o **exercício 10** em que, dado o ficheiro de texto "CIH Bilingual Medical Glossary English-Spanish.txt" deveriam ser encontradas e juntas palavras que seriam anagramas (por exemplo, "silent" e "listen"). A resolução proposta para este exercício é composta pelos seguintes passos:

<ol>
<li>
Primeiramente, foi necessário especificar o <em>encoding</em> em que o texto deveria ser lido. Para isso, definiu-se o parâmetro encoding="utf8" na função <em>open</em>. 
</li>
<li>
De seguida, definiu-se uma lista com todos os caracteres que não representavam letras (números, pontuação, entre outros), que foram substituídos por espaços. 
</li>
<li>
Foi ainda importante garantir que todas as letras estavam escritas com letra minúscula para que os anagramas fossem encontrados corretamente. Para além disso, removeram-se as palavras compostas por apenas uma letra, já que não faz sentido analisar anagramas para esses casos.
</li>
<li>
Com recurso aos <em>sets</em>, foi possível eliminar palavras repetidas que seriam desnecessárias para a análise do texto.
</li>
<li>
Por fim, foi criado um dicionário, **anagramas**, em que a chave corresponde à ordenação alfabética das letras existentes nas palavras e o valor corresponde a uma lista de palavras que foram encontradas com essas letras e que, por isso, são anagramas.
</li>
</ol>

O dicionário construído permitiu verificar que existiam vários anagramas no documento fornecido, como por exemplo:

<ul>
<li>
aegnr : ['range', 'negra', 'anger']
</li>
<li>
aaelnprt : ['paternal', 'prenatal']
</li>
<li>
below : ['below', 'bowel', 'elbow']
</li>
<li>
enost : ['onset', 'tenso', 'stone']
</li>
</ul>

As principais dificuldades deste trabalho foram garantir que se excluíam todos os caracteres que não eram letras. Foi possível garanti-lo imprimindo, após a construção do dicionário **anagramas**, a lista de chaves ordenada (print(sorted(anagramas.keys()))). Observando as primeiras palavras era possível verificar a existência de caracteres especiais, uma vez que os caracteres especiais são prioritários na ordenação (como por exemplo: "?bceeipr" (percibe) e "?eeinst" (siente, tienes) antes da remoção do caracter "?").

Foi possível observar que existiam, no total, 231 anagramas (consideram-se anagramas quando existe mais do que uma palavra para a mesma chave).