"""
Módulo de configuración de logging.

Este módulo configura el sistema de logging para la aplicación. Los logs se registran tanto en un archivo como en la consola.

Configuración
-------------

* **Nivel de logging**: INFO
* **Formato de logging**: `%(asctime)s - %(name)s - %(levelname)s - %(message)s`
* **Handlers**:
  * FileHandler: Guarda los logs en un archivo llamado `app.log`.
  * StreamHandler: Muestra los logs en la consola.

Variables
---------

* **logger**: Instancia de logger configurada para la aplicación.
"""

import logging

# Configuración básica del logging
logging.basicConfig(
    level=logging.INFO,  # Nivel de logging
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",  # Formato del logging
    handlers=[
        logging.FileHandler("app.log"),  # Handler para guardar logs en archivo
        logging.StreamHandler()  # Handler para mostrar logs en consola
    ]
)

# Crear una instancia de logger
logger = logging.getLogger("myapp")



