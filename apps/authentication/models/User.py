from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.hashers import (
    acheck_password,
    check_password,
    is_password_usable,
    make_password,
)
from django.contrib.auth.models import Group, Permission, PermissionsMixin
from django.db import models
from django.utils import timezone

from apps.settings.models import Country

from ..enums import UserRole
from ..managers import UserManager

__all__ = ["User"]


class User(AbstractBaseUser, PermissionsMixin):
    _passcode = None

    countryCode = models.CharField(
        max_length=5, verbose_name="Country Code", null=True, blank=True
    )
    mobileNumber = models.IntegerField(
        verbose_name="Mobile Number", null=True, blank=True
    )
    passcode = models.CharField(verbose_name="Passcode", max_length=128)
    firstName = models.CharField(
        max_length=50, verbose_name="First Name", null=True, blank=True
    )
    lastName = models.CharField(
        max_length=50, verbose_name="Last Name", null=True, blank=True
    )
    email = models.EmailField(
        blank=True, null=True, verbose_name="Email Address", unique=True
    )
    icloud = models.EmailField(blank=True, null=True, verbose_name="iCloud Address")
    nic = models.CharField(
        max_length=20, blank=True, null=True, verbose_name="NIC Number"
    )
    dateOfBirth = models.DateField(blank=True, null=True, verbose_name="Date of Birth")
    is_active = models.BooleanField(default=True, verbose_name="Active")
    is_superuser = models.BooleanField(default=False, verbose_name="Superuser")
    is_staff = models.BooleanField(default=False, verbose_name="Staff")
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name="Date Joined")
    last_login = models.DateTimeField(auto_now=True, verbose_name="Last Login")
    country = models.ForeignKey(
        Country,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Country",
    )
    passcodeUpdated = models.DateTimeField(
        verbose_name="Passcode Updated", null=True, blank=True
    )
    username = models.CharField(
        max_length=150, blank=True, null=True, verbose_name="Username"
    )

    groups = models.ManyToManyField(
        Group,
        related_name="authentication_user_groups",
        verbose_name="groups",
        blank=True,
        help_text=(
            "The groups this user belongs to. A user will get all permissions "
            "granted to each of their groups."
        ),
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="authentication_user_user_permissions",
        verbose_name="user permissions",
        blank=True,
        help_text="Specific permissions for this user.",
        related_query_name="user",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["firstName", "lastName", "countryCode", "mobileNumber"]

    objects = UserManager()

    def __str__(self):
        if self.firstName or self.lastName:
            return f"{self.firstName} {self.lastName}"
        if self.countryCode and self.mobileNumber:
            return f"+{self.countryCode}{self.mobileNumber}"
        if self.email:
            return self.email
        return self.icloud

    @property
    def fullName(self):
        return f"{self.firstName + ' ' if self.firstName else ''}{self.lastName if self.lastName else ''}"

    def setRole(self, role: UserRole):
        if not self.pk:
            raise ValueError("User must be saved before setting role")
        for userRole in UserRole.values:
            if self.groups.filter(name=userRole).exists():
                self.groups.remove(userRole)
        self.groups.add(Group.objects.get(name=role.value))

    def set_passcode(self, raw_passcode):
        self.passcode = make_password(raw_passcode)
        self._passcode = raw_passcode
        self.passcodeUpdated = timezone.now()

    def check_passcode(self, raw_passcode):
        def setter(raw_passcode):
            self.set_passcode(raw_passcode)
            # Passcode hash upgrades shouldn't be considered passcode changes.
            self._passcode = None
            self.save(update_fields=["passcode"])

        return check_password(raw_passcode, self.passcode, setter)

    async def acheck_passcode(self, raw_passcode):
        async def setter(raw_passcode):
            self.set_passcode(raw_passcode)
            # Password hash upgrades shouldn't be considered passcode changes.
            self._passcode = None
            await self.asave(update_fields=["passcode"])

        return await acheck_password(raw_passcode, self.passcode, setter)

    def set_unusable_passcode(self):
        # Set a value that will never be a valid hash
        self.passcode = make_password(None)

    def has_usable_passcode(self):
        return is_password_usable(self.passcode)

    def lastPasscodeUpdated(self):
        if self.passcodeUpdated:
            return self.passcodeUpdated
        return timezone.make_aware(timezone.datetime(2000, 1, 1, 0, 0, 0))

    @property
    def mobileNumberWithLength(self):
        if not self.country:
            if self.mobileNumber:
                return self.mobileNumber
            return None
        length = self.country.length
        if len(str(self.mobileNumber)) < length:
            return f"{str(self.mobileNumber):0>{length}}"
        return self.mobileNumber
