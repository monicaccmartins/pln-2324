# TPC3

No ficheiro TPC3.py, encontram-se as expressões regulares e substituições efetuadas no documento de texto "**dicionario_medico.txt**", com o objetivo de corrigir o máximo de erros encontrados na conversão de um ficheiro **.pdf** em **.txt**. Para além disso, foi desenvolvida uma página html (**DicionarioMedico.html**) com os termos e respetivas definições.

O objetivo principal desta ficha de exercícios foi a consolidação dos conhecimentos relacionados com Expressões Regulares e,com especial atenção aos fatores antagónicos da **cobertura** e **precisão**.

Foi fundamental analisar o documento de texto antes de começar o tratamento de erros, de modo a perceber quais os termos e situações que precisariam de mais atenção. Deste modo, durante o desenvolvimento deste trabalho foram tidos em atenção termos como: "cóclea", "cretinismo", "quimiotaxia", "rupo", "Sabin, vacina", "sulco", "vestíbulo", "zigopatia".

Primeiramente, começou por se perceber que, de uma forma geral, as definções estavam separadas do seu termo por **\n**. Para além disso, as definições de um termo separavam-se do termo seguinte por **\n\n**.

O tratamento de erros começou pela correção de quebras de página (**\f**), como é o caso dos termos "rupo" e "Sabin, vacina". Assim, optou-se por substituir a expressão regular **\n\n\f** por **\n~**. Dvee notar-se que o ~ foi utilizado para marcação dos termos, que será útil mais à frente.
Posto isto, apagaram-se as quebras de página (re.sub(r"\f", r"", texto)).

A expressão regular usada a seguir (re.sub(r"\.\n~", r".\n\n", texto)) serviu para corrigir os termos "rupo" e "Sabin, vacina" que, não estavam separados das definições anteriores por **\n\n**. Por outro lado, a expressão regular re.sub(r"\n~", r"\n", texto), corrigiu o termo vestíbulo, uma vez que se encontrava separado da sua definição por uma quebra de página.

A quinta *regex* utilizada, embora complexa, foi utilizada para corrigir o termo "sulco" que, apesar de não apresentar quebras de página, apresentava erros que podem ter surgido da conversão do ficheiro .pdf para .txt, já que a ordem da definição, sem esta regex, ficava trocada.

As duas expressões regulares realizadas a seguir foram também muito complexas. Porém, foram utilizadas com o objetivo de dar cobertura aos termos "quimiotaxia" e "cretinismo".

De seguida efetuou-se a marcação dos termos com "**@**".

Para o ficheiro html, foram dispostas duas colunas: "Termo" e "Definição". Os termos podem ser procurados fazendo *scroll* pela página ou então carregando numa das letras da barra lateral que faz com que a página vá diretamente para o primeiro termo que começa com essa letra. Para além disso o utilizador pode voltar ao início da página carregando na seta no final da barra lateral. Por fim, adicionou-se a possibilidade de, ao carregar num termo, redirecionar o utilizador para uma página de pesquisa do mesmo no google. 

De seguida encontra-se um vídeo rápido de demonstração do site:


https://github.com/monicaccmartins/pln-2324/assets/91961697/29bc5528-432a-4bb8-b9c8-b51f2edde43f


