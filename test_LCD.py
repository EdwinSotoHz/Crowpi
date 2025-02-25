import HD44780MCP
import time
import MCP230XX

i2cAddr = 0x21  # Dirección I2C del MCP23008/17
MCP = MCP230XX.MCP230XX('MCP23008', i2cAddr)

blPin = 7  # Pin de la retroiluminación
MCP.set_mode(blPin, 'output')
MCP.output(blPin, True)

LCD = HD44780MCP.HD44780(MCP, 1, -1, 2, [3, 4, 5, 6], rows=2, characters=16, mode=0, font=0)

try:
    message = "Este es un mensaje que se mueve..."
    while True:
        for i in range(len(message)):
            LCD.clear_display()
            LCD.display_string(message[i:i+16])  # Mostrar 16 caracteres a la vez
            time.sleep(0.3)  # Velocidad del desplazamiento

except KeyboardInterrupt:
    print("Programa terminado")
finally:
    MCP.output(blPin, False)  # Apagar la retroiluminación al finalizar