import os
import sys
import numpy as np
import struct
import time

current_dir = os.path.dirname(os.path.abspath(__file__))

embedded_systems_path = os.path.abspath(os.path.join(current_dir, "..", "..", "embedded_systems"))
if embedded_systems_path not in sys.path:
    sys.path.append(embedded_systems_path)
import labox_embedded_core


#print("All libraries and modules imported successfully")

FREQUENCY = 200
TIME_DURATION = 1.0
FREQUENCY_SAMPLING = 2000

def generate_waves():
    samples = np.linspace(0, TIME_DURATION, int(FREQUENCY_SAMPLING * TIME_DURATION), endpoint = False)
    signal = np.sin(2 * np.pi * FREQUENCY * samples)

    return signal


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

def encoder_to_payload(sensor_id:int, status_flags:int, raw_value:int) -> bytes:
    scaled_value = int(raw_value * 32767)

    payload_core = struct.pack("<BBh", sensor_id, status_flag, scaled_value)

    crc_byte = calculate_crc8(payload_core)

    return struct.pack("<BBhB", sensor_id, status_flag, scaled_value, crc_byte)



def run_simulation():
    signal_array = generate_waves()
    delay_seconds = 1.0 / FREQUENCY_SAMPLING

    print("Simulation is Running")

    """
    THERE IS NO IMPLEMENTATION FOR C++ BINDINGS YET
    """


