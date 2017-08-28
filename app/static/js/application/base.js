$(document).ready(function() {
    session();
    if (verifySession())
        setTimeout(research, 100);
    $("table").hide();
    if (document.getElementById("data_final")) {
        today = getToday();
        document.getElementById("data_final").setAttribute("max", today);
        document.getElementById("data_inicial").setAttribute("max", today);
    }
    if (document.getElementById("comune_select"))
        getComunes();
});

function session() {
    if (sessionStorage.actual) {
        sessionStorage.last = sessionStorage.actual;
        sessionStorage.actual = window.location.pathname;
    } else {
        sessionStorage.search = false;
        sessionStorage.actual = window.location.pathname;
    }
}

function canSearch() {
    return (String(sessionStorage.last).includes("novo") || String(sessionStorage.last).includes("edit")) &&
        (!String(sessionStorage.actual).includes("novo") || !String(sessionStorage.actual).includes("edit"))
}

function verifySession() {
    if (canSearch()) {
        if (sessionStorage.search == "true") {
            return true;
        } else {
            return false;
        }
    } else {
        if (sessionStorage.last == sessionStorage.actual)
            sessionStorage.search = false;
        return false;
    }
}

function research() {
    $("#btnSubmit").click();
}

$("#data_inicial").change(function() {
    document.getElementById("data_final").setAttribute("min", this.value);
});

function getToday() {
    var today = new Date();
    var dd = today.getDate();
    var mm = today.getMonth() + 1; //January is 0!
    var yyyy = today.getFullYear();
    if (dd < 10) {
        dd = '0' + dd
    }
    if (mm < 10) {
        mm = '0' + mm
    }
    today = yyyy + '-' + mm + '-' + dd;
    return today;
}

function serializeToJson(serializer) {
    var _string = '{';
    for (var ix in serializer) {
        var row = serializer[ix];
        _string += '"' + row.name + '":"' + row.value + '",';
    }
    var end = _string.length - 1;
    _string = _string.substr(0, end);
    _string += '}';
    return JSON.stringify(JSON.parse(_string));
}

function setMessage(msg) {
    $("#message").html("<span>" + msg + "</span>");
    $("#message").append('<div class="buttons"><input type="button" value="OK" onclick="$(\'#messager\').hide();"></div>');
    $("#messager").show();
}

function getButtons(urlEdit, urlAction, id, convert) {
    btnc = "";
    if (convert != "") {
        btnc = '<img class="image-button btnConvert" src="static/images/convert.png" alt="Converter para Cliente"' +
            ' url=\'' + urlAction + '{"convert":"' + id + '"}' + '\' onclick="btnConvert(this)">';
    }
    btn = '<td>';
    btn += btnc;
    btn += '<img class="image-button btnEdit" src="static/images/edit.png" alt="Editar" _id="' +
        id + '" url="' + urlEdit + '" onclick="btnEdit(this)">' +
        '<img class="image-button btnInactivate" src="static/images/exclude.png" alt="Inativar" _id="' +
        id + '" url="' + urlAction + '" onclick="btnInactivate(this)">' +
        '</td>';
    return btn;
}

function btnEdit(btn) {
    location.href = $(btn).attr("url") + $(btn).attr("_id");
}

function btnInactivate(btn) {
    $("#load").show();
    $.ajax({
        url: $(btn).attr("url") + $(btn).attr("_id"),
        type: 'PUT',
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify({ "ativo": "False" }),
        dataType: "json",
        success: function(response) {
            $("#load").hide();
            setMessage("Registro inativado com sucesso.");
            $("#btnSubmit").click();
        }
    });
}

function btnConvert(btn) {
    $("#load").show();
    $.getJSON($(btn).attr("url"))
        .done(function(data) {
            $("#load").hide();
            setMessage(data);
            $("#btnSubmit").click();
        })
        .fail(function(data) {
            $("#load").hide();
            setMessage("Houve um erro ao realizar esta operação.");
        });
}

function search(urlGET, urlEdit, fields, dataSerialized, convert = "") {
    sessionStorage.search = true;
    $("#load").show();
    tbody = $("tbody");
    tbody.empty();
    $.getJSON(urlGET + dataSerialized)
        .done(function(data) {
            if (data && data != "") {
                createTBody(data, tbody, urlGET, urlEdit, fields, dataSerialized, convert);
            } else {
                var tr = $('<tr>');
                tr.append('<td colspan="5" class="empty">Não foram encontrados registros para essa consulta.</td>');
                tbody.append(tr);
            }
            $("#load").hide();
            $("table").show();
        })
        .fail(function(data) {
            $("#load").hide();
            setMessage("Houve um erro ao fazer a consulta.");
        });
}

function createTBody(data, tbody, urlGET, urlEdit, fields, dataSerialized, convert) {
    data.forEach(function(element) {
        var tr = $('<tr>');
        fields.forEach(function(attr) {
            if (attr == "ativo") {
                if (element[attr] == "True")
                    tr.append('<td>Sim</td>');
                else
                    tr.append('<td>Não</td>');
            } else if (attr.includes("operation")) {
                expression = JSON.parse(attr);
                values = expression["values"].split(',');
                result = operation(expression["operation"], element[values[0]], element[values[1]]);
                tr.append('<td>' + result + '</td>');
            } else {
                tr.append('<td>' + element[attr] + '</td>');
            }
        });
        tr.append(getButtons(urlEdit, urlGET, element["_id"]["$oid"], convert));
        tbody.append(tr);
    });
}

function operation(operation, val1, val2) {
    calc = "";
    switch (operation) {
        case "MINUS":
            calc = val1 - val2;
            break;
    }
    return calc;
}

String.prototype.format = function() {
    var formatted = this;
    for (var arg in arguments) {
        formatted = formatted.replace("{" + arg + "}", arguments[arg]);
    }
    return formatted;
};

function postData(dataSerialized, url) {
    return $.ajax({
        url: url,
        type: 'POST',
        contentType: "application/json; charset=utf-8",
        data: dataSerialized,
        dataType: "json"
    });
}

function submitForm(dataSerialized, url, form, message, field, form) {
    $("#load").show();
    id = $("#_id").html();
    if (!id) {
        post = postData(dataSerialized, url);
        post.done(function(response) {
            $("#load").hide();
            setMessage(message.format(response[field]));
            $(form)[0].reset();
        });
        post.fail(function() {
            $("#load").hide();
            setMessage("Houve um erro ao salvar.");
        });
    } else {
        $.ajax({
            url: url + "/" + id,
            type: 'PUT',
            contentType: "application/json; charset=utf-8",
            data: dataSerialized,
            dataType: "json",
            success: function(response) {
                $("#load").hide();
                setMessage(message.format(response[field]));
            },
            error: function() {
                $("#load").hide();
                setMessage("Houve um erro ao salvar.");
            }
        });
    }
}

function getComunes() {
    comunes = $("#comune_select");
    $.getJSON('/api/comune/{"fields":["nome_comune"]}')
        .done(function(data) {
            data.forEach(function(element) {
                comunes.append(new Option(element["nome_comune"], element["nome_comune"]));
            });
        });
}

function prepareComment() {
    var comment = JSON.stringify($("#comentario").val());
    new_comment = comment.substr(1);
    new_comment = new_comment.substr(0, new_comment.length - 1);
    $("#comentario").val(new_comment);
}

function setComment() {
    var comment = $("#comentario").val();
    var input = comment.replace(/\r?\\n/g, '\n');
    $("#comentario").val(input);
}