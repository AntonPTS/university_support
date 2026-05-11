import yaml
import os
from contracts import IRequestSource
from data_sources import DbRequestSource, FileRequestSource, WebServiceRequestSource

class DataSourceFactory:
    """Фабричный метод выбора источника на основе конфигурации."""
    @staticmethod
    def create_from_config(config_path: str = "config.yaml") -> IRequestSource:
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Config not found: {config_path}")

        with open(config_path, "r", encoding="utf-8") as f:
            cfg = yaml.safe_load(f)

        source_type = cfg.get("dataSourceType", "db").lower()

        if source_type == "db":
            return DbRequestSource()
        elif source_type == "file":
            return FileRequestSource(cfg.get("filePath", "requests.json"))
        elif source_type == "web":
            return WebServiceRequestSource(cfg.get("apiUrl", "https://api.uni/support"))
        else:
            raise ValueError(f"Unknown dataSourceType: {source_type}")