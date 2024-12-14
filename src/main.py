# src/main.py
import cv2
from video_capture import VideoCapture
from angle_calculator import AngleCalculator
from speed_calculation import SpeedCalculator
from form_correction import FormCorrection
from settings import THRESHOLDS

def main():
    video = VideoCapture()
    angle_calc = AngleCalculator()
    speed_calc = SpeedCalculator()
    form_correct = FormCorrection(THRESHOLDS)
    exercise = 'squat'

    while True:
        ret, frame = video.cap.read()
        if not ret:
            break

        landmarks = video.pose_estimator.detect(frame)
        frame = video.pose_estimator.annotate(frame, landmarks)

        if landmarks:
            # Extract necessary joint coordinates
            # For example purposes, using arbitrary indices
            hip = [landmarks.landmark[23].x, landmarks.landmark[23].y]
            knee = [landmarks.landmark[25].x, landmarks.landmark[25].y]
            ankle = [landmarks.landmark[27].x, landmarks.landmark[27].y]

            knee_angle = angle_calc.calculate_angle(hip, knee, ankle)
            speed = speed_calc.calculate_speed(knee)

            angles = {'knee_angle': knee_angle}
            feedback = form_correct.analyze(exercise, angles, speed)

            # Display feedback
            cv2.putText(frame, f'Knee Angle: {knee_angle:.2f}', (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            for idx, msg in enumerate(feedback):
                cv2.putText(frame, msg, (10, 60 + idx * 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

        cv2.imshow('AI Personal Trainer', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video.release()

if __name__ == "__main__":
    main()