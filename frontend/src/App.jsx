import './App.css';
import 'react-toastify/dist/ReactToastify.css';
import 'tailwindcss/tailwind.css';
import { createContext, useEffect, useState } from "react";
import { useJwt } from "react-jwt";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { BasicLayout } from "./layouts/BasicLayout.jsx";
import { LoginPage } from "./components/pages/login/LoginPage.jsx";
import { AsignaturasUsuario } from "./components/pages/asignaturas/AsignaturasUsuario.jsx";
import { ProtectedRoute } from "./components/protectedRoute/ProtectedRoute.jsx";
import { Guardia } from "./components/pages/guardias/Guardia.jsx";
import { ListaGuardias } from "./components/listas/ListaGuardias.jsx";
import { GrupoGuardia } from "./components/pages/gruposGuardias/GrupoGuardia.jsx";
import { UploadPage } from "./components/pages/cargaDatos/UploadPage.jsx";
import { ToastContainer } from "react-toastify";
import { UsuarioTodos } from "./components/pages/usuarios/UsuarioTodos.jsx";
import { UsuarioUnico } from "./components/pages/usuarios/UsuarioUnico.jsx";
import { CalendarioGuardias } from "./components/calendario/CalendarioGuardias.jsx";
import { AusenciaUsuario } from "./components/pages/ausencias/AusenciaUsuario.jsx";

export const AppGlobal = createContext();

export function App() {
    const [token, setToken] = useState('');

    useEffect(() => {
        const storedToken = localStorage.getItem('tokenAppGuardias');
        if (storedToken) {
            setToken(storedToken);
        }
    }, []);

    const { decodedToken, isExpired } = useJwt(token);

    return (
        <AppGlobal.Provider value={{ token, decodedToken, isExpired }}>
            <BrowserRouter>
                <BasicLayout isTokenExpired={isExpired} setToken={setToken}>
                    <Routes>
                        <Route path="/login" element={<LoginPage setToken={setToken} />} />
                        <Route element={<ProtectedRoute redirectTo='/login'/>}>
                            <Route path="/" element={<Navigate to="/guardia" />} />
                            <Route path="/guardias" element={<CalendarioGuardias />} />
                            <Route path="/guardias/:fecha/tramo/:tramoHorario/profesor/:idProfesor" element={<Guardia />} />
                            <Route path="/gruposGuardias" element={<ListaGuardias />} />
                            <Route path="/gruposGuardias/:idGrupo" element={<GrupoGuardia />} />
                            <Route path="/profesor" element={<UsuarioTodos />} />
                            <Route path="/profesor/:idProfesor" element={<UsuarioUnico />} />
                            <Route path="/ausencia/crear/:idProfesor" element={<AusenciaUsuario />} />
                            <Route path="/profesor/:idProfesor/mod" element={<UsuarioUnico modify={true} />} />
                            <Route path="/asignaturas" element={<AsignaturasUsuario />} />
                            <Route path="/uploadData" element={<UploadPage />} />
                        </Route>
                        <Route path="*" element={<h1>404</h1>} />
                    </Routes>
                </BasicLayout>
            </BrowserRouter>
            <ToastContainer />
        </AppGlobal.Provider>
    );
}

export default AppGlobal;
