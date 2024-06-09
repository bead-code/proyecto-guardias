import {Navigate, Outlet} from "react-router-dom";
import {isExpired} from "react-jwt";
import {useContext} from "react";
import AppGlobal from "../../App.jsx";

export function ProtectedRoute({ children, isAuthenticated, redirectTo = "login", ...props }) {
    const {isExpired} = useContext(AppGlobal);

    if (isExpired) {
        return <Navigate to={redirectTo}/>
    }
    return <Outlet {...props} />
}