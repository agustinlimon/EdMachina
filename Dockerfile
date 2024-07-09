FROM python:3.11-slim

#* Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

#* Copia los archivos de requerimientos y los instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#* Copia el resto de la aplicación
COPY . .

#* Expone el puerto en el que la aplicación correrá
EXPOSE 8000

#* Comando para correr la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]