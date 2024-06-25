# Usar una imagen base oficial de Python
FROM python:3.12.3-alpine

# Establecer el directorio de trabajo en el contenedor
WORKDIR /back

# Copiar los archivos de back menos la carpeta .venv
COPY . /back

# Instalar las dependencias del proyecto
RUN pip install --no-cache-dir --upgrade -r docker/requirements.txt

# Comando para ejecutar la aplicación usando uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]