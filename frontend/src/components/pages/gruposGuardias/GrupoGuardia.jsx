import {Tipografia} from "../../tipografia/Tipografia.jsx";
import {Link, useParams} from "react-router-dom";
import {useEffect, useState} from "react";
import PropTypes from "prop-types";

export function GrupoGuardia() {
    const { idGrupo, pepe } = useParams()
    const [grupoGuardia, setGrupoGuardia] = useState({})
    useEffect(() => {
        fetch(`https://localhost:8080/gruposGuardias/${idGrupo}`)
            .then(res => res.json())
            .then(data => {
                setGrupoGuardia(data)
            })
    }, [idGrupo])
    return (
        <div className="grid grid-cols-2 grid-rows-[50px_1fr]] gap-4 w-full max-w-3xl m-auto bg-white shadow-md rounded p-8 items-start my-5 text-left">
            <h1 className="text-3xl col-span-2 text-center">Grupo de 111111 {pepe}</h1>
            <Tipografia className="text-3xl col-span-2 text-center">Grupo de guardias {"grupoGuardia.id"}</Tipografia>
            <div className="flex flex-col gap-4">
                <Tipografia className="text-xl">Dia de la semana: {"grupoGuardia.diaSemana"}</Tipografia>
                <Tipografia className="text-lg">Hora: {"grupoGuardia.hora"}</Tipografia>
                {/*Crear una linea de texto que indica el numero de guardias pendiente del grupo, este numero estara en verde en caso de ser 0.*/}
                <Tipografia className="text-lg">Guardias pendientes:
                    <Link to={`/guardias?dia=${grupoGuardia.dia}`}>{"grupoGuardia.pendientes"}</Link>
                </Tipografia>

            </div>
            <Tipografia className="text-lg">Guardias realizadas: </Tipografia>
        </div>
    )
}
