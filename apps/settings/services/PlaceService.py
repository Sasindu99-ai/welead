from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import NotFound

from apps.settings.services import LocationService
from vvecon.zorion.core import Service

from ..models import Place

__all__ = ["PlaceService"]


class PlaceService(Service):
    model = Place

    def __init__(self, *args, **kwargs):
        super(PlaceService, self).__init__(*args, **kwargs)

        self.locationService = LocationService()

    def getByPlaceId(self, placeId: str) -> Place:
        try:
            place = self.model.objects.filter(placeId=placeId).first()
            if place is None:
                raise NotFound("Place not found")
            return place
        except ObjectDoesNotExist:
            raise NotFound("Place not found")

    def getPlace(self, placeId: str) -> Place:
        try:
            place = self.getByPlaceId(placeId)
            if place is None:
                raise NotFound("Place not found")
            return place
        except (ObjectDoesNotExist, NotFound):
            return self.createPlace(placeId)

    def createPlace(self, placeId: str) -> Place:
        data = self.locationService.locationInfo(placeId)
        data = data.get("result")
        locName = data.get("name")
        if data.get("formatted_address")[0].isdigit():
            locName += ", " + ", ".join(data.get("formatted_address").split(",")[1:])
        else:
            locName += ", " + data.get("formatted_address")
        place = self.model.objects.create(
            name=locName,
            placeId=placeId,
            latitude=data.get("geometry").get("location").get("lat"),
            longitude=data.get("geometry").get("location").get("lng"),
        )
        return place
