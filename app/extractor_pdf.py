import PyPDF2
import io

def extraer_primeras_30_lineas(contenido_pdf: bytes) -> str:
    """
    Extrae las primeras 30 lineas de texto de un archivo PDF.

    :parem contenido_pdf: Contenido del archivo PDF en bytes.
    :return: Texto extraido de las primeras 30 lineas del PDF.
    """
    lector_pdf = PyPDF2.PdfReader(io.BytesIO(contenido_pdf))
    texto = ""
    for num_pagina in range(min(30,lector_pdf.numPages)):
        pagina = lector_pdf.getPage(num_pagina)
        texto += pagina.extract_text() + "\n"
    return texto
