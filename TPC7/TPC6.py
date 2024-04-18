from flask import Flask, render_template, request
import json
import re


# GET /                      : home page
# GET / conceitos            : listar
# GET / conceitos / <id>     : consultar
# PUT / conceitos / <id>     : editar conceito
# POST / conceitos           : adicionar conceito
# DELETE / conceitos / <id>  : apagar conceitos

app = Flask(__name__)



file=open(r"conceitos_v2.json",'r', encoding='utf-8')
conceitos=json.load(file)


@app.route("/")                                                                 # home page

def home():
    return render_template("home.html")



@app.route("/conceitos")                                                        # listar conceitos      

def listarconceitos():
    query = request.args.get("query")
    match = {}

    if query:
        for conceito in conceitos:
            if query.lower() in conceito.lower():
                conceiton = re.sub(rf'({query})', r'<b>\1</b>', conceito)
                match[conceiton] = {"desc": conceitos[conceito], "original": conceito}
  

    if match:
        return render_template("conceitos.html", conceitos=match, pesquisa =query, res=len(match))
    else:
        return render_template("conceitos.html", conceitos=conceitos, pesquisa=False)
    
    


@app.route("/conceitos/<designacao>")                                          # listar conceito com designacao

def consultar_Conceitos(designacao):
    if designacao in conceitos:
        return render_template("significado.html", conceitos=conceitos, termo=designacao) 
    else:
        return render_template("erro.html", error="Conceito não existe na base de dados")



@app.route("/traducoes")   
    
def traducoes():
    return render_template("traducoes.html", conceitos=conceitos)     

    

@app.route("/adicionarconceito", methods=["POST", "GET"])
def adicionar_conceitos():
    if request.method == "POST":
        designacao = request.form.get("designacao")
        descricao = request.form.get("descricao")
        traducao = request.form.get("traducao")
        
        file_out = open("conceitos_v2.json", "w", encoding="UTF-8")
        conceitos[designacao] = {"desc": descricao, "en": traducao}
        json.dump(conceitos, file_out, indent=4, ensure_ascii=False)
        file_out.close()

        return render_template("conceitos.html", conceitos=conceitos)

    
    return render_template("adicionarconceito.html", conceitos=conceitos)


@app.route("/conceitos/<designacao>", methods=["DELETE"])
def delete_conceitos(designacao):
    file_out = open("conceitos_v2.json", "w", encoding="UTF-8")
    del conceitos[designacao]
    json.dump(conceitos, file_out, indent=4, ensure_ascii=False)
    file_out.close()
    return render_template("conceitos.html", conceitos=conceitos)


@app.route("/table")

def table():
    return render_template("table.html", conceitos=conceitos)

@app.route("/pesquisa")


def pesquisa():
    query = request.args.get("query_conceito_ou_desc")
    match = {}

    if query:
        for conceito in conceitos:
            if query.lower() in conceito.lower():
                conceiton = re.sub(rf'({query})', r'<b>\1</b>', conceito)
                if query.lower() in conceitos[conceito]["desc"].lower():
                    descricaon = re.sub(rf'({query})', r'<b>\1</b>', conceitos[conceito]["desc"].lower())
                    match[conceiton] = {"desc": descricaon, "original": conceito}
                else:
                    match[conceiton] = {"desc": conceitos[conceito]["desc"], "original": conceito}
            else:
                if query.lower() in conceitos[conceito]["desc"].lower():
                    descricaon = re.sub(rf'({query})', r'<b>\1</b>', conceitos[conceito]["desc"].lower())
                    match[conceito] = {"desc": descricaon, "original": conceito}

    if match:
        return render_template("pesquisa.html", conceitos=match, pesquisa=query, res=len(match))
    else:
        return render_template("pesquisa.html", conceitos=conceitos, pesquisa=False)
    
    
    
app.run(host="localhost", port=4002, debug=True)

