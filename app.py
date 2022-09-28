# coding: utf-8
from flask import Flask, render_template
app = Flask("projeto")
@app.route("/")
def ola_mundo():
    nome="World Z"
    return render_template ("alo.html", n=nome), 200
    
app.run()