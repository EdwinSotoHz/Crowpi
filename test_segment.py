#!/usr/bin/env python3
from ht16k33segment_python import HT16K33Segment
import smbus
import time

# Configurar el Segment LED (I2C, dirección 0x70)
i2c = smbus.SMBus(1)
led = HT16K33Segment(i2c)
led.set_brightness(15)

try:
    # Mostrar un mensaje que se mueve en el Segment LED
    message = "1234"
    while True:
        for i in range(len(message)):
            led.clear()
            led.set_char(message[i], i)
            led.update()
            time.sleep(0.5)  # Velocidad del desplazamiento

except KeyboardInterrupt:
    print("Programa terminado")
finally:
    led.clear()  # Limpiar el Segment LED al finalizar