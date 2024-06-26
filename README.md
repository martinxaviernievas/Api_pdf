# PDF Email API

# FastAPI PDF Extractor

Este proyecto es una API RESTful desarrollada con FastAPI que permite recibir un archivo PDF, extraer las primeras 30 líneas de texto y enviar este contenido a una dirección de correo electrónico proporcionada.

## Requisitos

- Python 3.8 o superior
- FastAPI
- PyPDF2
- Mailtrap (opcional para pruebas de envío de correo)

## Instalación

1. Clona el repositorio:

    ```bash
    git clone https://github.com/martinxaviernievas/Api_pdf.git
    cd Api_pdf
    ```

2. Crea y activa un entorno virtual:

    ```bash
    python -m venv venv
    source venv/bin/activate # En Windows: venv\Scripts\activate
    ```

3. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

## Ejecución

1. Inicia la aplicación FastAPI:

    ```bash
    uvicorn main:app --reload
    ```

2. La API estará disponible en `http://127.0.0.1:8000`.


## Uso de la API

### Prueba rapida:

1. Si queres hacer una prueba rapida la podes hacer a travez de la interfaz de Fastapi en `http://127.0.0.1:8000/docs`.

2. Podes crear una cuenta rapida en Mailtrap que te proporcionara un host,usuario y contraseña para que modifiques en las partes indicadas en el codigo de enviar_email.pdf y siguiendo las pasos de la interfaz de Fastapi.


### Endpoint: `POST /upload`

Este endpoint permite subir un archivo PDF, extraer las primeras 30 líneas y enviar el contenido a un correo electrónico.

#### Solicitud

- **URL**: `http://127.0.0.1:8000/upload`
- **Método**: `POST`
- **Encabezados**: `Content-Type: multipart/form-data`
- **Cuerpo**:
    - `archivo`: El archivo PDF a subir.
    - `email`: La dirección de correo electrónico a la que se enviará el contenido extraído.

#### Ejemplo de solicitud

```http
POST /upload HTTP/1.1
Host: 127.0.0.1:8000
Content-Type: multipart/form-data

{
    "file": <pdf-file>,
    "email": "example@example.com"
}

Respuesta esperada:

{
    "success": true,
    "message": "El correo se ha enviado exitosamente a example@example.com" 
}
```

# Detalles de los Endpoints

## POST /upload

**Descripción**: Carga un archivo PDF, extrae las primeras 30 líneas de texto y envía el contenido por correo electrónico.

**Parámetros**:
- `archivo` (form-data, requerido): El archivo PDF a subir.
- `correo` (form-data, requerido): La dirección de correo electrónico a la que se enviará el contenido extraído.

**Respuestas**:
- `200 OK`: Éxito. El correo se ha enviado correctamente.
- `400 Bad Request`: Error. El archivo no es un PDF.
- `500 Internal Server Error`: Error al extraer el texto o al enviar el correo.

## Notas

- **Correo Electrónico**: Para pruebas de envío de correo, se recomienda usar Mailtrap o una configuración SMTP similar.
- **Seguridad**: Asegúrate de manejar correctamente las credenciales y la información sensible en un entorno de producción.
