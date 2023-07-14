
console.log(location.search)     // lee los argumentos pasados a este formulario
var args = location.search.substr(1).split('&');  
console.log(args)

var parts = []
for (let i = 0; i < args.length; ++i) {
    parts[i] = args[i].split('=');
}
console.log(parts)

//// [[“id",3] , [“nombre",’tv50’]]
//decodeUriComponent elimina los caracteres especiales que recibe en la URL 
document.getElementById("id").value = decodeURIComponent(parts[0][1])
document.getElementById("nombre").value = decodeURIComponent(parts[1][1])
document.getElementById("mail").value = decodeURIComponent(parts[2][1])
document.getElementById("domicilio").value =decodeURIComponent( parts[3][1])
document.getElementById("numero").value =decodeURIComponent( parts[4][1])

function modificar() {
    let id = document.getElementById("id").value
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
    let url = "https://artecodoacodo.pythonanywhere.com/clientes/"+id
    var options = {
        body: JSON.stringify(cliente),
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        redirect: 'follow'
    }
    fetch(url, options)
        .then(function () {
            console.log("modificado")
            alert("Registro modificado")
            window.location.href = "./clientes.html";  
        //NUEVO,  si les da error el fetch  comentar esta linea que puede dar error  
        })
        .catch(err => {
            // this.errored = true
           alert("Error al Modificar")
           console.error(err);
        })      
}