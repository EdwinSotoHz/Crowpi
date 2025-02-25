import HD44780MCP
import time
import MCP230XX

i2cAddr = 0x21
MCP = MCP230XX.MCP230XX('MCP23008', i2cAddr)

# Encender la retroiluminación del LCD
blPin = 7  # Pin de la retroiluminación
MCP.set_mode(blPin, 'output')
MCP.output(blPin, True)

LCD = HD44780MCP.HD44780(MCP, 1, -1, 2, [3, 4, 5, 6], rows=2, characters=16, mode=0, font=0)

try:
    LCD.display_string("Hola, CrowPi!")
    time.sleep(5)  # Mostrar el mensaje durante 5 segundos

    # Limpiar el LCD
    LCD.clear_display()

except KeyboardInterrupt:
    print("Programa terminado")
finally:
    MCP.output(blPin, False)  # Apagar la retroiluminación al finalizar