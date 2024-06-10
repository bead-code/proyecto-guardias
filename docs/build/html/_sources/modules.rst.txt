Utilidades de Seguridad
=======================

Funciones y utilidades para encriptar y verificar de contraseñas usando el algoritmo Argon2.

.. _security.hash:

Encriptar Contraseña
--------------------

.. autofunction:: security.hash.Hash.argon2

Verificar Contraseña
--------------------

.. autofunction:: security.hash.Hash.verify


Autenticación y Autorización
============================

Funciones y utilidades para la autenticación y autorización de usuarios.

Crear Token de Acceso
---------------------

.. autofunction:: security.oauth2.create_access_token

Verificar Token de Acceso
-------------------------

.. autofunction:: security.oauth2.verify_access_token

Obtener Usuario Logueado
----------------------

.. autofunction:: security.oauth2.get_current_profesor

Verificar el Rol de Administrador del token de acceso
-----------------------------------------------------

.. autofunction:: security.oauth2.check_admin_role


DAOS
====

Operaciones CRUD para Roles
---------------------------

Funciones para manejar las operaciones CRUD de la tabla roles.

Obtener Rol por ID
~~~~~~~~~~~~~~~~~~

.. autofunction:: dao.dao_rol.get_rol_by_id

Obtener Rol por Nombre
~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: dao.dao_rol.get_rol_by_nombre

Obtener Todos los Roles
~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: dao.dao_rol.get_roles

Crear Rol
~~~~~~~~~

.. autofunction:: dao.dao_rol.create_rol

Actualizar Rol
~~~~~~~~~~~~~~

.. autofunction:: dao.dao_rol.update_rol

Eliminar Rol
~~~~~~~~~~~~

.. autofunction:: dao.dao_rol.delete_rol


Operaciones CRUD para Tramo_Horario
---------------------------

Funciones para manejar las operaciones CRUD de la tabla tramo_horario.

Obtener Tramo_Horario por ID
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: dao.dao_tramo_horario.get_tramo_horario_by_id

Obtener Tramo_Horario por Nombre
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: dao.dao_tramo_horario.get_tramo_horario_by_nombre

Obtener Todos los Tramos_Horarios
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: dao.dao_tramo_horario.get_tramos_horarios

Crear Tramo_Horario
~~~~~~~~~~~~~~

.. autofunction:: dao.dao_tramo_horario.create_tramo_horario

Actualizar Tramo_Horario
~~~~~~~~~~~~~~

.. autofunction:: dao.dao_tramo_horario.update_tramo_horario

Eliminar Tramo_Horario
~~~~~~~~~~~~~~

.. autofunction:: dao.dao_tramo_horario.delete_tramo_horario


Operaciones CRUD para Profesor
---------------------------

Funciones para manejar las operaciones CRUD de la tabla profesor.

Obtener Profesor por ID
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: dao.dao_profesor.get_profesor_by_id

Obtener Profesor por Username
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: dao.dao_profesor.get_profesor_by_username

Obtener Todos los Profesores
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: dao.dao_profesor.get_profesores

Crear Profesor
~~~~~~~~~~~~~~

.. autofunction:: dao.dao_profesor.create_profesor

Actualizar Profesor
~~~~~~~~~~~~~~

.. autofunction:: dao.dao_profesor.update_profesor

Eliminar Profesor
~~~~~~~~~~~~~~

.. autofunction:: dao.dao_profesor.delete_profesor

Obtener Profesores Disponibles
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: dao.dao_profesor.get_profesores_disponibles_by_id_calendario


Operaciones CRUD para Guardia
---------------------------

Funciones para manejar las operaciones CRUD de las guardias.

Obtener Guardia por ID
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: dao.dao_guardia.get_guardia_by_id

Obtener Guardia por Fecha
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: dao.dao_guardia.get_guardia_by_fecha_tramo

Obtener Todas las Guardias
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: dao.dao_guardia.get_guardias

Obtener Guardias a las que ya se le asignado un profesor sustituto
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: dao.dao_guardia.get_guardias_asignadas

Obtener Guardias pendientes de asignación de profesor sustituto
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: dao.dao_guardia.get_guardias_pendientes

Obtener Guardias de un profesor
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: dao.dao_guardia.get_guardias_by_profesor

Crear Guardia
~~~~~~~~~~~~~~

