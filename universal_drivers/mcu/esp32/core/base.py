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

# @Incomplete
# This classes should be remodeled by reviewing unique properties of the device
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


    
