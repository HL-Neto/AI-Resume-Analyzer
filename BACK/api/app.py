
import os
import logging

from flask import Flask, jsonify
from gmail.modules_gmail import process_curriculum
from llm.agent import llm


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__,template_folder=os.path.join(BASE_DIR, "FRONT"))



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



