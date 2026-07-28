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

class BaseReaderModel(ABC):
    @abstractmethod
    def decode(self, data:str) -> Any:
        ...

    @abstractmethod
    def show_data_properties(self, data:Any) -> dict:
        ...
class DataCompressModel(ABC):
    
    @abstractmethod
    def run(self):
        ...

    @abstractmethod
    def get_storage_size(self, data: int):
        ...

    @abstractmethod
    def set_compression_size(self, data:Any) -> None:
        ...
class DataDecompressModel(ABC):
    @abstractmethod
    def run(self):
        ...

    @abstractmethod
    def decompression(self, data:Any) -> Any:
        ...

