# coding: utf-8
from flask import Flask
app = Flask("projeto")
@app.route("/")
def ola_mundo():
    return "Olá Mundo! Bem Vindo ao Teste no novo projeto!!", 200

app.run()