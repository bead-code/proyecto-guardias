import { Navigate, Outlet } from "react-router-dom";
import { isExpired } from "react-jwt";
import { useContext } from "react";
import { AppGlobal } from "../../App.jsx"; // Importa AppGlobal como una variable de contexto

export function ProtectedRoute({ children, redirectTo = "login", ...props }) {
    const { decodedToken, isExpired } = useContext(AppGlobal);

    if (!decodedToken || isExpired) {
        console.log("Redirecting to login")
        console.log(decodedToken)
        console.log(isExpired)
        return <Navigate to={redirectTo} />;
    }
    return <Outlet {...props} />;
}
