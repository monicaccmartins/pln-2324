import re
from unidecode import unidecode
import json


    
f = open("MC.xml", "r", encoding="utf-8")
texto = f.read()


texto = re.sub(r"<.+font=\"13\"><b>(.+)</b.+", r"@PI\1\n", texto)  # Identificação dos termos em portugues que serão traduzidos para ingles
texto = re.sub(r"<.+font=\"[67]\"><b>(.+)</b.+", r"@IP\1\n", texto)  # Identificação dos termos em ingles que serao traduzidos para portugues
texto = re.sub(r".+font=\"8\">(.+)<.+", r"@DEF\1\n", texto)  # Identificação das traduções

texto = re.sub(r"<.+>", "", texto)

marcas = ["DEF", "IP", "PI"]

for marca in marcas:                                       # este ciclo for serve para "combater" a greediness
    pattern = rf"@{marca}(.+?)[\n]+?@{marca}(.+?)"
        
    while (re.search(pattern, texto) != None): 
        texto = re.sub(pattern, rf"@{marca}\1\2", texto)    # regex para apanhar termos e definições com mais do que uma linha



texto = re.sub(r"@(.+)\s+–\s+[\n]+", r"@\1\n", texto)  # remoçao do - após significado


file_out = open("MC_out.xml", "w", encoding="utf-8")
file_out.write(texto)
file_out.close()


traducoesIP = re.findall(r'@IP(.+)[\n]+@DEF(.+)', texto)
traducoesPI = re.findall(r'@PI(.+)[\n]+@DEF(.+)', texto)

traducoesIP_dict = {traducao[0] : traducao[1] for traducao in traducoesIP}
traducoesPI_dict = {traducao[0] : traducao[1] for traducao in traducoesPI}

traducoes = {"IP": traducoesIP_dict, "PI": traducoesPI_dict}


print(len(traducoes["IP"]))
print(len(traducoes["PI"]))
file_out = open("traducoes.json", "w", encoding="UTF-8")
json.dump(traducoes, file_out, indent=4, ensure_ascii=False)
file_out.close()