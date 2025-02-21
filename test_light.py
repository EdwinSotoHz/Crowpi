import MultiToolKit as mtk 
import smbus
import time

lightBus = smbus.SMBus(1)

try:
    while True:
        light_level = mtk.read_light(lightBus)
        print(f"Light Level: {light_level} lx")
        time.sleep(0.5)
except KeyboardInterrupt:
    print("Programa terminado")