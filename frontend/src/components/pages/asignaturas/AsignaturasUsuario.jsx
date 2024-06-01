import {useParams} from "react-router-dom";
import {ListaAsignaturas} from "../../listas/ListaAsignaturas.jsx";

const mockAsignaturas = [
    {
        id: 2,
        nombre: "Matematicas",
        habilitado: true,
        aula: "A001",
        curso: "1ESO",
        profesor: {
            nick: "profesor1",
            color: "#FF0000",
            telefono: "123456789"
        },
        horas: [
            {
                dia: 1,
                hora: 1
            },
            {
                dia: 2,
                hora: 2
            }
        ]
    },
    {
        id: 3,
        nombre: "Lengua",
        habilitado: true,
        aula: "A002",
        curso: "1ESO",
        profesor: {
            nick: "profesor1",
            color: "#FF0000",
            telefono: "123456789"
        },
        horas: [
            {
                dia: 1,
                hora: 2
            },
            {
                dia: 2,
                hora: 1
            }
        ]
    },
    {
        id: 4,
        nombre: "Ingles",
        habilitado: false,
        aula: "A003",
        curso: "1ESO",
        profesor: {
            nick: "profesor1",
            color: "#FF0000",
            telefono: "123456789"
        },
        horas: [
            {
                dia: 1,
                hora: 3
            },
            {
                dia: 2,
                hora: 3
            }
        ]
    },
    {
        id: 5,
        nombre: "Fisica",
        habilitado: true,
        aula: "A004",
        curso: "1ESO",
        profesor: {
            nick: "profesor1",
            color: "#FF0000",
            telefono: "123456789"
        },
        horas: [
            {
                dia: 1,
                hora: 4
            },
            {
                dia: 2,
                hora: 4
            }
        ]
    },
    {
        id: 6,
        nombre: "Quimica",
        habilitado: true,
        aula: "A005",
        curso: "1ESO",
        profesor: {
            nick: "profesor1",
            color: "#FF0000",
            telefono: "123456789"
        },
        horas: [
            {
                dia: 1,
                hora: 5
            },
            {
                dia: 2,
                hora: 5
            }
        ]
    },
    {
        id: 7,
        nombre: "Biologia",
        habilitado: true,
        aula: "A006",
        curso: "1ESO",
        profesor: {
            nick: "profesor1",
            color: "#FF0000",
            telefono: "123456789"
        },
        horas: [
            {
                dia: 1,
                hora: 6
            },
            {
                dia: 2,
                hora: 6
            }
        ]
    },
    {
        id: 8,
        nombre: "Historia",
        habilitado: true,
        aula: "A007",
        curso: "1ESO",
        profesor: {
            nick: "profesor1",
            color: "#FF0000",
            telefono: "123456789"
        },
        horas: [
            {
                dia: 1,
                hora: 7
            },
            {
                dia: 2,
                hora: 7
            }
        ]
    },
    {
        id: 9,
        nombre: "Geografia",
        habilitado: true,
        aula: "A008",
        curso: "1ESO",
        profesor: {
            nick: "profesor1",
            color: "#FF0000",
            telefono: "123456789"
        },
        horas: [
            {
                dia: 1,
                hora: 8
            },
            {
                dia: 2,
                hora: 8
            }
        ]
    },
]

export function AsignaturasUsuario () {
    const { idUsuario } = useParams()
    return(
    <>
        <h1> Usuario {idUsuario}</h1>
        <ListaAsignaturas asignaturasInicial={mockAsignaturas}/>
    </>)
}