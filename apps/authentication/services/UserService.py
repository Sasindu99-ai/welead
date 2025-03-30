import re
from typing import Any

from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import NotFound, ValidationError

from apps.settings.services import CountryService
from vvecon.zorion.core import Service

from ..models import User

__all__ = ["UserService"]


class UserService(Service):
    mobileNumber = NotImplemented
    model = User
    updateInclude = ("firstName", "lastName")

    class Meta:
        model = User
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.countryService = CountryService()

    def getByMobileNumber(self, country: int, mobileNumber: int) -> User | None:
        return (
            self.model.objects.filter(country=country, mobileNumber=mobileNumber)
            .order_by("-date_joined")
            .first()
        )

    def getByEmail(self, email: str, default: Any = NotImplemented) -> User | None:
        user = self.model.objects.filter(email=email).order_by("-date_joined").first()
        if user is None and default is NotImplemented:
            raise NotFound("User not found")
        return user

    @staticmethod
    def validatePassword(password: str) -> tuple[bool, str]:
        if not re.search(r"\d", password):
            return False, "Password must contain at least one digit"
        if not re.search(r"[A-Z]", password):
            return False, "Password must contain at least one uppercase letter"
        if not re.search(r"[a-z]", password):
            return False, "Password must contain at least one lowercase letter"
        if not re.search(r"[@_!#$%^&*()<>?/\\|}{~:]", password):
            return False, "Password must contain at least one special character"
        return True, password

    def getTrustedUserByMobileNumber(self, countryId, mobileNumber) -> User:
        try:
            try:
                country = self.countryService.getById(countryId)
            except (NotFound, ObjectDoesNotExist):
                raise ValidationError({"countryCode": "Invalid country code"})
            countryCode = country.code

            user = self.getByMobileNumber(country.pk, mobileNumber)
            if user is None:
                return self.createNewUserByMobileNumber(
                    countryCode, country.pk, mobileNumber
                )
            return user
        except (NotFound, ObjectDoesNotExist):
            return self.createNewUserByMobileNumber(
                countryCode, country.pk, mobileNumber
            )

    def getTrustedUserByEmail(self, email: str) -> User:
        try:
            user = self.getByEmail(email, default=None)
            if user is None:
                return self.createNewUserByEmail(email)
            return user
        except (NotFound, ObjectDoesNotExist):
            return self.createNewUserByEmail(email)

    def createNewUserByMobileNumber(
        self, countryCode: str, country: int, mobileNumber: int
    ) -> User:
        return self.create(
            dict(countryCode=countryCode, mobileNumber=mobileNumber, country_id=country)
        )

    def createNewUserByEmail(self, email: str) -> User:
        return self.create(dict(email=email))

    def emailAuthenticate(self, email: str, password: str) -> User | None:
        user = self.getByEmail(email)
        if user is not None and user.check_password(password):
            return user
        return None
