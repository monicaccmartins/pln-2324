from flask import Flask, render_template, request
import json


# GET /                      : home page
# GET / conceitos            : listar
# GET / conceitos / <id>     : consultar
# PUT / conceitos / <id>     : editar conceito
# POST / conceitos           : adicionar conceito
# DELETE / conceitos / <id>  : apagar conceitos

app = Flask(__name__)


import json

file=open(r"conceitos.json",'r', encoding='utf-8')
conceitos=json.load(file)

file_trad=open(r"termos_traduzidos.txt",'r', encoding='utf-8')
#traducoes=file_trad.read()


res={}
trad_dict={}
for line in file_trad:
    pt,en=line.split("@")
    pt=pt.strip()
    en=en.strip()
    trad_dict[pt]=en

for conceito in conceitos:
    if conceito in trad_dict:
        tmp={"desc": conceitos[conceito],
            "en":trad_dict[conceito]}
        res[conceito] = tmp

    else:
        tmp={"desc":conceitos[conceito],
             "en":"sem traducao"
             }
        res[conceito]=tmp

file_out= open(r"conceitoss.json","w",encoding='utf-8')
json.dump(res,file_out,ensure_ascii=False,indent=4)



@app.route("/")                                                                 # home page

def home():
    return render_template("home.html")



@app.route("/conceitos")                                                        # listar conceitos      

def listarconceitos():
    query = request.args.get("query") 

    if query:
        if query in res.keys():
            return render_template("significado.html", conceitos=res, termo=query)
        else:
            return render_template("conceitos.html", conceitos=res)

    return render_template("conceitos.html", conceitos=res)              # variavel do jinja = variavel python



@app.route("/conceitos/<designacao>")                                          # listar conceito com designacao

def consultar_Conceitos(designacao):
    return render_template("significado.html", conceitos=res, termo=designacao) 



@app.route("/traducoes")   
    
def traducoes():
    return render_template("traducoes.html", conceitos=res)     
    


app.run(host="localhost", port=4002, debug=True)