import {ModifiedNavBar} from "../components/layout/NavBar.jsx";
import PropTypes from "prop-types";
import {Footer} from "../components/layout/Footer.jsx";
import {ToastContainer} from "react-toastify";

export function BasicLayout({decodedToken, isTokenExpired, setToken, children = ''}) {
    console.log("decodedToken")
    console.log(!isTokenExpired)

    return (
        <div className="flex flex-col min-h-screen">
            {!isTokenExpired
                ? <ModifiedNavBar setToken={setToken}/>
                : null}
            <div className="flex-grow w-full h-full place-content-center p-5">
                {children}
            </div>
            <Footer/>
        </div>
    )
}