from abc import ABC, abstractmethod 
from typing import Callable, Any
from dataclasses import dataclass


# @Incomplete
class BaseStorageModel(ABC):

    @abstractmethod
    def write(self, data: Any) -> None:
        ...
    
    @abstractmethod
    def read(self, data: Any) -> None:
        ...
    
    @abstractmethod
    def encrypt(self, data: Any) -> str:
        ...
    
    @abstractmethod
    def decrypt(self, data: str) -> Any:
        ...