.. autofunction:: dao.dao_guardia.create_guadia

Asignar Profesor Sustituto a Guardia
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: dao.dao_guardia.assign_profesor_sustituto

Operaciones CRUD para Grupos de Guardia
---------------------------

Funciones para manejar las operaciones CRUD de los grupos de guardia.

Obtener el Grupo de Guardia por tramo horario y dia
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: dao.dao_grupo_guardia.get_grupo_guardia

Obtener Todos los Grupos de Guardia
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: dao.dao_grupo_guardia.get_grupos_guardia

Operaciones CRUD para Curso
---------------------------
Funciones para manejar las operaciones CRUD de la tabla curso.

Obtener Curso por ID
~~~~~~~~~~~~~~~~~~~~

.. autofunction:: dao.dao_curso.get_curso_by_id

Obtener Curso por Nombre
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: dao.dao_curso.get_curso_by_nombre

Obtener Todos los Cursos
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: dao.dao_curso.get_cursos

Crear Curso
~~~~~~~~~~~

.. autofunction:: dao.dao_curso.create_curso

Actualizar Curso
~~~~~~~~~~~~~~

.. autofunction:: dao.dao_curso.update_curso

Eliminar Curso
~~~~~~~~~~~~

.. autofunction:: dao.dao_curso.delete_curso

Operaciones CRUD para Clase
---------------------------

Funciones para manejar las operaciones CRUD de la tabla clase.

Obtener Clase por ID
~~~~~~~~~~~~~~~~~~~~

.. autofunction:: dao.dao_clase.get_clase_by_id

Obtener Clase por Nombre
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: dao.dao_clase.get_clase_by_nombre

Obtener Todas las Clases
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: dao.dao_clase.get_clases

Crear Clase
~~~~~~~~~~~

.. autofunction:: dao.dao_clase.create_clase

Actualizar Clase
~~~~~~~~~~~~~~

.. autofunction:: dao.dao_clase.update_clase

Eliminar Clase
~~~~~~~~~~~~

.. autofunction:: dao.dao_clase.delete_clase

Operaciones CRUD para Calendario
---------------------------

Funciones para manejar las operaciones CRUD de la tabla calendario.

Obtener Calendario por ID del Calendario
~~~~~~~~~~~~~~~~~~~~

.. autofunction:: dao.dao_calendario.get_calendario_by_id

Obtener Calendario por el ID del Profesor
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: dao.dao_calendario.get_calendario_by_id_profesor

Obtener Calendario de un Profesor de la hora actual
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: dao.dao_calendario.get_actual_calendario_by_id_profesor

Crear Calendario
~~~~~~~~~~~

.. autofunction:: dao.dao_calendario.create_calendario

Operaciones CRUD para Aula
---------------------------

Funciones para manejar las operaciones CRUD de la tabla aula.

Obtener Aula por ID
~~~~~~~~~~~~~~~~~~~~

.. autofunction:: dao.dao_aula.get_aula_by_id

Obtener Aula por el Nombre
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: dao.dao_aula.get_aula_by_nombre

Obtener Todas las Aulas
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: dao.dao_aula.get_aulas

Crear Aula
~~~~~~~~~~~

.. autofunction:: dao.dao_aula.create_aula

Actualizar Aula
~~~~~~~~~~~~~~

.. autofunction:: dao.dao_aula.update_aula

Eliminar Aula
~~~~~~~~~~~~

.. autofunction:: dao.dao_aula.delete_aula

Operaciones CRUD para Actividad
---------------------------

Funciones para manejar las operaciones CRUD de la tabla Actividad.

Obtener Actividad por ID
~~~~~~~~~~~~~~~~~~~~

.. autofunction:: dao.dao_actividad.get_actividad_by_id

Obtener Actividad por el Nombre
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: dao.dao_actividad.get_actividad_by_nombre

Obtener Todas las Actividades
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: dao.dao_actividad.get_actividades

Crear Actividad
~~~~~~~~~~~

.. autofunction:: dao.dao_actividad.create_actividad

Actualizar Actividad
~~~~~~~~~~~~~~

.. autofunction:: dao.dao_actividad.update_actividad

Eliminar Actividad
~~~~~~~~~~~~

.. autofunction:: dao.dao_actividad.delete_actividad

Routers
=======

