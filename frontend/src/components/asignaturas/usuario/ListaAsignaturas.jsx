import PropTypes from 'prop-types';


function ItemAsignatura({ asignatura }) {
    return (
        <li >{asignatura.nombre}</li>
    );
}
export function ListaAsignaturas({asignaturas}) {
  return (
      <ul>
          {asignaturas.map((asignatura) => {
              return <ItemAsignatura asignatura={asignatura} key={asignatura.id} />
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
