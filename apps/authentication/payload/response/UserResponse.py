from vvecon.zorion import serializers

from ...models import User

__all__ = ["UserResponse"]


class UserResponse(serializers.ModelResponse):
    model = User
    fields = "__all__"
