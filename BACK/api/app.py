
import os

from flask import Flask, jsonify , render_template
from BACK.gmail.modules_gmail import process_curriculum
from BACK.llm.agent import llm

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)
FRONT_DIR = os.path.join(BASE_DIR, "FRONT")


app = Flask( __name__,template_folder=FRONT_DIR,static_folder=FRONT_DIR,static_url_path="/static")

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/push", methods=["POST"])
def processes_email_curriculum():
    
    
    resultado = process_curriculum()

    return jsonify({
        "success": True,
        "message": "Processamento dos currículos concluído",
        "resultado": resultado
    }), 200



@app.route("/analise", methods=["POST"])
def analise_curriculo():
 

    resultado = llm()

   
        
    return jsonify({
        "success": True,
        "message": "Análise concluída",
        "resultado": resultado
    }), 200



