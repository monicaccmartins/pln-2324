import re
from unidecode import unidecode

f = open("dicionario_medico.txt", "r", encoding="utf-8")
texto = f.read()

texto = re.sub(r"\n\n\f", r"\n~", texto)  # correçao de quebras de página, marca-se com ~ por causa de termo como "rupo"
texto = re.sub(r"\f", r"", texto)
texto = re.sub(r"\.\n~", r".\n\n", texto)  # caso específico do termo rupo
texto = re.sub(r"\n~", r"\n", texto)  # casos como o termo vestibulo\n\n\f
texto = re.sub(r"\n\n(.{,66})\n(.{,66})\n(.{,66})\n\n(.{,66})", r"\n\n\1\n\2 \4 \3", texto)  # sulco                   
print(texto)
texto = re.sub(r"(.{100,})\n\n(.{50,})\n(.*\.)\n\n", r"\1 \2 \3\n\n", texto) #quimiotaxia

texto = re.sub(r"(.{100,})\n\n(.{50,}\.)\n\n", r"\1 \2\n\n", texto) # cretinismo 
texto = re.sub(r"\n\n(.+)", r"\n\n@\1", texto)
texto = re.sub(r"@(.+)\n\n@", r"@\1\n", texto)
texto = re.sub(r"\n\n@(.+)\.", r"\1.\n\n@", texto) #distimia
print(len(texto))

# designacoes=[]
# designacoes=re.findall(r"@(.+)\n", texto)

definicoes = []  # lista de tuplos (designacao, definicao)
definicoes = re.findall(r"@(.+)\n([^@]+)", texto)

#for termo in definicoes:
#    term, defi = termo
#    if len(term.split(" ")) > 1 and "," in term:
#        print(term)


titulo = "<h3 id=\"top\"><img src=\"https://icones.pro/wp-content/uploads/2021/06/symbole-sante-orange.png\" style=\"width:50px;padding-right:4px;\"> Dicionário Médico </h3>"
descricao = ("<p>Este é  um dicionário médico desenvolvido na Unidade Curricular de Processamento de Linguagem Natural</p>")



barra="<div class='barra'>"          
barra += "<ul>"



body = "<body>"
body += "<div class='conteudo'>"
body += "<div class='definicoes'>"
body += "<table>"
body += "<tr><th>Termo<img src=\"https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Magnifying_glass_icon.svg/1200px-Magnifying_glass_icon.svg.png\" style=\"width:20px;padding-left:8px;\"></th><th>Definição</th></tr>"

primeiro_termo = definicoes[0];
atual=unidecode(primeiro_termo[0][0].upper())    #guarda a primeira letra do termo que estamos a analisar
barra += f"<li><a href='#{primeiro_termo[0]}'>{unidecode(primeiro_termo[0][0].upper())}</a></li>"

for termo in definicoes:
    body += "\n<tr>"
    body += (f"<td><a id={termo[0]} href='https://www.google.com/search?q={termo[0]}'>{termo[0]}</a></td>")
    body += f"<td>{termo[1]}</td>"
    body += "</tr>\n"
    if atual!=unidecode(termo[0][0].upper()):
        atual=unidecode(termo[0][0].upper())
        barra += f"<li><a href='#{termo[0]}'>{unidecode(termo[0][0].upper())}</a></li>"

barra += "<li><a href='#top'><img src=\"https://static.thenounproject.com/png/1037792-200.png\" style=\"width:28px;padding-left:8px;\"></a></li>"            
body += "</table>"
body += "</div>"
barra += "</ul>"
barra += "</div>"
body+=barra
body += "<div>"
body += "</body>"


CSS="""
<style>


p{
  padding-left: 10px;
  font-size: 25px;
  margin-top:15px;
}

h3{
  padding-left: 10px;
  padding-top: 10px;
  font-size: 40px;
  margin-top: 10px;
  margin-bottom: 0px;
  color:#ff7404;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI Adjusted", "Segoe UI", "Liberation Sans", sans-serif
  font-weight: 150px;
}

a:hover{
  color:#E4923D;
}

body {
  background-color: #f0f0f2;
  font-family: Roboto, sans-serif;
  font-size: 20px;
}


.conteudo {
  display: flex;
}

a {
  color: black;
}


table {
  border-collapse: separate;
  border-spacing: 2em;
  width:95%;
}

td {
  font-size: 20px;
}

ul {
  list-style-type: none;
}

tr:hover th{
  color: black;
}

th {
  padding: 12px;
  position: sticky;
  top: 0;
  font-size: 25px;
  border-bottom: 1pt solid black;
  background-color: #f0f0f2;
}

.barra {
  position: fixed;
  right: 25px;
  text-align: center;
  top:2%;
}


td:hover a {
    color:#E4923D;
}


li {
  margin-botoom:50px;
}

</style>"""


html = CSS+ titulo + descricao + body 


file_out = open("DicionarioMedico.html", "w")
file_out.write(html)
file_out.close()
