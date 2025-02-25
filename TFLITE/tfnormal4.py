import tensorflow as tf
import cv2
import numpy as np

# Cargar el modelo TFLite
interpreter = tf.lite.Interpreter(model_path="yolov5s_f16.tflite")
interpreter.allocate_tensors()

# Obtener detalles de la entrada y salida
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

capture = cv2.VideoCapture(0)

while True:
    # Captura
    isSuccessfulCapture, frameInfo = capture.read()
    if not isSuccessfulCapture:
        break

    contrast = 1.8  # 1 = Normal
    brightness = -5  # 0 = Normal
    frameInfoModified = cv2.convertScaleAbs(frameInfo, alpha=contrast, beta=brightness)

    # BGR (OpenCV) a RGB (modelo)
    frameInfo_rgb = cv2.cvtColor(frameInfoModified, cv2.COLOR_BGR2RGB)

    # Preparar el tensor de entrada
    input_frame = frameInfo_rgb.astype('float32')  # Convertir a float32
    input_frame /= 255.0  # Normalizar
    input_frame = np.expand_dims(input_frame, axis=0)  # Añadir batch dimension

    # Establecer la entrada del modelo
    interpreter.set_tensor(input_details[0]['index'], input_frame)
    interpreter.invoke()

    # Obtener resultados
    output_data = interpreter.get_tensor(output_details[0]['index'])

    # Procesar detecciones
    # Asegúrate de que las salidas están correctamente interpretadas según tu modelo
    detections = output_data[0]  # Ajusta este índice según la salida de tu modelo

    # Filtrar personas (si es que el modelo las clasifica)
    detections = [detection for detection in detections if detection[0] == 0]  # Filtrar por clase '0' (persona)

    if len(detections) > 0:
        print("Si hay personas")
    else:
        print("No hay personas")

    # Dibujar detecciones
    for detection in detections:
        x1, y1, x2, y2, conf, cls = detection
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        cv2.rectangle(frameInfoModified, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frameInfoModified, f"Persona {conf:.2f}", (x1, y1 - 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Mostrar el frame
    window_width = 650
    window_height = 520
    frameInfo_resized = cv2.resize(frameInfoModified, (window_width, window_height))

    cv2.namedWindow('YOLOv5 OpenCV', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('YOLOv5 OpenCV', window_width, window_height)
    cv2.imshow('YOLOv5 OpenCV', frameInfo_resized)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar camara y cerrar ventanas
capture.release()
cv2.destroyAllWindows()
