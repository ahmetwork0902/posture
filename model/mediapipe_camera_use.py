from time import * #time
import cv2
import mediapipe as mp
from constant import ESCAPE_KEY, RESIZE_VIDEO
from detect_pose import PoseDetector
from classify_pose import PoseClassifier
import pygame

pose_detector = PoseDetector()
pose_classifier = PoseClassifier()

if __name__ == "__main__":
    mp_pose = mp.solutions.pose
    mp_drawing = mp.solutions.drawing_utils

    pose_video = mp_pose.Pose(
        static_image_mode=False, min_detection_confidence=0.5, model_complexity=1,
    )

    pygame.init()
    pygame.mixer.init()

    video = cv2.VideoCapture(0)
    time1 = time()  # Время старта отсчёта

    good_pose_start_time = None
    bad_pose_start_time = None
    good_pose_duration = 0
    bad_pose_duration = 0

    while video.isOpened():
        ok, frame = video.read()
        if not ok:
            break

        frame = cv2.flip(frame, 1)
        frame_height, frame_width, _ = frame.shape

        frame = cv2.resize(frame, (int(frame_width * (RESIZE_VIDEO / frame_height)), RESIZE_VIDEO))

        frame, marks = pose_detector.detect_pose(frame, pose_video, display=False)

        if marks:
            frame, label = pose_classifier.classify_pose(marks, frame, display=False)
            time2 = time()

            if label == 'Good_pose':
                good_pose_duration += time2 - time1
            else:
                bad_pose_duration += time2 - time1

            if good_pose_duration + bad_pose_duration >= 1800:
                if bad_pose_duration > good_pose_duration:
                    pygame.mixer.music.load("asignal_sound.mp3")
                    pygame.mixer.music.play()

                print("Time spent in good pose: ", good_pose_duration)
                print("Time spent in bad pose: ", bad_pose_duration)

                # Здесь можно добавить код для сохранения статистики в SQL

                good_pose_duration = 0
                bad_pose_duration = 0
                time1 = time2

        cv2.imshow('Pose Classification', frame)
        key = cv2.waitKey(1)

        if key == ESCAPE_KEY:
            break

    video.release()
    cv2.destroyAllWindows()