Routers para los Tramos Horarios
--------------------------------

Obtener Tramo Horario por ID
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: routers.tramo_horario.get_tramo_horario_by_id

Obtener Tramo Horario por Nombre
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: routers.tramo_horario.get_tramo_horario_by_nombre

Obtener Todos los Tramos Horarios
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: routers.tramo_horario.get_tramos_horarios

Crear Tramo Horario
~~~~~~~~~~~~~~~~~~

.. autofunction:: routers.tramo_horario.create_tramo_horario


Actualizar Tramo Horario
~~~~~~~~~~~~~~~~~~~~

.. autofunction:: routers.tramo_horario.update_tramo_horario

Eliminar Tramo Horario
~~~~~~~~~~~~~~~~~~~~

.. autofunction:: routers.tramo_horario.delete_tramo_horario

Routers para los Roles
--------------------------------

Obtener Rol por ID
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: routers.rol.get_rol_by_id

Obtener Rol por Nombre
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: routers.rol.get_rol_by_nombre

Obtener Todos los Roles
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: routers.rol.get_roles

Crear Rol
~~~~~~~~~~~~~~~~~~

.. autofunction:: routers.rol.create_rol

Actualizar Rol
~~~~~~~~~~~~~~~~~~~~

.. autofunction:: routers.rol.update_rol

Eliminar Rol
~~~~~~~~~~~~~~~~~~~~

.. autofunction:: routers.rol.delete_rol



Routers para los Profesores
--------------------------------

Obtener Profesor por ID
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: routers.profesor.get_profesor_by_id

Obtener Profesor por Username
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: routers.profesor.get_profesor_by_username

Obtener Todos los Profesores
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: routers.profesor.get_profesores

Obtener profesores disponibles en un calendario
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: routers.profesor.get_profesores_disponibles_by_id_calendario

Crear Profesor
~~~~~~~~~~~~~~~~~~

.. autofunction:: routers.profesor.create_profesor


Actualizar Profesor
~~~~~~~~~~~~~~~~~~~~

.. autofunction:: routers.profesor.update_profesor

Eliminar Profesor
~~~~~~~~~~~~~~~~~~~~

.. autofunction:: routers.profesor.delete_profesor

Routers de login
--------------------------------

Login
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: routers.login.login


Routers para las Guardias
--------------------------------

Obtener guardias por fecha y tramo
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: routers.guardia.get_guardia_by_fecha_tramo

Obtener todas las guardias
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: routers.guardia.get_guardias

Obtener guardias asignadas
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: routers.guardia.get_guardias_asignadas


Obtener guardias pendientes
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: routers.guardia.get_guardias_pendientes

Obtener guardias de un profesor
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: routers.guardia.get_guardias_by_profesor

Crear guardia
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: routers.guardia.create_guardia

Asignar profesor sustituto a guardia
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: routers.guardia.assign_profesor_sustituto

Routers para los Grupos de Guardia
--------------------------------

Obtener grupo de guardia por tramo y dia
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: routers.grupo_guardia.get_grupo_guardia

Obtener todos los grupos de guardia
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: routers.grupo_guardia.get_grupos_guardia

Routers para los Cursos
--------------------------------

Obtener Curso por ID
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: routers.curso.get_curso_by_id

Obtener Curso por Nombre
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: routers.curso.get_curso_by_nombre

Obtener Todos los Cursos
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: routers.curso.get_cursos

Crear Curso
~~~~~~~~~~~~~~~~~~

.. autofunction:: routers.curso.create_curso

Actualizar Curso
~~~~~~~~~~~~~~~~~~~~

.. autofunction:: routers.curso.update_curso

Eliminar Curso
~~~~~~~~~~~~~~~~~~~~

.. autofunction:: routers.curso.delete_curso

Routers para las Clases
--------------------------------

Obtener Clase por ID
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: routers.clase.get_clase_by_id

Obtener Clase por Nombre
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: routers.clase.get_clase_by_nombre

Obtener Todas las Clases
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: routers.clase.get_clases

Crear Clase
~~~~~~~~~~~~~~~~~~

.. autofunction:: routers.clase.create_clase

Actualizar Clase
~~~~~~~~~~~~~~~~~~~~

.. autofunction:: routers.clase.update_clase

Eliminar Clase
~~~~~~~~~~~~~~~~~~~~

