import asyncio
from concurrent.futures import ThreadPoolExecutor
from datetime import timedelta

import requests
from django.contrib.auth import login
from django.utils import timezone

from apps.settings.payload.responses import Return
from apps.settings.payload.responses.CountryResponse import CountryResponse
from apps.settings.services import CountryService
from vvecon.zorion.utils import Utils
from vvecon.zorion.views import API, GetMapping, Mapping, PostMapping

from ..payload.request import (
    RequestEmailRequest,
    RequestOTPRequest,
    VerifyEmailRequest,
    VerifyOTPRequest,
)
from ..services import EmailService, SMSService, UserService

__all__ = ["V1Auth"]


@Mapping("api/v1/auth")
class V1Auth(API):
    executor = ThreadPoolExecutor()
    userService: UserService = UserService()
    countryService: CountryService = CountryService()

    @GetMapping("/country")
    def getCountryFromRequest(self, request):
        IP = request.META.get("HTTP_X_FORWARDED_FOR")
        geo = requests.get(f"https://ip-api.com/json/{IP}").json()
        if geo["status"] == "fail":
            country = self.countryService.getByName("Sri Lanka")
        else:
            country = self.countryService.getByName(geo["country"])
        return CountryResponse(data=country).json()

    @PostMapping("/request-otp")
    def requestOTP(self, request, data: RequestOTPRequest):
        if data.is_valid(raise_exception=True):
            country = data.validated_data["country"]
            mobileNumber = int(data.validated_data["mobileNumber"])
            user = self.userService.getTrustedUserByMobileNumber(country, mobileNumber)
            if user is None:
                return Return.badRequest(dict(message="Invalid user account"))
            if timezone.now() - user.lastPasscodeUpdated() < timedelta(minutes=1):
                time = f"{(60 - (timezone.now() - user.lastPasscodeUpdated()).seconds)} seconds"
                return Return.badRequest(
                    dict(
                        message=f"Please wait for {time} before requesting another OTP"
                    )
                )

            passcode = Utils.generatePasscode()
            user.set_passcode(passcode)
            user.save()

            self.executor.submit(
                lambda: asyncio.run(
                    SMSService.sendOTP(
                        f"+{user.countryCode}{user.mobileNumber}", passcode
                    )
                )
            )

            return Return.ok(
                dict(
                    result=dict(
                        country=user.country.pk,
                        countryCode=user.countryCode,
                        mobileNumber=user.mobileNumber,
                    )
                )
            )

    @PostMapping("/verify-otp")
    def verifyOTP(self, request, data: VerifyOTPRequest):
        if data.is_valid(raise_exception=True):
            country = data.validated_data["country"]
            mobileNumber = int(data.validated_data["mobileNumber"])
            user = self.userService.getTrustedUserByMobileNumber(
                country.pk, mobileNumber
            )
            if user is None:
                return Return.badRequest(dict(message="Invalid user account"))
            if user.check_passcode(data.validated_data["passcode"]) is False:
                return Return.badRequest(dict(message="Invalid passcode"))
            if timezone.now() - user.lastPasscodeUpdated() > timedelta(minutes=15):
                return Return.badRequest(dict(message="OTP has expired"))
            login(request, user)
            user.set_unusable_passcode()
            user.save()
            return Return.ok(dict(result=True))

    @PostMapping("/request-email")
    def requestEmail(self, request, data: RequestEmailRequest):
        if data.is_valid(raise_exception=True):
            user = self.userService.getTrustedUserByEmail(data.validated_data["email"])
            if user is None:
                return Return.badRequest(dict(message="Invalid user account"))
            if timezone.now() - user.lastPasscodeUpdated() < timedelta(minutes=1):
                time = f"{(60 - (timezone.now() - user.lastPasscodeUpdated()).seconds)} seconds"
                return Return.badRequest(
                    dict(
                        message=f"Please wait for {time} before requesting another OTP"
                    )
                )

            passcode = Utils.generatePasscode()
            user.set_passcode(passcode)
            user.save()

            self.executor.submit(
                lambda: asyncio.run(
                    EmailService.sendEmailOTPDefault(user.email, passcode)
                )
            )

            return Return.ok(dict(result=dict(email=user.email)))

    @PostMapping("/verify-email")
    def verifyEmail(self, request, data: VerifyEmailRequest):
        if data.is_valid(raise_exception=True):
            user = self.userService.getTrustedUserByEmail(data.validated_data["email"])
            if user is None:
                return Return.badRequest(dict(message="Invalid user account"))
            if user.check_passcode(data.validated_data["passcode"]) is False:
                return Return.badRequest(dict(message="Invalid passcode"))
            if timezone.now() - user.lastPasscodeUpdated() > timedelta(minutes=15):
                return Return.badRequest(dict(message="OTP has expired"))
            login(request, user)
            user.set_unusable_passcode()
            user.save()
            return Return.ok(dict(result=True))
