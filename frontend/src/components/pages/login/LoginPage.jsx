import { Login } from '../../login/Login.jsx';
import {mostrarToast} from "../../../utils/Notificaciones.js";



export function LoginPage({ setIsAuthenticated, ...props }) {
    return (
            <Login setIsAuthenticated={setIsAuthenticated} {...props}/>

    )
}