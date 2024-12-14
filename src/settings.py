# config/settings.py

THRESHOLDS = {
    'squat': {
        'knee_angle': {'min': 70, 'max': 130, 'ideal': 90},
        'hip_angle': {'min': 60, 'max': 120, 'ideal': 90},
        'ankle_angle': {'min': 50, 'max': 90, 'ideal': 70},
        'back_angle': {'min': 45, 'max': 90, 'ideal': 60},
        'speed': {
            'eccentric': {'min': 0.2, 'max': 0.5},  # meters/second
            'concentric': {'min': 0.3, 'max': 0.7}
        },
        'form_cues': [
            'Keep chest up',
            'Knees tracking over toes',
            'Weight in heels',
            'Maintain neutral spine'
        ]
    },
    'pushup': {
        'elbow_angle': {'min': 45, 'max': 120, 'ideal': 90},
        'shoulder_angle': {'min': 70, 'max': 110, 'ideal': 90},
        'back_angle': {'min': 170, 'max': 180, 'ideal': 180},
        'speed': {
            'eccentric': {'min': 0.1, 'max': 0.3},
            'concentric': {'min': 0.2, 'max': 0.4}
        },
        'form_cues': [
            'Core engaged',
            'Elbows at 45 degrees',
            'Neutral neck position',
            'Full range of motion'
        ]
    },
    'deadlift': {
        'hip_angle': {'min': 50, 'max': 100, 'ideal': 75},
        'knee_angle': {'min': 70, 'max': 120, 'ideal': 90},
        'back_angle': {'min': 45, 'max': 90, 'ideal': 60},
        'speed': {
            'eccentric': {'min': 0.2, 'max': 0.4},
            'concentric': {'min': 0.3, 'max': 0.6}
        },
        'form_cues': [
            'Bar over midfoot',
            'Shoulder blades retracted',
            'Hips hinge first',
            'Maintain neutral spine'
        ]
    }
}

# Additional settings for pose estimation confidence
POSE_CONFIDENCE_THRESHOLD = 0.7
SMOOTHING_WINDOW = 3  # frames for movement smoothing