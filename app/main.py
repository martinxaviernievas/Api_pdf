#Parametros a tener en cuenta para resolver la prueba tecnica:
'''
Technical Test: Python/Node
Objective:
The objective of this technical test is to assess the candidate's proficiency in Python or Node.js and their ability to develop a RESTful API that works with automation libraries
Requirements:
Develop a RESTful API using Node or Python
The API should include the following functionalities:
Receive a PDF file.
Extract the first 30 lines of the PDF.
Send an email with the extracted content to the provided email address.
Instructions:
The candidate can choose between Node and Python.
Include a README.md file with instructions for installing dependencies, running the project, and any other relevant details.
The project should be uploaded to a public GitHub repository.
Delivery time is 3 working days.
Example Endpoint:
Request (Node.js or Python):
http
POST /upload
Content-Type: multipart/form-data

{
    "file": <pdf-file>,
    "email": "example@example.com"
}

Expected Response:
{
    "success": true,
    "message": "The email has been successfully sent to example@example.com"
}


'''

from fastapi import FastAPI, UploadFile, Form, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.extractor_pdf import extraer_primeras_30_lineas
from app.enviar_email import enviar_email



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload")
async def subir_pdf(archivo: UploadFile, correo: str = Form(...)):

    """
    Carga un archivo PDF, extrae las primeras 30 lineas de texto y envia el contenido por correo electronico
    :param del archivo : Archivo PDF cargado
    :param correo : Direccion de correo electronico para enviar el contenido.
    return: JSONResponse indicando el exito de la operacion.
    """

    if archivo.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Tipo de archivo invalido. Solo se permiten archivos PDF.")

    contenido = await archivo.read()
    try:
        texto_extraido = extraer_primeras_30_lineas(contenido)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al extraer texto del PDF: {str(e)}")
    
    try:
        enviar_email(correo, texto_extraido)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al enviar el correo: {str(e)}")
    
    return JSONResponse(content={"exito": True, "mensaje": f"El correo se ha enviado exitosamente a {correo}"})

    