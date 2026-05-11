import uuid
from contracts import IRequestSource, Request

class DbRequestSource(IRequestSource):
    def exists(self, student_id: str, topic: str) -> bool:
        # TODO: Реальный SQL: SELECT count(*) FROM requests WHERE student_id=? AND topic=?
        return False

    def save(self, request: Request) -> int:
        # TODO: Реальный INSERT + RETURNING id
        return int(uuid.uuid4().int % 10000)

class FileRequestSource(IRequestSource):
    def __init__(self, file_path: str = "requests.json"):
        self.file_path = file_path
        self._cache = {}  # Имитация загрузки из файла

    def exists(self, student_id: str, topic: str) -> bool:
        # TODO: Поиск в десериализованном JSON
        return (student_id, topic) in self._cache

    def save(self, request: Request) -> int:
        # TODO: Запись в JSON, flush на диск
        new_id = int(uuid.uuid4().int % 10000)
        self._cache[(request.student_id, request.topic)] = new_id
        return new_id

class WebServiceRequestSource(IRequestSource):
    def __init__(self, api_url: str = "https://api.uni/support"):
        self.api_url = api_url

    def exists(self, student_id: str, topic: str) -> bool:
        # TODO: HTTP GET /requests/check
        return False

    def save(self, request: Request) -> int:
        # TODO: HTTP POST /requests
        return int(uuid.uuid4().int % 10000)