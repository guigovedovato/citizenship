$("#residenciaSearch").submit(function(e) {
    e.preventDefault(); //prevent submit
    data = serializeToJson($(this).serializeArray())
    search("/api/residencia/", "/residencia/edit/", ['comune', 'capacidade', 'vagas', '{"operation":"MINUS", "values":"capacidade,vagas"}', 'ativo'], data);
});

$("#residenciaForm").submit(function(e) {
    e.preventDefault(); //prevent submit
    data = serializeToJson($(this).serializeArray());
    submitForm(data, "/api/residencia", "residenciaForm", "Residencia {0} salva com sucesso.", "endereco", this);
});