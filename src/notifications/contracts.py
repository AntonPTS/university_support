from abc import ABC, abstractmethod

class IMessengerClient(ABC):
    @abstractmethod
    def send(self, student_id: str, message: str) -> bool: ...

class IAuth(ABC):
    @abstractmethod
    def authenticate(self) -> str: ...  # Возвращает токен

class IMessageSerializer(ABC):
    @abstractmethod
    def serialize(self, student_id: str, message: str) -> bytes: ...

class IErrorHandler(ABC):
    @abstractmethod
    def handle(self, error: Exception, context: str) -> bool: ...