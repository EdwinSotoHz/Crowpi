import cv2
import numpy as np
import tensorflow as tf

# Cargar el modelo TFLite
interpreter = tf.lite.Interpreter(model_path="efficientdet_lite0.tflite")
interpreter.allocate_tensors()

# Obtener el índice de los tensores de entrada y salida
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Iniciar la captura de video
capture = cv2.VideoCapture(0)

while True:
    # Captura
    isSuccessfulCapture, frame = capture.read()
    if not isSuccessfulCapture:
        break
    
    # Ajuste de contraste y brillo
    contrast = 1.8  # 1 = Normal
    brightness = -5  # 0 = Normal
    frame_modified = cv2.convertScaleAbs(frame, alpha=contrast, beta=brightness)

    # Preparar la imagen para la entrada del modelo
    image_rgb = cv2.cvtColor(frame_modified, cv2.COLOR_BGR2RGB)
    image_resized = cv2.resize(image_rgb, (320, 320))  # Redimensionar para el modelo

    # Normalizar y convertir la imagen a UINT8
    image_normalized = np.array(image_resized, dtype=np.float32)  # Convertir a float32
    image_normalized = (image_normalized / 255.0) * 255  # Normalizar a 0-255 y luego escalar
    image_uint8 = image_normalized.astype(np.uint8)  # Convertir a UINT8

    # Expansión para que tenga la forma [1, 320, 320, 3]
    image_np = np.expand_dims(image_uint8, axis=0)

    # Ejecutar la inferencia
    interpreter.set_tensor(input_details[0]['index'], image_np)
    interpreter.invoke()

    # Obtener las detecciones
    boxes = interpreter.get_tensor(output_details[0]['index'])[0]  # Coordenadas de la caja
    classes = interpreter.get_tensor(output_details[1]['index'])[0]  # Clases de objetos
    scores = interpreter.get_tensor(output_details[2]['index'])[0]  # Confianza de la predicción

    # Filtrar solo las detecciones de personas (clase 0)
    person_detected = False
    for i in range(len(scores)):
        if scores[i] > 0.5:  # Filtrar detecciones con más del 50% de confianza
            class_id = int(classes[i])
            if class_id == 0:  # 0 es "persona" en EfficientDet
                person_detected = True
                ymin, xmin, ymax, xmax = boxes[i]
                xmin, xmax = int(xmin * frame.shape[1]), int(xmax * frame.shape[1])
                ymin, ymax = int(ymin * frame.shape[0]), int(ymax * frame.shape[0])

                # Dibujar el rectángulo
                cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)
                label = f"Persona: {scores[i]:.2f}"
                cv2.putText(frame, label, (xmin, ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                break  # Detener la búsqueda si ya se detectó una persona

    if person_detected:
        print("¡Persona detectada!")
    else:
        print("No persona")

    # Escalar la imagen de la ventana
    window_width = 650
    window_height = 520
    frame_resized = cv2.resize(frame, (window_width, window_height))

    # Mostrar la ventana
    cv2.namedWindow('EfficientDet-Lite0 OpenCV', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('EfficientDet-Lite0 OpenCV', window_width, window_height)
    cv2.imshow('EfficientDet-Lite0 OpenCV', frame_resized)

    # Salir
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar las ventanas
capture.release()
cv2.destroyAllWindows()
