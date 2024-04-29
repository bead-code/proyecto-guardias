import { Login } from './Login.jsx';

export function LoginPage({ manejarSubmit, ...props }) {
    return (
            <Login manejarSubmit={manejarSubmit} {...props}/>

    )
}