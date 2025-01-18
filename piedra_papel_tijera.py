import cv2
import mediapipe as mp

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

    # Detección de gestos
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Dibujar los puntos de la mano
            mp.solutions.drawing_utils.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Obtener las posiciones de los dedos
            finger_tips = [hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP],
                           hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP],
                           hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP],
                           hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP],
                           hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]]

            # Lógica para detectar "piedra", "papel" o "tijera"
            if finger_tips[0].y < finger_tips[1].y and finger_tips[1].y < finger_tips[2].y:
                gesture = "Papel"
            elif finger_tips[0].y < finger_tips[1].y and finger_tips[1].y > finger_tips[2].y:
                gesture = "Piedra"
            elif finger_tips[0].y > finger_tips[1].y and finger_tips[1].y < finger_tips[2].y:
                gesture = "Tijera"
            else:
                gesture = "Desconocido"

            # Mostrar el gesto detectado
            cv2.putText(frame, gesture, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # Mostrar el resultado
    cv2.imshow('Piedra, Papel o Tijera', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()