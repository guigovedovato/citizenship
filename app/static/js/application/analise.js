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
    data = serializeToJson($("#analiseForm").serializeArray());
    submitForm(data, "/api/analise", false, "Análise do prospecto {0} salva com sucesso.", "prospecto", this);
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
    sessionStorage.menor_click = Number(sessionStorage.menor_click) + 1;
    var tr = $("<tr>");
    tr.attr("class", "menores");
    tr.append("<td>Filhos Menores</td>");
    tr.append("<td>Nascimento</td>");
    tr.append("<td><input type='text' name='nascimento_menor" + sessionStorage.menor_click + "_nome' id='nascimento_menor" + sessionStorage.menor_click + "_nome' placeholder='Digite o nome' value=''></td>");
    tr.append("<td><input type='text' name='nascimento_menor" + sessionStorage.menor_click + "_local' id='nascimento_menor" + sessionStorage.menor_click + "_local' placeholder='Digite o local' value=''></td>");
    tr.append("<td><input type='date' name='nascimento_menor" + sessionStorage.menor_click + "_data' id='nascimento_menor" + sessionStorage.menor_click + "_data' value=''></td>");
    tr.append("<td></td>");
    tr.append("<td></td>");
    tr.append("<td><input type='text' name='nascimento_menor" + sessionStorage.menor_click + "_doc' id='nascimento_menor" + sessionStorage.menor_click + "_doc' placeholder='Digite o doc' value=''></td>");
    tr.insertAfter("." + where);
}

function addBisavo(where) {
    $("#btnAvo").removeAttr("onclick")
    var tbody = $("tbody");
    var tr = $("<tr>");
    tr.append("<td rowspan='6' style='vertical-align:middle'>Bisavô/Bisavó</td>");
    tr.append("<td>Nascimento</td>");
    tr.append("<td><input type='text' name='nascimento_bisavo_nome' id='nascimento_bisavo_nome' placeholder='Digite o nome' value=''></td>");
    tr.append("<td><input type='text' name='nascimento_bisavo_local' id='nascimento_bisavo_local' placeholder='Digite o local' value=''></td>");
    tr.append("<td><input type='date' name='nascimento_bisavo_data' id='nascimento_bisavo_data' value=''></td>");
    tr.append("<td></td>");
    tr.append("<td></td>");
    tr.append("<td><input type='text' name='nascimento_bisavo_doc' id='nascimento_bisavo_doc' placeholder='Digite o doc' value=''></td>");
    var tdNascimento = $("<td rowspan='6' style='vertical-align:middle'>");
    var imgNascimento = $("<img id='btnBisavo' class='image-button'>");
    imgNascimento.attr("onclick", "addLine('trisavo','bisavo')");
    imgNascimento.attr("src", "/static/images/add.png");
    tdNascimento.append(imgNascimento);
    tr.append(tdNascimento);
    tbody.append(tr);
    tr = $("<tr>");
    tr.append("<td>Casamento</td>");
    tr.append("<td><input type='text' name='casamento_bisavo_nome' id='casamento_bisavo_nome' placeholder='Digite o nome' value=''></td>");
    tr.append("<td><input type='text' name='casamento_bisavo_local' id='casamento_bisavo_local' placeholder='Digite o local' value=''></td>");
    tr.append("<td><input type='date' name='casamento_bisavo_data' id='casamento_bisavo_data' value=''></td>");
    tr.append("<td><input type='number' name='casamento_bisavo_idade' id='casamento_bisavo_idade' value=''></td>");
    tr.append("<td><input type='text' name='casamento_bisavo_conjuge' id='casamento_bisavo_conjuge' placeholder='Digite o conjuge' value=''></td>");
    tr.append("<td><input type='text' name='casamento_bisavo_doc' id='casamento_bisavo_doc' placeholder='Digite o doc' value=''></td>");
    tbody.append(tr);
    tr = $("<tr>");
    tr.append("<td>Óbito</td>");
    tr.append("<td><input type='text' name='obito_bisavo_nome' id='obito_bisavo_nome' placeholder='Digite o nome' value=''></td>");
    tr.append("<td><input type='text' name='obito_bisavo_local' id='obito_bisavo_local' placeholder='Digite o local' value=''></td>");
    tr.append("<td><input type='date' name='obito_bisavo_data' id='obito_bisavo_data' value=''></td>");
    tr.append("<td><input type='number' name='obito_bisavo_idade' id='obito_bisavo_idade' value=''></td>");
    tr.append("<td><input type='text' name='obito_bisavo_conjuge' id='obito_bisavo_conjuge' placeholder='Digite o conjuge' value=''></td>");
    tr.append("<td><input type='text' name='obito_bisavo_doc' id='obito_bisavo_doc' placeholder='Digite o doc' value=''></td>");
    tbody.append(tr);
    tr = $("<tr>");
    tr.append("<td>Nasc Avô/Avó</td>");
    tr.append("<td><input type='text' name='nascimento_bisavo_avo_nome' id='nascimento_bisavo_avo_nome' placeholder='Digite o nome' value=''></td>");
    tr.append("<td></td>");
    tr.append("<td></td>");
    tr.append("<td><input type='number' name='nascimento_bisavo_avo_idade' id='nascimento_avo_bisavo_idade' value=''></td>");
    tr.append("<td><input type='text' name='nascimento_bisavo_avo_conjuge' id='nascimento_avo_bisavo_conjuge' placeholder='Digite o conjuge' value=''></td>");
    tr.append("<td></td>");
    tbody.append(tr);
    tr = $("<tr>");
    tr.append("<td>Cas Avô/Avó</td>");
    tr.append("<td><input type='text' name='casamento_bisavo_avo_nome' id='casamento_bisavo_avo_nome' placeholder='Digite o nome' value=''></td>");
    tr.append("<td></td>");
    tr.append("<td></td>");
    tr.append("<td><input type='number' name='casamento_bisavo_avo_idade' id='casamento_bisavo_avo_idade' value=''></td>");
    tr.append("<td><input type='text' name='casamento_bisavo_avo_conjuge' id='casamento_bisavo_avo_conjuge' placeholder='Digite o conjuge' value=''></td>");
    tr.append("<td></td>");
    tbody.append(tr);
    tr = $("<tr>");
    tr.attr("class", "bisavo");
    tr.append("<td>Nasc Pai/Mãe</td>");
    tr.append("<td><input type='text' name='nascimento_bisavo_paimae_nome' id='nascimento_bisavo_paimae_nome' placeholder='Digite o nome' value=''></td>");
    tr.append("<td></td>");
    tr.append("<td></td>");
    tr.append("<td><input type='number' name='nascimento_bisavo_paimae_idade' id='nascimento_bisavo_paimae_idade' value=''></td>");
    tr.append("<td><input type='text' name='nascimento_bisavo_paimae_conjuge' id='nascimento_bisavo_paimae_conjuge' placeholder='Digite o conjuge' value=''></td>");
    tr.append("<td></td>");
    tbody.append(tr);
}

