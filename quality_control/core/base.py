from abc import ABC, abstractmethod
from typing import Dict, Callable, Any, Optional
from enum import Enum


# @Incomplete
# This file and structures not completed, it @Must be revisited and this class is not urge to finish
class Status(Enum):
        CONTROLING = "controling"
        CHECKING = "checking"
        VALIDATING = "validating"
        ERROR = "error"
        CANCELLED = "cancelled"
        ACCEPTED = "accepted"
        REJECTED = "rejected"

class BaseQualityModel(ABC):
    def __init__(self, task: QualityTask, handler: Any) -> None:
        self.task = task
        self.handler = handler

    @abstractmethod
    def run (self) -> Dict[..., Any]:
        """ This functions runs the whole process"""
        pass
    
    @abstractmethod
    def extract_resuls(self, data:Dict[str, Any], title:str, format_type:str) -> None:
        """ This function will be a helper function for __init__ and also other classes which extended from this class to extract results in a format they like"""
        pass
    def cancel(self) -> None:
        self._status = Status.CANCELLED
        print("Process is cancelled")
class QualityTask:
    def __init__(self, task, status:Status) -> Dict[str, Any]:
        self.task = task
        self.status = status

    @property
    def task(self) -> str:
        return _task
    @task.setter
    def task(self, data:Dict[str, Any]):
        self._task = data

    @task.deleter
    def task(self) -> None:
        del _task
        print("Task is deleted")

    @property
    def status(self) -> int:
        return _status
    @status.setter
    def status(self, data:Status) -> None:
        self._status = data
    @status.deleter
    def status(self) -> None:
        del _status
        print("Deleted status")

