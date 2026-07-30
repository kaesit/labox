from abc import ABC, abstractmethod
from typing import Callablem, Any
from enum import Enum

# @Incomplete
# @Requirements
# What can be added to device status
class Status(Enum):
    OFF="off"
    RUNNING="running"
    CONNECTED="connected"
    DISCONNECTED="disconnected"
    RECOGNIZED="recognized"
    NOTRECOGNIZED="notrecognized"
    ERROR="error"
# @Incomplete
# This classes should be remodeled by reviewing unique properties of the device
# @Scenario
"""What if user customized his device before using labox, how can labox read and may save those custimazations for user
What else can be ESP32s unique attribute or properties that should we focus on this class
1. Can prioritize about Wi-Fi or Bluetooth connections because its use for this purpose way more than other devices are used for wireless connection
2. Can add more customizable feature because it can be programmed with python
3. Can work asynchnorous
""" 
class ESP32Model(ABC):
    def __init__(self, device_id: str):
        self.device_id = device_id
        self._status = Status.OFF
    
    @property
    def status(self) -> Status:
        return self._status

    @abstractmethod
    def setup(self) -> None:
        """ Will set all pins, connections or peripherals"""
        ...

    @abstractmethod
    def run(self):
        """ Main Execution """
        ...
    @abstractmethod
    def read_sensor(self) -> dict[str, Any]:
        ...
    @abstractmethod
    def handle_error(self, error: Exception) -> None:
        ...


    
