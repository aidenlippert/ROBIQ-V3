# src/video_capture.py
import cv2
from pose_estimation import PoseEstimator

class VideoCapture:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.pose_estimator = PoseEstimator()

    def release(self):
        self.cap.release()
        cv2.destroyAllWindows()