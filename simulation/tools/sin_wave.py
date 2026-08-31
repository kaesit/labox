import numpy as np
import zlib


FREQUENCY = 200
TIME_DURATION = 1.0
FREQUENCY_SAMPLING = 8000

def generate_waves():
    samples = np.linspace(0, TIME_DURATION, int(FREQUENCY_SAMPLING * TIME_DURATION), endpoint = False)
    signal = np.sin(2 * np.pi * FREQUENCY * samples)

    return signal


"""
@Incomplete
SensorPayload Structure
    uint8_t sensor_id 1 byte max, 255 sensor
    uint8_t status_flags 1 byte bitmask
    uint16_t value 2 bytes
    @Completed uint8_t crc 1 byte checksum

    Crc function is written, next step is writing data encoding for RingBuffer
    And using 5 BYTES MAXIMUM @Max
"""

def calculate_crc8(data: bytes) -> int:
    crc = 0x00
    for byte in data:
        crc ^= byte
        for _ in range (8):
            if crc & 0x80:
                crc = (crc << 1) ^ (0x07)
            else:
                crc <<= 1
            crc &= 0xFF
    return crc

generate_waves()
