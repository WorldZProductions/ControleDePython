# coding: utf-8
from flask import Flask
app = Flask("projeto")
@app.route("/")
def ola_mundo():
    return "Olá Mundo! Projeto Teste 3!!", 200

app.run()