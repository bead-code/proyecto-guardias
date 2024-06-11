
export function InputTexto({ className = '', children, ...props }) {
    const estiloInput = `w-full bg-gray-100 border-0 border-gray-300 text-black-200 rounded-lg text-sm px-5 py-2.5 text-center ${className}`;
    return (
        <input className={estiloInput} {...props}>
            {children}
        </input>
    )
}