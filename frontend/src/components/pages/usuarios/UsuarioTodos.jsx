import { ListaProfesores } from "../../listas/ListaProfesores.jsx";
import PropTypes from "prop-types";

/**
 * Componente que renderiza una lista de todos los usuarios.
 */
export function UsuarioTodos() {
    return (
        <ListaProfesores />
    );
}

UsuarioTodos.propTypes = {
    // Puedes definir prop types si este componente espera recibir propiedades
};
