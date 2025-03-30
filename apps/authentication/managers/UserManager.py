from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError

__all__ = ["UserManager"]


class UserManager(BaseUserManager):
    def create_user(
        self,
        countryCode,
        mobileNumber,
        firstName,
        lastName,
        email=None,
        nic=None,
        dateOfBirth=None,
        password=None,
    ):
        if not countryCode:
            raise ValidationError("Country Code is required")
        if not mobileNumber:
            raise ValidationError("Mobile Number is required")
        if not firstName:
            raise ValidationError("First Name is required")
        if not lastName:
            raise ValidationError("Last Name is required")
        user = self.model(
            countryCode=countryCode,
            mobileNumber=mobileNumber,
            firstName=firstName,
            lastName=lastName,
            email=email,
            nic=nic,
            dateOfBirth=dateOfBirth,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self,
        countryCode,
        mobileNumber,
        firstName,
        lastName,
        email=None,
        nic=None,
        dateOfBirth=None,
        password=None,
    ):
        user = self.create_user(
            countryCode=countryCode,
            mobileNumber=mobileNumber,
            firstName=firstName,
            lastName=lastName,
            email=email,
            nic=nic,
            dateOfBirth=dateOfBirth,
            password=password,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
