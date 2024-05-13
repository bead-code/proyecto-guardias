import {Tipografia} from "../../tipografia/Tipografia.jsx";
import {mostrarToast} from "../../../utils/Notificaciones.js";
import {Link, Navigate} from "react-router-dom";
import {toast} from "react-toastify";


export function ProximaGuardia({idProfesor}) {
    const manejarAceptar = async ({idProfesor, fecha, hora}) =>      {


        const respuesta = fetch("https://localhost:8080/guardias/1/aceptar", {
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

    const proximaGuardia = {
        id: 1,
        fecha: "2022-01-31",
        horaInicio: "14:10",
        horaFin: "14:30",
        aula: "A001",
        curso: "1ESO",
        profesorAusente: {
            nick: "profesor1",
            color: "#FF0000",
            telefono: "123456789"
        },
        profesorSustituto: {
            nick: "profesor3",
            color: "#FF0000",
            telefono: "123456789"
        }
    }
    proximaGuardia.fecha = new Date(proximaGuardia.fecha).toLocaleDateString()
    const porcentaje = -50
    let textoPorcentaje = `Llevas el mismo porcentaje de guardias que la media del grupo de guardias ¿Quieres aceptarla?`
    if (porcentaje > 0) {
        textoPorcentaje = `Llevas un ${Math.abs(porcentaje)}% de guardias más que la media del grupo de guardias ¿Quieres aceptarla?`
    } else if (porcentaje < 0) {
        textoPorcentaje = `Llevas ${Math.abs(porcentaje)}% de guardias menos que la media del grupo de guardias ¿Quieres aceptarla?`
    }

    // Componente que muestra la proxima guardia en una tarjeta
    return (
        <div className="flex flex-col gap-4 w-full max-w-3xl m-auto bg-white shadow-md rounded p-8 items-start my-5">
            <Tipografia className="text-3xl">Guardia
                dia {proximaGuardia.fecha}</Tipografia>
            <Tipografia className="text-xl">Hora: {proximaGuardia.horaInicio} - {proximaGuardia.horaFin}</Tipografia>
            <Tipografia className="text-lg">Aula: {proximaGuardia.aula}</Tipografia>
            <Tipografia className="text-lg">Curso: {proximaGuardia.curso}</Tipografia>
            <Tipografia className="text-lg">Profesor ausente: {proximaGuardia.profesorAusente.nick}</Tipografia>
            <Tipografia className="text-lg">Profesor sustituto: {proximaGuardia.profesorSustituto.nick}</Tipografia>
            <Tipografia className="text-lg">{textoPorcentaje}</Tipografia>
            <div className="flex gap-4 justify-center w-full">
                <Link to="/" className="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded"
                      onClick={() => manejarAceptar({
                          idProfesor: idProfesor,
                          fecha: proximaGuardia.fecha,
                          hora: proximaGuardia.horaInicio
                      })}>Aceptar
                </Link>
                <Link to="/" className="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded"
                      onClick={manejarRechazar}>Rechazar
                </Link>
            </div>
        </div>
    )
}

