from flask import Flask, render_template, request
from flask_mail import Mail, Message
from cliente import Cliente
from ventana import Ventana
from cotizacion import Cotizacion
from fpdf import FPDF
import os

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'  
app.config['MAIL_PORT'] = 587  
app.config['MAIL_USE_TLS'] = True  
app.config['MAIL_USERNAME'] = 'tu_correo@gmail.com'  
app.config['MAIL_PASSWORD'] = 'tu_contraseña' 
app.config['MAIL_DEFAULT_SENDER'] = 'tu_correo@gmail.com'

mail = Mail(app)

@app.route('/', methods=['GET'])
def inicio():
    return render_template('index.html')

@app.route('/cotizacion', methods=['GET', 'POST'])
def cotizacion():
    if request.method == 'POST':
        nombre_cliente = request.form['nombre']
        empresa_cliente = request.form['empresa']
        cantidad_ventanas = int(request.form['cantidad_ventanas'])

        estilo = request.form['estilo']
        ancho = float(request.form['ancho'])
        alto = float(request.form['alto'])
        acabado = request.form['acabado']
        tipo_vidrio = request.form['tipo_vidrio']
        esmerilado = request.form.get('esmerilado') == 'on'

        cliente = Cliente(nombre_cliente, empresa_cliente, cantidad_ventanas)

        ventanas = [Ventana(estilo, ancho, alto, acabado, tipo_vidrio, esmerilado) for _ in range(cantidad_ventanas)]
        
        cotizacion = Cotizacion(cliente, ventanas)
        total = cotizacion.calcular_total()

        return render_template('resumen.html', cliente=cliente, total=total, ventanas=ventanas)

    return render_template('cotizacion.html')

def generar_pdf(cliente, total, ventanas):
    pdf = FPDF()
    pdf.add_page()
    pdf.add_font('Arial', 'B', 'C:\Windows\Fonts\Arial', uni=True) 
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Resumen de Cotización", ln=True, align='C')
    pdf.cell(200, 10, txt=f"Cliente: {cliente.nombre}", ln=True)
    pdf.cell(200, 10, txt=f"Empresa: {cliente.empresa}", ln=True)
    pdf.cell(200, 10, txt=f"Cantidad de ventanas: {cliente.cantidad_ventanas}", ln=True)

    pdf.cell(200, 10, txt="Detalles de las Ventanas (Aplicados globalmente):", ln=True)
    pdf.cell(200, 10, txt=f"Estilo: {ventanas[0].estilo}", ln=True)
    pdf.cell(200, 10, txt=f"Ancho: {ventanas[0].ancho} cm", ln=True)
    pdf.cell(200, 10, txt=f"Alto: {ventanas[0].alto} cm", ln=True)
    pdf.cell(200, 10, txt=f"Acabado: {ventanas[0].acabado}", ln=True)
    pdf.cell(200, 10, txt=f"Tipo de Vidrio: {ventanas[0].tipo_vidrio}", ln=True)
    pdf.cell(200, 10, txt=f"Esmerilado: {'Sí' if ventanas[0].esmerilado else 'No'}", ln=True)
    pdf.cell(200, 10, txt=f"Total: ${total}", ln=True)

    pdf_dir = r"C:\Users\AKBAR\Desktop\cotizaciones_ventanas"  
    pdf_file_path = os.path.join(pdf_dir, f"{cliente.nombre}_cotizacion.pdf")
    pdf.output(pdf_file_path)

    return pdf_file_path

@app.route('/enviar_correo', methods=['POST'])
def enviar_correo():
    nombre_cliente = request.form['nombre']
    empresa_cliente = request.form['empresa']
    cantidad_ventanas = int(request.form['cantidad_ventanas'])
    estilo = request.form['estilo']
    ancho = float(request.form['ancho'])
    alto = float(request.form['alto'])
    acabado = request.form['acabado']
    tipo_vidrio = request.form['tipo_vidrio']
    esmerilado = request.form.get('esmerilado') == 'on'
    destinatario = request.form['email']

    cliente = Cliente(nombre_cliente, empresa_cliente, cantidad_ventanas)
    ventanas = [Ventana(estilo, ancho, alto, acabado, tipo_vidrio, esmerilado) for _ in range(cantidad_ventanas)]

    cotizacion = Cotizacion(cliente, ventanas)
    total = cotizacion.calcular_total()

    pdf_file_path = generar_pdf(cliente, total, ventanas)

    msg = Message("Cotización de Ventanas", recipients=[destinatario])
    msg.body = f"Hola {nombre_cliente},\n\nAdjunto encontrarás la cotización para tu solicitud.\n\nSaludos."
    
    msg.charset = 'utf-8'

    with app.open_resource(pdf_file_path) as pdf:
        msg.attach(os.path.basename(pdf_file_path), "application/pdf", pdf.read())

    mail.send(msg)

    os.remove(pdf_file_path)

    return "Correo enviado exitosamente!"

@app.route('/generar_pdf', methods=['POST'])
def generar_pdf_route():
    nombre_cliente = request.form['nombre']
    empresa_cliente = request.form['empresa']
    cantidad_ventanas = int(request.form['cantidad_ventanas'])
    estilo = request.form['estilo']
    ancho = float(request.form['ancho'])
    alto = float(request.form['alto'])
    acabado = request.form['acabado']
    tipo_vidrio = request.form['tipo_vidrio']
    esmerilado = request.form.get('esmerilado') == 'on'

    cliente = Cliente(nombre_cliente, empresa_cliente, cantidad_ventanas)
    ventanas = [Ventana(estilo, ancho, alto, acabado, tipo_vidrio, esmerilado) for _ in range(cantidad_ventanas)]

    cotizacion = Cotizacion(cliente, ventanas)
    total = cotizacion.calcular_total()

    pdf_file_path = generar_pdf(cliente, total, ventanas)

    if pdf_file_path:
        return f"PDF generado exitosamente: {pdf_file_path}"
    else:
        return "Error al generar el PDF."

if __name__ == '__main__':
    app.run(debug=True)

