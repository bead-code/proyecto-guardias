
export function EtiquetaPersonalizada({children, className}) {
    const estiloEtiqueta = `text-gray-700 text-sm font-medium ${className}`;
    return (
        <label className={estiloEtiqueta}>{children}</label>
    )
}