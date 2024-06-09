import {Link, useParams} from "react-router-dom";
import {useEffect, useState} from "react";
import PropTypes from "prop-types";
import {Typography} from "@material-tailwind/react";

export function GrupoGuardia() {
    const { idGrupo, pepe } = useParams()
    const [grupoGuardia, setGrupoGuardia] = useState({})
    useEffect(() => {
        fetch(`http://localhost:8080/gruposGuardias/${idGrupo}`)
            .then(res => res.json())
            .then(data => {
                setGrupoGuardia(data)
            })
    }, [idGrupo])
    return (
        <div className="grid grid-cols-2 grid-rows-[50px_1fr]] gap-4 w-full max-w-3xl m-auto bg-white shadow-md rounded p-8 items-start my-5 text-left">
            <h1 className="text-3xl col-span-2 text-center">Grupo de 111111 {pepe}</h1>
            <Typography className="text-3xl col-span-2 text-center">Grupo de guardias {"grupoGuardia.id"}</Typography>
            <div className="flex flex-col gap-4">
                <Typography className="text-xl">Dia de la semana: {"grupoGuardia.diaSemana"}</Typography>
                <Typography className="text-lg">Hora: {"grupoGuardia.hora"}</Typography>
                {/*Crear una linea de texto que indica el numero de guardias pendiente del grupo, este numero estara en verde en caso de ser 0.*/}
                <Typography className="text-lg">Guardias pendientes:
                    <Link to={`/guardias?dia=${grupoGuardia.dia}`}>{"grupoGuardia.pendientes"}</Link>
                </Typography>

            </div>
            <Typography className="text-lg">Guardias realizadas: </Typography>
        </div>
    )
}
