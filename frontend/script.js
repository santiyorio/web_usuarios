const API = "http://127.0.0.1:8000"


async function cargarUsuarios() {

    const res = await fetch(API + "/usuarios")

    const datos = await res.json()

    const lista = document.getElementById("lista")

    lista.innerHTML = ""

    for (let u of datos) {

        const li = document.createElement("li")

        li.innerText = u[1] + " - " + u[2]

        lista.appendChild(li)
    }
}



async function agregarUsuario() {

    const nombre = document.getElementById("nombre").value
    const edad = document.getElementById("edad").value

    await fetch(API + "/agregar", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            nombre: nombre,
            edad: parseInt(edad)
        })
    })

    cargarUsuarios()
}