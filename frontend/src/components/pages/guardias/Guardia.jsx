import {mostrarToast} from "../../../utils/Notificaciones.js";
import {Link, Navigate} from "react-router-dom";
import {toast} from "react-toastify";
import {useContext} from "react";
import AppGlobal from "../../../App.jsx";
import {Card, CardBody, CardHeader, Typography} from "@material-tailwind/react";
import {AvatarModificado} from "../../usuarios/AvatarModificado.jsx";


export function Guardia() {
    const {decodeToken} = useContext(AppGlobal);
    const manejarAceptar = async ({idProfesor, fecha, hora}) => {


        const respuesta = fetch("https://localhost:8000/guardias/1/aceptar", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                id_profesor: idProfesor,
            },)
        })
        const toastGuardia = toast.loading('Procesando peticion de tomar la guardia', {position: "bottom-right"})

        respuesta.then(async (res) => {
            const data = await res.json();
            if (res.ok) {
                toast.update(toastGuardia, {
                    render: 'Guardia aceptada correctamente',
                    type: 'success',
                    isLoading: false,
                    autoClose: 3000
                })
            } else {
                toast.update(toastGuardia, {
                    render: 'Ha ocurrido un error al asignar la guardia del dia ' + fecha + " a las " + hora + ". Por favor, inténtelo de nuevo.",
                    type: 'error',
                    isLoading: false,
                    autoClose: 3000
                })
            }

        }).catch((error) => {
            toast.update(toastGuardia, {
                render: 'Ha ocurrido un error al asignar la guardia del dia ' + fecha + " a las " + hora + ". Por favor, inténtelo de nuevo.",
                type: 'error',
                isLoading: false,
                autoClose: 3000
            })
        });
        Navigate({to: "/"})
    }
    const manejarRechazar = () => {
        console.log("manejarRechazar")
    }

    const guardia = {
        id: 1,
        fecha: "2022-01-31",
        horaInicio: "14:10",
        horaFin: "14:30",
        aula: "A001",
        curso: "1ESO",
        profesorAusente: {
            username: "profesor1",
            nombre: "Pepe grillo",
            color: "#FF0000",
        },
        profesorSustituto: {
            nick: "profesor3",
            color: "#FF0000",
            telefono: "123456789"
        }
    }
    guardia.fecha = new Date(guardia.fecha).toLocaleDateString()
    const porcentaje = -50
    let textoPorcentaje = `Llevas el mismo porcentaje de guardias que la media del grupo de guardias ¿Quieres aceptarla?`
    if (porcentaje > 0) {
        textoPorcentaje = `Llevas un ${Math.abs(porcentaje)}% de guardias más que la media del grupo de guardias ¿Quieres aceptarla?`
    } else if (porcentaje < 0) {
        textoPorcentaje = `Llevas ${Math.abs(porcentaje)}% de guardias menos que la media del grupo de guardias ¿Quieres aceptarla?`
    }

    // Componente que muestra la proxima guardia en una tarjeta
    return (
        <Card>
            <CardHeader variant='gradient' color='gray'></CardHeader>
            <CardBody className='justify-end'>
                <Typography variant='small' className='text-left'>Guardia día {guardia.fecha}</Typography>
                <Typography variant='lead' className='text-left'>Hora: {guardia.fecha}</Typography>
                <Typography variant='paragraph' className='text-left'>Aula: {guardia.aula}</Typography>
                <Typography variant='paragraph' className='text-left'>Curso: {guardia.curso}</Typography>
                <div className='flex gap-3 align-middle'>
                    <Typography variant='paragraph' className='text-left flex gap-4'>
                        Profesor ausente:
                    </Typography>
                    <AvatarModificado className='inline h' profesor={guardia.profesorAusente}/>
                </div>
                <Typography variant='paragraph' className='text-left'>Aula: {guardia.aula}</Typography>
            </CardBody>
        </Card>
    )
}

