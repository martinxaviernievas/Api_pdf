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

