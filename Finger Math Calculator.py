import cv2
import mediapipe as mp

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2)
mp_draw = mp.solutions.drawing_utils

# Finger tip landmarks index as per MediaPipe
finger_tips = [4, 8, 12, 16, 20]

# Start webcam
cap = cv2.VideoCapture(0)

def count_fingers(hand_landmarks, hand_label):
    count = 0
    # Thumb
    if hand_label == "Right":
        if hand_landmarks.landmark[finger_tips[0]].x < hand_landmarks.landmark[finger_tips[0] - 1].x:
            count += 1
    else:  # Left hand
        if hand_landmarks.landmark[finger_tips[0]].x > hand_landmarks.landmark[finger_tips[0] - 1].x:
            count += 1
    # Other fingers
    for tip in finger_tips[1:]:
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            count += 1
    return count

while True:
    success, image = cap.read()
    if not success:
        break

    image = cv2.flip(image, 1)  # Mirror the image
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_image)

    total_fingers = 0
    hand_fingers = []

    if result.multi_hand_landmarks and result.multi_handedness:
        for hand_landmarks, hand_handedness in zip(result.multi_hand_landmarks, result.multi_handedness):
            mp_draw.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            label = hand_handedness.classification[0].label  # "Left" or "Right"
            fingers = count_fingers(hand_landmarks, label)
            hand_fingers.append(fingers)
            total_fingers += fingers

    # Display finger count and addition
    if len(hand_fingers) == 2:
        text = f"{hand_fingers[0]} + {hand_fingers[1]} = {total_fingers}"
    elif len(hand_fingers) == 1:
        text = f"{hand_fingers[0]}"
    else:
        text = "Show hands with fingers!"

    cv2.putText(image, text, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.4, (0, 255, 0), 3)
    cv2.imshow("Finger Math Addition", image)

    if cv2.waitKey(1) & 0xFF == 27:  # Press ESC to exit
        break

cap.release()
cv2.destroyAllWindows()
