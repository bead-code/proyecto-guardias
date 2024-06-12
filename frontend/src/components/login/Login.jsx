import { mostrarToast } from "../../utils/Notificaciones.js";
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
import { useContext, useState, useEffect } from "react";
import { useNavigate } from 'react-router-dom';
import AppGlobal from "../../App.jsx";

export function Login({ setToken }) {
    const [nombreUsuario, setNombreUsuario] = useState('');
    const [contrasena, setContrasena] = useState('');
    const { decodedToken, isExpired } = useContext(AppGlobal);
    const navigate = useNavigate();

    useEffect(() => {
        if (decodedToken && !isExpired) {
            navigate('/');
        }
    }, [decodedToken, isExpired, navigate]);

    const manejarSubmit = async (event) => {
        event.preventDefault();
        if (nombreUsuario === '' || contrasena === '') {
            mostrarToast('Datos incompletos', 'warning');
            return;
        }

        try {
            const response = await fetch('http://localhost:8000/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: new URLSearchParams({ username: nombreUsuario, password: contrasena })
            });

            const data = await response.json();
            if (response.ok) {
                setToken(data.access_token);
                localStorage.setItem('tokenAppGuardias', data.access_token);
                navigate('/');
            } else {
                console.error(data.error);
                mostrarToast('Credenciales erroneas', 'error');
            }
        } catch (error) {
            mostrarToast('No se ha podido comunicar con el servidor', 'error');
        }
    };

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
            <form onSubmit={manejarSubmit}>
                <CardBody className="flex flex-col gap-4">
                    <Input
                        label="Username"
                        size="lg"
                        value={nombreUsuario}
                        onChange={(e) => setNombreUsuario(e.target.value)}
                    />
                    <Input
                        label="Password"
                        size="lg"
                        type="password"
                        value={contrasena}
                        onChange={(e) => setContrasena(e.target.value)}
                    />
                </CardBody>
                <CardFooter className="pt-0">
                    <Button
                        variant="gradient"
                        fullWidth
                        type="submit"
                    >
                        Sign In
                    </Button>
                    <div className="-ml-2.5">
                        <Checkbox label="Remember Me" />
                    </div>
                </CardFooter>
            </form>
        </Card>
    );
}
