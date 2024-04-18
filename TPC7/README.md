# TPC7

O trabalho de casa do dia 15 de março consistia na implementação de DataTables para apresentar a informação do dicionário médico criado na aula anterior (TPC6). Para além disso, também foi pedido que fosse implementado um sistema de pesquisa (por conceitos e/ou definições), bem como permitir que alguns conceitos fossem eliminados da base de dados, ou adicionados.

No que diz respeito às DataTables, foi adicionada uma "página" para o efeito. A sua implementação foi relativamente simples, já que bastava mudar o conteúdo que aparecia nas linhas do template utilizado. O resultado desta página pode ser verificado a seguir:

https://github.com/monicaccmartins/pln-2324/assets/91961697/2768eefc-20ac-4790-bdea-461a53817116

Para implementar a pesquisa, foi melhorado o sistema de pesquisa desenvolvido no TPC6, que apenas permitia a procura por termos exatamente iguais à query submetida. Assim, a página "Conceitos", foi melhorada e, quando é efetuada uma pesquisa, são devolvidos todos os conceitos que contêm o termo pesquisado. Para esta implementação foi fundamental, colocar a negrito a parte do conceito que fazia "match" com a query. Para isso, foi utilizada a seguinte expressão regular: 

conceiton = re.sub(rf'({query})', r'\<b\>\1\</b\>', conceito). 

Depois, foi criado um dicionário com os resultados que deveriam ser devolvidos:

match[conceiton] = {"desc": conceitos[conceito], "original": conceito}. 

A criação deste dicionário foi fundamental para garantir que o elemento bold era guardado e "recebido" pela página HTML. Para além disso, o guardar o conceito sem elemento bold com a chave "original" permitia garantir que o utilizador era redirecionado para a página correspondente ao conceito, após a pesquisa.

De forma semelhante, implementou-se uma página chamada "Pesquisa" que permite pesquisar, quer por conceito, quer por definição.

No que toca à adição de um conceito à base de dados, adicionou-se um botão "+" junto aos títulos das páginas "Conceitos" e "Pesquisa". Por fim, para a eliminação do conceito, foi implementado um botão na página do mesmo, para que pudesse ser eliminado. 

De seguida pode observar-se o funcionamento do sistema de pesquisa por conceito e a adição de um conceito à base de dados:

https://github.com/monicaccmartins/pln-2324/assets/91961697/5a7870b2-b4c9-48f7-98b6-c8d564a4156b


Observe-se, agora, o funcionamento do sistema de pesquisa por conceito e/ou definição e a eliminação do conceito "ola_":



https://github.com/monicaccmartins/pln-2324/assets/91961697/a3a2d75b-7292-436a-befd-96549d3b30de


Um dos obstáculos encontrados durante o desenvolvimento deste trabalho foi o facto de a página HTML não reconhecer os elementos "bold" utilizados para identificar o match da query pesquisada. Para combater isto, foi utilizado o modo "safe" na página HTML, para garantir que o elemento bold recebido era interpretado como uma definição de HTML, e não como texto. (https://jinja.palletsprojects.com/en/3.0.x/templates/). 

