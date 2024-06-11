import { ModifiedNavBar } from "../components/layout/NavBar.jsx";
import PropTypes from "prop-types";
import { Footer } from "../components/layout/Footer.jsx";
import { ToastContainer } from "react-toastify";

export function BasicLayout({ decodedToken, isTokenExpired, setToken, children }) {
    return (
        <div className="flex flex-col min-h-screen">
            {!isTokenExpired && <ModifiedNavBar setToken={setToken} />}
            <div className="flex-grow w-full h-full place-content-center p-5">
                {children}
            </div>
            <Footer currentYear={new Date().getFullYear()}/>
            <ToastContainer />
        </div>
    );
}

BasicLayout.propTypes = {
    decodedToken: PropTypes.object,
    isTokenExpired: PropTypes.bool.isRequired,
    setToken: PropTypes.func.isRequired,
    children: PropTypes.node
};

export default BasicLayout;
