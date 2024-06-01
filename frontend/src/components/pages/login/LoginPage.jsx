import {Login} from '../../login/Login.jsx';



export function LoginPage({ setToken, ...props }) {
    return (
            <Login setToken={setToken} {...props}/>

    )
}