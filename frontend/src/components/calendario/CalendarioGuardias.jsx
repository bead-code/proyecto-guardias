import FullCalendar from '@fullcalendar/react';
import dayGridPlugin from '@fullcalendar/daygrid'; // a plugin!
import timeGridPlugin from '@fullcalendar/timegrid'; // for week and day views
import interactionPlugin from "@fullcalendar/interaction";
import { useContext, useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import esLocale from '@fullcalendar/core/locales/es';
import AppGlobal from "../../App.jsx";

export function CalendarioGuardias() {
    const navigate = useNavigate();
    const { token } = useContext(AppGlobal);
    const [guardias, setGuardias] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchGuardias = async () => {
            try {
                const response = await fetch(`http://localhost:8000/guardias/all`, {
                    method: 'GET',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': 'Bearer ' + token
                    }
                });
                if (!response.ok) {
                    throw new Error('Error al obtener los datos de guardias');
                }
                const data = await response.json();
                setGuardias(data);
                setLoading(false);
            } catch (error) {
                console.error(error);
                setLoading(false);
            }
        };
        fetchGuardias();
    }, [token]);

    const handleEventClick = (info) => {
        console.log(info.event.extendedProps.url);
        navigate(info.event.extendedProps.url);
    };

    let eventosGuardias = guardias.map((guardia) => {
        let color = 'green';
        if (guardia.profesor_sustituto.id_profesor === 9999) {
            color = 'orange';
        }

        return {
            title: guardia.profesor.nombre,
            start: guardia.fecha + ' ' + guardia.tramo_horario.hora_inicio,
            end: guardia.fecha + ' ' + guardia.tramo_horario.hora_fin,
            extendedProps: {
                url: `/guardias/${guardia.fecha}/tramo/${guardia.tramo_horario.id_tramo_horario}/profesor/${guardia.profesor.id_profesor}`
            },
            color: color
        };
    });

    return (
        <div className='max-w-4xl max-h-[calc(100vh-300px)] mx-auto'>
            {loading ? (
                <p>Cargando...</p>
            ) : (
                <FullCalendar
                    height={'calc(100vh - 300px)'}
                    initialView={'dayGridMonth'}
                    plugins={[dayGridPlugin, timeGridPlugin, interactionPlugin]}
                    headerToolbar={{
                        left: 'prev,next today',
                        center: 'title',
                        right: 'dayGridMonth,timeGridWeek,timeGridDay'
                    }}
                    weekends={false}
                    events={eventosGuardias}
                    eventClick={handleEventClick}
                    locales={esLocale}
                    locale={'es'}
                />
            )}
        </div>
    );
}
