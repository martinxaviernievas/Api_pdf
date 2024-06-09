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
    git clone https://github.com/tu_usuario/pdf_email_api.git
    cd pdf_email_api
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

1. En extractor_pdf.py
   Modifica lo siguiente: 

## Ejecución

1. Iniciar el servidor:
    ```sh
    uvicorn app.main:app --reload
    ```

2. La API estará disponible en `http://127.0.0.1:8000/docs`.

## Uso

Enviar una solicitud `POST` a `/upload` con un archivo PDF y un email:
En donde dice Try Out ingrese: El PDF que desee
ingrese el mail del remitente ( Te recomiendo Mailtrap)

### Ejemplo de Solicitud
```http
POST /upload
Content-Type: multipart/form-data

{
    "file": <pdf-file>,
    "email": "example@example.com"
}