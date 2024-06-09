import {Button, Card, CardBody, CardHeader, Tooltip, Typography} from "@material-tailwind/react";
import {MuiColorInput} from "mui-color-input";
import {useContext, useEffect, useState} from "react";
import {useNavigate, useParams} from "react-router-dom";
import AppGlobal from "../../../App.jsx";
import dayjs from 'dayjs';
import {DatePicker} from '@mui/x-date-pickers/DatePicker';
import {TimePicker} from '@mui/x-date-pickers/TimePicker';
import {AdapterDayjs} from "@mui/x-date-pickers/AdapterDayjs";
import {LocalizationProvider} from '@mui/x-date-pickers/LocalizationProvider';

export function AusenciaUsuario() {
    const {idProfesor} = useParams();
    const {token} = useContext(AppGlobal);
    const navigate = useNavigate();
    const [usuario, setUsuario] = useState({});
    const [fechaInicio, setFechaInicio] = useState(null);
    const [fechaFin, setFechaFin] = useState(null);
    const [horaInicio, setHoraInicio] = useState(null);
    const [horaFin, setHoraFin] = useState(null);


    useEffect(() => {
        fetch(`http://localhost:8000/profesor/${idProfesor}`, {
            method: 'GET', headers: {
                'Content-Type': 'application/json', 'Authorization': 'Bearer ' + token
            }
        }).then(async (response) => {
            if (response.status === 200) {
                const data = await response.json();
                setUsuario(data);
            } else {
                console.log('No se ha podido obtener el profesor');
            }
        })
    }, []);

    const handleCrearAusencia = () => {
        // Crear post a una url basada en http://localhost:8000/guardias?id_profesor=412685&fecha_inicio=2024-06-08&fecha_fin=2024-08-06&hora_inicio=09%3A20%3A00&hora_fin=10%3A20%3A00
        fetch(`http://localhost:8000/guardias?id_profesor=${idProfesor}&fecha_inicio=${fechaInicio}&fecha_fin=${fechaFin}&hora_inicio=${horaInicio}&hora_fin=${horaFin}`, {
            method: 'POST', headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + token
            }
        }).then(async (response) => {
                if (response.ok) {
                    navigate('/guardias');
                } else {
                    console.log('No se ha podido crear la ausencia');
                }
            }
        )
    }

    const handleCabioFecha = (date, setDate) => {
        // Change date format to 'YYYY-MM-DD'
        const formattedDate = date.format('YYYY-MM-DD');
        setDate(formattedDate);
    }
    const handleCabioHora = (hour, setHour) => {
        // Change hour format to 'HH:mm:ss'
        const formattedHour = hour.format('HH:mm:ss').replaceAll(':', '%3A');
        setHour(formattedHour);
    }

    const today = dayjs();
    const yesterday = today.subtract(1, 'day');
    const todayStartOfTheDay = today.startOf('day');
    console.log("fechaInicio")
    console.log(fechaInicio)
    console.log("fechaFin")
    console.log(fechaFin)
    console.log("horaInicio")
    console.log(horaInicio)
    console.log("horaFin")
    console.log(horaFin)
    const minDate = dayjs().startOf('day');
    const maxDate = dayjs().add(1, 'year').startOf('day');
    const minHour = dayjs().set('hour', 8).startOf('hour');
    const maxHour = dayjs().set('hour', 22).startOf('hour');
    return (<Card className='max-w-screen-2xl m-auto'>
        <CardHeader variant="gradient" color="gray" className='flex justify-center py-5 gap-2'>
            <Typography variant='h2' color="white" size="xl">Crear ausencia</Typography>
        </CardHeader>
        <CardBody className='text-center'>
            <div className='flex flex-col flex-wrap gap-5'>
                <div className='flex flex-wrap flex-row gap-2'>
                    <Typography variant='h4' color="black" size="xl">Usuario:</Typography>
                    <Typography variant='lead' color="black" size="xl"
                                className='mr-auto'>{usuario?.nombre ? usuario.nombre : 'No se ha podido obtener el usuario'}</Typography>
                </div>
                <div className='flex flex-wrap flex-row gap-2'>
                    <Typography variant='h4' color="black" size="xl">Fecha inicio:</Typography>
                    <LocalizationProvider dateAdapter={AdapterDayjs}>
                        <DatePicker
                            disablePast
                            views={['year', 'month', 'day']}
                            onChange={(date) => {
                                handleCabioFecha(date, setFechaInicio);
                            }}
                            minDate={minDate}
                            maxDate={maxDate}
                            className='sm:w-full md:w-1/3 lg:w-1/4'
                        />
                        <TimePicker
                            views={['hours', 'minutes']}
                            onChange={(hour) => {
                                handleCabioHora(hour, setHoraInicio);
                            }}
                            className='sm:w-full md:w-1/3 lg:w-1/4'
                            minTime={minHour}
                            maxTime={maxHour}
                        />

                    </LocalizationProvider>
                </div>
                <div className='flex flex-wrap flex-row gap-2'>
                    <Typography variant='h4' color="black" size="xl">Fecha fin:</Typography>
                    <LocalizationProvider dateAdapter={AdapterDayjs}>
                        <DatePicker
                            disablePast
                            views={['year', 'month', 'day']}
                            onChange={(date) => {
                                handleCabioFecha(date, setFechaFin);
                            }}
                            className='sm:w-full md:w-1/3 lg:w-1/4'
                            minDate={minDate}
                            maxDate={maxDate}
                        />
                        <TimePicker
                            views={['hours', 'minutes']}
                            onChange={(hour) => {
                                handleCabioHora(hour, setHoraFin);
                            }}
                            className='sm:w-full md:w-1/3 lg:w-1/4'
                            minTime={minHour}
                            maxTime={maxHour}
                        />

                    </LocalizationProvider>
                </div>

                <div className='flex flex-wrap flex-row lg:justify-end w-full gap-2'>
                    <Button color="red" ripple="light"
                            onClick={() => navigate('/profesor/' + idProfesor)}>Cancelar</Button>
                    <Button color="green" ripple="light" onClick={handleCrearAusencia}>Crear ausencia</Button>
                </div>
            </div>
        </CardBody>
    </Card>);
}