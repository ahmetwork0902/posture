import math


class LandmarkAngleCalculator:
    def __init__(self):
        pass

    def calculate_angle(self, landmark1, landmark2, landmark3):
        '''
        Рассчитать угол между тремя точками
        '''
        x1, y1, _ = landmark1
        x2, y2, _ = landmark2
        x3, y3, _ = landmark3
        angle = math.degrees(math.atan2(y3 - y2, x3 - x2) - math.atan2(y1 - y2, x1 - x2))
        if angle < 0:
            angle += 360
        return angle

    def calculate_angle_horiz(self, landmark1, landmark2):
        '''
        Рассчитать угол между двумя точками
        '''
        x1, y1, _ = landmark1
        x2, y2, _ = landmark2
        angle = math.degrees(math.atan2(y2 - y1, x2 - x1))
        return angle
