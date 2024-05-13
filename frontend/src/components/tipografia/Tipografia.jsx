export function Tipografia({children, className = 'text-medium text-left text-black', ...props}) {
    return <p className={className} {...props}>{children}</p>
}