import cv2
import mediapipe as mp

# Initialize MediaPipe Hands and Drawing Utils
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

# Finger tip landmark indices
FINGER_TIP_IDS = [4, 8, 12, 16, 20]

# Initialize webcam feed
cap = cv2.VideoCapture(0)

# Initialize MediaPipe Hands model
with mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Unable to access webcam.")
            break

        # Flip the frame horizontally for a mirrored view
        frame = cv2.flip(frame, 1)

        # Convert the frame to RGB (MediaPipe requires RGB images)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame to detect hands
        results = hands.process(frame_rgb)

        total_finger_count = 0  # To store combined count
        hand_index = 0  # Index for multiple hands

        if results.multi_hand_landmarks and results.multi_handedness:
            for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
                hand_index += 1

                # Draw landmarks and connections on the frame
                mp_drawing.draw_landmarks(
                    frame,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style()
                )

                # Get handedness label (Left or Right)
                hand_label = handedness.classification[0].label  # 'Left' or 'Right'
                is_right_hand = hand_label == 'Right'

                # Finger counting logic for the current hand
                finger_count = 0
                landmarks = hand_landmarks.landmark

                # Thumb detection (adjust logic for left/right hand)
                if is_right_hand:
                    if landmarks[FINGER_TIP_IDS[0]].x < landmarks[FINGER_TIP_IDS[0] - 1].x:
                        finger_count += 1
                else:
                    if landmarks[FINGER_TIP_IDS[0]].x > landmarks[FINGER_TIP_IDS[0] - 1].x:
                        finger_count += 1

                # Other fingers detection
                for i in range(1, 5):
                    if landmarks[FINGER_TIP_IDS[i]].y < landmarks[FINGER_TIP_IDS[i] - 2].y:
                        finger_count += 1

                # Add current hand's count to the total
                total_finger_count += finger_count

                # Display finger count for each hand
                cv2.putText(frame, f"{hand_label} Hand: {finger_count} Fingers", 
                            (10, 50 * hand_index), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

        # Display the combined finger count
        cv2.putText(frame, f"Total: {total_finger_count} Fingers", 
                    (10, 50 * (hand_index + 1)), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

        # Display the frame
        cv2.imshow('Finger Counting (Both Hands)', frame)

        # Break the loop on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release resources
cap.release()
cv2.destroyAllWindows()
