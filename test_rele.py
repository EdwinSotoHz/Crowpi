import MultiToolKit as mtk 
from gpiozero import OutputDevice as Relay
import time

relay = Relay(21)

relay.on() # Activar
print("Relay activado (circuito abierto)")
time.sleep(1)
relay.off() # Desactivar
print("Relay desactivado (circuito cerrado)")


relay.toggle() # Cambiar el estado del relay
print("Relay activado (circuito abierto)")

mtk.relayBlink(relay, 0.5, 0.5, 5) # Activar/desactivar en intervalos