.. autofunction:: routers.clase.delete_clase

Routers para los Calendarios
--------------------------------

Obtener Calendario por ID
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: routers.calendario.get_calendario_by_id

Obtener Calendario de un Profesor
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: routers.calendario.get_calendario_by_id_profesor

Obtener Calendario de un Profesor en la hora actual
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: routers.calendario.get_actual_calendario_by_id_profesor

Crear Calendario
~~~~~~~~~~~~~~~~~~

.. autofunction:: routers.calendario.create_calendario

Generar Calendario a partir de dos archivos XML
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: routers.calendario.upload_tables


Routers para las Aulas
--------------------------------

Obtener Aula por ID
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: routers.aula.get_aula_by_id

Obtener Aula por Nombre
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: routers.aula.get_aula_by_nombre

Obtener Todas las Aulas
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: routers.aula.get_aulas

Crear Aula
~~~~~~~~~~~~~~~~~~

.. autofunction:: routers.aula.create_aula

Actualizar Aula
~~~~~~~~~~~~~~~~~~~~

.. autofunction:: routers.aula.update_aula

Eliminar Aula
~~~~~~~~~~~~~~~~~~~~

.. autofunction:: routers.aula.delete_aula

Routers para las Actividades
--------------------------------

Obtener Actividad por ID
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: routers.actividad.get_actividad_by_id

Obtener Actividad por Nombre
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: routers.actividad.get_actividad_by_nombre

Obtener Todas las Actividades
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: routers.actividad.get_actividades

Crear Actividad
~~~~~~~~~~~~~~~~~~

.. autofunction:: routers.actividad.create_actividad

Actualizar Actividad
~~~~~~~~~~~~~~~~~~~~

.. autofunction:: routers.actividad.update_actividad

Eliminar Actividad
~~~~~~~~~~~~~~~~~~~~

.. autofunction:: routers.actividad.delete_actividad

Base de datos
=============

Métodos de gestión de la base de datos
---------------------------------------

Obtener la sesión de la base de datos
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: db.database.get_db

Truncar todas las tablas de la base de datos
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: db.database.truncate_all_tables

Modelos de la base de datos
===========================

Modelo de la tabla Rol
----------------------

.. autoclass:: db.models.Rol

Modelo de la tabla Profesor
----------------------

.. autoclass:: db.models.Profesor

Modelo de la tabla Curso
----------------------

.. autoclass:: db.models.Curso

Modelo de la tabla Clase
----------------------

.. autoclass:: db.models.Clase

Modelo de la tabla Actividad
----------------------

.. autoclass:: db.models.Actividad

Modelo de la tabla Aula
----------------------

.. autoclass:: db.models.Aula

Modelo de la tabla TramoHorario
----------------------

.. autoclass:: db.models.TramoHorario

Modelo de la tabla Calendario
----------------------

.. autoclass:: db.models.Calendario


Schemas para la validación de los datos de entrada y salida de las rutas.
===================

Token de Acceso
--------------------------------------------------------------------------

Schema del Token de Acceso
~~~~~~~~~~~~~

.. autoclass:: db.schemas.Token

Login
--------------------------------------------------------------------------

Schema de los datos de login
~~~~~~~~~~~~~

.. autoclass:: db.schemas.LoginData

Rol
--------------------------------------------------------------------------

Schema para crear un rol
~~~~~~~~~~~~~

.. autoclass:: db.schemas.RolCreate

Schema para actualizar un rol
~~~~~~~~~~~~~

.. autoclass:: db.schemas.RolUpdate

Schema de Rol en formato DTO
~~~~~~~~~~~~~

.. autoclass:: db.schemas.RolDTO

Profesor
--------------------------------------------------------------------------

Schema para crear un profesor
~~~~~~~~~~~~~

.. autoclass:: db.schemas.ProfesorCreate

Schema para actualizar un profesor
~~~~~~~~~~~~~

.. autoclass:: db.schemas.ProfesorUpdate


Schema de Profesor en formato DTO
~~~~~~~~~~~~~

.. autoclass:: db.schemas.ProfesorDTO

Schema de Profesor para autenticación
~~~~~~~~~~~~~

.. autoclass:: db.schemas.ProfesorAuth

Curso
--------------------------------------------------------------------------

Schema para crear un curso
~~~~~~~~~~~~~

