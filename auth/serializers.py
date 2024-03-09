from fastapi_auth import serializers


class UserSerializer(serializers.Serializer):
    email: str
