from gpiozero import DigitalInputDevice as MOTION
import time

motion = MOTION(23)

while True:
   if(motion.value == 0):
         print("Nothing moves ...")
   elif(motion.value == 1):
         print("Motion detected!")
   time.sleep(0.1)