# Mejora: Implementación de Envío de Correo y Creación de PDF

## Descripción de la Mejora

Esta mejora incluye la implementación de dos características clave en la aplicación de cotización de ventanas:

1. **Envío de Cotización por Correo Electrónico**
2. **Generación de un Archivo PDF con la Cotización**

## 1. Envío de Cotización por Correo Electrónico

### Funcionalidad

Los usuarios pueden recibir su cotización por correo electrónico tras enviar el formulario. Esta funcionalidad se implementa utilizando la extensión Flask-Mail.

### Implementación

- Se configuró Flask-Mail en la aplicación Flask para gestionar el envío de correos electrónicos.
- Se creó una ruta `/enviar_correo` que maneja el envío del correo electrónico al destinatario con el PDF adjunto.
- El mensaje de correo incluye un saludo personalizado y un archivo PDF que resume la cotización.

### Código

El siguiente fragmento muestra cómo se envía el correo:

```python
@app.route('/enviar_correo', methods=['POST'])
def enviar_correo():
    # Recopilar datos del formulario
    destinatario = request.form['email']
    # Generar el PDF
    pdf_file_path = generar_pdf(cliente, total, ventanas)
    
    msg = Message("Cotización de Ventanas", recipients=[destinatario])
    msg.body = f"Hola {nombre_cliente},\n\nAdjunto encontrarás la cotización para tu solicitud.\n\nSaludos."
    with app.open_resource(pdf_file_path) as pdf:
        msg.attach(os.path.basename(pdf_file_path), "application/pdf", pdf.read())
    mail.send(msg)
