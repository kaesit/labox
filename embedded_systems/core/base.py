from abc import ABC, abstractmethod
from typing import Callable, Any, Dict, Optional
from enum import IntEnum




class BaseStateMachine(ABC):
    def __init__(self, state_step: int):
        self.state_step = state_step
        self._transition_matrix: dict  = {}
        self._lock = threading.Lock()

    
    @abstractmethod
    def EventHandler(self) -> None:
        # @Incomplete
        """ This function will be an abstracted event handler for base state machine class"""
        ...

    @abstractmethod
    def ActionHandler(self) -> None:
        # @Incomplete
        """ This function will be an abstracted action handler for base state machine class"""
        ...

    @abstractmethod
    def TransitionHandler(self) -> None: 
        # @Incomplete i have no idea if we need a complex dictionary formatted information or nothing for the output this part @Must be revisited.
        """ This function will be an abstracted transition handler for base state machine class"""
        ...

    @abstractmethod
    def States (self) -> None:
        # @Incomplete i have no idea if we need a complex dictionary formatted information or nothing for the output this part @Must be revisited.
        """ This function will be an abstracted State function for base state machine class"""
        ...

class BaseWatchDogTimer(ABC):
    def __init__(self, timeout: int):
        self.timeout = timeout

    @abstractmethod
    def start(self):
        # @Incomplete
        """ Starts watchdog timer"""
        pass
    @abstractmethod
    def feed(self):
        # @Incomplete
        """ Resets watchdog timer"""
        pass
    @abstractmethod
    def stop(self):
        # @Incomplete
        """ Stops watchdog timer"""
        pass

class ErrorSeverity(IntEnum):
    INFO = 0
    WARNING = 1
    RECOVERABLE = 2
    CRITICAL = 3
    FATAL = 4

class BaseErrorHandling(ABC):
    def __init__(self, error: Exception) -> None:
        """ This function will be base function for exception handling"""
        pass

    @abstractmethod
    def _get_system_time(self):
        """ This function will get system time"""
        pass
    
    @abstractmethod
    def report_error(self, msg:str, context: Optional[Dict[str, Any]]) -> None:
        """ This function will show an error output in dict format"""
        pass
    
    @abstractmethod
    def get_error_count(self) -> int:
        return self._error_count

    @absractmethod
    def get_last_error(self) -> Optional[Dict[str, Any]]:
        return self._last_error

# @Incomplete
# @Robustness
# This is not complete and @Must be revisited, flaws are so much: there are no itemSize structure, no buffer_destroy function
class RingBuffer():
    
    def __init__(self, head:int, tail: int, buffer_capacity:int, data: bytearray = None):
        self.head = head
        self.tail = tail
        self.buffer_capacity = buffer_capacity
        
        if data is None:
            self.data = bytearray(buffer_capacity)
        else:
            self.data = data

    
    def push(self):
        """ This is the data add function of Ring Buffer class"""
        pass
    
    def pop(self):
        """ This is the data add function of Ring Buffer class"""
        pass
    
    def is_buffer_empty(self) -> bool:
        """ This function will check if the ring buffer is empty or not"""
        pass
    
    def is_buffer_full(self) -> bool:
        """ This function will check if the ring buffer is full or not"""
        pass
    
    def get_free_space_of_buffer(self) -> int:
        """ This function will return empty space in ring buffer"""
        pass

class BaseHardwareInterface(ABC):
    # @Incomplete
    # @Scenario: This will be an abstract Interface for communicating between embedded devices.
    """ 
    Context: 
    Must be thread safe like every other thing on this system other wise must be revisited
    This is a interface structure so it must abstracted so well that no other problem occur in any test case             
    """
    # @F-Test: there are no test cases for this class
    def __init__(self):
        pass

class BaseCommandDispatcher(ABC):
    def __init__(self):
        pass
class BasePayloadParser(ABC):
    def __init__(self):
        pass
