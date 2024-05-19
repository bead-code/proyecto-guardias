import xml.etree.ElementTree as ET
import pandas as pd

from db.database import Session

file_path = './generador_horarios/Exportacion_hacia_generadores_de_horarios.xml'

def parse_xml_to_dataframes():
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


