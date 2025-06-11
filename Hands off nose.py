import cv2
import mediapipe as mp
import math
import pygame

# Setup MediaPipe
mpFaceMesh = mp.solutions.face_mesh
mpHands = mp.solutions.hands
mpDraw = mp.solutions.drawing_utils

faceMesh = mpFaceMesh.FaceMesh()
hands = mpHands.Hands()

# Setup sound
pygame.init()
pygame.mixer.init()
alarm_sound = pygame.mixer.Sound("audio/beep-06.wav")

# Distance threshold for "touching"
TOUCH_THRESHOLD = 0.05

cap = cv2.VideoCapture(0)
alarm_playing = False

while True:
    success, frame = cap.read()
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process face and hands
    face_results = faceMesh.process(frame_rgb)
    hand_results = hands.process(frame_rgb)

    nose_x, nose_y = None, None

    # Get nose position (landmark 1 is nose tip)
    if face_results.multi_face_landmarks:
        face_landmarks = face_results.multi_face_landmarks[0]
        nose = face_landmarks.landmark[1]
        nose_x, nose_y = nose.x, nose.y

        # Draw green circle on nose
        height, width, channel = frame.shape
        nose_pixel_x = int(nose.x * width)
        nose_pixel_y = int(nose.y * height)
        cv2.circle(frame, (nose_pixel_x, nose_pixel_y), 5, (255, 0, 255), -1)

    hand_near_nose = False

    # Check if hand is near nose
    if nose_x is not None and hand_results.multi_hand_landmarks:
        for hand in hand_results.multi_hand_landmarks:
            mpDraw.draw_landmarks(frame, hand, mpHands.HAND_CONNECTIONS)

            for landmark in hand.landmark:
                # Calculate distance between hand point and nose
                distance = math.sqrt((landmark.x - nose_x) ** 2 + (landmark.y - nose_y) ** 2)

                if distance < TOUCH_THRESHOLD:
                    hand_near_nose = True
                    break

            if hand_near_nose:
                break

    # Handle alarm
    if hand_near_nose and not alarm_playing:
        print("Hand touched nose! Starting alarm.")
        alarm_sound.play(-1)
        alarm_playing = True
    elif not hand_near_nose and alarm_playing:
        print("Hand moved away. Stopping alarm.")
        alarm_sound.stop()
        alarm_playing = False

    cv2.imshow("Hand-to-Nose Detection", frame)
    if cv2.waitKey(1) & 0xff == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()