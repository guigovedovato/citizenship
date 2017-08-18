from app import app
from flask import render_template, url_for
import os

@app.route("/")
def index():
    return render_template('board.htm')

@app.route("/cliente")
def clienteView():
    return render_template('cliente.htm')

@app.route("/agenda")
def agendaView():
    return render_template('agenda.htm')

@app.route("/prospecto")
def prospectoView():
    return render_template('prospecto.htm')

@app.route("/comune")
def comuneView():
    return render_template('comune.htm')

@app.route("/residencia")
def residenciaView():
    return render_template('residencia.htm')

@app.route("/prospecto/novo")
def prospectoForm():
    return render_template('prospectoform.htm')

@app.route("/comune/novo")
def comuneForm():
    return render_template('comuneform.htm')

@app.route("/residencia/novo")
def residenciaForm():
    return render_template('residenciaform.htm')