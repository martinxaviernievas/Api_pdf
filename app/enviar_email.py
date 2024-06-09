import smtplib
from email.mime.text import MIMEText

def enviar_email(destinatario: str, contenido: str):
    """
    Envia un correo con el contenido especificado al destinatario.
    :param destinatario: Direccion de correo (destinatario)
    :param contenido: Contenido del email.
    """

    remitente = "ejemplo@gmail.com o usuario de Mailtrap" #Cambiar por tu correo, sea el real o uno creado artificialmente
    contrasena =  "contraseña de aplicacion o Pass de Mailtrap" # Cambiar por tu contraseña del correo electronico

    #Crear el mensaje MIME
    msg = MIMEText(contenido)
    msg["Subject"] = "Contenido extraido del PDF"
    msg["From"] = remitente
    msg["To"] = destinatario

    # Conectar con el servidor SMTP y enviar el correo
    with smtplib.SMTP("smtp.mailtrap.io",2525) as servidor: # Ejemplo con Mailtrap
        servidor.login("Usuario o email","Contraseña") # Ejemplo con Mailtrap
        servidor.sendmail(remitente,destinatario, msg.as_string())