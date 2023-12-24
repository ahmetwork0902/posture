import cv2
import mediapipe as mp
import matplotlib.pyplot as plt
from calculate_angle import LandmarkAngleCalculator


class PoseClassifier(LandmarkAngleCalculator):
    def __init__(self):
        super().__init__()

    def classify_pose(self, landmarks, output_image, display=False):
        left_elbow_angle = self.calculate_angle(landmarks[mp.solutions.pose.PoseLandmark.LEFT_EAR.value],
                                                landmarks[mp.solutions.pose.PoseLandmark.LEFT_SHOULDER.value],
                                                landmarks[mp.solutions.pose.PoseLandmark.RIGHT_SHOULDER.value])

        right_elbow_angle = self.calculate_angle(landmarks[mp.solutions.pose.PoseLandmark.RIGHT_EAR.value],
                                                 landmarks[mp.solutions.pose.PoseLandmark.RIGHT_SHOULDER.value],
                                                 landmarks[mp.solutions.pose.PoseLandmark.LEFT_SHOULDER.value])

        eyes_incline = self.calculate_angle_horiz(landmarks[mp.solutions.pose.PoseLandmark.LEFT_EAR.value],
                                                  landmarks[mp.solutions.pose.PoseLandmark.RIGHT_EAR.value])

        label = f'left {left_elbow_angle}, right {right_elbow_angle} Bad_pose'
        color = (0, 0, 255)

        # if ((63 <= right_elbow_angle <= 65) or (298 <= left_elbow_angle <= 300)) and (-10 <= eyes_incline <= 10):
        #     label = 'Good_pose'

        if (62 <= right_elbow_angle <= 68) and (298 <= left_elbow_angle <= 302):  # and (-15 <= eyes_incline <= 15):
            label = 'Good_pose'

        if label != 'Unknown Pose':
            color = (0, 255, 0)

        cv2.putText(output_image, label, (10, 30), cv2.FONT_HERSHEY_PLAIN, 2, color, 2)

        if display:
            plt.figure(figsize=[10, 10])
            plt.imshow(output_image[:, :, ::-1]);
            plt.title("Output Image");
            plt.axis('off');
        else:
            return output_image, label
