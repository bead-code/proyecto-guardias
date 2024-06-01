import {EtiquetaPersonalizada} from "../../formField/EtiquetaPersonalizada.jsx";
import * as PropTypes from "prop-types";
import {useRef, useState} from "react";
import {Navigate} from "react-router-dom";


function FileShow({fichero, handleRemove}) {
    // Limitar la longitud del nombre del fichero a mostrar
    const MAX_LENGTH = 20;
    const nombreFichero = fichero.name.length > MAX_LENGTH
        ? fichero.name.substring(0, MAX_LENGTH) + '...'
        : fichero.name;

    // Componente que muestra el nombre del fichero subido y permite eliminarlo
    return (
        <div className='flex gap-2 justify-between'>
            <h2 className='content-center'>{nombreFichero}</h2>
            <button className='border-2 border-red-500 rounded-full text-red-900 p-1 hover:bg-red-200'
                    onClick={handleRemove}>Eliminar
            </button>
        </div>
    )
}

function InputFile({texto, fichero, setFichero, props}) {
    const handleClick = event => {
        hiddenFileInput.current.click();
    };
    const handleChange = event => {
        const fileUploaded = event.target.files[0];
        console.log(fileUploaded)
        setFichero(fileUploaded);
        // handleFile(fileUploaded);
    };
    const hiddenFileInput = useRef(null);

    return (
        <div className={'flex flex-col w-1/2 gap-2 min-h-full justify-between'}>
            <EtiquetaPersonalizada>{texto}</EtiquetaPersonalizada>
            {fichero
                ? <FileShow fichero={fichero} handleRemove={() => setFichero(null)}/>
                : <>
                    <button className='border-2 border-blue-500 rounded-full hover:bg-blue-200 p-1'
                            onClick={handleClick}>
                        Upload a file
                    </button>
                    <input
                        type="file"
                        onChange={handleChange}
                        ref={hiddenFileInput}
                        style={{display: 'none'}} // Make the file input element invisible
                    /></>
            }
        </div>
    )
}

export function UploadPage({handleFile}) {
    const [ficheroIds, setFicheroIds] = useState(null);
    const [ficheroRelaciones, setFicheroRelaciones] = useState(null);

    const manejarSubida = (e) => {
        e.preventDefault();
        // enviar los ficheros al servidor mediante una peticion POST con application/json
        const formData = new FormData();
        formData.append('ficheroIds', ficheroIds);
        formData.append('ficheroRelaciones', ficheroRelaciones);
        fetch('https://localhost:8000/horario/upload_xml', {
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
        Navigate({to: "/"});
    }


    return (<>
            <form onSubmit={manejarSubida}
                  className='flex flex-col gap-5 w-full max-w-xl m-auto bg-white shadow-md rounded p-8 items-center'>
                <div className='flex w-full gap-5'>
                    <InputFile texto={'Subir fichero de identificadores'} fichero={ficheroIds}
                               setFichero={setFicheroIds}/>
                    <InputFile texto={'Subir fichero de relaciones '} fichero={ficheroRelaciones}
                               setFichero={setFicheroRelaciones}/>
                </div>
                <button type='submit'
                        className='bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded w-1/2'>Cargar
                    datos
                </button>
            </form>
        </>
    );
}