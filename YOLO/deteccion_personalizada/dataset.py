import cv2
import os

folder = 'Objects'
directory = 'C:/Users/edwin/Documents/IoT/EntornosVENV/YOLO/deteccion_personalizada' 
folder_path = os.path.join(directory, folder)

if not os.path.exists(folder_path):
    print('Folder created: ', folder_path)
    os.makedirs(folder_path)

count = 0

capture = cv2.VideoCapture(0)

modelName = 'calculator'
limit = 100

while True:
    # Captura
    isSuccessfulCapture, frameInfo = capture.read()
    if not isSuccessfulCapture:
        break

    cv2.imshow("Capture Photos", frameInfo)

    # tecla de inicio
    key = cv2.waitKey(1)

    # guardar foto
    if key == ord('s'):
        photoName = os.path.join(folder_path, f"{modelName}_{count}.jpg")
        cv2.imwrite(photoName, frameInfo)
        print(f"Photo {count} saved")
        count += 1

    # terminar
    if key == 27 or count >= limit:
        break

capture.release() # Liberar Cam
cv2.destroyAllWindows() # Quitar window