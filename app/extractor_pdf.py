import PyPDF2
import io

def extraer_primeras_30_lineas(contenido_pdf: bytes) -> str:
    """
    Extrae las primeras 30 líneas de texto de un archivo PDF.

    :param contenido_pdf: Contenido del archivo PDF en bytes.
    :return: Texto extraído de las primeras 30 líneas del PDF.
    """
    lector_pdf = PyPDF2.PdfReader(io.BytesIO(contenido_pdf))
    texto = ""
    for num_pagina in range(min(30, len(lector_pdf.pages))):
        pagina = lector_pdf.pages[num_pagina]
        texto += pagina.extract_text() + "\n"
    return texto

