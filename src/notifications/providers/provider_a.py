from notifications.contracts import IMessengerClient, IAuth, IMessageSerializer, IErrorHandler

class AuthA(IAuth):
    def authenticate(self) -> str: return "token_a_v1"

class SerializerA(IMessageSerializer):
    def serialize(self, student_id: str, message: str) -> bytes:
        return f"A|{student_id}|{message}".encode()

class ErrorHandlerA(IErrorHandler):
    def handle(self, error: Exception, context: str) -> bool:
        print(f"[ProviderA] {context}: {error}")
        return True  # A всегда "игнорирует" ошибки

class ClientA(IMessengerClient):
    def __init__(self, auth: IAuth, serializer: IMessageSerializer, handler: IErrorHandler):
        self.auth, self.serializer, self.handler = auth, serializer, handler
    def send(self, student_id: str, message: str) -> bool:
        try:
            token = self.auth.authenticate()
            payload = self.serializer.serialize(student_id, message)
            # TODO: Реальный HTTP POST к API ProviderA с token
            print(f"[ProviderA] Sent: {payload}")
            return True
        except Exception as e:
            return self.handler.handle(e, "send")