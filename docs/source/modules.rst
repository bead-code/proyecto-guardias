Bienvenido a la documentación del proyecto Guardias-back!
=========================================================

Esta documentación ha sido generada automáticamente a partir del código fuente del proyecto. A continuación se muestra una descripción general de los módulos y clases que componen el proyecto.

Utilidades de Seguridad
=======================

.. automodule:: security.hash
    :members:
    :undoc-members:
    :show-inheritance:


Autenticación y Autorización
============================

.. autoclass:: security.oauth2
    :members:
    :undoc-members:
    :show-inheritance:

Models
======

.. automodule:: db.models
    :members: Rol, Profesor, Curso, Clase, Actividad, Aula, TramoHorario, Calendario
    :undoc-members:
    :show-inheritance:

Schemas
=======

.. automodule:: db.schemas
    :members: Token, LoginData, RolCreate, RolUpdate, RolDTO, ProfesorCreate, ProfesorUpdate, ProfesorUpdatePassword, ProfesorDTO, ProfesorAuth, CursoCreate, CursoUpdate, CursoDTO, ActividadCreate, ActividadUpdate, ActividadDTO, ActividadCalendario, AulaCreate, AulaUpdate, AulaDTO, ClaseCreate, ClaseUpdate, ClaseDTO, TramoHorarioCreate, TramoHorarioUpdate, TramoHorarioDTO, CalendarioCreate, CalendarioDTO
    :undoc-members:
    :show-inheritance:

DAOS
====

Operaciones CRUD para Tramo_Horario
-----------------------------------

.. automodule:: dao.dao_tramo_horario
    :members:
    :undoc-members:
    :show-inheritance:



Operaciones CRUD para Roles
---------------------------

.. automodule:: dao.dao_rol
    :members:
    :undoc-members:
    :show-inheritance:


Operaciones CRUD para Profesor
------------------------------

.. automodule:: dao.dao_profesor
    :members:
    :undoc-members:
    :show-inheritance:

Operaciones CRUD para Guardia
-----------------------------

.. automodule:: dao.dao_grupo_guardia
    :members:
    :undoc-members:
    :show-inheritance:

Operaciones CRUD para Curso
---------------------------

.. automodule:: dao.dao_curso
    :members:
    :undoc-members:
    :show-inheritance:

Operaciones CRUD para Clase
---------------------------

.. automodule:: dao.dao_clase
    :members:
    :undoc-members:
    :show-inheritance:

Operaciones CRUD para Calendario
--------------------------------

.. automodule:: dao.dao_calendario
    :members:
    :undoc-members:
    :show-inheritance:

Operaciones CRUD para Aula
--------------------------

.. automodule:: dao.dao_aula
    :members:
    :undoc-members:
    :show-inheritance:

Operaciones CRUD para Actividad
-------------------------------

.. automodule:: dao.dao_actividad
    :members:
    :undoc-members:
    :show-inheritance:

Routers
=======

Routers para los Tramos Horarios
--------------------------------

.. automodule:: routers.tramo_horario
    :members:
    :undoc-members:
    :show-inheritance:

Routers para los Roles
----------------------

.. automodule:: routers.rol
    :members:
    :undoc-members:
    :show-inheritance:

Routers para los Profesores
---------------------------

.. automodule:: routers.profesor
    :members:
    :undoc-members:
    :show-inheritance:

Routers de login
----------------

Login
~~~~~

.. automodule:: routers.login
    :members:
    :undoc-members:
    :show-inheritance:

Routers para los Grupos de Guardia
----------------------------------

.. automodule:: routers.grupo_guardia
    :members:
    :undoc-members:
    :show-inheritance:

Routers para las Guardias
-------------------------

.. automodule:: routers.guardia
    :members:
    :undoc-members:
    :show-inheritance:



Routers para los Cursos
-----------------------

.. automodule:: routers.curso
    :members:
    :undoc-members:
    :show-inheritance:


Routers para las Clases
-----------------------

.. automodule:: routers.clase
    :members:
    :undoc-members:
    :show-inheritance:


Routers para los Calendarios
----------------------------

.. automodule:: routers.calendario
    :members:
    :undoc-members:
    :show-inheritance:

Routers para las Aulas
----------------------

.. automodule:: routers.aula
    :members:
    :undoc-members:
    :show-inheritance:

Routers para las Actividades
----------------------------

.. automodule:: routers.actividad
    :members:
    :undoc-members:
    :show-inheritance:

Base de datos
=============

.. automodule:: db.database
    :members:
    :undoc-members:
    :show-inheritance:

Generador de calendario
=======================

Conversor que permite convertir un archivo XML en distintos dataframes de pandas
--------------------------------------------------------------------------------

.. automodule:: generador_calendario.conversor_xml_to_df
    :members:
    :undoc-members:
    :show-inheritance:

Generador de actividades
------------------------

.. automodule:: generador_calendario.generador_actividades
    :members:
    :undoc-members:
    :show-inheritance:

Generador de aulas
-------------------

.. automodule:: generador_calendario.generador_aulas
    :members:
    :undoc-members:
    :show-inheritance:

Generador de calendario
-----------------------

.. automodule:: generador_calendario.generador_calendario
    :members:
    :undoc-members:
    :show-inheritance:

Generador de clases
-------------------

.. automodule:: generador_calendario.generador_clases
    :members:
    :undoc-members:
    :show-inheritance:

Generador de cursos
-------------------

.. automodule:: generador_calendario.generador_cursos
    :members:
    :undoc-members:
    :show-inheritance:

Generador de profesores
-----------------------

.. automodule:: generador_calendario.generador_profesores
    :members:
    :undoc-members:
    :show-inheritance:

Generador de roles
------------------

.. automodule:: generador_calendario.generador_roles
    :members:
    :undoc-members:
    :show-inheritance:

Generador de tramos horarios
----------------------------

.. automodule:: generador_calendario.generador_tramos_horarios
    :members:
    :undoc-members:
    :show-inheritance:





































