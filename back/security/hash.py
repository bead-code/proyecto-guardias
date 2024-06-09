"""
Este módulo proporciona utilidades para el hash y verificación de contraseñas usando el algoritmo Argon2.
"""

from passlib.context import CryptContext

# Configuración del contexto de hash usando Argon2
pwd_cxt = CryptContext(schemes=["argon2"], deprecated="auto")


class Hash:
    """
    Clase para realizar operaciones de hash y verificación de contraseñas.

    Métodos estáticos
    -----------------
    argon2(password: str) -> str
        Genera un hash de la contraseña usando Argon2.

    verify(plain_password: str, hashed_password: str) -> bool
        Verifica que una contraseña en texto plano coincida con su hash.
    """

    @staticmethod
    def argon2(password: str) -> str:
        """
        Genera un hash de la contraseña usando Argon2.

        Parameters
        ----------
        password : str
            La contraseña en texto plano que se quiere hashear.

        Returns
        -------
        str
            El hash de la contraseña.
        """
        return pwd_cxt.hash(password)

    @staticmethod
    def verify(plain_password: str, hashed_password: str) -> bool:
        """
        Verifica que una contraseña en texto plano coincida con su hash.

        Parameters
        ----------
        plain_password : str
            La contraseña en texto plano.
        hashed_password : str
            El hash de la contraseña.

        Returns
        -------
        bool
            True si la contraseña coincide con su hash, False en caso contrario.
        """
        return pwd_cxt.verify(plain_password, hashed_password)
