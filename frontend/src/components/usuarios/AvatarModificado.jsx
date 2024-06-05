import Avatar from "@mui/material/Avatar";
import {Typography} from "@material-tailwind/react";

function calculateTextColor(backgroundColor) {
    let color = "#000000";
    let r, g, b, brightness;
    if (backgroundColor) {
        r = parseInt(backgroundColor.slice(1, 3), 16);
        g = parseInt(backgroundColor.slice(3, 5), 16);
        b = parseInt(backgroundColor.slice(5, 7), 16);
        brightness = ((r * 299) + (g * 587) + (b * 114)) / 1000;
        color = brightness > 125 ? '#000000' : '#FFFFFF';
    }
    return color;

}

function stringAvatar(profesor) {
    let nameLetter = profesor.nombre.split(' ')[0][0]
    let surnameLetter = profesor.nombre.split(' ')[1] ? profesor.nombre.split(' ')[1][0] : ''
    let avatar = `${nameLetter}${surnameLetter}`.toUpperCase()
    return {
        sx: {
            bgcolor: profesor.color, color: calculateTextColor(profesor.color),
        }, children: `${avatar}`,
    };
}

export function AvatarModificado({profesor, className, ...props}) {
    return (
        <div className='flex gap-2'>
            <Avatar {...stringAvatar(profesor)} />
            <Typography variant='lead' className='capitalize'>
                {profesor.nombre}
            </Typography>
        </div>)
}