
import { BotonBase } from "../inputs/buttons/BotonBase.jsx";
import { InputTexto } from "../inputs/InputTexto.jsx";
import { EtiquetaPersonalizada } from "../formField/EtiquetaPersonalizada.jsx";
import { Link } from "react-router-dom";
import { mostrarToast } from "../../utils/Notificaciones.js";
import { Navigate } from "react-router-dom";
import PropTypes from "prop-types";

const manejarSubmit = async (event, nombreUsuario, contrasena, setIsAuthenticated) => {
    event.preventDefault();
    const credentials = {
        email: nombreUsuario,
        password: contrasena
    }
    if (nombreUsuario === '' || contrasena === '') {
        mostrarToast('Datos incompletos', 'warning');
        return
    }
    const respuesta = fetch('https://reqres.in/api/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(credentials)
    });
    respuesta.then(async (res) => {
        const data = await res.json();
        if (res.ok) {
            // Guardar el token en el estado global o en local storage
            localStorage.setItem('tokenAppGuardias', data.token);
            setIsAuthenticated(true);
            mostrarToast('Login correcto ' + data.token, 'success');
        } else {
            console.error(data.error);
            mostrarToast('Error en el login', 'error');
        }

    }).catch((error) => {
        mostrarToast('No se ha podido comunicar con el servidor', 'error');
    });
}

export function Login({setIsAuthenticated}) {
    const DEFAULT_USER = "eve.holt@reqres.in";
    const DEFAULT_PASSWORD = "cityslicka";
    let nombreUsuario = DEFAULT_USER;
    let contrasena = DEFAULT_PASSWORD;

    // funcion que se ejecuta al enviar el formulario

    const manejarNombre = (e) => {
        nombreUsuario = e.target.value;
    }
    const manejarContrasena = (e) => {
        contrasena = e.target.value;
    }

    // componente que devuelve el formulario para iniciar sesion en la aplicacion
    return (
        <form onSubmit={(event) => manejarSubmit(event, nombreUsuario, contrasena, setIsAuthenticated)}
              className='flex flex-col gap-1 w-full max-w-xs m-auto bg-white shadow-md rounded p-8 items-start '>
            <EtiquetaPersonalizada>Nombre de usuario</EtiquetaPersonalizada>
            <InputTexto type="text" name="nombre" placeholder='Introduce DNI del usuario' onChange={manejarNombre}
                        className='mb-2'/>
            <EtiquetaPersonalizada>Constraseña</EtiquetaPersonalizada>
            <InputTexto type="password" name="contrasena" placeholder='Introduce contraseña del usuario'
                        onChange={manejarContrasena}/>
            <BotonBase type="submit"
                       className='mt-4'>
                Iniciar sesion</BotonBase>
        </form>
    )
}
Login.prototype = {
    manejarSubmit: PropTypes.func.isRequired
}
manejarSubmit.propTypes = {
    event: PropTypes.object.isRequired,
    nombreUsuario: PropTypes.string.isRequired,
    contrasena: PropTypes.string.isRequired,
    setIsAuthenticated: PropTypes.func.isRequired
}