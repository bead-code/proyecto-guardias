import PropTypes from "prop-types";
import {useParams} from "react-router-dom";
import {useEffect, useState} from "react";


function ItemGuardia({guardiaInicial, eliminarGuardia, ...props}) {
    const [guardia, setGuardia] = useState(guardiaInicial)
    const manejarEliminar = (id) => {
        eliminarGuardia(id)
    }
    return (
        <li className="flex px-5 w-full bg-amber-100 shadow" {...props}>
            <h2 className='mr-auto text-pretty'> {guardia.nombre} </h2>
            <button className='text-red-700 font-medium rounded-lg text-sm p-2 m-2 text-center outline-2 outline-red-700 outline hover:outline-none hover:bg-red-700 hover:text-white transition-none delay-0' onClick={() => (manejarEliminar(guardia.id))}>Eliminar</button>
        </li>
    );
}

export function ListaGuardias() {
    // recibir parametro opcional de la url
    const {id} = useParams()
    const [guardias, setGuardias] = useState([])
    useEffect(() => {
        fetch(`http://localhost:8080/guardias`)
            .then(res => res.json())
            .then(data => {
                setGuardias(data)
            })
    }, [id])


    return (
        <div>
            <h1>Lista de guardias</h1>
            <ul className="mt-2 max-w-2xl m-auto">
                {guardias.map((guardia) => {
                    return <ItemGuardia guardiaInicial={guardia} key={guardia.id}/>
                })}
            </ul>
        </div>
    )
}

ItemGuardia.propTypes = {
    guardiaInicial: PropTypes.shape({
        id: PropTypes.number.isRequired,
        nombre: PropTypes.string.isRequired,
    }).isRequired
}
// Lista de guardias
ListaGuardias.propTypes =
    PropTypes.arrayOf(
        ItemGuardia.propTypes
    ).isRequired