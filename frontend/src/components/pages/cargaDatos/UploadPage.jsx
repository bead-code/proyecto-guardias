import {EtiquetaPersonalizada} from "../../formField/EtiquetaPersonalizada.jsx";
import {useState} from "react";
import {useNavigate} from "react-router-dom";
import {styled} from '@mui/material/styles';
import Button from '@mui/material/Button';
import CloudUploadIcon from '@mui/icons-material/CloudUpload';


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
    // Limitar la longitud del nombre del fichero a mostrar
    const MAX_LENGTH = 20;
    const nombreFichero = fichero.name.length > MAX_LENGTH
        ? fichero.name.substring(0, MAX_LENGTH) + '...'
        : fichero.name;

    // Componente que muestra el nombre del fichero subido y permite eliminarlo
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
    // Manejar la eliminacion del fichero
    const handleRemove = () => {
        setFichero(null);
    }
    const handleFileChange = (event) => {
        const fileUploaded = event.target.files[0];
        console.log(fileUploaded)
        setFichero(fileUploaded);
        // handleFile(fileUploaded);
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

    const manejarSubida = (e) => {
        e.preventDefault();
        // enviar los ficheros al servidor mediante una peticion POST con application/json
        const formData = new FormData();
        formData.append('ficheroIds', ficheroIds);
        formData.append('ficheroRelaciones', ficheroRelaciones);
        fetch('http://localhost:8000/horario/upload_xml', {
            method: 'POST',
            body: formData
        }).then((res) => {
            if (res.ok) {
                console.log('Datos subidos correctamente');
            } else {
                console.error('Error al subir los datos');
            }
        }).catch((error) => {
            console.error('Error al subir los datos');
        });
        navigate("/");
    }


    return (<>
            <form onSubmit={manejarSubida}
                  className='flex flex-col gap-5 w-full max-w-xl m-auto bg-white shadow-md rounded p-8 items-center'>
                <div className='flex lg:flex-nowrap flex-wrap justify-center w-full gap-5'>
                    <InputFile texto={'Subir fichero de identificadores'} fichero={ficheroIds}
                               setFichero={setFicheroIds}/>
                    <InputFile texto={'Subir fichero de relaciones '} fichero={ficheroRelaciones}
                               setFichero={setFicheroRelaciones}/>
                </div>
                <Button type='submit' variant='outlined'
                        className='bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded w-1/2'>Cargar
                    datos
                </Button>
            </form>
        </>
    );
}