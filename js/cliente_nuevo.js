function guardar() {
    let n = document.getElementById("nombre").value
    let m = document.getElementById("mail").value
    let d = document.getElementById("domicilio").value
    let t = parseInt(document.getElementById("numero").value)

    

    let cliente = {
        nombre: n,
        mail: m,
        domicilio: d,
        numero: t
    }
    let url = "https://artecodoacodo.pythonanywhere.com/clientes"
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