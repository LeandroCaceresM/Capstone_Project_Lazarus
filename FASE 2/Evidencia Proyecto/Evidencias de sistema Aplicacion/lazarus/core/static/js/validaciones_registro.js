// ==================== VALIDAR FECHA (16+ AÑOS) ====================

const inputFecha = document.getElementById("fecha_nacimiento");
const errorFecha = document.getElementById("error_fecha");

const hoy = new Date();
const fechaMax = new Date(hoy.getFullYear() - 16, hoy.getMonth(), hoy.getDate());
const fechaMaxStr = fechaMax.toISOString().split('T')[0];

if (inputFecha) {
    inputFecha.setAttribute("max", fechaMaxStr);

    inputFecha.addEventListener("change", function () {
        const fechaIngresada = new Date(this.value);
        if (fechaIngresada > fechaMax) {
            errorFecha.style.display = "block";
            this.value = "";
        } else {
            errorFecha.style.display = "none";
        }
    });
}



// ==================== VALIDAR TELÉFONO (Formato 569XXXXXXXX) ====================

const telefonoInput = document.getElementById("telefono");

if (telefonoInput) {
    telefonoInput.addEventListener("input", () => {

        telefonoInput.value = telefonoInput.value.replace(/\D/g, "");

        if (!telefonoInput.value.startsWith("569")) {
            telefonoInput.value = "569";
        }

        if (telefonoInput.value.length > 11) {
            telefonoInput.value = telefonoInput.value.slice(0, 11);
        }
    });
}



// ==================== SOLO FORMATEAR RUT (SIN VALIDAR) ====================

// Formatear RUT mientras escribe
function formatearRut(rut) {
    rut = rut.toUpperCase().replace(/[^0-9K]/g, "");

    if (rut.length <= 1) return rut;

    const cuerpo = rut.slice(0, -1).replace(/\B(?=(\d{3})+(?!\d))/g, ".");
    const dv = rut.slice(-1);

    return `${cuerpo}-${dv}`;
}

const inputRut = document.getElementById("rut");

if (inputRut) {

    inputRut.addEventListener("input", () => {

        let limpio = inputRut.value.toUpperCase().replace(/[^0-9K]/g, "");

        if (limpio.length > 9) limpio = limpio.slice(0, 9);

        inputRut.value = limpio.length >= 2 ? formatearRut(limpio) : limpio;
    });

    // NO VALIDAR — no alert, no borde rojo
    inputRut.addEventListener("blur", () => {
        inputRut.style.borderColor = ""; // dejar normal
    });
}
