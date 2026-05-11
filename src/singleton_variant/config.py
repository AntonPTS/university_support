import yaml
import os
import threading
from dataclasses import dataclass

@dataclass
class AppConfig:
    audit_enabled: bool = True
    provider: str = "providerA"

class AppConfigSingleton:
    _instance = None
    _lock = threading.Lock()

    def __init__(self, config_path: str = "config.yaml"):
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Config not found: {config_path}")
        with open(config_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        self.audit_enabled = data.get("audit_enabled", True)
        self.provider = data.get("notificationProvider", "providerA")

    @classmethod
    def get_instance(cls, config_path: str = "config.yaml") -> "AppConfigSingleton":
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = cls(config_path)
        return cls._instance

    @classmethod
    def reset(cls):
        with cls._lock:
            cls._instance = None