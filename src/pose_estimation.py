# src/pose_estimation.py
import cv2
import mediapipe as mp

class PoseEstimator:
    def __init__(self):
        self.pose = mp.solutions.pose.Pose()
        self.drawing = mp.solutions.drawing_utils

    def detect(self, frame):
        results = self.pose.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        return results.pose_landmarks

    def annotate(self, frame, landmarks):
        if landmarks:
            self.drawing.draw_landmarks(frame, landmarks, mp.solutions.pose.POSE_CONNECTIONS)
        return frame