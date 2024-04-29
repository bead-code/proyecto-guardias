
import { BotonBase } from "../inputs/buttons/BotonBase.jsx";
import { InputTexto } from "../inputs/InputTexto.jsx";
import { EtiquetaPersonalizada } from "../formField/EtiquetaPersonalizada.jsx";
import { Link } from "react-router-dom";
import { mostrarToast } from "../../utils/Notificaciones.js";
import { Navigate } from "react-router-dom";
import PropTypes from "prop-types";

export function Login({ manejarSubmit }) {
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
        <form onSubmit={(event) => manejarSubmit(event, nombreUsuario, contrasena)}
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