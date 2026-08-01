from abc import ABC, abstractmethod
from typing import Callable, Any
from enum import Enum




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
