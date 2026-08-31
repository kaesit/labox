import numpy as np

FREQUENCY = 200
TIME_DURATION = 1.0
FREQUENCY_SAMPLING = 8000

def generate_waves():
    samples = np.linspace(0, TIME_DURATION, int(FREQUENCY_SAMPLING * TIME_DURATION), endpoint = False)
    signal = np.sin(2 * np.pi * FREQUENCY * samples)

    return signal


generate_waves()
