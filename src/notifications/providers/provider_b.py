from notifications.contracts import IMessengerClient, IAuth, IMessageSerializer, IErrorHandler

class AuthB(IAuth):
    def authenticate(self) -> str: return "Bearer token_b_v2"  # Другой формат токена

class SerializerB(IMessageSerializer):
    def serialize(self, student_id: str, message: str) -> bytes:
        import json
        return json.dumps({"uid": student_id, "msg": message, "ver": 2}).encode()

class ErrorHandlerB(IErrorHandler):
    def handle(self, error: Exception, context: str) -> bool:
        # B логирует и пробрасывает ошибку
        with open("errors_b.log", "a") as f: f.write(f"{context}: {error}\n")
        return False

class ClientB(IMessengerClient):
    def __init__(self, auth: IAuth, serializer: IMessageSerializer, handler: IErrorHandler):
        self.auth, self.serializer, self.handler = auth, serializer, handler
    def send(self, student_id: str, message: str) -> bool:
        token = self.auth.authenticate()
        payload = self.serializer.serialize(student_id, message)
        # TODO: Реальный gRPC вызов к ProviderB с заголовком Authorization: {token}
        print(f"[ProviderB] Sent: {payload}")
        return True  # B считает отправку успешной по умолчанию