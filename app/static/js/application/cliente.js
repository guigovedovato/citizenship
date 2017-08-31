$("#clienteSearch").submit(function(e) {
    e.preventDefault(); //prevent submit
    data = serializeToJson($(this).serializeArray())
    search("/api/cliente/", "/cliente/edit/", ['cognome', 'nome', 'celular', 'ativo'], data);
});

$("#clienteForm").submit(function(e) {
    e.preventDefault(); //prevent submit
    prepareComment();
    data = serializeToJson($(this).serializeArray());
    submitForm(data, "/api/cliente", "clienteForm", "Cliente {0} salvo com sucesso.", "cognome", this);
    setComment();
});

function getDocuments(kind) {
    alert("TODO");
}

$(document).ready(function() {
    today = getToday();
    document.getElementById("data_emissao_passaporte").setAttribute("max", today);
    document.getElementById("data_nascimento").setAttribute("max", today);
    document.getElementById("data_nascimento_pai").setAttribute("max", today);
    document.getElementById("data_nascimento_mae").setAttribute("max", today);
    setEstadoCivil();
    setFormacao();
    setConsulados();
    setTimeout(setComune, 100);
    setTimeout(setResidencia, 200);
});

$("#comune_select").change(function() {
    residencias = $("#residencia_select");
    residencias.find('option').not(':first').remove();
    $.getJSON('/api/residencia/{"comune":"' + $(this).find(":selected").val() + '"}')
        .done(function(data) {
            data.forEach(function(element) {
                residencias.append(new Option(element["endereco"], element["endereco"]));
            });
        });
});

function setEstadoCivil() {
    estadoCivil = $("#_estado_civil").html();
    $("#estado_civil_select").val(estadoCivil);
}

function setFormacao() {
    formacao = $("#_formacao").html();
    $("#formacao_select").val(formacao);
}

function setComune() {
    comune = $("#_comune").html();
    $("#comune_select").val(comune);
    $("#comune_select").change();
}

function setResidencia() {
    residencia_italia = $("#_residencia_italia").html();
    $("#residencia_select").val(residencia_italia);
}

function setConsulados() {
    jQuery('.consulados').each(function() {
        if ($("#_consulado").html().indexOf($(this).val()) > -1) {
            $(this).prop("checked", true);
        }
    });
}