# Usa una imagen base con Node.js
FROM node:18-alpine

# Establecer el directorio de trabajo en el contenedor
WORKDIR /frontend

# Copia el package.json y el package-lock.json
COPY package*.json ./

# Instala las dependencias
RUN npm install

# Copia el resto de los archivos de la aplicación
COPY . /frontend

# Construye la aplicación
RUN npm run build

EXPOSE 4173

# Comando por defecto para correr la aplicación
CMD ["npm", "run", "preview", "--", "--host"]
