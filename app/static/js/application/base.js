$(document).ready(function() {
    if (session())
        research();
    $("table").hide();
    if (document.getElementById("data_final"))
        getToday();
});

function session() {
    if (sessionStorage.actual) {
        sessionStorage.last = sessionStorage.actual;
        sessionStorage.actual = window.location.pathname;
    } else {
        sessionStorage.actual = window.location.pathname;
    }
    if ((String(sessionStorage.last).includes("novo") || String(sessionStorage.last).includes("edit")) &&
        (!String(sessionStorage.actual).includes("novo") || !String(sessionStorage.actual).includes("edit")))
        return true;
    else
        return false;
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
    document.getElementById("data_final").setAttribute("max", today);
    document.getElementById("data_inicial").setAttribute("max", today);
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

function getButtons(urlEdit, urlInactivate, id) {
    return '<td>' +
        '<img class="image-button btnEdit" src="static/images/edit.png" alt="Editar" _id="' +
        id + '" url="' + urlEdit + '" onclick="btnEdit(this)">' +
        '<img class="image-button btnInactivate" src="static/images/exclude.png" alt="Inativar" _id="' +
        id + '" url="' + urlInactivate + '" onclick="btnInactivate(this, \'nome_comune\')">' +
        '</td>'
}

function btnEdit(btn) {
    location.href = $(btn).attr("url") + $(btn).attr("_id");
}

function btnInactivate(btn, who) {
    $("#load").show();
    $.ajax({
        url: $(btn).attr("url") + $(btn).attr("_id"),
        type: 'PUT',
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify({ "ativo": "False" }),
        dataType: "json",
        success: function(response) {
            $("#load").hide();
            setMessage(response[who] + " inativado(a) com sucesso.");
            $("#btnSubmit").click();
        }
    });
}