import os
from datetime import timedelta

def field_blank(list):
    return {k:v for k, v in list.items() if v != ""}

def like(query, parameter):
    if query.get(parameter):
        query[parameter] = {"$regex": query[parameter]}

def gte(query, parameter):
    if query.get(parameter):
        query[parameter] = {"$gte": int(query[parameter])}

def dates(query):
    if query.get("data_inicial"):
        query["data_cadastro"] = {'$gte': query["data_inicial"]}
        query.pop("data_inicial")
    if query.get("data_final"):
        if not query.get("data_cadastro"):
            query["data_cadastro"] = {'$lte': query["data_final"]}
        else:
            query["data_cadastro"].update({'$lte': query["data_final"]})
        query.pop("data_final")

def from_on_to_boolean(query):
    for key, value in query.items():
        if value == "on":
            query[key] = "True"

def itens_false(entity, itens):
    for item in itens:
        if not entity.get(item):
            entity[item] = str(False)

def is_number(var):
    try:
        int(var)
        return True
    except:
        return False

def to_int(query, fields):
    for field in fields:
        if(query.get(field)):
            query[field] = int(query[field])

def get_separated_by_comma(lista_origem):
    destino = ""
    for origem in lista_origem:
        destino += ", " + origem
    return destino[2:]

def get_data(date):
    from datetime import datetime
    new_date = convert_date(date)
    return datetime.strftime(new_date, "%d/%m/%Y")

def convert_date(str_date):
    from datetime import datetime
    return datetime.strptime(str_date, '%Y-%m-%d')

def date_convert(date):
    from datetime import datetime
    return datetime.strftime(date, "%d/%m/%Y")

def create_directory(directory, folder):
    path = os.path.join(directory, folder)
    if not os.path.exists(path):
        os.makedirs(path)
    return path

def get_age(birth, date):
    born = convert_date(birth)
    today = convert_date(date)
    extra_year = 1 if ((today.month, today.day) < (born.month, born.day)) else 0
    return today.year - born.year - extra_year
