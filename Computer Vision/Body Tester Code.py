# Made 3/20/2024 at 10:12 AM
# A version 2 script that uses computer vision to track the entire body of a person and draw a stick-figure overlay that moves along with the humans movements

import cv2
import mediapipe as mp

# Initialize mediapipe pose module
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Set up boolean variables for major body parts
body_parts = {
    "left_shoulder": False,
    "right_shoulder": False,
    "left_elbow": False,
    "right_elbow": False,
    "left_wrist": False,
    "right_wrist": False,
    "left_hip": False,
    "right_hip": False,
    "left_knee": False,
    "right_knee": False,
    "left_ankle": False,
    "right_ankle": False
}

# Function to check body part movement
def check_body_parts(landmarks):
    global body_parts

    if landmarks:
        # Left shoulder
        if landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].visibility > 0.5:
            body_parts["left_shoulder"] = True
        else:
            body_parts["left_shoulder"] = False

        # Right shoulder
        if landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].visibility > 0.5:
            body_parts["right_shoulder"] = True
        else:
            body_parts["right_shoulder"] = False

        # Left elbow
        if landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].visibility > 0.5:
            body_parts["left_elbow"] = True
        else:
            body_parts["left_elbow"] = False

        # Right elbow
        if landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].visibility > 0.5:
            body_parts["right_elbow"] = True
        else:
            body_parts["right_elbow"] = False

        # Left wrist
        if landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].visibility > 0.5:
            body_parts["left_wrist"] = True
        else:
            body_parts["left_wrist"] = False

        # Right wrist
        if landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].visibility > 0.5:
            body_parts["right_wrist"] = True
        else:
            body_parts["right_wrist"] = False

        # Left hip
        if landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].visibility > 0.5:
            body_parts["left_hip"] = True
        else:
            body_parts["left_hip"] = False

        # Right hip
        if landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].visibility > 0.5:
            body_parts["right_hip"] = True
        else:
            body_parts["right_hip"] = False

        # Left knee
        if landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].visibility > 0.5:
            body_parts["left_knee"] = True
        else:
            body_parts["left_knee"] = False

        # Right knee
        if landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].visibility > 0.5:
            body_parts["right_knee"] = True
        else:
            body_parts["right_knee"] = False

        # Left ankle
        if landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].visibility > 0.5:
            body_parts["left_ankle"] = True
        else:
            body_parts["left_ankle"] = False

        # Right ankle
        if landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].visibility > 0.5:
            body_parts["right_ankle"] = True
        else:
            body_parts["right_ankle"] = False

# Main function
def main():
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Flip the frame horizontally
        frame = cv2.flip(frame, 1)

        # Convert the BGR image to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame
        results = pose.process(rgb_frame)

        if results.pose_landmarks:
            # Draw pose landmarks
            mp_pose.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            # Check body part movement
            check_body_parts(results.pose_landmarks)

        # Display body part movement
        print("Body parts movement:", body_parts)

        cv2.imshow('Pose Tracking', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()