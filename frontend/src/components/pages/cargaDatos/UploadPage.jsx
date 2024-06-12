import {EtiquetaPersonalizada} from "../../camposFormulario/EtiquetaPersonalizada.jsx";
import {useContext, useState} from "react";
import {useNavigate} from "react-router-dom";
import {styled} from '@mui/material/styles';
import Button from '@mui/material/Button';
import CloudUploadIcon from '@mui/icons-material/CloudUpload';
import AppGlobal from "../../../App.jsx";
import {toast} from "react-toastify";
import {mostrarToast} from "../../../utils/Notificaciones.js";

const VisuallyHiddenInput = styled('input')({
    clip: 'rect(0 0 0 0)',
    clipPath: 'inset(50%)',
    height: 1,
    overflow: 'hidden',
    position: 'absolute',
    bottom: 0,
    left: 0,
    whiteSpace: 'nowrap',
    width: 1,
});

function FileShow({fichero, handleRemove}) {
    const MAX_LENGTH = 20;
    const nombreFichero = fichero.name.length > MAX_LENGTH
        ? fichero.name.substring(0, MAX_LENGTH) + '...'
        : fichero.name;

    return (
        <div className='flex gap-2 justify-between items-center'>
            <span>{nombreFichero}</span>
            <Button variant='outlined' color='error'
                    onClick={handleRemove}>Eliminar
            </Button>
        </div>
    )
}

function InputFile({texto, fichero, setFichero, props}) {
    const handleRemove = () => {
        setFichero(null);
    }
    const handleFileChange = (event) => {
        const fileUploaded = event.target.files[0];
        console.log(fileUploaded)
        setFichero(fileUploaded);
    };
    return (
        <div className={'flex flex-col lg:w-1/2 w-full gap-2 min-h-full justify-between'}>
            <EtiquetaPersonalizada>{texto}</EtiquetaPersonalizada>
            {fichero
                ? <FileShow fichero={fichero} handleRemove={handleRemove}/>
                : <Button
                    component="label"
                    role={undefined}
                    variant="contained"
                    tabIndex={-1}
                    startIcon={<CloudUploadIcon/>}
                >
                    Upload file
                    <VisuallyHiddenInput type="file" onChange={handleFileChange}/>
                </Button>}
        </div>
    )
}

export function UploadPage({handleFile}) {
    const [ficheroIds, setFicheroIds] = useState(null);
    const [ficheroRelaciones, setFicheroRelaciones] = useState(null);
    const navigate = useNavigate();
    const {token} = useContext(AppGlobal);
    let toastUpload = null;

    const manejarSubida = (e) => {
        e.preventDefault();

        if (!ficheroIds || !ficheroRelaciones) {
            mostrarToast('Debes subir ambos ficheros', 'error');
            return;
        }

        const formData = new FormData();
        formData.append('tablas', ficheroIds);
        formData.append('calendario', ficheroRelaciones);

        toastUpload = toast.loading('Procesando subida de información', {position: "bottom-right"});

        fetch('http://localhost:8000/calendario/generar_calendario/', {
            method: 'POST',
            headers: {
                'Authorization': 'Bearer ' + token
            },
            body: formData
        }).then((res) => {
            if (res.ok) {
                console.log('Datos subidos correctamente');
                navigate("/");
                toast.update(toastUpload, {
                    render: 'Datos subidos correctamente',
                    type: 'success',
                    isLoading: false,
                    autoClose: 3000,
                });
            } else {
                console.error('Error al subir los datos');
                toast.update(toastUpload, {
                    render: 'Error al subir los datos',
                    type: 'error',
                    isLoading: false,
                    autoClose: 3000,
                });
            }
        }).catch((error) => {
            console.error('Error al subir los datos', error);
            toast.update(toastUpload, {
                render: 'Error al subir los datos',
                type: 'error',
                isLoading: false,
                autoClose: 3000,
            });
        });
    }

    return (
        <>
            <form onSubmit={manejarSubida}
                  className='flex flex-col gap-5 w-full max-w-xl m-auto bg-white shadow-md rounded p-8 items-center'>
                <div className='flex lg:flex-nowrap flex-wrap justify-center w-full gap-5'>
                    <InputFile texto={'Subir fichero de identificadores'} fichero={ficheroIds}
                               setFichero={setFicheroIds}/>
                    <InputFile texto={'Subir fichero de relaciones '} fichero={ficheroRelaciones}
                               setFichero={setFicheroRelaciones}/>
                </div>
                <Button type='submit' variant='outlined'
                        className='bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded w-1/2'>
                    Cargar datos
                </Button>
            </form>
        </>
    );
}
