import MultiToolKit as mtk 
from gpiozero import Button
import time

#independentButtons = mtk.createIndepententsButtons()
#independentButtons["UP"].is_pressed

btnUp = Button(26)
btnDown = Button(13)
btnRight = Button(19)
btnLeft = Button(25)

print("Boton UP: Esperando a ser presionado")
btnUp.wait_for_press() 
print("Boton UP: Presionado")

print("Boton UP: Esperando a ser soltado")
btnUp.wait_for_release()
print("Boton UP: soltado")

try:
    while True:
        if btnUp.is_pressed:
            print("Botón UP presionado")
        elif btnDown.is_pressed:
            print("Botón DOWN presionado")
        elif btnRight.is_pressed:
            print("Botón RIGHT soltado")
        elif btnLeft.is_pressed:
            print("Botón LEFT soltado")
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Programa terminado")
    
