// Utilidad para mostrar toasts en la aplicacion
import {toast} from 'react-toastify';
export function mostrarToast(contenido, tipo) {
    const AUTO_CLOSE_TIME = 3000;
    let toastConfig = {
            type: tipo,
            pauseOnHover: false,
            pauseOnFocusLoss: false,
            autoClose: AUTO_CLOSE_TIME,
            closeOnClick: true,
            draggable: true,
            position: 'bottom-right',
        }
    toast(contenido, toastConfig);
}