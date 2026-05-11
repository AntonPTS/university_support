import yaml
from abc import ABC, abstractmethod
from .contracts import IMessengerClient, IAuth, IMessageSerializer, IErrorHandler

# Абстрактная фабрика (контракт семейства)
class INotificationFamily(ABC):
    @abstractmethod
    def create_auth(self) -> IAuth: ...
    @abstractmethod
    def create_serializer(self) -> IMessageSerializer: ...
    @abstractmethod
    def create_error_handler(self) -> IErrorHandler: ...
    @abstractmethod
    def create_client(self) -> IMessengerClient: ...

# Конкретные фабрики
class ProviderAFamily(INotificationFamily):
    from .providers.provider_a import AuthA, SerializerA, ErrorHandlerA, ClientA
    def create_auth(self): return self.AuthA()
    def create_serializer(self): return self.SerializerA()
    def create_error_handler(self): return self.ErrorHandlerA()
    def create_client(self):
        return self.ClientA(self.create_auth(), self.create_serializer(), self.create_error_handler())

class ProviderBFamily(INotificationFamily):
    from .providers.provider_b import AuthB, SerializerB, ErrorHandlerB, ClientB
    def create_auth(self): return self.AuthB()
    def create_serializer(self): return self.SerializerB()
    def create_error_handler(self): return self.ErrorHandlerB()
    def create_client(self):
        return self.ClientB(self.create_auth(), self.create_serializer(), self.create_error_handler())

# Фабрика выбора семейства по конфигу
class NotificationFamilyFactory:
    @staticmethod
    def create_from_config(config_path: str = "config.yaml") -> INotificationFamily:
        with open(config_path, "r", encoding="utf-8") as f:
            cfg = yaml.safe_load(f)
        provider = cfg.get("notificationProvider", "providerA").lower()
        if provider == "providera": return ProviderAFamily()
        elif provider == "providerb": return ProviderBFamily()
        else: raise ValueError(f"Unknown provider: {provider}")