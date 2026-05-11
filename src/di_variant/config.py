import yaml
import os
from dataclasses import dataclass

@dataclass
class AppConfigDI:
    audit_enabled: bool = True
    provider: str = "providerA"

    @classmethod
    def from_file(cls, path: str = "config.yaml") -> "AppConfigDI":
        if not os.path.exists(path):
            raise FileNotFoundError(f"Config not found: {path}")
        with open(path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        return cls(
            audit_enabled=data.get("audit_enabled", True),
            provider=data.get("notificationProvider", "providerA")
        )