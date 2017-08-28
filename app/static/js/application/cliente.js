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

function getDocuments() {
    alert("TODO");
}