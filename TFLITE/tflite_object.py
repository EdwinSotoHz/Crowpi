import cv2
import numpy as np
import tflite_runtime.interpreter as tflite

# Cargar el modelo TensorFlow Lite personalizado
model_path = "best.tflite"  # Cambia esto por tu modelo personalizado
interpreter = tflite.Interpreter(model_path=model_path)
interpreter.allocate_tensors()

# Obtener detalles de entrada y salida
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Tamaño de entrada del modelo
input_shape = input_details[0]['shape'][1:3]

# Iniciar la cámara
capture = cv2.VideoCapture(0)

while True:
    # Capturar frame
    isSuccessfulCapture, frame = capture.read()
    if not isSuccessfulCapture:
        break

    # Preprocesar la imagen para el modelo
    frame_resized = cv2.resize(frame, input_shape)
    frame_rgb = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2RGB)
    frame_normalized = frame_rgb / 255.0
    frame_input = np.expand_dims(frame_normalized, axis=0).astype(np.float32)

    # Establecer los datos de entrada
    interpreter.set_tensor(input_details[0]['index'], frame_input)

    # Realizar la inferencia
    interpreter.invoke()

    # Obtener los resultados
    output_data = interpreter.get_tensor(output_details[0]['index'])

    # Postprocesar los resultados (detecciones)
    detections = output_data[0]  # Formato: [x1, y1, x2, y2, confianza, clase]

    # Dibujar las cajas y etiquetas en el frame original
    for detection in detections:
        x1, y1, x2, y2, conf, cls = detection
        if conf > 0.5:  # Filtrar por confianza
            x1, y1, x2, y2 = int(x1 * frame.shape[1]), int(y1 * frame.shape[0]), int(x2 * frame.shape[1]), int(y2 * frame.shape[0])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f"Class {int(cls)} {conf:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Mostrar el frame
    cv2.imshow('YOLOv5 TensorFlow Lite', frame)

    # Salir con 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar las ventanas
capture.release()
cv2.destroyAllWindows()