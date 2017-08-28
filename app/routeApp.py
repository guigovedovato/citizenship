from app import app
from flask import render_template

# ---- Agenda ----
@app.route("/agenda")
def agendaView():
    return render_template('agenda/agenda.htm', currentAgenda = "current")

# ---- Board ----
@app.route("/")
def index():
    return render_template('cliente/board.htm', currentBoard = "current")

# ---- Cliente ----
@app.route("/cliente")
def clienteView():
    return render_template('cliente/cliente.htm', currentCliente = "current")

@app.route("/cliente/edit/<entity_id>")
def clienteEdit(entity_id):
    from core.bo.clienteBo import ClienteBo
    cliente = ClienteBo()
    entity = cliente.get_by_id(entity_id)
    return render_template('cliente/clienteform.htm', cliente = entity, currentCliente = "current")

# ---- Comune ----
@app.route("/comune")
def comuneView():
    return render_template('comune/comune.htm', currentComune = "current")

@app.route("/comune/novo")
def comuneNovo():
    return render_template('comune/comuneform.htm', comune = None, currentComune = "current")

@app.route("/comune/edit/<entity_id>")
def comuneEdit(entity_id):
    from core.bo.comuneBo import ComuneBo
    comune = ComuneBo()
    entity = comune.get_by_id(entity_id)
    return render_template('comune/comuneform.htm', comune = entity, currentComune = "current")

# ---- Prospecto ----
@app.route("/prospecto")
def prospectoView():
    return render_template('prospecto/prospecto.htm', currentProspecto = "current")

@app.route("/prospecto/novo")
def prospectoNovo():
    return render_template('prospecto/prospectoform.htm', prospecto = None, currentProspecto = "current")

@app.route("/prospecto/analise/<entity_id>")
def prospectoAnalise(entity_id):
    from core.bo.analiseBo import AnaliseBo
    analise = AnaliseBo()
    entity = analise.get_by_id(entity_id)
    return render_template('prospecto/analise.htm', analise = entity, currentProspecto = "current")

@app.route("/prospecto/edit/<entity_id>")
def prospectoEdit(entity_id):
    from core.bo.prospectoBo import ProspectoBo
    prospecto = ProspectoBo()
    entity = prospecto.get_by_id(entity_id)
    return render_template('prospecto/prospectoform.htm', prospecto = entity, currentProspecto = "current")

# ---- Residencia ----
@app.route("/residencia")
def residenciaView():
    return render_template('residencia/residencia.htm', currentResidencia = "current")

@app.route("/residencia/novo")
def residenciaNovo():
    return render_template('residencia/residenciaform.htm', residencia = None, currentResidencia = "current")

@app.route("/residencia/edit/<entity_id>")
def residenciaEdit(entity_id):
    from core.bo.residenciaBo import ResidenciaBo
    residencia = ResidenciaBo()
    entity = residencia.get_by_id(entity_id)
    return render_template('residencia/residenciaform.htm', residencia = entity, currentResidencia = "current")