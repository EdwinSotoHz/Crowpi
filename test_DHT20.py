from DFRobot_DHT20 import DFRobot_DHT20
import MultiToolKit as mtk
import time

try:
    while True:
        temperature, humidity, crc_error = mtk.read_dht20("temperature_and_humidity")

        if crc_error:
            print("Error: CRC no válido")
        else:
            temperature_f = temperature * 9 / 5 + 32

            print(f"Temperatura: {temperature:.2f}°C / {temperature_f:.2f}°F")
            print(f"Humedad Relativa: {humidity:.2f}%")

        time.sleep(5)

except KeyboardInterrupt:
    print("Programa terminado")