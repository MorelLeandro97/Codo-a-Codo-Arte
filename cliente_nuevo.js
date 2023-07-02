function guardar() {
    let n = document.getElementById("nombre").value
    let m = parseFloat(document.getElementById("mail").value)
    let d = parseInt(document.getElementById("domicilio").value)
    let t = document.getElementById("numero").value

    

    let cliente = {
        nombre: n,
        mail: m,
        domicilio: d,
        telefono: t
    }
    let url = "https://crud23033.pythonanywhere.com/clientes"
    var options = {
        body: JSON.stringify(cliente),
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
    }
    fetch(url, options)
        .then(function () {
            console.log("creado")
            alert("Grabado")
            // Devuelve el href (URL) de la página actual
            window.location.href = "./clientes.html";  
            // Handle response we get from the API
        })
        .catch(err => {
            //this.errored = true
            alert("Error al grabar" )
            console.error(err);
        })
}