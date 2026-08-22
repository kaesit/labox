import os, sys
from typing import Dict, Any
from enum import Enum


GRAVITY = 9.81 # m/sˆ2
VOLT = 3.3 # Volt
RESISTANCE = 5000 # OHM
ADC = 20 # 20 bit



# @Incomplete i don't really know how to implement environmental situations into a simulation model
# but the context of this class will contain those specific parameters that help us to make simulation multi environmental
"""
@Scenario
environmental details:
{
    environment: sterilized lab,
    dust_ratio : %2
    wind : 0(km)

}
"""
class EnvironmentalSimulationModel():
    def __init__(self, simulation_title:str = "Environmental Simulation",  environmental_details: Dict[str, Any]):
        self.simulation_title = simulation_title
        self.environment_details = self.environmental_details
        print(self.environmental_details)
        self.is_running = False

    def run(self) -> Dict[str, Any]:
        """
        @Incomplete
        Context:
        This function will run the main parameter list of the result spesific for that environment
        Firstly gonna use the main simulation model from core and runs through it test for spesific environments and then outputs a result that how well it performed
        """
        self.is_running = True
        print(f"Starting {simulation_title}")
    def cancel ():
        self.is_running = False
        print(f"Cancelling {simulation_title}")



class SensorType(Enum):
    BAROMETER = 1
    SUPER_SONIC = 2
    LIDAR = 3
    GYRO = 4
    GPS = 5
    HEAT = 6



"""
Barometer formula: h = p / (x * g)


"""
class SensorSimulationModel():

    def __init__(self, simulation_title:str = "Sensor Simulation", sensor_type: SensorType = SensorType.BAROMETER):
        self.simulation_title = simulation_title
        self.sensor_type = sensor_type
        self.results = {}
        self.is_running = False

    def run (self) -> Dict[str, Any]:
        self.is_running = True
        print(f"Starting {self.simulation_title}")

    def cancel(self) -> None:
        self.is_running = False
        print(f"Cancelling {simulation_title}")
