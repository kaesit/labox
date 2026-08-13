import os, sys
from typing import Dict, Any
from enum import Enum

class SimulationType(Enum):
    CIRCUIT = 1
    ROBOTIC = 2
    STORAGE = 3
    VISION = 4
    SENSOR = 5


class SimulationModel():
    def __init__(self, simulation_title: str = "System Simulation",
                 simulation_type: SimulationType = SimulationType.CIRCUIT):
        self.simulation_title = simulation_title
        self.simulation_type = simulation_type
        
        self.is_running = False
        self.results = {}
    
    def start_simulation(self) -> None:
        self.is_running = True
        print(f"Starting {self.simulation_title}")
    
    def cancel(self) -> None:
        self.is_running = False
        print(f"Cancelling {self.simulation_title}")

