import './App.css'
import 'react-toastify/dist/ReactToastify.css';
import 'tailwindcss/tailwind.css';
import {createContext, useContext, useState} from "react";
import {useJwt} from "react-jwt";
import {BrowserRouter, Routes, Route, useNavigate} from "react-router-dom";
import {BasicLayout} from "./layouts/BasicLayout.jsx";
import {LoginPage} from "./components/pages/login/LoginPage.jsx";
import {AsignaturasUsuario} from "./components/pages/asignaturas/AsignaturasUsuario.jsx";
import {ProtectedRoute} from "./components/protectedRoute/ProtectedRoute.jsx";
import {ProximaGuardia} from "./components/pages/guardias/ProximaGuardia.jsx";
import {ListaGuardias} from "./components/listas/ListaGuardias.jsx";
import {GrupoGuardia} from "./components/pages/gruposGuardias/GrupoGuardia.jsx";
import {UploadPage} from "./components/pages/cargaDatos/UploadPage.jsx";
import {ToastContainer} from "react-toastify";
import {UsuarioTodos} from "./components/pages/usuarios/UsuarioTodos.jsx";
import {UsuarioUnico} from "./components/pages/usuarios/UsuarioUnico.jsx";


export const AppGlobal = createContext();

export function App() {
    const [token, setToken] = useState(localStorage.getItem('tokenAppGuardias'));
    const {decodedToken, isExpired} = useJwt(token);
    return (
        <>
            <BrowserRouter>
                <AppGlobal.Provider value={{token, decodedToken, isExpired}}>
                    <BasicLayout decodedToken={decodedToken} isTokenExpired={isExpired} setToken={setToken}>
                        <Routes>
                            <Route path="/guardias" element={<ListaGuardias></ListaGuardias>}/>
                            <Route path="/gruposGuardias" element={<ListaGuardias></ListaGuardias>}/>
                            <Route path="/gruposGuardias/:idGrupo" element={<GrupoGuardia></GrupoGuardia>}/>
                            <Route path="/login" element={<LoginPage setToken={setToken}/>}/>
                            {/* Ruta protegida */}
                            <Route element={<ProtectedRoute isAuthenticated={token}/>}>
                                <Route path="/" element={<h1>Landing pagee</h1>}/>
                                <Route path="/dashboard" element={<h1>Dashboard</h1>}/>
                                <Route path="/profesor" element={<UsuarioTodos/>}/>
                                <Route path="/profesor/:idProfesor" element={<UsuarioUnico/>}/>
                                <Route path="/asignaturas" element={<AsignaturasUsuario/>}/>
                                <Route path="/proximaguardia" element={<ProximaGuardia/>}/>
                                <Route path="/uploadData" element={<UploadPage/>}/>
                            </Route>
                            {/* Ruta protegida */}
                            <Route path="*" element={<h1>404</h1>}/>
                        </Routes>
                    </BasicLayout>
                </AppGlobal.Provider>
                <ToastContainer/>
            </BrowserRouter>
        </>
    )
}

export default AppGlobal;

