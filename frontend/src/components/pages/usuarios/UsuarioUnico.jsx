import {useContext, useEffect, useRef, useState} from "react";
import {useNavigate, useParams} from "react-router-dom";
import AppGlobal from "../../../App.jsx";
import {Button, Card, CardBody, CardHeader, Tooltip, Typography} from "@material-tailwind/react";
import EditIcon from "@mui/icons-material/Edit.js";
import DoneIcon from "@mui/icons-material/Done.js";
import CloseIcon from "@mui/icons-material/Close.js";
import {mostrarToast} from "../../../utils/Notificaciones.js";
import CircularProgress from '@mui/material/CircularProgress';
import {MuiColorInput, matchIsValidColor} from 'mui-color-input'


export function UsuarioUnico({defaultUser = undefined, modify = false, ...prop}) {
    const [isEditedColor, setIsEditedColor] = useState(false);
    const [isEditingUsername, setIsEditingUsername] = useState(false);
    const [isEditingName, setIsEditingName] = useState(false);
    const [usuario, setUsuario] = useState(defaultUser);
    const [color, setColor] = useState(usuario?.color || '');
    const {idProfesor} = useParams();
    const {token} = useContext(AppGlobal);
    const usernameField = useRef(null);
    const nameField = useRef(null);
    const colorEditer = useRef(null);
    const navigate = useNavigate();

    useEffect(() => {
        if (!usuario) {
            fetch(`http://localhost:8000/profesor/${idProfesor}`, {
                method: 'GET', headers: {
                    'Content-Type': 'application/json', 'Authorization': 'Bearer ' + token,
                }
            })
                .then((response) => response.json())
                .then((data) => {
                    setUsuario(data);
                    setColor(data.color);
                });
        }
    }, [usuario, idProfesor, token]);

    // Page that shows the information of a single user (profesor)
    if (!usuario) {
        return (
            <Card className='max-w-screen-2xl m-auto'>
                <CardHeader variant="gradient" color="gray" className='flex justify-center py-5 gap-2'>
                    <Typography variant='h2' color="white" size="xl" ref={usernameField}>Usuario</Typography>
                </CardHeader>
                <CardBody className='text-center'>
                    <CircularProgress/>
                </CardBody>
            </Card>
        );
    }

    const handleSaveUser = (valueToChange, setEditingFunction) => {
        setEditingFunction(false);
        fetch(`http://localhost:8000/profesor/${idProfesor}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + token,
            },
            body: JSON.stringify(valueToChange)
        }).then((response) => {
            if (!response.ok) {
                console.log("Error al actualizar el usuario");
                mostrarToast(`No se ha podido actualizar el usuario`, 'error');
                setUsuario({...usuario});  // Reset to previous state
            } else {
                mostrarToast(`Usuario actualizado correctamente`, 'success');
            }
        }).catch((error) => {
            console.log("Error al actualizar el usuario");
            mostrarToast(`No se ha podido actualizar el usuario`, 'error');
            setUsuario({...usuario});  // Reset to previous state
            setEditingFunction(true);
        });
        setUsuario({...usuario, ...valueToChange});
    }

    const handleInputColor = (color) => {
        if (!matchIsValidColor(color)) {
            mostrarToast(`El color no es válido`, 'error');
            return;
        }
        setColor(color);
        setIsEditedColor(true);
    }

    const handleSaveColor = () => {
        handleSaveUser({color: color}, setIsEditedColor);
    }
    return (
        <Card className='max-w-screen-2xl m-auto'>
            <CardHeader variant="gradient" color="gray" className='flex justify-center py-5 gap-2'>
                <Typography variant='h2' color="white" size="xl" ref={usernameField}>Usuario</Typography>
            </CardHeader>
            <CardBody className='text-center'>
                <div className="flex flex-col gap-4">
                    <div className='flex flex-wrap flex-row gap-2'>
                        <Typography variant='h4' color="black" size="xl">Nombre de usuario:</Typography>
                        <Typography variant='lead' color="black" size="xl" className='mr-auto'
                                    ref={usernameField}>{usuario.username ? usuario.username : 'No asignado'}</Typography>
                        {modify ? (isEditingUsername ?
                                <div className='flex gap-2'>
                                    <Tooltip content="Cancelar">
                                        <Button
                                            onClick={() => {
                                                usernameField.current.contentEditable = 'false';
                                                setIsEditingUsername(false);
                                                usernameField.current.innerText = usuario.username ? usuario.username : 'No asignado';
                                            }}
                                            color="red"
                                            size='lg'
                                            variant='text'
                                        >
                                            <CloseIcon/>
                                        </Button>
                                    </Tooltip>
                                    <Tooltip content="Guardar">
                                        <Button
                                            onClick={() => {
                                                handleSaveUser({username: usernameField.current.innerText}, setIsEditingUsername)
                                            }}
                                            color="green"
                                            size='lg'
                                            variant='text'
                                        >
                                            <DoneIcon/>
                                        </Button>
                                    </Tooltip>
                                </div> : <Tooltip content="Editar">
                                    <Button
                                        onClick={() => {
                                            usernameField.current.contentEditable = 'true';
                                            setIsEditingUsername(true);
                                            usernameField.current.focus();
                                        }}
                                        size='lg'
                                        variant='text'
                                    >
                                        <EditIcon/>
                                    </Button>
                                </Tooltip>)
                            : <></>}
                    </div>
                    <div className='flex flex-wrap flex-row gap-2'>
                        <Typography variant='h4' color="black" size="xl">Nombre:</Typography>
                        <Typography variant='lead' color="black" size="xl" className='mr-auto'
                                    ref={nameField}>{usuario.nombre}</Typography>
                        {modify ? (isEditingName ?
                                <div className='flex gap-2'>
                                    <Tooltip content="Cancelar">
                                        <Button
                                            onClick={() => {
                                                nameField.current.contentEditable = 'false';
                                                setIsEditingName(false);
                                                nameField.current.innerText = usuario.nombre;
                                            }}
                                            color="red"
                                            size='lg'
                                            variant='text'
                                        >
                                            <CloseIcon/>
                                        </Button>
                                    </Tooltip>
                                    <Tooltip content="Guardar">
                                        <Button
                                            onClick={() => {
                                                handleSaveUser({nombre: nameField.current.innerText}, setIsEditingName)
                                            }}
                                            color="green"
                                            size='lg'
                                            variant='text'
                                        >
                                            <DoneIcon/>
                                        </Button>
                                    </Tooltip>
                                </div> : <Tooltip content="Editar">
                                    <Button
                                        onClick={() => {
                                            nameField.current.contentEditable = 'true';
                                            setIsEditingName(true);
                                            nameField.current.focus();
                                        }}
                                        size='lg'
                                        variant='text'
                                    >
                                        <EditIcon/>
                                    </Button>
                                </Tooltip>)
                            : <></>}
                    </div>
                    <div className='flex flex-wrap flex-row gap-2'>
                        <Typography variant='h4' color="black" size="xl">Cargo:</Typography>
                        <Typography variant='lead' color="black" size="xl"
                                    className='mr-auto capitalize'>{usuario.rol.nombre}</Typography>
                    </div>
                    <div className='flex flex-wrap flex-row gap-2'>
                        {modify ?
                            <MuiColorInput value={color} onChange={handleInputColor} format="hex" ref={colorEditer}/> :
                            <MuiColorInput value={color} onChange={handleInputColor} format="hex" ref={colorEditer}
                                           disabled/>}
                        {modify ? (isEditedColor && <>
                                <Tooltip content="Cancelar">
                                    <Button
                                        onClick={() => {
                                            setIsEditedColor(false);
                                            setColor(usuario.color);
                                        }}
                                        color="red"
                                        size='lg'
                                        variant='text'
                                    >
                                        <CloseIcon/>
                                    </Button>
                                </Tooltip>
                                <Tooltip content="Guardar">
                                    <Button
                                        onClick={handleSaveColor}
                                        color="green"
                                        size='lg'
                                        variant='text'
                                    >
                                        <DoneIcon/>
                                    </Button>
                                </Tooltip>
                            </>)
                            : <></>}
                    </div>
                    <div className='flex flex-wrap flex-row gap-2 justify-end'>
                        <Button color="red" onClick={() => navigate(`/ausencia/crear/${idProfesor}`)}>
                            Crear ausencia
                        </Button>
                    </div>
                </div>
            </CardBody>
        </Card>
    );
}
