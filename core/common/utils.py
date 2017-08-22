def intersection(list):
    return {k:v for k, v in list.items() if v != ""}

def like(query, parameter):
    query[parameter] = {"$regex": query[parameter]}
    return query

def dates(query):
    pass