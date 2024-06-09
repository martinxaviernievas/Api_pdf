import smtplib
from email.mime.text import MIMEText

def enviar_email(destinatario: str, contenido: str):
    """
    Envia un correo con el contenido especificado al destinatario.
    :param destinatario: Direccion de correo (destinatario)
    :param contenido: Contenido del email.
    """

    remitente = "c2e1ae89cd8a78" #Cambiar por tu correo, sea el real o uno creado artificialmente
    contrasena =  "3b2b998e464fcd" # Cambiar por tu contraseña del correo electronico

    #Crear el mensaje MIME
    msg = MIMEText(contenido)
    msg["Subject"] = "Contenido extraido del PDF"
    msg["From"] = remitente
    msg["To"] = destinatario

    # Conectar con el servidor SMTP y enviar el correo
    with smtplib.SMTP("sandbox.smtp.mailtrap.io",2525) as servidor: # Ejemplo con Mailtrap
        servidor.login("c2e1ae89cd8a78","3b2b998e464fcd")
        servidor.sendmail(remitente,destinatario, msg.as_string())