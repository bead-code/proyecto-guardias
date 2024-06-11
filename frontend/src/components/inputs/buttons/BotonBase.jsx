import PropTypes from "prop-types";

export function BotonBase({ children = '', className='', ...props }) {
    const estiloBoton = `w-full text-white bg-primary-600 hover:bg-primary-700 font-medium rounded-lg text-sm px-5 py-2.5 text-center focus:bg-primary-900 ${className}`;
    return (
        <button className={estiloBoton} {...props}>
            {children}
        </button>
    );

}
BotonBase.propTypes = {
    children: PropTypes.string,
    className: PropTypes.string
}