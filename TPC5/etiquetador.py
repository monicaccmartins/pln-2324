import json
import re
from deep_translator import GoogleTranslator

file_descricao = open("conceitos.json", encoding="UTF-8")
file_traducoes = open("termos_traduzidos.txt", encoding="UTF-8")
file_livro = open ("LIVRO-Doenças-do-Aparelho-Digestivo.txt", encoding="UTF-8")

texto = file_livro.read()
traducoes = file_traducoes.read()
descricoes = json.load(file_descricao)
traducoes = re.findall(r"(.+)\s@\s(.+)", traducoes)   # lista de tuplos do tipo (termo, traducao)
traducoes = dict(traducoes)                          # dicionario do tipo {termo: traducao}

descricao_traducao = {}                              # dicionario do tipo {termo: {en: traducao}, {desc: descricao}}

for termo in descricoes:
    if termo in traducoes:
        descricao_traducao[termo] = {"descricao": descricoes[termo], "en": traducoes[termo]}
    else:
        descricao_traducao[termo] = {"descricao": descricoes[termo], "en": "Tradução indisponível"}


blacklist=["de", "e", "para", "pelo", "os", "são", "este"]

conceitos_min = {chave.lower() : descricao_traducao[chave] for chave in descricao_traducao}

def etiquetador(matched):
    palavra = matched[0]
    original = palavra           
    palavra = palavra.lower()
    if palavra in conceitos_min and palavra not in blacklist:
        info = conceitos_min[palavra]                           # dicionario do tipo {"en": traducao, "descricao": descricao do termo}
        etiqueta= f"<a href='' title='En: {info["en"]} &#013;Significado: {info["descricao"]}'>{original}</a>"
        return etiqueta
    else:
        return original
    


# expressao = "\b" + re.escape(designacao) + "\b"  # escape protege expressoes regulares e caracteres especiais
expressao = r'[\wáéçãóõíúâêÁÉÇÃÓÕÍÚÂÊ]+'
texto = re.sub(expressao, etiquetador, texto, flags=re.IGNORECASE)
#tirar /n antes das substituiçoes? ver title vida que tem <br>
texto = re.sub(r"\n", r"<br>", texto)
texto = re.sub(r"\f", r"<hr/>", texto)
    

file_out = open("livro.html", "w", encoding="UTF-8")
    
print(texto, file=file_out)
