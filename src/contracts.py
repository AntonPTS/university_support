from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Request:
    student_id: str
    topic: str
    text: str
    channel: str
    is_urgent: bool = False

class IRequestSource(ABC):
    """Контракт источника обращений (изменчивая инфраструктура)."""
    @abstractmethod
    def exists(self, student_id: str, topic: str) -> bool: ...
    
    @abstractmethod
    def save(self, request: Request) -> int: ...