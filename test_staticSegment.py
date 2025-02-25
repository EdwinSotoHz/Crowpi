#!/usr/bin/env python3
from ht16k33segment_python import HT16K33Segment
import smbus
import time

# Configurar el Segment LED (I2C, dirección 0x70)
i2c = smbus.SMBus(1)
led = HT16K33Segment(i2c)
led.set_brightness(15)

try:
    # Mostrar un número fijo en el Segment LED
    led.set_number(8, 0, True)
    led.set_number(8, 1, True)
    led.set_number(8, 2, True)
    led.set_number(8, 3, True)
    led.set_colon(True)
    led.update()
    time.sleep(5)  # Mostrar el número durante 5 segundos

except KeyboardInterrupt:
    print("Programa terminado")
finally:
    led.clear()  # Limpiar el Segment LED al finalizar