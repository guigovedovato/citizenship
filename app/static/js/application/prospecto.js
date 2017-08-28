$("#prospectoSearch").submit(function(e) {
    e.preventDefault(); //prevent submit
    data = serializeToJson($(this).serializeArray())
    search("/api/prospecto/", "/prospecto/edit/", ['cognome', 'nome', 'celular', 'ativo'], data, "convert");
});

$("#prospectoForm").submit(function(e) {
    e.preventDefault(); //prevent submit
    prepareComment();
    data = serializeToJson($(this).serializeArray());
    submitForm(data, "/api/prospecto", "prospectoForm", "Prospecto {0} salvo com sucesso.", "cognome", this);
    setComment();
});

function analise(id) {

}

function doAnalise() {

}

function callAnaliseURL() {
    location.href = "/prospecto/analise/" + $("#_id").html();
}

$(document).ready(function() {
    today = getToday();
    if (document.getElementById("data_contato"))
        document.getElementById("data_contato").setAttribute("max", today);
    document.getElementById("data_interesse").setAttribute("min", today);
});