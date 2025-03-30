from rest_framework import serializers

from ...services import UserService

__all__ = ["LoginRequest"]


class LoginRequest(serializers.Serializer):
    countryCode = serializers.CharField(max_length=5)
    mobileNumber = serializers.IntegerField()
    passcode = serializers.CharField(max_length=6)

    def validate(self, data):
        countryCode = data.get("countryCode")
        mobileNumber = data.get("mobileNumber")
        passcode = data.get("passcode")
        if countryCode is None:
            raise serializers.ValidationError(
                {"countryCode": "Country code is required"}
            )
        if mobileNumber is None:
            raise serializers.ValidationError(
                {"mobileNumber": "Mobile number is required"}
            )
        if passcode is None:
            raise serializers.ValidationError({"passcode": "Passcode is required"})
        user = UserService().getByMobileNumber(mobileNumber)
        if user is None:
            raise serializers.ValidationError({"mobileNumber": "User not found"})
        if user.countryCode != countryCode:
            raise serializers.ValidationError({"countryCode": "Invalid country code"})
        data["user"] = user
        return data
