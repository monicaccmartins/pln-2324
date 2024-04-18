# TPC7

O trabalho de casa do dia 15 de março consistia na implementação de DataTables para apresentar a informação do dicionário médico criado na aula anterior (TPC6). Para além disso, também foi pedido que fosse implementado um sistema de pesquisa (por conceitos e/ou definições), bem como permitir que alguns conceitos fossem eliminados da base de dados, ou adicionados.

No que diz respeito às DataTables, foi adicionada uma "página" para o efeito. A sua implementação foi relativamente simples, já que bastava mudar o conteúdo que aparecia nas linhas do template utilizado. O resultado desta página pode ser verificado a seguir:



Para implementar a pesquisa, foi melhorado o sistema de pesquisa desenvolvido no TPC6, que apenas permitia a procura por termos exatamente iguais à query submetida. Assim, a página "Conceitos", foi melhorada e, quando é efetuada uma pesquisa, são devolvidos todos os conceitos que contêm o termo pesquisado. Para esta implementação foi fundamental, colocar a negrito a parte do conceito que fazia "match" com a query. Para isso, foi utilizada a seguinte expressão regular: conceiton = re.sub(rf'({query})', r'<b>\1</b>', conceito). Depois, foi criado um dicionário com os resultados que deveriam ser devolvidos (match[conceiton] = {"desc": conceitos[conceito], "original": conceito}). A criação deste dicionário foi fundamental para garantir que o elemento bold era guardado e "recebido" pela página HTML. Para além disso, o guardar o conceito sem elemento bold com a chave "original" permitia garantir que o utilizador era redirecionado para a página correspondente ao conceito, após a pesquisa.
No seguinte vídeo pode verificar-se a utilização desta implementação:



De forma semelhante, implementou-se uma página chamada "Pesquisa" que permite, pesquisar quer por conceito, quer por definição:



No que toca à adição de um conceito à base de dados, adicionou-se um botão "+" junto aos títulos das páginas "Conceitos" e "Pesquisa". Por fim, para a eliminação do conceito, foi implementado um botão na página do mesmo, para que pudesse ser eliminado. 