import {Navigate, Outlet} from "react-router-dom";

export function ProtectedRoute({ children, isAuthenticated, redirectTo = "login", ...props }) {
    if (!isAuthenticated) {
        return <Navigate to={redirectTo}/>
    }
    return <Outlet {...props} />
}