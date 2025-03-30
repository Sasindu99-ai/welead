from vvecon.zorion import serializers

from ...models import User

__all__ = ["VerifyOTPRequest"]


class VerifyOTPRequest(serializers.ModelRequest):
    class Meta:
        model = User
        fields = ["country", "mobileNumber", "passcode"]
