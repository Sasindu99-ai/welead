from vvecon.zorion import serializers

__all__ = ["RequestEmailRequest"]


class RequestEmailRequest(serializers.Request):
    email = serializers.EmailField()
