# coding: utf-8
from flask import Flask, render_template
app = Flask("projeto")
@app.route("/")
def ola_mundo():
    nome="World Z"
    produtos= [
    {"nome": "Tablet Gráfico  - Básico", "preco": 399.90},
    {"nome": "PC Gamer - Simples", "preco": 999.99}]

    return render_template ("alo.html", n=nome, aProdutos=produtos), 200
    
app.run()