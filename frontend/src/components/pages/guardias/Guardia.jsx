import {mostrarToast} from "../../../utils/Notificaciones.js";
import Select from '@mui/material/Select';
import {useNavigate, useParams} from "react-router-dom";
import {toast} from "react-toastify";
import {useContext, useEffect, useRef, useState} from "react";
import AppGlobal from "../../../App.jsx";
import {Button, Card, CardBody, CardHeader, Typography} from "@material-tailwind/react";
import {AvatarModificado} from "../../usuarios/AvatarModificado.jsx";
import {Box, FormControl, InputLabel, MenuItem} from "@mui/material";
import CircularProgress from "@mui/material/CircularProgress";

export function Guardia() {
    const {fecha, tramoHorario, idProfesor} = useParams();
    const {decodeToken, token} = useContext(AppGlobal);
    const campoSustituto = useRef();
    const [guardia, setGuardia] = useState(undefined);
    const [profesorAsignadoModificado, setProfesorAsignadoModificado] = useState(null);
    const [profesoresDisponibles, setProfesoresDisponibles] = useState([]);
    const navigate = useNavigate();
    useEffect(() => {
        fetch(`http://localhost:8000/guardias?id_profesor=${idProfesor}&fecha=${fecha}&id_tramo_horario=${tramoHorario}`, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
                Authorization: `Bearer ${token}`
            }
        })
            .then(async (res) => {
                const data = await res.json();
                if (res.ok) {
                    setGuardia(data);
                    setProfesorAsignadoModificado(data.profesor_sustituto?.id_profesor ?? 9999);
                } else {
                    mostrarToast("Error al cargar la guardia", "error");
                }
            });

        fetch(`http://localhost:8000/profesor/disponible?fecha=${fecha}&id_tramo_horario=${tramoHorario}`, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
                Authorization: `Bearer ${token}`
            }
        })
            .then(async (res) => {
                const data = await res.json();
                if (res.ok) {
                    setProfesoresDisponibles(data);
                } else {
                    mostrarToast("Error al cargar los profesores disponibles", "error");
                }
            });
    }, [token]);

    if (!guardia) {
        return (
            <Card className='max-w-4xl max-h-[calc(100vh-300px)] m-auto'>
                <CardHeader variant='gradient' color='gray'>
                    <Typography variant='h2' className='p-3'>Guardia</Typography>
                </CardHeader>
                <CardBody className='gap-5 flex-grow justify-between'>
                    <CircularProgress/>
                </CardBody>
            </Card>);
    }

    const handleCambioProfesorSustituto = (event) => {
        const profesor = event.target.value;
        setProfesorAsignadoModificado(profesor);
    };

    const actualizarGuardia = (nuevoProfesor) => {
        let profesorSustituto = profesoresDisponibles.find((profesor) => profesor.id_profesor === nuevoProfesor);
        setGuardia({
            ...guardia,
            profesor_sustituto: profesorSustituto ? profesorSustituto : 9999
        });
    };

    const manejarAceptar = () => {
        actualizarGuardia(profesorAsignadoModificado);

        const toastGuardia = toast.loading('Procesando petición de tomar la guardia', {position: "bottom-right"});

        fetch(`http://localhost:8000/guardias/${guardia.id_calendario}?id_profesor_sustituto=${profesorAsignadoModificado ?? 9999}`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
                Authorization: `Bearer ${token}`
            }
        })
            .then((res) => {
                    if (!res.ok) {
                        throw new Error('Error al asignar la guardia');
                    }
                    if (profesorAsignadoModificado === 9999) {
                        toast.update(toastGuardia, {
                            render: 'Guardia desasignada',
                            type: 'success',
                            isLoading: false,
                            autoClose: 3000,
                        });
                    } else {
                        toast.update(toastGuardia, {
                            render: 'Guardia asignada',
                            type: 'success',
                            isLoading: false,
                            autoClose: 3000,
                        });
                    }
                    navigate('/guardias');
                }
            )
            .catch(() => {
                toast.update(toastGuardia, {
                    render: 'Error al asignar la guardia',
                    type: 'error',
                    isLoading: false,
                    autoClose: 3000,
                });
            });
    };

    const manejarRechazar = () => {
        setProfesorAsignadoModificado(guardia.profesor_sustituto?.id_profesor || 9999);
    };

    const formatoFecha = new Date(guardia.fecha).toLocaleDateString();
    const porcentaje = -50;
    const textoPorcentaje =
        porcentaje > 0
            ? `Llevas un ${Math.abs(porcentaje)}% de guardias más que la media del grupo de guardias. ¿Quieres aceptarla?`
            : `Llevas ${Math.abs(porcentaje)}% de guardias menos que la media del grupo de guardias. ¿Quieres aceptarla?`;

    console.log('guardia.profesor_sustituto?.id_profesor')
    console.log(guardia.profesor_sustituto?.id_profesor ?? 'yippie')
    console.log(profesorAsignadoModificado)


    return (
        <Card className='max-w-4xl lg:max-h-[calc(100vh-300px)] m-auto'>
            <CardHeader variant='gradient' color='gray'>
                <Typography variant='h2' className='p-3'>Guardia</Typography>
            </CardHeader>
            <CardBody className='gap-5 flex-grow justify-between'>
                <Typography variant='lead' className='text-left'><b>Día:</b> {formatoFecha}</Typography>
                <Typography variant='lead'
                            className='text-left'><b>Hora:</b> {guardia.tramo_horario.hora_inicio} - {guardia.tramo_horario.hora_fin}
                </Typography>
                <Typography variant='lead' className='text-left'><b>Aula:</b> {guardia.aula.nombre}</Typography>
                <Typography variant='lead' className='text-left'><b>Curso:</b> {guardia.curso.nombre}</Typography>
                <div className='flex flex-wrap gap-3 place-items-center h-24'>
                    <Typography variant='lead' className='text-left flex gap-4 place-items-center'><b>Profesor
                        ausente:</b></Typography>
                    <AvatarModificado className='inline' profesor={guardia.profesor}/>
                </div>
                <div className='flex flex-wrap gap-3 place-items-center'>
                    <Typography variant='lead' className='text-left flex gap-4 place-items-center min-w-44'><b>Profesor
                        sustituto:</b></Typography>
                    <FormControl className='max-w-96'>
                        <InputLabel id="etiqueta">Sustituto</InputLabel>
                        <Select
                            ref={campoSustituto}
                            labelId="etiqueta"
                            label="Sustituto"
                            value={profesorAsignadoModificado}
                            onChange={handleCambioProfesorSustituto}
                        >
                            <MenuItem className='h-16' value={9999}>Sin asignar</MenuItem>
                            {profesoresDisponibles.map((profesor) => (
                                <MenuItem className='h-16' value={profesor.id_profesor} key={profesor.id_profesor}>
                                    <AvatarModificado disableOnClick className='inline' profesor={profesor}/>
                                </MenuItem>
                            ))}
                        </Select>
                    </FormControl>
                </div>
                {(profesorAsignadoModificado ?? 9999) !== (guardia.profesor_sustituto?.id_profesor ?? 9999) && (
                    <div className='flex gap-3 place-items-center justify-end h-20 w-full'>
                        <Button variant='filled' color='red' onClick={manejarRechazar}>Cancelar</Button>
                        <Button variant='filled' color='green' onClick={manejarAceptar}>Confirmar</Button>
                    </div>
                )}
            </CardBody>
        </Card>
    );
}
