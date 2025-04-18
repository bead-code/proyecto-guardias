import {useContext, useEffect, useState} from "react";
import {Navbar, Collapse, Typography, IconButton, Button} from "@material-tailwind/react";
import {Bars3Icon, XMarkIcon} from "@heroicons/react/24/outline";
import {NavLink} from "react-router-dom";
import {useNavigate} from "react-router-dom";
import AppGlobal from "../../App.jsx";

const navItems = [
    {id: 7, url: '/guardias', content: 'Guardias', allowedRoles: ["ADMIN", "JEFE_DE_ESTUDIOS", "DIRECTOR", "PROFESOR"]},
    {id: 9, url: '/cargaDatos', content: 'Cargar datos', allowedRoles: ["ADMIN"]},
    {id: 10, url: '/profesor', content: 'Profesores', allowedRoles: ["ADMIN", "JEFE_DE_ESTUDIOS", "DIRECTOR"]}
];

function NavList({isUserAuthenticated, setToken, onElementClicked}) {
    const navigate = useNavigate();
    const {decodedToken} = useContext(AppGlobal);
    const handleLogout = () => {
        setToken(null);
        localStorage.removeItem('tokenAppGuardias');
        navigate('/login');
    };

    if (!isUserAuthenticated || !decodedToken) {
        return (
            <ul className="my-2 flex flex-col flex-wrap place-content-center lg:place-content-end gap-2 lg:mb-0 lg:mt-0 lg:flex-row lg:items-center lg:gap-6">
                <Typography
                    as="li"
                    variant="small"
                    color="blue-gray"
                    className="p-1 font-medium"
                    onClick={onElementClicked}
                >
                    <NavLink to="/login" className="flex items-center hover:text-blue-500 transition-colors">
                        Login
                    </NavLink>
                </Typography>
            </ul>
        );
    }

    return (
        <ul className="my-2 flex flex-col flex-wrap place-content-center lg:place-content-end gap-2 lg:mb-0 lg:mt-0 lg:flex-row lg:items-center lg:gap-6">
            {navItems.map((navItem) => (
                navItem.allowedRoles.includes(decodedToken.rol) && (
                    <Typography
                        as="li"
                        variant="small"
                        color="blue-gray"
                        className="p-1 font-medium"
                        key={navItem.id}
                        onClick={onElementClicked}
                    >
                        <NavLink to={navItem.url} className="flex items-center hover:text-blue-500 transition-colors">
                            {navItem.content}
                        </NavLink>
                    </Typography>)
            ))}
            {decodedToken && (
                <Typography
                    as="li"
                    variant="small"
                    color="blue-gray"
                    className="p-1 font-medium"
                    onClick={onElementClicked}
                >
                    <NavLink to={`/profesor/${decodedToken.sub}/mod`}
                             className="flex items-center hover:text-blue-500 transition-colors">
                        Mi Usuario
                    </NavLink>
                </Typography>
            )}


            {isUserAuthenticated && <Button onClick={handleLogout}>Log out</Button>}
        </ul>
    );
}

export function ModifiedNavBar({setToken}) {
    const {decodedToken, isExpired} = useContext(AppGlobal);
    const [showMenu, setShowMenu] = useState(false);
    const navigate = useNavigate();

    const onMenuClick = () => {
        setShowMenu(false);
    };

    const handleWindowResize = () => {
        window.innerWidth >= 960 && setShowMenu(false);
    };

    useEffect(() => {
        window.addEventListener("resize", handleWindowResize);

        return () => {
            window.removeEventListener("resize", handleWindowResize);
        };
    }, []);

    if (isExpired) {
        return null;
    }

    return (
        <Navbar className="mx-auto max-w-screen-2xl px-6 py-3">
            <div className="flex items-center justify-between text-blue-gray-900">
                <Typography
                    as="a"
                    href="#"
                    variant="h6"
                    className="mr-4 cursor-pointer py-1.5"
                >
                    Aplicacion guardias
                </Typography>
                <div className="hidden lg:block">
                    <NavList
                        decodedToken={decodedToken}
                        isUserAuthenticated={!isExpired}
                        setToken={setToken}
                    />
                </div>
                <IconButton
                    variant="text"
                    className="ml-auto h-6 w-6 text-inherit hover:bg-transparent focus:bg-transparent active:bg-transparent lg:hidden"
                    ripple={false}
                    onClick={() => setShowMenu(!showMenu)}
                >
                    {showMenu ? (
                        <XMarkIcon className="h-6 w-6" strokeWidth={2}/>
                    ) : (
                        <Bars3Icon className="h-6 w-6" strokeWidth={2}/>
                    )}
                </IconButton>
            </div>
            <Collapse open={showMenu}>
                <NavList
                    onElementClicked={onMenuClick}
                    isUserAuthenticated={!isExpired}
                    setToken={setToken}
                />
            </Collapse>
        </Navbar>
    );
}
