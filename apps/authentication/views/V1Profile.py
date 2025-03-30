from apps.authentication.services import UserService
from apps.settings.payload.responses import Return
from vvecon.zorion.auth import Authorized
from vvecon.zorion.views import API, Mapping, PutMapping

from ..payload.request import UpdateProfileRequest

__all__ = ["V1Profile"]


@Mapping("api/v1/profile")
class V1Profile(API):
    userService: UserService = UserService()

    @PutMapping("")
    @Authorized(True)
    def updateProfile(self, request, data: UpdateProfileRequest):
        if data.is_valid(raise_exception=True):
            user = self.userService.getById(request.user.pk)
            if user is None:
                Return.badRequest("User not found")
            self.userService.update(user, data.validated_data)
            return Return.ok()
