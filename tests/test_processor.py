import pytest
from interfaces import RequestRepository, NotificationService, Logger

# Заглушки, имитирующие будущую подмену зависимостей
class StubRepository:
    def __init__(self, is_duplicate: bool = False):
        self.is_duplicate = is_duplicate
    def exists(self, student_id, topic) -> bool:
        return self.is_duplicate
    def save(self, data) -> int:
        return 101

class StubNotificationService:
    def __init__(self):
        self.sent_messages = []
    def send(self, channel, student_id, message):
        self.sent_messages.append((channel, student_id, message))

class StubLogger:
    def __init__(self):
        self.logs = []
    def write(self, message):
        self.logs.append(message)

# Целевой класс-заготовка
class RequestProcessor:
    def __init__(self, repo: RequestRepository, notifier: NotificationService, logger: Logger):
        self.repo = repo
        self.notifier = notifier
        self.logger = logger

    def process(self, student_id, topic, text, channel, urgent=False) -> str:
        raise NotImplementedError("Рефакторинг в процессе")


@pytest.mark.xfail(reason="Шаг 2 плана не выполнен: process() пока заглушка")
def test_create_new_request():
    # Подмена: репозиторий не проверяет дубли, notifier и логгер не пишут в файлы
    repo = StubRepository(is_duplicate=False)
    notifier = StubNotificationService()
    logger = StubLogger()

    processor = RequestProcessor(repo, notifier, logger)
    result = processor.process("S1", "schedule", "Help", "email")


@pytest.mark.xfail(reason="Шаг 2 плана не выполнен: process() пока заглушка")
def test_duplicate_request():
    # Подмена: репозиторий сразу сообщает о дубле
    repo = StubRepository(is_duplicate=True)
    notifier = StubNotificationService()
    logger = StubLogger()

    processor = RequestProcessor(repo, notifier, logger)
    result = processor.process("S1", "schedule", "Help", "email")