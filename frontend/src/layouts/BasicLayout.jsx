import { Navbar } from "../components/layout/NavBar.jsx";
import PropTypes from "prop-types";
import { Footer } from "../components/layout/Footer.jsx";
import {ToastContainer} from "react-toastify";

export function BasicLayout({children = ''}) {
    return (
    <>
        <Navbar/>
        <div className="h-full grow">
        {children}
        </div>
        <ToastContainer/>
        <Footer/>
    </>
    )
}
BasicLayout.propTypes = {
    children: PropTypes.node
}