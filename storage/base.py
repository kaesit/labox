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
# @Incomplete
class StorageOptimizer():
    def __init__(self):
        ...

class DataCompressModel():
    def __init__(self):
        ...

class BaseWriterModel(ABC):
    @abstractmethod
    def encode(self, data: Any) -> str:
        ...
    
    @abstractmethod
    def get_storage_device_info(self, data: Any) -> dict:
        ...

