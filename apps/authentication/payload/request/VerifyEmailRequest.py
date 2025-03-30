from vvecon.zorion import serializers

__all__ = ["VerifyEmailRequest"]


class VerifyEmailRequest(serializers.Request):
    email = serializers.EmailField()
    passcode = serializers.CharField()
