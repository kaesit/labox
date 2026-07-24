from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any

@dataclass
class ExperimentStep:
    name: str
    action: str
    params: dict= field(default_factory=dict)
    timeout_s: float = 30.0
    # @Incomplete: retry policy, on_failure hook eksik

@dataclass
class ExperimentProtocol:
    name: str
    steps: list[ExperimentStep]
    metadata: dict = field(default_factory=dict)

class BaseExperiment(ABC):
    def __init__(self, protocol: ExperimenProtocol):
        self.protocol = protocol

    @abstractmethod
    def run(self) -> dict:
        """Executes each step in order, returns collected results."""
        ...
    @abstractmethod
    def to_tasks(self) -> list["Task"]:
        """Converts protocol steps into scheduler.Task objects."""
        ...
