import PropTypes from 'prop-types';


function ItemAsignatura({ asignatura, ...props}) {
    return (
        <li className="flex justify-between px-5 w-full bg-amber-100 shadow" {...props}>
            <h2> {asignatura.nombre} </h2>
            <select className="bg-transparent [&>option]:bg-transparent" name="cars" id="cars">
                <option value="volvo">Volvo</option>
                <option value="saab">Saab</option>
                <option value="opel">Opel</option>
                <option value="audi">Audi</option>
            </select>
            {esHabilitado
            ? <input type="checkbox" onClick={manejarHabilitado} ></input>
            : <input type="checkbox" onClick={manejarHabilitado} checked ></input>
            }
        </li>
    );
}

export function ListaAsignaturas({asignaturas}) {
    return (
        <ul className="[&>li]:mt-2 max-w-2xl m-auto">
            {asignaturas.map((asignatura) => {
                return <ItemAsignatura asignatura={asignatura} key={asignatura.id}/>
          })}

      </ul>
  );
}
ItemAsignatura.propTypes = {
    asignatura: PropTypes.shape({
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
ListaAsignaturas.propTypes = PropTypes.arrayOf(
    ItemAsignatura.propTypes
).isRequired
