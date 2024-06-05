import {
    Button,
    Tooltip,
    Typography
} from "@material-tailwind/react";
import {useContext, useEffect, useState} from "react";
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import {useNavigate} from "react-router-dom";
import {mostrarToast} from "../../utils/Notificaciones.js";
import {TableFooter, TablePagination} from "@mui/material";
import DeleteIcon from '@mui/icons-material/Delete';
import EditIcon from '@mui/icons-material/Edit';
import {AppGlobal} from '../../App.jsx';
import {AvatarModificado} from '../usuarios/AvatarModificado.jsx';


export function ListaProfesores() {
    const {token} = useContext(AppGlobal);
    const TABLE_HEAD = ["Usuario", "Rol", "Acciones"];
    const [profesores, setProfesores] = useState([]);
    const navigate = useNavigate();
    useEffect(() => {
        loadProfesores()
    }, []);
    const handleChangePage = (event, newPage) => {
        setPage(newPage);
        loadProfesores();
    }
    const handleChangeRowsPerPage = (event) => {
        setRowsPerPage(parseInt(event.target.value, 10));
        setPage(0);
        loadProfesores();
    }
    const handleDelete = (profesorEliminado) => {
        deleteProfesor(profesorEliminado);
    }
    const deleteProfesor = (profesorEliminado) => {
        setProfesores(profesores.filter(profesor => profesor.id_profesor !== profesorEliminado.id_profesor));
        fetch(`http://localhost:8000/profesor/${profesorEliminado.id_profesor}`, {
            method: 'DELETE', headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + token,
            },
        }).then((response) => {
            if (!response.ok) {
                mostrarToast(`No se ha podido eliminar a ${profesorEliminado.nombre}`, 'error')
                setProfesores(profesores)
            }
        }).catch((error) => {
            mostrarToast(`No se ha podido eliminar a ${profesorEliminado.nombre}`, 'error')
            setProfesores(profesores)
        });

    }
    const loadProfesores = () => {
        console.log("token")
        console.log(token)
        fetch(`http://localhost:8000/profesor?page=${page}&limit=${rowsPerPage}`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + token,
            }
        })
            .then((response) => response.json())
            .then((data) => {
                setProfesores(data);
            });
    }
    let [rowsPerPage, setRowsPerPage] = useState(5);
    let [page, setPage] = useState(0);
    const emptyRows =
        page > 0 ? Math.max(0, (1 + page) * rowsPerPage - profesores.length) : 0;
    return (
        <Paper className='max-w-4xl mx-auto h-full'>
            <TableContainer className='max-w-4xl mx-auto max-h-[calc(100vh-250px)]'>
                <Table aria-label="custom table" stickyHeader>
                    <TableHead>
                        <TableRow>
                            <TableCell align="left">Usuario</TableCell>
                            <TableCell align="center">Rol</TableCell>
                            <TableCell align="center">Acciones</TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody className='overflow-scroll max-h-96'>
                        {(rowsPerPage > 0
                                ? profesores.slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage)
                                : profesores
                        ).map((row) => (
                            <TableRow key={row.id_profesor}>
                                <TableCell component="th" scope="row">
                                    <div className='flex gap-2 items-center'>
                                        <AvatarModificado profesor={row}/>
                                    </div>
                                </TableCell>
                                <TableCell style={{width: 200}} align="center">
                                    <Typography variant='lead' className='lowercase'>{row.rol.nombre}</Typography>
                                </TableCell>
                                <TableCell style={{width: 160}} align="center">
                                    <div className='flex gap-2 w-full justify-center'>
                                        <Tooltip content="Editar Usuario">
                                            <Button variant="gradient" className='p-3'
                                                    onClick={() => navigate(`/profesor/${row.id_profesor}/mod`, { state: { defaultUser: row, modify: true } })}>
                                                <EditIcon/>
                                            </Button>
                                        </Tooltip>
                                        <Tooltip content="Eliminar Usuario">
                                            <Button variant="outlined" color="red" className='p-3' onClick={() => {
                                                handleDelete(row)
                                            }}>
                                                <DeleteIcon/>
                                            </Button>
                                        </Tooltip>
                                    </div>
                                </TableCell>
                            </TableRow>
                        ))}
                    </TableBody>
                </Table>
            </TableContainer>

            <TablePagination
                rowsPerPageOptions={[5, 10, 25, {label: 'All', value: -1}]}
                component="div"
                colSpan={3}
                count={profesores.length}
                rowsPerPage={rowsPerPage}
                page={page}


                onPageChange={handleChangePage}

                onRowsPerPageChange={handleChangeRowsPerPage}
            />
        </Paper>
    );

}