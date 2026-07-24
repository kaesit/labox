from abc import ABC, abstractmethod
from enum import Enum
from dataclasses import dataclass
from typing import Callable, Any

class TaskStatus(Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"

@dataclass
class Task:
    id: str
    fn: Callable[..., Any]
    args: tuple = ()
    kwargs: dict = None
    priority: int = 0
    status: TaskStatus = TaskStatus.PENDING
    depends_on: list[str] = None # @Incomplete : There is no dependency graph yet.

class BaseScheduler(ABC):
    @abstractmethod
    def submit(self, task: Task) -> str: ...

    @abstractmethod
    def cancel(self, task_id: str) -> bool: ...

    @abstractmethod
    def status(self, task_id: str) -> TaskStatus: ...

    @abstractmethod
    def run(self) -> None:
        """Blocking or async main loop that executes pending tasks."""
        ...
