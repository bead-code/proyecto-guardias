import xml.etree.ElementTree as ET
import pandas as pd

from generador_horarios.conversor_xml_to_df import parse_xml_to_dataframes

# Parse the XML file
tree = ET.parse('xml/Horario.xml')
root = tree.getroot()

# Extract data for all professors
all_data = []

for horario_regular in root.findall(".//grupo_datos[@seq='HORARIOS_REGULARES']"):
    for profesor in horario_regular.findall("grupo_datos"):
        profesor_id = profesor.find("dato[@nombre_dato='X_EMPLEADO']").text if profesor.find(
            "dato[@nombre_dato='X_EMPLEADO']") is not None else ''
        fecha_toma_pos = profesor.find("dato[@nombre_dato='F_TOMAPOS']").text if profesor.find(
            "dato[@nombre_dato='F_TOMAPOS']") is not None else ''

        for actividad in profesor.findall("grupo_datos"):
            dia_semana = actividad.find("dato[@nombre_dato='N_DIASEMANA']").text if actividad.find(
                "dato[@nombre_dato='N_DIASEMANA']") is not None else ''
            tramo = actividad.find("dato[@nombre_dato='X_TRAMO']").text if actividad.find(
                "dato[@nombre_dato='X_TRAMO']") is not None else ''
            dependencia = actividad.find("dato[@nombre_dato='X_DEPENDENCIA']").text if actividad.find(
                "dato[@nombre_dato='X_DEPENDENCIA']") is not None else ''
            unidad = actividad.find("dato[@nombre_dato='X_UNIDAD']").text if actividad.find(
                "dato[@nombre_dato='X_UNIDAD']") is not None else ''
            oferta_matrig = actividad.find("dato[@nombre_dato='X_OFERTAMATRIG']").text if actividad.find(
                "dato[@nombre_dato='X_OFERTAMATRIG']") is not None else ''
            materia = actividad.find("dato[@nombre_dato='X_MATERIAOMG']").text if actividad.find(
                "dato[@nombre_dato='X_MATERIAOMG']") is not None else ''
            fecha_inicio = actividad.find("dato[@nombre_dato='F_INICIO']").text if actividad.find(
                "dato[@nombre_dato='F_INICIO']") is not None else ''
            fecha_fin = actividad.find("dato[@nombre_dato='F_FIN']").text if actividad.find(
                "dato[@nombre_dato='F_FIN']") is not None else ''
            hora_inicio = actividad.find("dato[@nombre_dato='N_HORINI']").text if actividad.find(
                "dato[@nombre_dato='N_HORINI']") is not None else ''
            hora_fin = actividad.find("dato[@nombre_dato='N_HORFIN']").text if actividad.find(
                "dato[@nombre_dato='N_HORFIN']") is not None else ''
            actividad_id = actividad.find("dato[@nombre_dato='X_ACTIVIDAD']").text if actividad.find(
                "dato[@nombre_dato='X_ACTIVIDAD']") is not None else ''
            all_data.append([
                profesor_id, fecha_toma_pos, dia_semana, tramo, dependencia, unidad, oferta_matrig, materia,
                fecha_inicio, fecha_fin, hora_inicio, hora_fin, actividad_id
            ])

# Create a DataFrame
df_horario = pd.DataFrame(all_data, columns=[
    'ID_PROFESOR', 'DIA', 'TRAMO_ID', 'AULA_ID', 'CLASE', 'CURSO_ID',
    'MATERIA_ID', 'FECHA_INICIO', 'FECHA_FIN', 'HORA_INICIO', 'HORA_FIN', 'ID_ACTIVIDAD'
])

df_xml = parse_xml_to_dataframes()

roles = {
    'M. Belén Aguilar Aguilar': 'directora',
    'Mario Lobo Del Olmo': 'jefe de estudios',
    'Rosalina Ugidos Valdueza': 'jefe de estudios',
    'Mariano Iglesias Molina': 'jefe de estudios',
    'Paula Pereira Fernández': 'jefe de estudios',
    'Isabel La Parra Casado': 'jefe de estudios'
}

df_xml.rename(columns={"X_EMPLEADO": "ID Profesor"}, inplace=True)
if not df_xml.empty:
    df_xml['NOMBRE_COMPLETO'] = df_xml['NOMBRE'] + ' ' + df_xml['APELLIDO1'] + ' ' + df_xml['APELLIDO2']
    df_xml['ROL'] = df_xml['NOMBRE_COMPLETO'].apply(lambda x: roles.get(x, 'profesor'))
    df_xml.drop(columns=['NOMBRE', 'APELLIDO1', 'APELLIDO2'], inplace=True)
