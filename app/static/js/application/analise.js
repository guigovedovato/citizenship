function getProspectos() {
    prospectos = $("#prospecto_select");
    $.getJSON('/api/prospecto/{"fields":["cognome", "nome"]}')
        .done(function(data) {
            data.forEach(function(element) {
                prospectos.append(new Option(element["cognome"] + " " + element["nome"], element["cognome"] + " " + element["nome"]));
            });
        });
}

function doAnalise() {
    alert("Será feita a Análise");
}

function addLine(who, where) {
    switch (who) {
        case "menores":
            addMenores(where);
            break;
        case "bisavo":
            addBisavo(where);
            break;
        case "trisavo":
            addTrisavo(where);
            break;
    }
}

function addMenores(where) {
    var tr = $("<tr>");
    tr.attr("class", "menores");
    tr.append("<td>Filhos Menores</td>");
    tr.append("<td>Nascimento</td>");
    tr.append("<td><input type='text'></td>");
    tr.append("<td><input type='text'></td>");
    tr.append("<td><input type='date'></td>");
    tr.append("<td></td>");
    tr.append("<td></td>");
    tr.append("<td><input type='text'></td>");
    tr.insertAfter("." + where);
}

function addBisavo(where) {
    $("#btnAvo").removeAttr("onclick")
    var tbody = $("tbody");
    var tr = $("<tr>");
    tr.append("<td rowspan='6' style='vertical-align:middle'>Bisavô/Bisavó</td>");
    tr.append("<td>Nascimento</td>");
    tr.append("<td><input type='text'></td>");
    tr.append("<td><input type='text'></td>");
    tr.append("<td><input type='date'></td>");
    tr.append("<td></td>");
    tr.append("<td></td>");
    tr.append("<td><input type='text'></td>");
    var tdNascimento = $("<td rowspan='6' style='vertical-align:middle'>");
    var imgNascimento = $("<img id='btnBisavo' class='image-button'>");
    imgNascimento.attr("onclick", "addLine('trisavo','bisavo')");
    imgNascimento.attr("src", "/static/images/add.png");
    tdNascimento.append(imgNascimento);
    tr.append(tdNascimento);
    tbody.append(tr);
    tr = $("<tr>");
    tr.append("<td>Casamento</td>");
    tr.append("<td><input type='text'></td>");
    tr.append("<td><input type='text'></td>");
    tr.append("<td><input type='date'></td>");
    tr.append("<td><input type='number'></td>");
    tr.append("<td><input type='text'></td>");
    tr.append("<td><input type='text'></td>");
    tbody.append(tr);
    tr = $("<tr>");
    tr.append("<td>Óbito</td>");
    tr.append("<td><input type='text'></td>");
    tr.append("<td><input type='text'></td>");
    tr.append("<td><input type='date'></td>");
    tr.append("<td><input type='number'></td>");
    tr.append("<td><input type='text'></td>");
    tr.append("<td><input type='text'></td>");
    tbody.append(tr);
    tr = $("<tr>");
    tr.append("<td>Nasc Avô/Avó</td>");
    tr.append("<td><input type='text'></td>");
    tr.append("<td></td>");
    tr.append("<td></td>");
    tr.append("<td><input type='number'></td>");
    tr.append("<td><input type='text'></td>");
    tr.append("<td></td>");
    tbody.append(tr);
    tr = $("<tr>");
    tr.append("<td>Cas Avô/Avó</td>");
    tr.append("<td><input type='text'></td>");
    tr.append("<td></td>");
    tr.append("<td></td>");
    tr.append("<td><input type='number'></td>");
    tr.append("<td><input type='text'></td>");
    tr.append("<td></td>");
    tbody.append(tr);
    tr = $("<tr>");
    tr.attr("class", "bisavo");
    tr.append("<td>Nasc Pai/Mãe</td>");
    tr.append("<td><input type='text'></td>");
    tr.append("<td></td>");
    tr.append("<td></td>");
    tr.append("<td><input type='number'></td>");
    tr.append("<td><input type='text'></td>");
    tr.append("<td></td>");
    tbody.append(tr);
}

function addTrisavo(where) {
    $("#btnBisavo").removeAttr("onclick")
    var tbody = $("tbody");
    var tr = $("<tr>");
    tr.append("<td rowspan='6' style='vertical-align:middle'>Trisavô/Trisavó</td>");
    tr.append("<td>Nascimento</td>");
    tr.append("<td><input type='text'></td>");
    tr.append("<td><input type='text'></td>");
    tr.append("<td><input type='date'></td>");
    tr.append("<td></td>");
    tr.append("<td></td>");
    tr.append("<td><input type='text'></td>");
    tbody.append(tr);
    tr = $("<tr>");
    tr.append("<td>Casamento</td>");
    tr.append("<td><input type='text'></td>");
    tr.append("<td><input type='text'></td>");
    tr.append("<td><input type='date'></td>");
    tr.append("<td><input type='number'></td>");
    tr.append("<td><input type='text'></td>");
    tr.append("<td><input type='text'></td>");
    tbody.append(tr);
    tr = $("<tr>");
    tr.append("<td>Óbito</td>");
    tr.append("<td><input type='text'></td>");
    tr.append("<td><input type='text'></td>");
    tr.append("<td><input type='date'></td>");
    tr.append("<td><input type='number'></td>");
    tr.append("<td><input type='text'></td>");
    tr.append("<td><input type='text'></td>");
    tbody.append(tr);
    tr = $("<tr>");
    tr.append("<td>Nasc Bisavô/Bisavó</td>");
    tr.append("<td><input type='text'></td>");
    tr.append("<td></td>");
    tr.append("<td></td>");
    tr.append("<td><input type='number'></td>");
    tr.append("<td><input type='text'></td>");
    tr.append("<td></td>");
    tbody.append(tr);
    tr = $("<tr>");
    tr.append("<td>Cas Bisavô/Bisavó</td>");
    tr.append("<td><input type='text'></td>");
    tr.append("<td></td>");
    tr.append("<td></td>");
    tr.append("<td><input type='number'></td>");
    tr.append("<td><input type='text'></td>");
    tr.append("<td></td>");
    tbody.append(tr);
    tr = $("<tr>");
    tr.append("<td>Nasc Avô/Avó</td>");
    tr.append("<td><input type='text'></td>");
    tr.append("<td></td>");
    tr.append("<td></td>");
    tr.append("<td><input type='number'></td>");
    tr.append("<td><input type='text'></td>");
    tr.append("<td></td>");
    tbody.append(tr);
}

$(document).ready(function() {
    getProspectos();
});