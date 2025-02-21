from gpiozero import OutputDevice as Vibration
import MultiToolKit as mtk 
import time

vibration = Vibration(27)
mtk.vibrationBlink(vibration, on_time=0.5, off_time=0.5, n=5)

while True:
    vibration.on()
    print("Módulo de vibración activado")
    time.sleep(1)  
    vibration.off()
    print("Módulo de vibración desactivado")
    time.sleep(1)  

