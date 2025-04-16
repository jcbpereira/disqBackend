# posture_buffer.py

# Use deque to store the last 60 pitch values
# Calculate the rolling average each time a new pitch is added
# Expose two functions:
# - add_pitch_measurement(pitch: float) -> float
# - get_current_average() -> float

from collections import deque
from threading import Lock

pitch_buffer = deque(maxlen=60)
current_average = 0.0
lock = Lock()

def add_pitch_measurement(pitch: float) -> int:
    global current_average
    with lock:
        pitch_buffer.append(pitch)
        current_average = sum(pitch_buffer) / len(pitch_buffer)
        return int(current_average)
# Not used right now
def get_current_average() -> float:
    with lock:
        return current_average