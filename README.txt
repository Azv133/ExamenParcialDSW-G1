## Indicaciones para desplegar la web

1. Crear el archivo .env y llenar los datos según como se creó la base de datos, como se muestra a continuación:
USER = TUUSUARIO
PASSWORD = TUPWD
DATABASE = NOMBREBD
HOST = IPSERVER
SERVER = postgresql

#Ejemplo:
USER = postgres
PASSWORD = 123456
DATABASE = G1DSW
HOST = localhost:5432
SERVER = postgresql

2. Ingresar a la carpeta donde tenemos todos los archivos de la appWeb
cd ruta_de_carpeta

3. Crear el entorno virtual con el siguiente comando:
virtualenv venv

4. Activar el entorno virtual:
venv\Scripts\activate

5. Con el entorno activado (venv), instalamos los requerimientos, utilziando el siguiente comando:
pip install -r requirements.txt

6. Finalmente, desplegamos la aplicación web con el siguiente comando:
flask run