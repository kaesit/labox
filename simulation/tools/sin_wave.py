import os
import sys
# deprecated may be used later import numpy as np
import struct
import time
import math

current_dir = os.path.dirname(os.path.abspath(__file__))

embedded_systems_path = os.path.abspath(os.path.join(current_dir, "..", "..", "embedded_systems"))
if embedded_systems_path not in sys.path:
    sys.path.append(embedded_systems_path)
import labox_embedded_core


#print("All libraries and modules imported successfully")

FREQUENCY = 1.0
TIME_DURATION = 10.0
FREQUENCY_SAMPLING = 100

# deprecated may be used later
"""
def generate_waves():
    samples = np.linspace(0, TIME_DURATION, int(FREQUENCY_SAMPLING * TIME_DURATION), endpoint = False)
    signal = np.sin(2 * np.pi * FREQUENCY * samples)

    return signal
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

    payload_core = struct.pack("<BBh", sensor_id, status_flags, scaled_value)

    crc_byte = calculate_crc8(payload_core)

    return struct.pack("<BBhB", sensor_id, status_flags, scaled_value, crc_byte)



def run_simulation(sensor_buffer):
    delay_seconds = 1.0 / FREQUENCY_SAMPLING

    print("Simulation is Running")
    start_time = time.time()
    step = 0

    while True:

        current_time = time.time() - start_time

        raw_value = math.sin(2 * math.pi * FREQUENCY * current_time)
        payload = encoder_to_payload(sensor_id=1, status_flags=0, raw_value=raw_value)

        for byte_val in payload:
            sensor_buffer.push(byte_val)

        if step % 100 == 0:
            print(f"Step: {step:04d} | Signal: {raw_value:+.2f} | Buffer Load: {sensor_buffer.available()} bytes")

        step+=1
        time.sleep(delay_seconds)

if __name__ == "__main__":
    run_simulation()

