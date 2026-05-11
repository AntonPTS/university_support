import threading
from .config import AppConfigSingleton

class AuditLoggerSingleton:
    _instance = None
    _lock = threading.Lock()

    def __init__(self):
        self.logs = []

    @classmethod
    def get_instance(cls) -> "AuditLoggerSingleton":
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = cls()
        return cls._instance

    def log(self, student_id: str, request_id: int, channel: str, success: bool):
        cfg = AppConfigSingleton.get_instance()
        if cfg.audit_enabled:
            self.logs.append({
                "student_id": student_id, "request_id": request_id,
                "channel": channel, "success": success
            })

    @classmethod
    def reset(cls):
        with cls._lock:
            cls._instance = None  # При следующем get_instance() создастся новый экземпляр с чистым logs