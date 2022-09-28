# coding: utf-8
from flask import Flask
app = Flask("projeto")
@app.route("/")
def ola_mundo():
    return "Olá Mundo! Reformulação do Projeto, Hoje o clima está fresco", 200

app.run()