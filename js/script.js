const nombre = document.querySelector("[name=nombre]");
const email = document.querySelector("[name=email]");
const telefono = document.querySelector("[name=telefono]");
const mensaje = document.querySelector("[name=mensaje]");

const validateEmptyField = (e) => {
    const field = e.target;
    const fielValue = e.target.value;

    if (fielValue.trim().length == 0) {
        field.classList.add("invalid");
        field.nextElementSibling.innerHTML = `El campo ${field.name} es obligatorio`;
    } else {
        field.classList.remove("invalid");
        field.nextElementSibling.innerHTML = "";
    }
}

const validateEmailFormat = (e) => {
    const field = e.target;
    const fielValue = e.target.value;
    const regex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;

    if (fielValue.trim().length > 5 && !regex.test(fielValue)) {
        field.classList.add("invalid");
        field.nextElementSibling.innerHTML = `El campo ${field.name} no tiene un formato válido`;
    } else {
        field.classList.remove("invalid");
        field.nextElementSibling.innerHTML = "";
    }
}




nombre.addEventListener("blur", validateEmptyField);
email.addEventListener("blur", validateEmptyField);
mensaje.addEventListener("blur", validateEmptyField);
telefono.addEventListener("blur", validateEmptyField);
email.addEventListener("input", validateEmailFormat);