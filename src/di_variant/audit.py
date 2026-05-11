from .config import AppConfigDI

class AuditLoggerDI:
    """Явная зависимость. Не создаёт и не читает конфиг сам."""
    def __init__(self, config: AppConfigDI, storage: list = None):
        self.config = config
        # ✅ Правильная проверка: сохраняем ссылку на переданный список, даже если он пустой
        self.storage = storage if storage is not None else []

    def log(self, student_id: str, request_id: int, channel: str, success: bool):
        if self.config.audit_enabled:
            self.storage.append({
                "student_id": student_id, "request_id": request_id,
                "channel": channel, "success": success
            })