from abc import ABC, abstractmethod
from typing import Dict, Callable, Any, Optional
from enum import Enum

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
    def __init__(self) -> Dict[str, Any]:
        pass


