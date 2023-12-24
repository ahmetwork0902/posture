import cv2
import mediapipe as mp
import matplotlib.pyplot as plt

mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils


class PoseDetector:
    def __init__(self):
        self.mp_pose = mp.solutions.pose
        self.mp_drawing = mp.solutions.drawing_utils
        self.pose = self.mp_pose.Pose()

    def detect_pose(self, image, pose, display=True):
        '''
        Функция позволяет распознать узлы mediapipe
        :args:
            image: Входящее фото или видео, откуда требуется считать позу
            pose: Функция распознания позы
            display: Отображать исходную фотку или нет
        :return:
            output_image: Входящее изображение с наложенными точками распознавания
            landmarks: список распознанных точек и их координаты
        '''

        output_image = image.copy()
        imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = pose.process(imageRGB)
        height, width, _ = image.shape
        landmarks = []

        if results.pose_landmarks:
            self.mp_drawing.draw_landmarks(image=output_image, landmark_list=results.pose_landmarks,
                                           connections=mp_pose.POSE_CONNECTIONS)
            for landmark in results.pose_landmarks.landmark:
                landmarks.append((int(landmark.x * width), int(landmark.y * height),
                                  (landmark.z * width)))

        if display:
            plt.figure(figsize=[22, 22])
            plt.subplot(121)
            plt.imshow(image[:, :, ::-1])
            plt.title("Original Image")
            plt.axis('off')
            plt.subplot(122)
            plt.imshow(output_image[:, :, ::-1])
            plt.title("Output Image")
            plt.axis('off')
            mp_drawing.plot_landmarks(results.pose_world_landmarks, mp_pose.POSE_CONNECTIONS)
        else:
            return output_image, landmarks