.. autoclass:: db.schemas.CursoCreate

Schema para actualizar un curso
~~~~~~~~~~~~~

.. autoclass:: db.schemas.CursoUpdate

Schema de Curso en formato DTO
~~~~~~~~~~~~~

.. autoclass:: db.schemas.CursoDTO

Actividad
--------------------------------------------------------------------------

Schema para crear una actividad
~~~~~~~~~~~~~

.. autoclass:: db.schemas.ActividadCreate

Schema para actualizar una actividad
~~~~~~~~~~~~~

.. autoclass:: db.schemas.ActividadUpdate

Schema de Actividad en formato DTO
~~~~~~~~~~~~~

.. autoclass:: db.schemas.ActividadDTO

Aula
--------------------------------------------------------------------------

Schema para crear un aula
~~~~~~~~~~~~~

.. autoclass:: db.schemas.AulaCreate

Schema para actualizar un aula
~~~~~~~~~~~~~

.. autoclass:: db.schemas.AulaUpdate

Schema de Aula en formato DTO
~~~~~~~~~~~~~

.. autoclass:: db.schemas.AulaDTO

Clase
--------------------------------------------------------------------------

Schema para crear una clase
~~~~~~~~~~~~~

.. autoclass:: db.schemas.ClaseCreate

Schema para actualizar una clase
~~~~~~~~~~~~~

.. autoclass:: db.schemas.ClaseUpdate

Schema de Clase en formato DTO
~~~~~~~~~~~~~

.. autoclass:: db.schemas.ClaseDTO

Tramo Horario
--------------------------------------------------------------------------

Schema para crear un tramo horario
~~~~~~~~~~~~~

.. autoclass:: db.schemas.TramoHorarioCreate

Schema para actualizar un tramo horario
~~~~~~~~~~~~~

.. autoclass:: db.schemas.TramoHorarioUpdate

Schema de Tramo Horario en formato DTO
~~~~~~~~~~~~~

.. autoclass:: db.schemas.TramoHorarioDTO

Calendario
--------------------------------------------------------------------------

Schema para crear un calendario
~~~~~~~~~~~~~

.. autoclass:: db.schemas.CalendarioCreate

Schema de Calendario en formato DTO
~~~~~~~~~~~~~

.. autoclass:: db.schemas.CalendarioDTO

Generador de calendario
=======================

Conversor que permite convertir un archivo XML en distintos dataframes de pandas.
---------------------------------------------------------------------------------

Convertir un archivo XML en los dataframes necesarios para crear las tablas de la base de datos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: generador_calendario.conversor_xml_to_df.load_tables

Convertir un archivo XML en el dataframe necesario para generar el calendario de todo el año
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: generador_calendario.conversor_xml_to_df.load_calendario

Generador de actividades
------------------------

Generador de actividades a partir de un dataframe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: generador_calendario.generador_actividades.generate_actividades_from_dataframe

Generador de aulas
-------------------

Generador de aulas a partir de un dataframe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: generador_calendario.generador_aulas.generate_aulas_from_dataframe

Generador de calendario
-----------------------

Generador de calendario a partir de un dataframe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: generador_calendario.generador_calendario.generate_calendario_from_dataframe

Generador de clases
-------------------

Generador de clases a partir de un dataframe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: generador_calendario.generador_clases.generate_clases_from_dataframe

Generador de cursos
-------------------

Generador de cursos a partir de un dataframe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: generador_calendario.generador_cursos.generate_cursos_from_dataframe

Generador de profesores
-----------------------

Generador de profesores a partir de un dataframe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: generador_calendario.generador_profesores.generate_profesores_from_dataframe

Generador de roles
-------------------

Generador de roles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: generador_calendario.generador_roles.generate_roles

Generador de tramos horarios
---------------------------

Conversor de minutos a horas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: generador_calendario.generador_tramos_horarios.minutos_a_hora

Generador de tramos horarios a partir de un dataframe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: generador_calendario.generador_tramos_horarios.generate_tramos_horarios_from_dataframe

Generador de tablas de la base de datos a partir de dos archivos XML por defecto
-------------------

.. autofunction:: generador_calendario.generador_tablas.generate_tables_from_path


Generador de las tablas de la base de datos a partir de dos archivo XML
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: generador_calendario.generador_tablas.generate_tables_from_files


