function addTrisavo(where) {
    $("#btnBisavo").removeAttr("onclick")
    var tbody = $("tbody");
    var tr = $("<tr>");
    tr.append("<td rowspan='6' style='vertical-align:middle'>Trisavô/Trisavó</td>");
    tr.append("<td>Nascimento</td>");
    tr.append("<td><input type='text' name='nascimento_trisavo_nome' id='nascimento_trisavo_nome' placeholder='Digite o nome' value=''></td>");
    tr.append("<td><input type='text' name='nascimento_trisavo_local' id='nascimento_trisavo_local' placeholder='Digite o local' value=''></td>");
    tr.append("<td><input type='date' name='nascimento_trisavo_data' id='nascimento_trisavo_data' value=''></td>");
    tr.append("<td></td>");
    tr.append("<td></td>");
    tr.append("<td><input type='text' name='nascimento_trisavo_doc' id='nascimento_trisavo_doc' placeholder='Digite o doc' value=''></td>");
    tbody.append(tr);
    tr = $("<tr>");
    tr.append("<td>Casamento</td>");
    tr.append("<td><input type='text' name='casamento_trisavo_nome' id='casamento_trisavo_nome' placeholder='Digite o nome' value=''></td>");
    tr.append("<td><input type='text' name='casamento_trisavo_local' id='casamento_trisavo_local' placeholder='Digite o local' value=''></td>");
    tr.append("<td><input type='date' name='casamento_trisavo_data' id='casamento_trisavo_data' value=''></td>");
    tr.append("<td><input type='number' name='casamento_trisavo_idade' id='casamento_trisavo_idade' value=''></td>");
    tr.append("<td><input type='text' name='casamento_trisavo_conjuge' id='casamento_trisavo_conjuge' placeholder='Digite o conjuge' value=''></td>");
    tr.append("<td><input type='text' name='casamento_trisavo_doc' id='casamento_trisavo_doc' placeholder='Digite o doc' value=''></td>");
    tbody.append(tr);
    tr = $("<tr>");
    tr.append("<td>Óbito</td>");
    tr.append("<td><input type='text' name='obito_trisavo_nome' id='obito_trisavo_nome' placeholder='Digite o nome' value=''></td>");
    tr.append("<td><input type='text' name='obito_trisavo_local' id='obito_trisavo_local' placeholder='Digite o local' value=''></td>");
    tr.append("<td><input type='date' name='obito_trisavo_data' id='obito_trisavo_data' value=''></td>");
    tr.append("<td><input type='number' name='obito_trisavo_idade' id='obito_trisavo_idade' value=''></td>");
    tr.append("<td><input type='text' name='obito_trisavo_conjuge' id='obito_trisavo_conjuge' placeholder='Digite o conjuge' value=''></td>");
    tr.append("<td><input type='text' name='obito_trisavo_doc' id='obito_trisavo_doc' placeholder='Digite o doc' value=''></td>");
    tbody.append(tr);
    tr = $("<tr>");
    tr.append("<td>Nasc Bisavô/Bisavó</td>");
    tr.append("<td><input type='text' name='nascimento_trisavo_bisavo_nome' id='nascimento_trisavo_bisavo_nome' placeholder='Digite o nome' value=''></td>");
    tr.append("<td></td>");
    tr.append("<td></td>");
    tr.append("<td><input type='number' name='nascimento_trisavo_bisavo_idade' id='nascimento_trisavo_bisavo_idade' value=''></td>");
    tr.append("<td><input type='text' name='nascimento_trisavo_bisavo_conjuge' id='nascimento_trisavo_bisavo_conjuge' placeholder='Digite o conjuge' value=''></td>");
    tr.append("<td></td>");
    tbody.append(tr);
    tr = $("<tr>");
    tr.append("<td>Cas Bisavô/Bisavó</td>");
    tr.append("<td><input type='text' name='casamento_trisavo_bisavo_nome' id='casamento_trisavo_bisavo_nome' placeholder='Digite o nome' value=''></td>");
    tr.append("<td></td>");
    tr.append("<td></td>");
    tr.append("<td><input type='number' name='casamento_trisavo_bisavo_idade' id='casamento_trisavo_bisavo_idade' value=''></td>");
    tr.append("<td><input type='text' name='casamento_trisavo_bisavo_conjuge' id='casamento_trisavo_bisavo_conjuge' placeholder='Digite o conjuge' value=''></td>");
    tr.append("<td></td>");
    tbody.append(tr);
    tr = $("<tr>");
    tr.append("<td>Nasc Avô/Avó</td>");
    tr.append("<td><input type='text' name='nascimento_trisavo_avo_nome' id='nascimento_trisavo_avo_nome' placeholder='Digite o nome' value=''></td>");
    tr.append("<td></td>");
    tr.append("<td></td>");
    tr.append("<td><input type='number' name='nascimento_trisavo_avo_idade' id='nascimento_trisavo_avo_idade' value=''></td>");
    tr.append("<td><input type='text' name='nascimento_trisavo_avo_conjuge' id='nascimento_trisavo_avo_conjuge' placeholder='Digite o conjuge' value=''></td>");
    tr.append("<td></td>");
    tbody.append(tr);
}

function getLastDomain() {
    var domain = (window.location.pathname).split("/");
    return domain[3];
}

function verifyDomain() {
    return Number.isInteger(parseInt(getLastDomain()))
}

function changeToBlank(str, ch) {
    var newStr = "";
    var strList = str.split(ch);
    strList.forEach(function(element) {
        newStr += element + " ";
    });
    return newStr.substr(0, newStr.length - 1);
}

function createProspectName() {
    var select = $("#prospecto_select");
    if (typeof(select) != 'undefined' && select != null) {
        var h = $("<h2>");
        var value = changeToBlank(getLastDomain(), "%20");
        h.html(value);
        h.insertAfter($("#prospecto"));
        var hidden = $("<input>");
        hidden.attr("type", "hidden");
        hidden.attr("id", "prospecto");
        hidden.attr("name", "prospecto");
        hidden.attr("value", value);
        hidden.insertAfter(h);
        select.remove();
    }
}

$(document).ready(function() {
    sessionStorage.menor_click = 0;
    if (verifyDomain()) {
        getProspectos();
    } else {
        createProspectName();
    }
});