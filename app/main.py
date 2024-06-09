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

@app.post("/subir")
async def subir_pdf(archivo: UploadFile, correo: str = Form(...)):
    """
    Carga un archivo PDF, extrae las primeras 30 lineas de texto y envia el contenido por correo electronico
    parametro del archivo : Archivo PDF cargado
    parametro correo : Direccion de correo electronico para enviar el contenido.
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

    