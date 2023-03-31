# Deve-se instalar a bilbioteca OpenCV no ESO32-CAM

# https://docs.opencv.org/4.x/dc/d88/tutorial_traincascade.html
# Segue o link acima para criar arquivo XLM

import cv2
import os

# Configurações do ESP32-CAM
os.environ['CAMERA_MODEL'] = 'ESP32-CAM'
os.environ['CAMERA_PORT'] = '0'
os.environ['CAMERA_FRAME_SIZE'] = '640x480'

# Carrega o arquivo XML com as características do objeto a ser detectado (ser humano)
human_cascade = cv2.CascadeClassifier('human.xml')

# Inicia a câmera
camera = cv2.VideoCapture(0)

while True:
    # Captura um frame da câmera
    ret, frame = camera.read()

    # Converte a imagem para tons de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detecta seres humanos na imagem
    humans = human_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Desenha um retângulo ao redor de cada ser humano detectado
    for (x, y, w, h) in humans:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Exibe o resultado na tela
    cv2.imshow('Human detection', frame)

    # Aguarda a tecla 'q' ser pressionada para sair
    if cv2.waitKey(1) == ord('q'):
        break

# Libera a câmera e fecha a janela
camera.release()
cv2.destroyAllWindows()
