import PropTypes from 'prop-types';
import {useState} from "react";
import { GrStatusDisabled, GrStatusGood  } from "react-icons/gr";
import {useParams} from "react-router-dom";
import {Typography} from "@material-tailwind/react";


function ItemAsignatura({ asignaturaInicial, eliminarAsignatura, ...props}) {
    // TODO: Mostrar boton para eliminar la asignatura.
    // TODO: Mostrar las horas de la asignatura.
    // TODO: Mostrar opcion para modificar las horas de la asignatura.
    // TODO: Mostrar opcion para modificar el aula de la asignatura.

    const [asignatura, setAsignatura] = useState(asignaturaInicial);
    const [deshabilitarCheck, setDeshabilitarCheck] = useState(false);

    const manejarHabilitado = (e) => {
        setDeshabilitarCheck(!deshabilitarCheck);
        setAsignatura({
            ...asignatura,
            habilitado: !asignatura.habilitado
        });

    }

    const estiloBotonEliminar = 'text-red-700 font-medium rounded-lg text-sm p-2 m-2 text-center outline-2 outline-red-700 outline hover:outline-none hover:bg-red-700 hover:text-white transition-none delay-0'
    const estiloHabilitada = "flex px-5 w-full bg-amber-100 shadow"
    const estiloInhabilitada = "flex px-5 w-full bg-blue-100 shadow"
    return (
        <li className={asignatura.habilitado ? estiloHabilitada : estiloInhabilitada} {...props}>
            <Typography className='mr-auto min-h-full content-center'> {asignatura.nombre} </Typography>
            <button className={estiloBotonEliminar} onClick={manejarHabilitado}>{asignatura.habilitado ? 'Deshabilitar' : 'Habilitar'}</button>
        </li>
    );
}

export function ListaAsignaturas({asignaturasInicial}) {
    // TODO: Mostrar un mensaje si no hay asignaturas (habilitadas).
    // TODO: Mostrar un boton para guardar los cambios en caso de haber algun cambio.
    // TODO: Mostrar un boton para añadir una nueva asignatura.
    const {fechaDesde, fechaHasta} = useParams();
    const [asignaturas, setAsignaturas] = useState(asignaturasInicial)
    return (
        <ul className="[&>li]:mt-2 max-w-2xl m-auto">
            {asignaturas.map((asignatura) => {
                return <ItemAsignatura asignaturaInicial={asignatura} key={asignatura.id}/>
            })}

        </ul>
    );
}

ItemAsignatura.propTypes = {
    asignaturaInicial: PropTypes.shape({
        id: PropTypes.number.isRequired,
        nombre: PropTypes.string.isRequired,
        habilitado: PropTypes.bool.isRequired,
        aula: PropTypes.string,
        curso: PropTypes.string.isRequired,
        profesor: PropTypes.shape({
            nick: PropTypes.string.isRequired,
            color: PropTypes.string.isRequired,
            telefono: PropTypes.string.isRequired
        }).isRequired,
        horas: PropTypes.arrayOf(
            PropTypes.shape({
                dia: PropTypes.number.isRequired,
                hora: PropTypes.number.isRequired
            })
        ).isRequired
    }).isRequired
}
// Lista de asignaturas agrupadas por curso
ListaAsignaturas.propTypes =
    PropTypes.arrayOf(
        ItemAsignatura.propTypes
    ).isRequired

