import cv2
import numpy as np
import tflite_runtime.interpreter as tflite

# Cargar el modelo TFLite
interpreter = tflite.Interpreter(model_path="efficientdet_lite0.tflite")
interpreter.allocate_tensors()

# Obtener detalles de entrada y salida
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Dimensiones de entrada del modelo
input_shape = input_details[0]['shape']
height, width = input_shape[1], input_shape[2]

# Inicializar la captura de video
capture = cv2.VideoCapture(0)

while True:
    # Captura de frame
    ret, frame = capture.read()
    if not ret:
        break

    # Redimensionar el frame al tamaño de entrada del modelo
    input_frame = cv2.resize(frame, (width, height))
    input_frame = np.expand_dims(input_frame, axis=0).astype(np.uint8)  # [1, 320, 320, 3]

    # Realizar la detección
    interpreter.set_tensor(input_details[0]['index'], input_frame)
    interpreter.invoke()

    # Obtener resultados
    boxes = interpreter.get_tensor(output_details[0]['index'])[0]  # Coordenadas de las cajas
    classes = interpreter.get_tensor(output_details[1]['index'])[0]  # Clases detectadas
    scores = interpreter.get_tensor(output_details[2]['index'])[0]  # Confianza de detección

    # Dibujar las cajas de detección en la imagen
    for i in range(len(scores)):
        if scores[i] > 0.5:  # Filtrar detecciones con más del 50% de confianza
            ymin, xmin, ymax, xmax = boxes[i]  # Coordenadas normalizadas
            xmin, xmax = int(xmin * frame.shape[1]), int(xmax * frame.shape[1])
            ymin, ymax = int(ymin * frame.shape[0]), int(ymax * frame.shape[0])

            # Dibujar rectángulo en la imagen
            cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)
            label = f"Clase {int(classes[i])}: {scores[i]:.2f}"
            cv2.putText(frame, label, (xmin, ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Mostrar el frame con detecciones
    cv2.imshow("EfficientDet-Lite0 TFLite", frame)

    # Presionar 'q' para salir
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
capture.release()
cv2.destroyAllWindows()
