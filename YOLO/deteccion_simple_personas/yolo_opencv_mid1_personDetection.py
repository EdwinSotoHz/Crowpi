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

    # Detectar persona (clase 0)
    person_detected = False
    for detection in detections:
        class_id = int(detection[5])  # indice de la clase
        if class_id == 0:  # 0 es "persona" en YOLOv5
            person_detected = True
            break

    if person_detected:
        print("¡Persona detectada!")
    else:
        print("No persona")

    # Cajas
    results.render()
    
    # RGB (YOLOv5) a BGR (OpenCV)
    frameInfo_bgr = cv2.cvtColor(results.ims[0], cv2.COLOR_RGB2BGR)

    # Escalar
    window_width = 650  # Ancho
    window_height = 520  # Alto
    frameInfo_resized = cv2.resize(frameInfo_bgr, (window_width, window_height))

    # Ventana
    cv2.namedWindow('YOLOv5 OpenCV', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('YOLOv5 OpenCV', window_width, window_height)
    cv2.imshow('YOLOv5 OpenCV', frameInfo_resized)

    # Salir
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar las ventanas
capture.release()
cv2.destroyAllWindows()