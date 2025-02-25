import torch
import cv2
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

capture = cv2.VideoCapture(0)

while True:
    # Captura
    isSuccessfulCapture, frameInfo = capture.read()
    if not isSuccessfulCapture:
        break
    
    contrast = 1.8  # 1 = Normal
    brightness = -5  # 0 = Normal
    frameInfoModified = cv2.convertScaleAbs(frameInfo, alpha=contrast, beta=brightness)

    # BGR (OpenCV) a RGB (YOLOv5)
    frameInfo_rgb = cv2.cvtColor(frameInfoModified, cv2.COLOR_BGR2RGB)

    # Prediccion
    results = model(frameInfo_rgb)

    # Detecciones [x1, y1, x2, y2, confianza, clase]
    detections = results.xyxy[0]
    detections = [detection for detection in detections if int(detection[5]) == 0] # filtar personas clase 0

    # Si hay personas en el frame
    if len(detections) > 0:
        print("Si hay")
    else:
        print("No hay")

    for detection in detections:
        # Dibujar solo la primera persona detectada
        x1, y1, x2, y2, conf, cls = detection
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        cv2.rectangle(frameInfoModified, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frameInfoModified, f"Persona {conf:.2f}", (x1, y1 - 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Escalar el frame
    window_width = 650  # Ancho
    window_height = 520  # Alto
    frameInfo_resized = cv2.resize(frameInfoModified, (window_width, window_height))

    # Mostrar el frame en la ventana
    cv2.namedWindow('YOLOv5 OpenCV', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('YOLOv5 OpenCV', window_width, window_height)
    cv2.imshow('YOLOv5 OpenCV', frameInfo_resized)

    # Salir
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar camara y cerrar ventanas
capture.release()
cv2.destroyAllWindows()
