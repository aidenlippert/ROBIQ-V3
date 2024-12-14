# src/form_correction.py
class FormCorrection:
    def __init__(self, thresholds):
        self.thresholds = thresholds

    def analyze(self, exercise, angles, speed):
        feedback = []
        thresholds = self.thresholds.get(exercise, {})
        for joint, limits in thresholds.items():
            angle = angles.get(joint)
            if angle:
                if angle < limits['min']:
                    feedback.append(f"Increase your {joint} angle.")
                elif angle > limits['max']:
                    feedback.append(f"Decrease your {joint} angle.")
        if speed > thresholds.get('speed', {}).get('max', float('inf')):
            feedback.append("Slow down your movement.")
        return feedback