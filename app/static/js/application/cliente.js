$("#clienteSearch").submit(function(e) {
    e.preventDefault(); //prevent submit
    data = serializeToJson($(this).serializeArray())
    search("/api/cliente/", "/cliente/edit/", [''], data, "");
});

$("#clienteForm").submit(function(e) {
    e.preventDefault(); //prevent submit
    data = serializeToJson($(this).serializeArray());
    submitForm(data, "/api/cliente", "clienteForm", "Cliente {0} salvo com sucesso.", "");
});

function getContract() {
    alert("TODO");
}