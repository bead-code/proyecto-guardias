export function Tipografia({children, className, ...props}) {
    if (className) {
        return <p className={`text-gray-700 text-sm font-medium ${className}`} {...props}>{children}</p>
    }
    return <p className={className} {...props}>{children}</p>
}