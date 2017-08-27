def fieldBlank(list):
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

def fromOnToBoolean(query):
    for key, value in query.items():
        if value == "on":
            query[key] = "True"

def itensFalse(entity, itens):
    for item in itens:
        if not entity.get(item):
            entity[item] = str(False)

def isNumber(var):
    try:
        int(var)
        return True
    except:
        return False

def toInt(query, fields):
    for field in fields:
        if(query.get(field)):
            query[field] = int(query[field])