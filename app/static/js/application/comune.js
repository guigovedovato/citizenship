$("#comuneSearch").submit(function(e) {
    e.preventDefault(); //prevent submit
    data = serializeToJson($(this).serializeArray())
    search("/api/comune/", "/comune/edit/", ['nome_comune', 'nome_contato', 'telefone_contato', 'ativo'], data);
});

$("#comuneForm").submit(function(e) {
    e.preventDefault(); //prevent submit
    data = serializeToJson($(this).serializeArray());
    submitForm(data, "/api/comune", true, "Comune {0} salvo com sucesso.", "nome_comune", this);
});