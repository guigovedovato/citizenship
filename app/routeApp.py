from app import app
from flask import render_template, url_for
import os

# ---- Board ----
@app.route("/")
def index():
    return render_template('board.htm')

# ---- Cliente ----
@app.route("/cliente")
def clienteView():
    return render_template('cliente.htm')

@app.route("/cliente/edit/<entity_id>")
def clienteEdit(entity_id):
    from core.bo.clienteBo import ClienteBo
    cliente = ClienteBo()
    entity = cliente.get_by_id(entity_id)
    return render_template('clienteform.htm', cliente = entity)

# ---- Agenda ----
@app.route("/agenda")
def agendaView():
    return render_template('agenda.htm')

# ---- Prospecto ----
@app.route("/prospecto")
def prospectoView():
    return render_template('prospecto.htm')

@app.route("/prospecto/novo")
def prospectoNovo():
    return render_template('prospectoform.htm', prospecto = None)

@app.route("/prospecto/edit/<entity_id>")
def prospectoEdit(entity_id):
    from core.bo.prospectoBo import ProspectoBo
    prospecto = ProspectoBo()
    entity = prospecto.get_by_id(entity_id)
    return render_template('prospectoform.htm', prospecto = entity)

# ---- Comune ----
@app.route("/comune")
def comuneView():
    return render_template('comune.htm')

@app.route("/comune/novo")
def comuneNovo():
    return render_template('comuneform.htm', comune = None)

@app.route("/comune/edit/<entity_id>")
def comuneEdit(entity_id):
    from core.bo.comuneBo import ComuneBo
    comune = ComuneBo()
    entity = comune.get_by_id(entity_id)
    return render_template('comuneform.htm', comune = entity)

# ---- Residencia ----
@app.route("/residencia")
def residenciaView():
    return render_template('residencia.htm')

@app.route("/residencia/novo")
def residenciaNovo():
    return render_template('residenciaform.htm', residencia = None)

@app.route("/residencia/edit/<entity_id>")
def residenciaEdit(entity_id):
    from core.bo.residenciaBo import ResidenciaBo
    residencia = ResidenciaBo()
    entity = residencia.get_by_id(entity_id)
    return render_template('residenciaform.htm', residencia = entity)