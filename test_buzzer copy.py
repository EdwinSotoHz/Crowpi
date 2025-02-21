import MultiToolKit as mtk 
from gpiozero import Buzzer
import time

buzzer = Buzzer(18)  

buzzer.on() 
print("on")

time.sleep()

buzzer.off()
print("off")

mtk.buzzerzBeep(buzzer, repeat=5)
#mtk.buzzerzBeep(buzzer, 1, 1, 2)