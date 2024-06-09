import FullCalendar from '@fullcalendar/react'
import dayGridPlugin from '@fullcalendar/daygrid' // a plugin!
import interactionPlugin from "@fullcalendar/interaction"
import {useEffect, useState} from "react";
import {useNavigate} from "react-router-dom";

export function Calendario() {
    const navigate = useNavigate();
    const [guardias, setGuardias] = useState([])
    useEffect(() => {
        fetch(`http://localhost:8000/guardias/all`)
            .then(res => res.json())
            .then(data => {
                setGuardias(data)
            })
    }, [])
    let eventosGuardias = guardias.map((guardia) => {
        let color = 'green';
        if (guardia.profesor_sustituto.id_profesor === 9999) {
            color = 'red';
        }
        // return {
        //     title: guardia.profesor.nombre,
        //     date: guardia.fecha,
        //     url: `http://localhost:5173/guardias/${guardia.fecha}/tramo/${guardia.tramo_horario.id_tramo_horario}/profesor/${guardia.profesor.id_profesor}`,
        //     color: color
        // }
        return {
            title: guardia.profesor.nombre,
            start: guardia.fecha + ' ' + guardia.tramo_horario.hora_inicio,
            end: guardia.fecha + ' ' + guardia.tramo_horario.hora_fin,
            extendedProps : {
                url: `/guardias/${guardia.fecha}/tramo/${guardia.tramo_horario.id_tramo_horario}/profesor/${guardia.profesor.id_profesor}`
            },
            color: color
        }
    })
    return (
        <div className='max-w-4xl max-h-[calc(100vh-300px)] mx-auto'>
            <FullCalendar

                plugins={[dayGridPlugin, interactionPlugin]}
                weekends={false}
                events={eventosGuardias}
                eventClick={ (info) => {
                    console.log(info.event.extendedProps.url)
                    navigate(info.event.extendedProps.url)
                }
                }
            />
        </div>
    )
}