import { Typography } from "@material-tailwind/react";
import PropTypes from "prop-types";

export function Footer() {
    const currentYear = new Date().getFullYear();

    return (
        <footer className="bg-gray-800 text-white text-center py-4 max-h-32">
            <Typography className='text-white content-center'>
                <span>© {currentYear} Todos los derechos reservados</span>
            </Typography>
        </footer>
    );
}

Footer.propTypes = {
    currentYear: PropTypes.number.isRequired,
};
