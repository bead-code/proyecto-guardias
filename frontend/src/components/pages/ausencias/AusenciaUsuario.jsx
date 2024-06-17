import {
    Button,
    Card,
    CardBody,
    CardHeader,
    Typography,
} from "@material-tailwind/react";
import {useContext, useEffect, useState} from "react";
import {useNavigate, useParams} from "react-router-dom";
import {AppGlobal} from "../../../App.jsx";
import dayjs from "dayjs";
import {DatePicker, TimePicker} from "@mui/x-date-pickers";
import {AdapterDayjs} from "@mui/x-date-pickers/AdapterDayjs";
import {LocalizationProvider} from "@mui/x-date-pickers/LocalizationProvider";
import {mostrarToast} from "../../../utils/Notificaciones.js";

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
        const fetchUsuario = async () => {
            try {
                const response = await fetch(`http://192.168.1.94:8000/profesor/${idProfesor}`, {
                    method: "GET",
                    headers: {
                        "Content-Type": "application/json",
                        Authorization: "Bearer " + token,
                    },
                });
                if (response.ok) {
                    const data = await response.json();
                    setUsuario(data);
                } else {
                    console.log("No se ha podido obtener el profesor");
                }
            } catch (error) {
                console.error("Error:", error);
                mostrarToast("No se ha podido obtener el profesor", "error");
            }
        };
        fetchUsuario();
    }, [idProfesor, token]);

    const handleCrearAusencia = async () => {
        try {
            const startDateTime = dayjs(`${fechaInicio}T${horaInicio}`);
            const endDateTime = dayjs(`${fechaFin}T${horaFin}`);

            if (!fechaInicio || !fechaFin || !horaInicio || !horaFin) {
                mostrarToast("Rellena todos los campos", "error");
                return;
            }

            if (startDateTime.isAfter(endDateTime)) {
                mostrarToast("La fecha de inicio no puede ser mayor a la fecha de fin", "error");
                return;
            }

            const queryParams = new URLSearchParams({
                id_profesor: idProfesor,
                fecha_inicio: fechaInicio,
                fecha_fin: fechaFin,
                hora_inicio: horaInicio,
                hora_fin: horaFin,
            }).toString();

            const response = await fetch(`http://192.168.1.94:8000/guardias?${queryParams}`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    Authorization: "Bearer " + token,
                },
            });

            if (response.ok) {
                navigate("/guardias");
            } else {
                mostrarToast("No se ha podido crear la ausencia", "error");
            }
        } catch (error) {
            console.error("Error:", error);
            mostrarToast("No se ha podido crear la ausencia", "error");
        }
    };

    const handleCambiarFecha = (date, setDate) => {
        if (date) {
            const formattedDate = date.format("YYYY-MM-DD");
            setDate(formattedDate);
        }
    };

    const handleCambiarHora = (hour, setHour) => {
        if (hour) {
            const formattedHour = hour.format("HH:mm:ss");
            setHour(formattedHour);
        }
    };

    const minDate = dayjs().startOf("day");
    const maxDate = dayjs().add(1, "year").startOf("day");
    const minHour = dayjs().set("hour", 8).startOf("hour");
    const maxHour = dayjs().set("hour", 22).startOf("hour");

    return (
        <Card className="max-w-screen-2xl m-auto">
            <CardHeader variant="gradient" color="gray" className="flex justify-center py-5 gap-2">
                <Typography variant="h2" color="white" size="xl">
                    Crear ausencia
                </Typography>
            </CardHeader>
            <CardBody className="text-center">
                <div className="flex flex-col flex-wrap gap-5">
                    <div className="flex flex-wrap flex-row gap-2">
                        <Typography variant="h4" color="black" size="xl">
                            Usuario:
                        </Typography>
                        <Typography variant="lead" color="black" size="xl" className="mr-auto">
                            {usuario?.nombre || "No se ha podido obtener el usuario"}
                        </Typography>
                    </div>
                    <div className="flex flex-wrap flex-row gap-2">
                        <Typography variant="h4" color="black" size="xl">
                            Fecha inicio:
                        </Typography>
                        <LocalizationProvider dateAdapter={AdapterDayjs}>
                            <DatePicker
                                disablePast
                                views={["year", "month", "day"]}
                                onChange={(date) => handleCambiarFecha(date, setFechaInicio)}
                                minDate={minDate}
                                maxDate={maxDate}
                                className="sm:w-full md:w-1/3 lg:w-1/4"
                            />
                            <TimePicker
                                views={["hours", "minutes"]}
                                onChange={(hour) => handleCambiarHora(hour, setHoraInicio)}
                                className="sm:w-full md:w-1/3 lg:w-1/4"
                                minTime={minHour}
                                maxTime={maxHour}
                            />
                        </LocalizationProvider>
                    </div>
                    <div className="flex flex-wrap flex-row gap-2">
                        <Typography variant="h4" color="black" size="xl">
                            Fecha fin:
                        </Typography>
                        <LocalizationProvider dateAdapter={AdapterDayjs}>
                            <DatePicker
                                disablePast
                                views={["year", "month", "day"]}
                                onChange={(date) => handleCambiarFecha(date, setFechaFin)}
                                minDate={minDate}
                                maxDate={maxDate}
                                className="sm:w-full md:w-1/3 lg:w-1/4"
                            />
                            <TimePicker
                                views={["hours", "minutes"]}
                                onChange={(hour) => handleCambiarHora(hour, setHoraFin)}
                                className="sm:w-full md:w-1/3 lg:w-1/4"
                                minTime={minHour}
                                maxTime={maxHour}
                            />
                        </LocalizationProvider>
                    </div>
                    <div className="flex flex-wrap flex-row lg:justify-end w-full gap-2">
                        <Button color="red" onClick={() => navigate("/profesor/" + idProfesor)}>
                            Cancelar
                        </Button>
                        <Button color="green" onClick={handleCrearAusencia}>
                            Confirmar ausencia
                        </Button>
                    </div>
                </div>
            </CardBody>
        </Card>
    );
}
