from typing import Dict, Any, Callable, Optional
import asyncio
import os
import sys
import struct

sys.path.append("..")
from quality_control.core.base import BaseQualityModel, QualityTask, Status
from simulation.tools.sin_wave import *
current_dir = os.path.dirname(os.path.abspath(__file__))

embedded_systems_path = os.path.abspath(os.path.join(current_dir, "..", "embedded_systems"))
if embedded_systems_path not in sys.path:
    sys.path.append(embedded_systems_path)
import labox_embedded_core
print(dir(labox_embedded_core))

print("ALL MODULES SUCCESSFULLY IMPORTED")



def decoder_to_consumer(raw_5_bytes:bytes) -> Dict[str, Any]:
    unpacked_data = struct.unpack("<BBhB", raw_5_bytes)
    sensor_id = unpacked_data[0]
    status_flags = unpacked_data[1]
    raw_value = unpacked_data[2]
    crc_byte = unpacked_data[3]
    return {
            "sensor_id": sensor_id,
            "status_flags": status_flags,
            "raw_value": raw_value,
            "crc_byte": crc_byte
    }

async def consumer_loop(sensor_buffer):
    print("CONSUMER IS STARTED")

    while True:
        if sensor_buffer.available() >= 5:
            packet_bytes = bytearray()

            for _ in range(5):
                byte_val = sensor_buffer.pop()
                packet_bytes.append(byte_val)

            telemetry_data = decoder_to_consumer(packet_bytes)

            print(f"TELEMETRY IS RECEIVED: {telemetry_data}")

        await asyncio.sleep(0.001)



class QualityTestPipeline():
    def __init__(self, quality_test:BaseQualityModel) -> None:
        self.quality_test = quality_test
        run(quality_test)

    def run (self, quality_test: BaseQualityModel, *args, **kwargs):
        print("Quality Tests has began")
        try:
            quality_test.run()
        except (ImportError, ArithmeticError, MemoryError, AssertionError, ValueError) as error_details:
            print(f"There are errors, error details: {error_details}")
            self.cancel()

    def cancel(self) -> None:
        self.quality_test.cancel()

class SimulationTestPipeline():
    def __init__(self, simulation_title:str = "Pipeline Simulation", simulation_details: Dict[str, Any] = None):
        # @Incomplete because i hadn't write any sentence for simulation module so this part will wait until i decide what will be the boundaries of simulation module
        self.simulation_title = simulation_title
        self.simulation_details = simulation_details
        self.is_running = False

    def run (self):
        self.is_running = True
        print(f"Simulation {self.simulation_title} is running")

    def cancel(self):
        self.is_running = False
        print(f"Simulation {self.simulation_title} is canceled")

# @Incomplete This class will install firmware to devices but i need to add more layers and Rust bindings to be sure how correctly install firmware to a custom designed device that is buid by user
class FirmwareloaderPipeline():
    def __init__(self) -> None:
        """ Context:
        @Incomplete
        @Scenario : some of the circuit checker libraries should use or derive to take advantage of it, otherwise that heavy libraries will just make our 'optimization-driven' platform
        slower and slower.
        Additionally: all this __init__ function actually just gets the parameters and runs the loader
        """
        self.is_load_safe = False

        if self.is_load_safe :
            self.load()
        else:
            self.circuit_checker

    def simulate(self, circuit_details) -> bool:
        """
        This function will use circuit simulators to return a boolean value
        """
        pass
    def circuit_checker(self, circuit_details):
        """ This function will check circuit details,
            Context: Circuit details are not just connections of sensors, also going to check protocols, driver dependencies
            and other electrical parameterts to be sure that device won't be damaged or empty after process
        """
        # is_circuit_ok = simulate(circuit_details) This function will run the simulation and return a boolean value for controls
        if is_circuit_ok:
            self.is_load_safe = True
        else:
            False

    def loader(self, event_details: Dict[str, Any]):
        """ This function will upload firmware to selected devices"""
        pass


async def main():

    shared_buffer = labox_embedded_core.ByteRingBuffer(1024)

    await asyncio.gather(
            asyncio.to_thread(run_simulation, shared_buffer),
            consumer_loop(shared_buffer)

    )

if __name__ == "__main__":
    asyncio.run(main())
