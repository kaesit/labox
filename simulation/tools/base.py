import os, sys
from typing import Dict, Any



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
    def __init__(self, environmental_details: Dict[str, Any]):
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
    def cancel ()
