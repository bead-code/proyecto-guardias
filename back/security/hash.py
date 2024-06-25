"""
Módulo de utilidades para el manejo de contraseñas.

Este módulo proporciona funciones para generar y verificar contraseñas utilizando el algoritmo Argon2.

Clases
------

* **Hash**: Clase que proporciona métodos para generar y verificar contraseñas.

Métodos
-------

* **argon2**: Genera un hash Argon2 para una contraseña dada.
* **verify**: Verifica una contraseña en texto plano contra un hash dado.
"""

from passlib.context import CryptContext

# Configuración del contexto de Passlib para usar Argon2
pwd_cxt = CryptContext(schemes=["argon2"], deprecated="auto")

class Hash():
    """
    Clase que proporciona métodos para generar y verificar contraseñas utilizando el algoritmo Argon2.
    """

    @staticmethod
    def argon2(password: str) -> str:
        """
        Genera un hash Argon2 para una contraseña dada.

        :param password: La contraseña en texto plano que se va a hashear.
        :type password: str
        :returns: El hash Argon2 de la contraseña.
        :rtype: str

        Ejemplo de uso:

        .. code-block:: python

            hashed_password = Hash.argon2("mi_contraseña_segura")
        """
        return pwd_cxt.hash(password)

    @staticmethod
    def verify(plain_password: str, hashed_password: str) -> bool:
        """
        Verifica una contraseña en texto plano contra un hash dado.

        :param plain_password: La contraseña en texto plano.
        :type plain_password: str
        :param hashed_password: El hash con el que se va a comparar la contraseña.
        :type hashed_password: str
        :returns: `True` si la contraseña coincide con el hash, `False` en caso contrario.
        :rtype: bool

        Ejemplo de uso:

        .. code-block:: python

            is_valid = Hash.verify("mi_contraseña_segura", hashed_password)
        """
        return pwd_cxt.verify(plain_password, hashed_password)
