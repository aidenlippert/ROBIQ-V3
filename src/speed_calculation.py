# src/speed_calculator.py
import time
import numpy as np

class SpeedCalculator:
    def __init__(self):
        self.prev_time = None
        self.prev_pos = None

    def calculate_speed(self, current_pos):
        current_time = time.time()
        if self.prev_time and self.prev_pos:
            dt = current_time - self.prev_time
            dx = np.linalg.norm(np.array(current_pos) - np.array(self.prev_pos))
            speed = dx / dt
        else:
            speed = 0
        self.prev_time = current_time
        self.prev_pos = current_pos
        return speed