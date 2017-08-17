from app import app
from flask import send_from_directory
import os

root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")

@app.route("/")
def index():
    return send_from_directory(root, 'index.htm')

@app.route("/prospecto")
def prospectoView():
    return send_from_directory(root, 'prospecto.htm')

@app.route("/cliente")
def clienteView():
    return send_from_directory(root, 'cliente.htm')

@app.route("/comune")
def comuneView():
    return send_from_directory(root, 'comune.htm')

@app.route("/residencia")
def residenciaView():
    return send_from_directory(root, 'residencia.htm')

@app.route("/prospecto/novo")
def prospectoForm():
    return send_from_directory(root, 'prospectoform.htm')

@app.route("/comune/novo")
def comuneForm():
    return send_from_directory(root, 'comuneform.htm')

@app.route("/residencia/novo")
def residenciaForm():
    return send_from_directory(root, 'residenciaform.htm')