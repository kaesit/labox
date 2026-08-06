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
    def __init__(self) -> None:
        pass

class QualityTask:
    def __init__(self, task) -> Dict[str, Any]:
        self.task = taks

    @property
    def task(self) -> str:
        return _task
    @task.setter
    def task(self, data:Dict[str, Any]):
        self._task = data


