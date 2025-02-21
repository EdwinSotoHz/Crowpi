# Lección: Uso del Sensor de Tacto (Touch Sensor)
from gpiozero import Button
import time

# Configurar el sensor de tacto en el pin GPIO 17
touch_sensor = Button(17)

try:
    while True:
        if touch_sensor.is_pressed:
            print("Sensor de tacto presionado")
        else:
            print("Sensor de tacto no presionado")
        time.sleep(0.1)  # Pequeño delay para evitar lecturas repetidas

except KeyboardInterrupt:
    print("Programa terminado")