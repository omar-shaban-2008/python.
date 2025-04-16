import pandas as pd
from flask import Flask, render_template, request



def trova_valore(utente_selezionato,valore):
    df = pd.read_csv("profilo.csv").to_dict(orient='records')
    valori = df[utente_selezionato].values()
    lista = list(valori)
    return lista[valore]

def trova_chiave(valore):
    df = pd.read_csv("profilo.csv").to_dict(orient='records')
    lista = list(df[0].keys())
    return lista[valore]

app = Flask(__name__)

@app.route('/')
def Index():
    return render_template("index.html", 
                           nome = trova_valore(0,0), 
                           cognome = trova_valore(0,1), 
                           scuola = trova_valore(0,2), 
                           hobby = trova_valore(0,3), 
                           chiave3 = trova_chiave(2), 
                           chiave4 = trova_chiave(3))



@app.route("/modifica", methods=["GET", "POST"])
def modifica():
    if request.method == "POST":
        nuovo_profilo = {
        trova_chiave(0) : request.form["nome"],
        trova_chiave(1) : request.form["cognome"],
        trova_chiave(2) : request.form["scuola"],
        trova_chiave(3) : request.form["hobby"]
        }
        df = pd.DataFrame([nuovo_profilo])
        df.to_csv("profilo.csv", index=False)

    return render_template("modifica.html",
                            chiave1 = trova_chiave(0), 
                            chiave2 = trova_chiave(1),
                            chiave3 = trova_chiave(2), 
                            chiave4 = trova_chiave(3)
                            )


if __name__ == '__main__':
    app.run(debug=True)