$("#comuneSearch").submit(function(e) {
    e.preventDefault(); //prevent submit
    $("#load").show();
    tbody = $("tbody");
    tbody.empty();
    $.getJSON("/api/comune/" + serializeToJson($(this).serializeArray()))
        .done(function(data) {
            if (data && data != "") {
                data.forEach(function(element) {
                    var tr = $('<tr>');
                    ['nome_comune', 'nome_contato', 'telefone_contato', 'ativo'].forEach(function(attr) {
                        if (attr == "ativo")
                            if (element[attr] == "True")
                                tr.append('<td>Sim</td>');
                            else
                                tr.append('<td>Não</td>');
                        else
                            tr.append('<td>' + element[attr] + '</td>');
                    });
                    tr.append(getButtons("/comune/edit/", "/api/comune/", element["_id"]["$oid"]));
                    tbody.append(tr);
                });
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
});

$("#comuneForm").submit(function(e) {
    e.preventDefault(); //prevent submit
    $("#load").show();
    data = serializeToJson($(this).serializeArray());
    id = $("#_id").html();
    if (!id) {
        $.ajax({
            url: "/api/comune",
            type: 'POST',
            contentType: "application/json; charset=utf-8",
            data: data,
            dataType: "json",
            success: function(response) {
                $("#load").hide();
                document.getElementById("comuneForm").reset();
                setMessage("Comune " + response["nome_comune"] + " salva com sucesso.");
            },
            error: function() {
                $("#load").hide();
                setMessage("Houve um erro ao salvar.");
            }
        });
    } else {
        $.ajax({
            url: "/api/comune/" + id,
            type: 'PUT',
            contentType: "application/json; charset=utf-8",
            data: data,
            dataType: "json",
            success: function(response) {
                $("#load").hide();
                setMessage("Comune " + response["nome_comune"] + " salva com sucesso.");
            },
            error: function() {
                $("#load").hide();
                setMessage("Houve um erro ao salvar.");
            }
        });
    }
});