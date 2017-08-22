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
    $.get("http://127.0.0.1:5000/api/comune/" + serializeToJson($(this).serializeArray()))
        .done(function(data) {
            alert(JSON.stringify(data));
        })
        .fail(function(data) {
            alert("erro: " + JSON.stringify(data));
        });
});