from rest_framework import serializers

from apps.settings.services import CountryService

__all__ = ["RequestOTPRequest"]


class RequestOTPRequest(serializers.Serializer):
    country = serializers.IntegerField()
    mobileNumber = serializers.CharField(max_length=20)

    def validate(self, data):
        countryService = CountryService()

        country = data.get("country")
        mobileNumber = data.get("mobileNumber")
        if country is None:
            raise serializers.ValidationError(
                {"countryCode": "Country code is required"}
            )
        if mobileNumber is None:
            raise serializers.ValidationError(
                {"mobileNumber": "Mobile number is required"}
            )
        country = countryService.getById(country)
        if country is None:
            raise serializers.ValidationError({"countryCode": "Invalid country code"})
        if len(mobileNumber) != country.length:
            raise serializers.ValidationError(
                {"mobileNumber": f"Mobile number must be {country.length} digits"}
            )
        if not mobileNumber.isdigit():
            raise serializers.ValidationError(
                {"mobileNumber": "Mobile number must be numeric"}
            )
        return super().validate(data)
