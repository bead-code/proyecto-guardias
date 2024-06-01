import {useContext, useEffect, useState} from "react";
import {useParams} from "react-router-dom";
import AppGlobal from "../../../App.jsx";
import {Card, CardBody, CardHeader, Typography} from "@material-tailwind/react";

export function UsuarioUnico({defaultUser = undefined, ...prop}) {
    const [usuario, setUsuario] = useState(defaultUser);
    const {idProfesor} = useParams();
    const {token} = useContext(AppGlobal);
    useEffect(() => {
        if (usuario === undefined) {
            fetch(`http://localhost:8000/profesor/${idProfesor}`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer ' + token,
                }
            })
                .then((response) => response.json())
                .then((data) => {
                    setUsuario(data);
                });
        }
    }, []);
    // Page that shows the information of a single user (profesor)

    if (usuario === undefined) {
        return (
            <div>
                <h1>Cargando...</h1>
            </div>
        );
    }
    return (
        <Card>
            <CardHeader color="blueGray">
                <Typography variant='h1'>Usuario</Typography>
            </CardHeader>
            <CardBody>
                <div className="flex flex-col gap-4">
                    <div>
                        <h3>Nombre:</h3>
                        <p>{usuario.nombre}</p>
                    </div>
                    <div>
                        <h3>Username:</h3>
                        <p>{usuario.username}</p>
                    </div>
                    <div>
                        <h3>Rol:</h3>
                        <p>{usuario.rol.nombre}</p>
                    </div>
                </div>
            </CardBody>
        </Card>
    )
}