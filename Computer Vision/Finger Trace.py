# Made on 7/28/2024 at 6:36 PM
# Uses computer vision to track hand movement and move the computers mouse accordingly

import cv2
import mediapipe as mp
import pyautogui
import math

pyautogui.FAILSAFE = False

# Initialize hands module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

# Initialize previous finger tip position
WRISTXPrev = 0
WRISTYPrev = 0

cap = cv2.VideoCapture(1)

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Frame Flip
    frame = cv2.flip(frame, 1)

    # BGR -> RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process frame
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw landmarks

            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        
            # Access WRIST finger tip
            MiddleFinger = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP]
            Index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            Thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]

            TX = Thumb_tip.x * frame.shape[1]
            TY = Thumb_tip.y * frame.shape[0]

            IX = Index_tip.x * frame.shape[1]
            IY = Index_tip.y * frame.shape[0]

            threshold = 15

            # Get current finger tip position

            MiddleFinger_X = 0 #2318
            MiddleFinger_Y = 0 #297

            WMiddleFinger_X = MiddleFinger.x * frame.shape[1] # 1 is rows
            MiddleFinger_Y = MiddleFinger.y * frame.shape[0] #0 is colums

            

            # Calculate change in finger tip position
            Y_Change = MiddleFinger_Y - WRISTYPrev
            X_Change = MiddleFinger_X - WRISTXPrev

            # Move mouse
            pyautogui.moveRel(X_Change * 2, Y_Change * 2)

            # Update previous finger tip position
            MiddleFinger_X_Prev = MiddleFinger_X_Prev
            MiddleFinger_Y_Prev = MiddleFinger_Y_Prev

            #Check for finger click

            distance = calculate_distance(IX, IY, TX, TY)

            if distance < threshold:
                pyautogui.click()





    cv2.imshow('Hand Tracking', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()