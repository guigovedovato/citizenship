function addClass(witch) {
    var choice = "";
    switch (witch) {
        case "0":
            choice = "d0";
            break;
        case "1":
            choice = "d1";
            break;
        case "2":
            choice = "d2";
            break;
        case "3":
            choice = "d3";
            break;
        case "4":
            choice = "d4";
            break;
        case "5":
            choice = "d5";
            break;
        default:
            choice = "vencido";
    }
    return choice;
}

function createDiv() {
    var div = $('<div>');
    div.attr("class", "3u 12u(mobile)");
    return div;
}

function createSection(expiracao) {
    var section = $('<section>');
    section.attr("class", "box feature");
    section.addClass(addClass(expiracao));
    return section;
}

function createContent(content) {
    var p = $("<p>")
    p.append(content["data"])
    if (content["aeroporto"]) {
        p.append("<br>" + content["hora"])
        p.append("<br>" + content["aeroporto"])
    }
    if (content["comune"]) {
        p.append("<br>" + content["comune"])
    }
    if (parseInt(content["expiracao"]) < 0)
        p.append("<br> <b>Vencido</b>")
    else if (parseInt(content["expiracao"]) == 0)
        p.append("<br> <b>Hoje</b>")
    else
        p.append("<br> <b>Faltam " + content["expiracao"] + " dias</b>")
    return p;
}

function createBoard(item) {
    var div = createDiv()
    var section = createSection(item["expiracao"]);
    section.append("<h3>" + item["cognome"] + " " + item["nome"] + "</h3>");
    section.append(createContent(item));
    div.append(section);
    return div;
}

function getBoard() {
    $.getJSON('/api/cliente/{"board":"true"}')
        .done(function(data) {
            JSON.parse(JSON.stringify(data)).forEach(function(element) {
                $("#load").show();
                var recepcao = $("#recepcao");
                element["recepcao"].forEach(function(item) {
                    recepcao.append(createBoard(item));
                })
                $("#load").hide();
                $("#load").show();
                var residencia = $("#residencia")
                element["residencia"].forEach(function(item) {
                    residencia.append(createBoard(item));
                })
                $("#load").hide();
                $("#load").show();
                var naoRenuncia = $("#naoRenuncia")
                element["naoRenuncia"].forEach(function(item) {
                    naoRenuncia.append(createBoard(item));
                })
                $("#load").hide();
                $("#load").show();
                var passaporte = $("#passaporte")
                element["passaporte"].forEach(function(item) {
                    passaporte.append(createBoard(item));
                })
                $("#load").hide();
            });
        });
}

$(document).ready(function() {
    getBoard();
});