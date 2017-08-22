$(document).ready(function() {
    $("table").hide();
});

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

$("#comuneSearch").submit(function(e) {
    e.preventDefault(); //prevent submit
    $("#load").show();
    tbody = $("tbody");
    tbody.empty();
    $.getJSON("http://127.0.0.1:5000/api/comune/" + serializeToJson($(this).serializeArray()))
        .done(function(data) {
            data.forEach(function(element) {
                var tr = $('<tr>');
                ['nome_comune', 'nome_anagrafe', 'telefone_contato', 'ativo'].forEach(function(attr) {
                    tr.append('<td>' + element[attr] + '</td>');
                });
                tr.append('<td>' +
                    '<img class="image-button" src="static/images/edit.png" alt="Editar">' +
                    '<img class="image-button" src="static/images/exclude.png" alt="Inativar">' +
                    '</td>');
                tbody.append(tr);
            });
            $("#load").hide();
            $("table").show();
        })
        .fail(function(data) {
            alert("erro: " + JSON.stringify(data));
        });
});