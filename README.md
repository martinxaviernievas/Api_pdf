# PDF Email API

## Descripción
Este proyecto es una API RESTful desarrollada en Python utilizando FastAPI. La API permite recibir un archivo PDF, extraer las primeras 30 líneas de contenido y enviar ese contenido a una dirección de correo electrónico proporcionada.


## Requisitos
- Python 3.8+
- FastAPI
- Uvicorn
- PyPDF2


## Instalación

1. Clonar el repositorio:
    ```sh
    git clone https://github.com/martinxaviernievas/Api_pdf.git
    cd Api_pdf
    ```

2. Crear un entorno virtual y activarlo:
    ```sh
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```

3. Instalar las dependencias:
    ```sh
    pip install -r requirements.txt
    ```

## Configuracion:


1. En enviar_email.py modificar lo siguiente:

   remitente = "ejemplo@gmail.com o usuario de Mailtrap" 
   contrasena =  "contraseña de aplicacion o Pass de Mailtrap" 
   Tambien:
   with smtplib.SMTP("smtp.mailtrap.io",2525) as servidor: # Ejemplo con Mailtrap
   servidor.login("Usuario o email","Contraseña") # Ejemplo con Mailtrap
 

## Ejecución

1. Iniciar el servidor:
    ```sh
    uvicorn app.main:app --reload
    ```

2. Prueba de forma rapida a la interfaz de FastApi a esta direcion : http://127.0.0.1:8000/docs


## Endpoint: /upload
    Este endpoint permite subir un archivo PDF y enviar el contenido extraído por correo electrónico.

## Parámetros
    archivo: Archivo PDF a subir.
    correo: Dirección de correo electrónico para enviar el contenido.

### Ejemplo de Solicitud
```http
POST /upload
Content-Type: multipart/form-data

{
    "file": <pdf-file>,
    "email": "example@example.com"
}