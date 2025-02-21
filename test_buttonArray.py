from gpiozero import Button, LED
from time import sleep
import MultiToolKit as mtk

rows, cols, key_map = mtk.createButtonArray()
try:
    print("Esperando a que se presione un botón...")
    while True:
        key = mtk.scanButtonArray(rows, cols, key_map) 
        if key and key != '6':
            print(f"Botón presionado: {key}")
        if key == '6':
            print(f"Presionaste específicamente {key}")
        sleep(0.1) 
except KeyboardInterrupt:
    print("Programa terminado")
    
finally:
    for row in rows:
        row.close()
    for col in cols:
        col.close()