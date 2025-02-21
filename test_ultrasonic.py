# Lección: Uso del Sensor Ultrasónico (Ultrasonic Sensor)
from gpiozero import DistanceSensor
import time

# Configurar el sensor ultrasónico (ECHO: GPIO 12, TRIG: GPIO 16)
ultrasonic_sensor = DistanceSensor(echo=12, trigger=16)

try:
    while True:
        distance = ultrasonic_sensor.distance * 100  # Convertir a centímetros
        print(f"Distancia: {distance:.2f} cm")
        time.sleep(1)  # Esperar 1 segundo antes de la siguiente lectura

except KeyboardInterrupt:
    print("Programa terminado")