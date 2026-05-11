from contracts import IRequestSource, Request
from unittest.mock import Mock

class RequestProcessor:
    """Доменная логика. Зависит только от контракта, не создаёт объекты и не читает конфиг."""
    def __init__(self, data_source: IRequestSource, logger=None, notifier=None, responder=None):
        self.data_source = data_source
        self.logger = logger or Mock()
        self.notifier = notifier or Mock()
        self.responder = responder or Mock()

    def process(self, student_id: str, topic: str, text: str, channel: str, urgent: bool = False) -> str:
        if not student_id or not topic or not text:
            raise ValueError("Bad request")

        req = Request(student_id, topic, text, channel, urgent)

        if self.data_source.exists(student_id, topic):
            self.logger.write(f"Duplicate: {student_id}")
            return "Already exists"

        req_id = self.data_source.save(req)
        self.logger.write(f"Created id={req_id}")
        self.notifier.send(channel, student_id, f"Request #{req_id}")
        return self.responder.build(topic) if self.responder else "Request accepted"