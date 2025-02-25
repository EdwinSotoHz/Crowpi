import torch
import cv2

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

capture = cv2.VideoCapture(0)

while True:
    # Captura
    isSuccessfulCapture, frameInfo = capture.read()
    if not isSuccessfulCapture:
        break
    
    # BGR (OpenCV) a RGB (YOLOv5)
    frameInfo_rgb = cv2.cvtColor(frameInfo, cv2.COLOR_BGR2RGB)

    # Prediccion
    results = model(frameInfo_rgb)
    results.render()  # Cajas

    # RGB (YOLOv5) a BGR (OpenCV)
    frameInfo_bgr = cv2.cvtColor(results.ims[0], cv2.COLOR_RGB2BGR)
    cv2.imshow('YOLOv5 OpenCV', frameInfo_bgr) # Ventana

    # Salir
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release() # Liberar Cam
cv2.destroyAllWindows() # Quitar window