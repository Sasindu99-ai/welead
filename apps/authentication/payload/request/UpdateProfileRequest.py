from vvecon.zorion import serializers

from ...models import User

__all__ = ["UpdateProfileRequest"]


class UpdateProfileRequest(serializers.ModelRequest):
    class Meta:
        model = User
        fields = ("firstName", "lastName")
