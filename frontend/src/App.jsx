import './App.css'
import {ToastContainer} from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
// import tailwindcss from 'tailwindcss'
import 'tailwindcss/tailwind.css';
import {useState} from "react";
import {useJwt} from "react-jwt";
import {
    BrowserRouter,
    Routes,
    Route
} from "react-router-dom";
import {BasicLayout} from "./layouts/BasicLayout.jsx";
import {ListaAsignaturas} from "./components/asignaturas/usuario/ListaAsignaturas.jsx";
import {mostrarToast} from "./utils/Notificaciones.js";
import PropTypes from 'prop-types';
import {LoginPage} from "./components/login/LoginPage.jsx";

const manejarSubmit = async (event, nombreUsuario, contrasena) => {
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
            mostrarToast('Login correcto ' + data.token, 'success');
        } else {
            console.error(data.error);
            mostrarToast('Error en el login', 'error');
        }

    }).catch((error) => {
        mostrarToast('No se ha podido comunicar con el servidor', 'error');
    });
}

export function App() {
    const [isAuthenticated, setIsAuthenticated] = useState(false);
    const {
        decodedToken,
        isExpired
    } = useJwt("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c");
    const mockAsignaturas = [
        {
            id: 1,
            nombre: "Matemáticas",
            habilitado: true,
            horas: [
                {
                    dia: 0,
                    hora: 10
                }
            ]
        },
        {
            id: 2,
            nombre: "Lengua",
            habilitado: false,
            horas: [
                {
                    dia: 1,
                    hora: 1
                }
            ]
        },
        {
            id: 3,
            nombre: "Inglés",
            habilitado: true,
            horas: [
                {
                    dia: 1,
                    hora: 2
                }
            ]
        },
        {
            id: 4,
            nombre: "Historia",
            habilitado: true,
            horas: [
                {
                    dia: 2,
                    hora: 3
                }
            ]
        },
        {
            id: 5,
            nombre: "Física",
            habilitado: true,
            horas: [
                {
                    dia: 3,
                    hora: 4
                }
            ]
        },
        {
            id: 6,
            nombre: "Química",
            habilitado: true,
            horas: [
                {
                    dia: 4,
                    hora: 5
                }
            ]
        }
    ]


    return (
        <>
            <BrowserRouter>
                <BasicLayout>
                    <Routes>
                        <Route path="/" element={<ListaAsignaturas asignaturas={mockAsignaturas}/>}/>
                        <Route path="/Login" element={<LoginPage manejarSubmit={manejarSubmit}/>}/>
                        <Route path="/signup" element={<h1>me llamo pepe signup</h1>}/>
                        <Route path="/dashboard" element={<h1>Dashboard</h1>}/>
                    </Routes>
                </BasicLayout>
            </BrowserRouter>
        </>
    )
}

manejarSubmit.propTypes = {
    event: PropTypes.object.isRequired,
    nombreUsuario: PropTypes.string.isRequired,
    contrasena: PropTypes.string.isRequired
}
