from flask import Flask, render_template_string
import time
import MultiToolKit as mtk 
from gpiozero import OutputDevice as Relay

app = Flask(__name__)

button_state = "apagado"

html = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Control de Botones</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; background-color: #222; color: #fff; }
        .button { padding: 20px 40px; font-size: 20px; cursor: pointer; border-radius: 10px; color: white; border: none; margin: 10px; }
        .buttonGreen { background-color: #4CAF50; }
        .buttonRed { background-color: #FF6347; }
        .buttonBlue { background-color: #007BFF; }
        .buttonYellow { background-color: #FFC107; }
    </style>
</head>
<body>
    <h1>Control de Estado del Botón</h1>
    <p>Estado actual del botón: {{ state }}</p>
    <a href="/toggle"><button class="button buttonGreen {{ 'buttonOff' if state == 'encendido' else '' }}">Toggle Estado (Verde)</button></a>
    <a href="/toggle_red"><button class="button buttonRed {{ 'buttonOff' if state == 'encendido' else '' }}">Toggle Estado (Rojo)</button></a>
    <a href="/toggle_blue"><button class="button buttonBlue {{ 'buttonOff' if state == 'encendido' else '' }}">Toggle Estado (Azul)</button></a>
    <a href="/toggle_yellow"><button class="button buttonYellow {{ 'buttonOff' if state == 'encendido' else '' }}">Toggle Estado (Amarillo)</button></a>
</body>
</html>
"""

@app.route('/')
def home():
    print('Accedió a la app') 
    return render_template_string(html, state=button_state)

@app.route('/toggle')
def toggle_button():
    relay = Relay(21)
    global button_state
    if button_state == "apagado":
        button_state = "encendido"
        relay.on()
    else:
        button_state = "apagado"
        relay.off()
        
    print(button_state)  
    return render_template_string(html, state=button_state)

@app.route('/toggle_red')
def toggle_button_red():
    relay = Relay(21)
    global button_state
    if button_state == "apagado":
        
        button_state = "encendido"
        relay.on()
    else:
        button_state = "apagado"
        relay.off()
        
    print(button_state)  
    return render_template_string(html, state=button_state)

@app.route('/toggle_blue')
def toggle_button_blue():
    relay = Relay(21)
    global button_state
    if button_state == "apagado":
        button_state = "encendido"
        relay.on()
    else:
        button_state = "apagado"
        relay.off()
        
    print(button_state)  
    return render_template_string(html, state=button_state)

@app.route('/toggle_yellow')
def toggle_button_yellow():
    relay = Relay(21)
    global button_state
    if button_state == "apagado":
        button_state = "encendido"
        relay.on()
    else:
        button_state = "apagado"
        relay.off()
        
    print(button_state)  
    return render_template_string(html, state=button_state)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)