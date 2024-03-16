import json
from deep_translator import GoogleTranslator


file = open("conceitos.json", encoding="UTF-8")
conceitos = json.load(file)

novo_dict = {}


for designacao_pt in conceitos:
    print(designacao_pt)
    try:
        designacao_en = GoogleTranslator(source='pt', target='en').translate(designacao_pt)
        novo_dict[designacao_pt] = {"desc": conceitos[designacao_pt], "en": designacao_en}
    except TranslationNotFound as e:
        novo_dict[designacao_pt] = {"desc": conceitos[designacao_pt], "en": "Tradução indisponível"}
    except RequestError as e:
        novo_dict[designacao_pt] = {"desc": conceitos[designacao_pt], "en": "Tradução indisponível"}


file_out = open("conceitos_v2.json", "w", encoding="UTF-8")
json.dump(novo_dict, file_out, indent=4, ensure_ascii=False)

print(novo_dict)