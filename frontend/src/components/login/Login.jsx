import {mostrarToast} from "../../utils/Notificaciones.js";
import {
    Button,
    Card,
    CardBody,
    CardFooter,
    CardHeader,
    Checkbox,
    Input,
    Typography
} from "@material-tailwind/react";
import {useContext, useState} from "react";
import {useNavigate} from 'react-router-dom';
import AppGlobal from "../../App.jsx";

export function Login({setToken}) {
    const DEFAULT_USER = "admin";
    const DEFAULT_PASSWORD = "1234";

    const [nombreUsuario, setNombreUsuario] = useState(DEFAULT_USER);
    const [contrasena, setContrasena] = useState(DEFAULT_PASSWORD);

    const navigate = useNavigate();

    const manejarSubmit = async (event, nombreUsuario, contrasena, setToken) => {
        event.preventDefault();
        const credentials = {
            username: nombreUsuario,
            password: contrasena
        }
        if (nombreUsuario === '' || contrasena === '') {
            mostrarToast('Datos incompletos', 'warning');
            return
        }
        const respuesta = fetch('http://localhost:8000/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: new URLSearchParams(credentials)
        });
        respuesta.then(async (res) => {
            const data = await res.json();
            console.log(data)
            if (res.ok) {
                // Guardar el token en el estado global o en local storage
                setToken(data.access_token);
                localStorage.setItem('tokenAppGuardias', data.access_token);
                mostrarToast('Login correcto', 'success');
                navigate('/dashboard')
            } else {
                console.error(data.error);
                mostrarToast('Error en el login', 'error');
            }

        }).catch((error) => {
            mostrarToast('No se ha podido comunicar con el servidor', 'error');
        });
    }

    const manejarNombre = (e) => {
        setNombreUsuario(e.target.value);
    }

    const manejarContrasena = (e) => {
        setContrasena(e.target.value);
    }


    return (
        <Card className="m-5 max-w-sm mx-auto">
            <CardHeader
                variant="gradient"
                color="gray"
                className="mb-4 grid h-28 place-items-center"
            >
                <Typography variant="h3" color="white">
                    Sign In
                </Typography>
            </CardHeader>
            <CardBody className="flex flex-col gap-4">
                <Input
                    label="Email"
                    size="lg"
                    value={nombreUsuario}
                    onChange={manejarNombre}
                />
                <Input
                    label="Password"
                    size="lg"
                    type="password"
                    value={contrasena}
                    onChange={manejarContrasena}
                />
            </CardBody>
            <CardFooter className="pt-0">
                <Button variant="gradient" fullWidth
                        onClick={(event) => manejarSubmit(event, nombreUsuario, contrasena, setToken)}>
                    Sign In
                </Button>
                <div className="-ml-2.5">
                    <Checkbox label="Remember Me"/>
                </div>
            </CardFooter>
        </Card>
    );
}