$("#clienteSearch").submit(function(e) {
    e.preventDefault(); //prevent submit
    data = serializeToJson($(this).serializeArray())
    search("/api/cliente/", "/cliente/edit/", ['cognome', 'nome', 'celular', 'ativo'], data);
});

$("#clienteForm").submit(function(e) {
    e.preventDefault(); //prevent submit
    prepareComment();
    data = serializeToJson($(this).serializeArray());
    submitForm(data, "/api/cliente", true, "Cliente {0} salvo com sucesso.", "cognome", this);
    setComment();
});

function verifyFields(kind) {
    var response = true;
    if (kind == "contrato")
        response = verifyContract(response);
    else
        response = verifyRichiedente(response);
    if (!response)
        setMessage("Atenção", "Os campos marcados deverão ser preenchidos.");
    return response;
}

function verifyContract(response) {
    if (!$("#residencia").val()) {
        $("#residencia").addClass("required");
        response = false;
    }
    if (!$("#estado_civil_select").val()) {
        $("#estado_civil_select").addClass("required");
        response = false;
    }
    if (!$("#passaporte").val()) {
        $("#passaporte").addClass("required");
        response = false;
    }
    return response;
}

function verifyRichiedente(response) {
    if (!$("#residencia").val()) {
        $("#residencia").addClass("required");
        response = false;
    }
    if (!$("#estado_civil_select").val()) {
        $("#estado_civil_select").addClass("required");
        response = false;
    }
    if (!$("#email").val()) {
        $("#email").addClass("required");
        response = false;
    }
    if (!$("#nato_a").val()) {
        $("#nato_a").addClass("required");
        response = false;
    }
    if (!$("#data_nascimento").val()) {
        $("#data_nascimento").addClass("required");
        response = false;
    }
    if (!$("#formacao").val()) {
        $("#formacao").addClass("required");
        response = false;
    }
    if (!$("#profissao").val()) {
        $("#profissao").addClass("required");
        response = false;
    }
    if (!$("#cognome_pai").val()) {
        $("#cognome_pai").addClass("required");
        response = false;
    }
    if (!$("#nome_pai").val()) {
        $("#nome_pai").addClass("required");
        response = false;
    }
    if (!$("#nato_a_pai").val()) {
        $("#nato_a_pai").addClass("required");
        response = false;
    }
    if (!$("#data_nascimento_pai").val()) {
        $("#data_nascimento_pai").addClass("required");
        response = false;
    }
    if (!$("#cognome_mae").val()) {
        $("#cognome_mae").addClass("required");
        response = false;
    }
    if (!$("#nome_mae").val()) {
        $("#nome_mae").addClass("required");
        response = false;
    }
    if (!$("#nato_a_mae").val()) {
        $("#nato_a_mae").addClass("required");
        response = false;
    }
    if (!$("#data_nascimento_mae").val()) {
        $("#data_nascimento_mae").addClass("required");
        response = false;
    }
    return response;
}

function getDocuments(kind) {
    $("#load").show();
    removeRequiredClasses();
    if (verifyFields(kind)) {
        $.get("/api/cliente/{\"document\":\"" + kind + "\", \"cliente\":\"" + $("#_id").html() + "\"}")
            .done(function(response) {
                setMessage("Sucesso", "Arquivo salvo.");
            })
            .fail(function(data) {
                setMessage("Erro", "Houve um erro ao salvar o arquivo.");
            });
    }
    $("#load").hide();
}

$(document).ready(function() {
    today = getToday();
    document.getElementById("data_emissao_passaporte").setAttribute("max", today);
    document.getElementById("data_nascimento").setAttribute("max", today);
    document.getElementById("data_nascimento_pai").setAttribute("max", today);
    document.getElementById("data_nascimento_mae").setAttribute("max", today);
    setEstadoCivil();
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

function setComune() {
    comune = $("#_comune").html();
    $("#comune_select").val(comune);
    $("#comune_select").change();
}

function setResidencia() {
    var residencia_italia = $("#_residencia_italia").val();
    $("#residencia_select").val(residencia_italia);
}

function setConsulados() {
    jQuery('.consulados').each(function() {
        if ($("#_consulado").html().indexOf($(this).val()) > -1) {
            $(this).prop("checked", true);
        }
    });
}