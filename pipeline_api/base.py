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
    def __init__(self):
        # @Incomplete because i hadn't write any sentence for simulation module so this part will wait until i decide what will be the boundaries of simulation module
        pass

# @Incomplete This class will install firmware to devices but i need to add more layers and Rust bindings to be sure how correctly install firmware to a custom designed device that is buid by user
class FirmwareloaderPipeline():
    
    def __init__(self) -> None:
        pass

    def circuit_checker(self, circuit_details):
        """ This function will check circuit details, 
            Context: Circuit details are not just connections of sensors, also going to check protocols, driver dependencies
            and other electrical parameterts to be sure that device won't be damaged or empty after process
        """
        pass

    def loader(self, event_details: Dict[str, Any]):
        """ This function will upload firmware to selected devices"""
        pass

