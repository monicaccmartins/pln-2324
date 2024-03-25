# TPC5

O trabalho do dia 18 de março consistia na conclusão do dicionário médico que começou a ser desenvolvido na aula com recurso ao Flask e ao Bootstrap.

Esta pasta é composta por:
<ul>
<li>Diretoria de templates html utilizados;</li>
<li>Ficheiros json com informação relativa aos conceitos médicos;</li>
<li>Ficheiro txt com a tradução de alguns termos médicos;</li>
<li>TPC6.py que contém o código desenvolvido para o desenvolvimento da aplicação com recurso ao Flask e Bootstrap.</li>
</ul>

Para visualizar uma página de entrada mais agradável visualmente, foi adicionada uma imagem ao ficheiro "home.html":



Para além disso, na página dos conceitos permitiu-se a pesquisa por termos. Assim, se o termo pesquisado existir no dicionário médico o utilizador é redirecionado para a página desse conceito, sendo possível verificar a sua descrição e a tradução do mesmo para alguns idiomas. Caso o termo não exista no dicionário médico, a página mantêm-se nos conceitos.
Esta barra de pesquisa foi desenvolvida com recurso ao método "GET".



No que diz respeito às traduções, foi utilizado o efeito "collapse" do Bootstrap para que, quando se carregasse no botão "English" fosse disponibilizada a tradução do termo. Para além disso, os botões relativos aos idiomas italiano e francês, abrem uma nova janela no google tradutor para que seja realizada a tradução do termo.



A página das traduções contêm uma tabela cujas colunas dizem respeito aos termos e respetivas traduções (para inglês). Se o utilizador pretender, pode carregar no termo e será direcionado para a página do mesmo.



As principais dificuldades deste TPC estiveram relacionadas com a implementação do método de pesquisa, já que o mesmo exigia uma coordenação entre o template html e o ficheiro python desenvolvido.