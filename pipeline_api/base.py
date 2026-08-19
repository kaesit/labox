from typing import Dict, Any, Callable, Optional
from quality_control.core.base import BaseQualityModel, QualityTask, Status
import asyncio

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
    def __init__(self, simulation_title:str = "Pipeline Simulation", simulation_details: Dict[str, Any]):
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

