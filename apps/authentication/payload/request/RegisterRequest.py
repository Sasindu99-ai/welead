from rest_framework import serializers

from ...enums import UserRole
from ...models import User
from ...services import UserService


class RegisterRequest(serializers.Serializer):
    countryCode = serializers.CharField(max_length=5)
    mobileNumber = serializers.IntegerField()
    firstName = serializers.CharField(max_length=50)
    lastName = serializers.CharField(max_length=50)
    role = serializers.ChoiceField(choices=UserRole, default=UserRole.GUEST)

    def __init__(self, *args, **kwargs):
        super(RegisterRequest, self).__init__(*args, **kwargs)
        self.userService = UserService()

    def validate(self, data) -> dict:
        super().validate(data)
        countryCode = data.get("countryCode")
        mobileNumber = data.get("mobileNumber")
        if countryCode is None:
            raise serializers.ValidationError(
                {"countryCode": "Country code is required"}
            )
        if mobileNumber is None:
            raise serializers.ValidationError(
                {"mobileNumber": "Mobile number is required"}
            )
        user = self.userService.getByMobileNumber(mobileNumber)
        if user is not None:
            raise serializers.ValidationError({"message": "User already exists"})
        return data

    def save(self) -> User:
        user = User(
            countryCode=self.validated_data["countryCode"],
            mobileNumber=self.validated_data["mobileNumber"],
            firstName=self.validated_data["firstName"],
            lastName=self.validated_data["lastName"],
        )
        user.save()
        user.setRole(self.validated_data["role"])
        return user
