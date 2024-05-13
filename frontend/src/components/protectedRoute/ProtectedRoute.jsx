import {Navigate, Outlet} from "react-router-dom";
import {Navbar} from "../layout/NavBar.jsx";

export function ProtectedRoute({ children, isAuthenticated, redirectTo = "login", ...props }) {
    if (!isAuthenticated) {
        return <Navigate to={redirectTo}/>
    }
    return <Outlet {...props} />
}