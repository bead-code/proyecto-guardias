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
import {mostrarToast} from "./utils/Notificaciones.js";
import PropTypes from 'prop-types';
import {LoginPage} from "./components/login/LoginPage.jsx";
import {AsignaturasUsuario} from "./components/pages/asignaturas/AsignaturasUsuario.jsx";
import {ProtectedRoute} from "./components/protectedRoute/ProtectedRoute.jsx";
import {ProximaGuardia} from "./components/pages/guardias/ProximaGuardia.jsx";

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

const mockAsignaturas = [
    {
        id: 2,
        nombre: "Matematicas",
        habilitado: true,
        aula: "A001",
        curso: "1ESO",
        profesor: {
            nick: "profesor1",
            color: "#FF0000",
            telefono: "123456789"
        },
        horas: [
            {
                dia: 1,
                hora: 1
            },
            {
                dia: 2,
                hora: 2
            }
        ]
    },
    {
        id: 3,
        nombre: "Lengua",
        habilitado: true,
        aula: "A002",
        curso: "1ESO",
        profesor: {
            nick: "profesor1",
            color: "#FF0000",
            telefono: "123456789"
        },
        horas: [
            {
                dia: 1,
                hora: 2
            },
            {
                dia: 2,
                hora: 1
            }
        ]
    },
    {
        id: 4,
        nombre: "Ingles",
        habilitado: true,
        aula: "A003",
        curso: "1ESO",
        profesor: {
            nick: "profesor1",
            color: "#FF0000",
            telefono: "123456789"
        },
        horas: [
            {
                dia: 1,
                hora: 3
            },
            {
                dia: 2,
                hora: 3
            }
        ]
    },
    {
        id: 5,
        nombre: "Fisica",
        habilitado: true,
        aula: "A004",
        curso: "1ESO",
        profesor: {
            nick: "profesor1",
            color: "#FF0000",
            telefono: "123456789"
        },
        horas: [
            {
                dia: 1,
                hora: 4
            },
            {
                dia: 2,
                hora: 4
            }
        ]
    },
    {
        id: 6,
        nombre: "Quimica",
        habilitado: true,
        aula: "A005",
        curso: "1ESO",
        profesor: {
            nick: "profesor1",
            color: "#FF0000",
            telefono: "123456789"
        },
        horas: [
            {
                dia: 1,
                hora: 5
            },
            {
                dia: 2,
                hora: 5
            }
        ]
    },
    {
        id: 7,
        nombre: "Biologia",
        habilitado: true,
        aula: "A006",
        curso: "1ESO",
        profesor: {
            nick: "profesor1",
            color: "#FF0000",
            telefono: "123456789"
        },
        horas: [
            {
                dia: 1,
                hora: 6
            },
            {
                dia: 2,
                hora: 6
            }
        ]
    },
    {
        id: 8,
        nombre: "Historia",
        habilitado: true,
        aula: "A007",
        curso: "1ESO",
        profesor: {
            nick: "profesor1",
            color: "#FF0000",
            telefono: "123456789"
        },
        horas: [
            {
                dia: 1,
                hora: 7
            },
            {
                dia: 2,
                hora: 7
            }
        ]
    },
    {
        id: 9,
        nombre: "Geografia",
        habilitado: true,
        aula: "A008",
        curso: "1ESO",
        profesor: {
            nick: "profesor1",
            color: "#FF0000",
            telefono: "123456789"
        },
        horas: [
            {
                dia: 1,
                hora: 8
            },
            {
                dia: 2,
                hora: 8
            }
        ]
    },
]

export function App() {
    const [isAuthenticated, setIsAuthenticated] = useState(false);
    const {
        decodedToken,
        isExpired
    } = useJwt("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c");



    return (
        <>
            <BrowserRouter>
                <BasicLayout>
                    <Routes>
                        <Route path="/guardias" element={<ListaGuardias></ListaGuardias>}/>
                        <Route path="/gruposGuardias" element={<ListaGuardias></ListaGuardias>}/>
                        <Route path="/gruposGuardias/:idGrupo" element={<GrupoGuardia></GrupoGuardia>}/>
                        <Route path="/login" element={<LoginPage setIsAuthenticated={setIsAuthenticated}/>}/>
                        <Route path="/signup" element={<h1>me llamo pepe signup</h1>}/>
                        {/* Ruta protegida */}
                        <Route element={<ProtectedRoute isAuthenticated={isAuthenticated}/>}>
                            <Route path="/" element={<h1>Landing pagee</h1>}/>
                            <Route path="/dashboard" element={<h1>Dashboard</h1>}/>
                            <Route path="/usuario/:idUsuario/asignaturas" element={<AsignaturasUsuario/>}/>
                            <Route path="/proximaguardia" element={<ProximaGuardia/>}/>
                        </Route>
                        {/* Ruta protegida */}
                        <Route path="*" element={<h1>404</h1>}/>
                    </Routes>
                </BasicLayout>
            </BrowserRouter>
        </>
    )
}

