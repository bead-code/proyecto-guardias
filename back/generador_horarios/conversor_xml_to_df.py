import xml.etree.ElementTree as ET
from datetime import datetime
from io import BytesIO

import pandas as pd

file_path = './generador_horarios/Exportacion_hacia_generadores_de_horarios.xml'


def load_tables_from_file(file: BytesIO):
    tree = ET.parse(file)
    root = tree.getroot()
    data = {}
    def process_grupo(grupo, group_name):
        items = []
        for subgrupo in grupo.findall('grupo_datos'):
            datos = {}
            for dato in subgrupo.findall('dato'):
                nombre_dato = dato.get('nombre_dato')
                datos[nombre_dato] = dato.text
            if datos:
                items.append(datos)
        if items:
            data[group_name] = items
    for grupo in root.findall('.//grupo_datos'):
        seq = grupo.get('seq')
        process_grupo(grupo, seq)
    dataframes = {}
    for key, value in data.items():
        dataframes[key] = pd.DataFrame(value)
    return dataframes


def load_calendario_from_file(file: BytesIO):
    tree = ET.parse(file)
    root = tree.getroot()

    all_data = []

    for horario_regular in root.findall(".//grupo_datos[@seq='HORARIOS_REGULARES']"):
        for profesor in horario_regular.findall("grupo_datos"):
            profesor_id = profesor.find("dato[@nombre_dato='X_EMPLEADO']").text if profesor.find(
                "dato[@nombre_dato='X_EMPLEADO']") is not None else ''
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
                all_data.append([
                    profesor_id, dia_semana, tramo, dependencia, unidad, oferta_matrig, materia
                ])
    df_calendario = pd.DataFrame(all_data, columns=[
        'ID_PROFESOR', 'DIA', 'ID_TRAMO', 'ID_AULA', 'ID_CLASE', 'ID_CURSO',
        'ID_ACTIVIDAD'
    ])
    df_calendario.loc[:, 'DIA'] = df_calendario['DIA'].astype(int)
    start_date = datetime(2023, 9, 1)
    end_date = datetime(2024, 8, 31)
    date_range = pd.date_range(start=start_date, end=end_date)
    extended_schedule = []
    day_mapping = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5}
    for date in date_range:
        day_of_week = date.weekday()
        if day_of_week in day_mapping:
            day_number = day_mapping[day_of_week]
            daily_schedule = df_calendario[df_calendario['DIA'] == day_number].copy()
            if not daily_schedule.empty:
                daily_schedule['FECHA'] = date
                extended_schedule.append(daily_schedule)
            else:
                print(f"No entries found for day_number {day_number} on date {date}")
    if extended_schedule:
        extended_schedule_df = pd.concat(extended_schedule, ignore_index=True)
    else:
        extended_schedule_df = pd.DataFrame()
    extended_schedule_df = extended_schedule_df.loc[:, ~extended_schedule_df.columns.duplicated()]
    extended_schedule_df["DIA"] = extended_schedule_df["DIA"].astype(int)
    return extended_schedule_df


def load_tables_from_path():
    tree = ET.parse(file_path)
    root = tree.getroot()

    data = {}

    def process_grupo(grupo, group_name):
        items = []
        for subgrupo in grupo.findall('grupo_datos'):
            datos = {}
            for dato in subgrupo.findall('dato'):
                nombre_dato = dato.get('nombre_dato')
                datos[nombre_dato] = dato.text
            if datos:
                items.append(datos)
        if items:
            data[group_name] = items

    for grupo in root.findall('.//grupo_datos'):
        seq = grupo.get('seq')
        process_grupo(grupo, seq)

    dataframes = {}
    for key, value in data.items():
        dataframes[key] = pd.DataFrame(value)

    return dataframes

def load_calendario_from_path():
    tree = ET.parse('./generador_horarios/Horario.xml')
    root = tree.getroot()

    all_data = []

    for horario_regular in root.findall(".//grupo_datos[@seq='HORARIOS_REGULARES']"):
        for profesor in horario_regular.findall("grupo_datos"):
            profesor_id = profesor.find("dato[@nombre_dato='X_EMPLEADO']").text if profesor.find(
                "dato[@nombre_dato='X_EMPLEADO']") is not None else ''
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
                all_data.append([
                    profesor_id, dia_semana, tramo, dependencia, unidad, oferta_matrig, materia
                ])

    # Create a DataFrame
    df_calendario = pd.DataFrame(all_data, columns=[
        'ID_PROFESOR', 'DIA', 'ID_TRAMO', 'ID_AULA', 'ID_CLASE', 'ID_CURSO',
        'ID_ACTIVIDAD'
    ])

    df_calendario.loc[:, 'DIA'] = df_calendario['DIA'].astype(int)


    start_date = datetime(2023, 9, 1)
    end_date = datetime(2024, 8, 31)
    date_range = pd.date_range(start=start_date, end=end_date)


    extended_schedule = []


    day_mapping = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5}



    for date in date_range:
        day_of_week = date.weekday()
        if day_of_week in day_mapping:
            day_number = day_mapping[day_of_week]
            daily_schedule = df_calendario[df_calendario['DIA'] == day_number].copy()
            if not daily_schedule.empty:
                daily_schedule['FECHA'] = date
                extended_schedule.append(daily_schedule)
            else:
                print(f"No entries found for day_number {day_number} on date {date}")


    if extended_schedule:
        extended_schedule_df = pd.concat(extended_schedule, ignore_index=True)
    else:
        extended_schedule_df = pd.DataFrame()


    extended_schedule_df = extended_schedule_df.loc[:, ~extended_schedule_df.columns.duplicated()]

    extended_schedule_df["DIA"] = extended_schedule_df["DIA"].astype(int)

    return extended_schedule_df


