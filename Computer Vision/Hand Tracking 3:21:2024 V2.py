# Made on 3/21/2024 at 8:16 PM
# Second version for hand tracking using computer vision

import cv2
import mediapipe as mp
mp_drawings = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mphands = mp.solutions.hands

cap = cv2.VideoCapture(0)
hands = mphands.Hands

while cap.isOpened():
    data, image = cap.read()

    if not data:
        break

    image = cv2.flip(image, 1)
    
    imageFinal = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    results = hands.process(imageFinal)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawings.draw_landmarks(imageFinal, hand_landmarks, mphands.HAND_CONNECTIONS)
    cv2.imshow('Handtracker', imageFinal)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release
cv2.destroyAllWindows

