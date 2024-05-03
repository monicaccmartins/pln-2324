# TPC8

O trabalho de casa do dia 29 de abril consistia na utilização da biblioteca "Word2Vec" para construir modelos capazes de prever se uma determinada palavra pertence a um determinado contexto. Para tal, foram fornecidos dois documentos em formato TXT com dois livros do Harry Potter: "A Câmara dos Segredos" e "A Pedra Filosofal". 

Assim, para a construção dos diferentes modelos, foram definidas 3 abordagens diferentes:
<ul>
<li>Inclusão apenas dos tokens do livro "A Câmara dos Segredos";</li>
<li>Inclusão apenas dos tokens do livro "A Pedra Filosofal";</li>
<li>Inclusão dos tokens de ambos os livros.</li>
</ul>

Para possibilitar a comparação da qualidade dos modelos, foram usados os seguintes critérios:
<ul>
<li>Most similar to “harry”: Para avaliar a capacidade do modelo de perceber quais os termos frequentemente associados à personagem principal</li>
<li>Does not match between "harry", "rony", "coruja": Para avaliar a capacidade que o modelo tem de distinguir pessoas de animais;</li>
<li>Does not match between "minerva", "dumbledore", "quirrell": Para avaliar a capacidade de o modelo entender a hierarquia dos diferentes professores;</li>
<li>Does not match between "edwiges", "rony", "coruja": Para avaliar a capacidade de o modelo compreender a que categoria os nomes pertencem (por exemplo: se pertence a um animal ou a uma pessoa);</li>
<li>Does not match between "edwiges", "hagrid", "dumbledore": Para avaliar, com outros nomes, a capacidade que o modelo tem de distinguir pessoas de animais;</li>
<li>Does not match between "harry", "dumbledore", "voldemort": Para avaliar a capacidade que o modelo tem de distinguir personalidades (bons, maus).</li>
</ul>


Na tabela seguinte apresentam-se os parâmetros dos diferentes modelos testados, bem como o resultado obtidopara cada um dos critérios:



Verifica-se que o modelo que apresentou uma performance mais "perto" do esperado foi o modelo que incluía apenas o livro "Harry Potter e a Câmara dos Segredos", com os parâmetros 100, 5, 1, 1, 20, 3 (para os valores de vector_size, window, SG, Min_count, epochs, workers, respetivamente).

Este modelo, apenas não "percebeu" corretamente a diferença entre o nome da "edwiges" (coruja), "hagrid" (pessoa) e "dumbledore" (pessoa).


Também foi utilizada a funcionalidade "similarity" para observar a similaridade entre os termos "harry" e "voldemort", que deu 99% de similaridade.


Com este trabalho foi possível testar as diferentes funcionalidades dos modelos da biblioteca "Word2Vec" e entender a importância da definição dos diferentes parâmetros.