from gpiozero import Button, Buzzer, LED
from DFRobot_DHT20 import DFRobot_DHT20
import time
import smbus


def buzzerzBeep(buzzer, on_time=0.2, off_time=0.2, repeat=5):
    for _ in range(repeat):
        buzzer.on()
        print('beep')###
        time.sleep(on_time)
        buzzer.off()
        time.sleep(off_time)



def createIndepententsButtons():
    buttons = {
        "UP": Button(26),
        "DOWN": Button(13),
        "RIGHT": Button(19),
        "LEFT": Button(25)
    }
    return buttons



def createButtonArray():
    rows = [Button(27), Button(22), Button(5), Button(6)] 
    cols = [Button(25), Button(26), Button(19), Button(13)]
    
    button_matrix = [[(row, col) for col in cols] for row in rows]
    return button_matrix

def isPressed(button):
    row, col = button
    return row.is_pressed and col.is_pressed

def isReleased(button):
    row, col = button
    return row.is_released and col.is_released



def relayBlink(relay, on_time=1, off_time=1, n=None):
    count = 0
    while n is None or count < n:
        relay.on()
        print("Relay activado (circuito abierto)")
        time.sleep(on_time)
        relay.off()
        print("Relay desactivado (circuito cerrado)")
        time.sleep(off_time)
        count += 1


def vibrationBlink(vibration_motor, on_time=1, off_time=1, n=None):
    count = 0
    while n is None or count < n:
        vibration_motor.on()
        print("Módulo de vibración activado")
        time.sleep(on_time)
        vibration_motor.off()
        print("Módulo de vibración desactivado")
        time.sleep(off_time)
        count += 1



def createButtonArray():
    row_pins = [27, 22, 5, 6]  # Filas/entradas
    col_pins = [25, 26, 19, 13]  # Columnas/salidas

    key_map = [
        ['1', '2', '3', '4'],
        ['5', '6', '7', '8'],
        ['9', '10', '11', '12'],
        ['13', '14', '15', '16']
    ]

    rows = [Button(pin, pull_up=True) for pin in row_pins]
    cols = [LED(pin) for pin in col_pins]

    return rows, cols, key_map 

def scanButtonArray(rows, cols, key_map):
    for col_index, col in enumerate(cols):
        col.off()  
        for row_index, row in enumerate(rows):
            if row.is_active:
                return key_map[row_index][col_index]  # Devolver la tecla correspondiente
        col.on() 
    return None 

def read_light(lightBus, mode = 0x11):
    SENSOR_ADDRESS = 0x5C
    MEASUREMENT_MODE = mode
    data = lightBus.read_i2c_block_data(SENSOR_ADDRESS, MEASUREMENT_MODE, 2)
    light_level = (data[1] + (256 * data[0])) / 1.2
    return light_level


def read_dht20(mode="temperature_and_humidity"):
    I2C_BUS = 0x01  
    I2C_ADDRESS = 0x38  

    dht20 = DFRobot_DHT20(I2C_BUS, I2C_ADDRESS)

    if mode == "temperature_and_humidity":
        return dht20.get_temperature_and_humidity()
    elif mode == "temperature":
        return dht20.get_temperature()
    elif mode == "humidity":
        return dht20.get_humidity()
    else:
        raise ValueError("Modo no válido. Usa 'temperature_and_humidity', 'temperature' o 'humidity'.")
