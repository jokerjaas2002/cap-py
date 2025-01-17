import cv2
import mediapipe as mp
import random

# Inicializar Mediapipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Captura de video
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Procesar la imagen
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    # Detección de gestos aquí
    # (Implementar la lógica para detectar "piedra", "papel" o "tijera")

    # Mostrar el resultado
    cv2.imshow('Piedra, Papel o Tijera', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()