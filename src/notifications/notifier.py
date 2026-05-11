from .contracts import IMessengerClient

class StudentNotifier:
    """Работает только с контрактом. Не создаёт, не выбирает, не конфигурирует."""
    def __init__(self, client: IMessengerClient):
        self.client = client
    
    def notify_request_created(self, student_id: str, request_id: int) -> bool:
        message = f"Your request #{request_id} has been created"
        return self.client.send(student_id, message)
    
    def notify_duplicate(self, student_id: str, topic: str) -> bool:
        message = f"Duplicate request on topic '{topic}'"
        return self.client.send(student_id, message)