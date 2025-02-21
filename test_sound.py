import MultiToolKit as mtk 
from gpiozero import DigitalInputDevice as Sound
import time

sound = Sound(24)

#sound.wait_for_active() 
#sound.wait_for_inactive() 

try:
    while True:
        if sound.value == 0:
            print("Sonido detectado")
        elif sound.value == 1:
            print("Sonido NO detectado")
        time.sleep(0.1)  
        
except KeyboardInterrupt:
    print("Programa terminado")
