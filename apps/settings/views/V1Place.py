from urllib.parse import unquote

from apps.settings.payload.responses import Return
from apps.settings.services import LocationService
from vvecon.zorion.logger import Logger
from vvecon.zorion.views import API, Mapping, PostMapping

__all__ = ["V1Place"]


@Mapping("api/v1/place")
class V1Place(API):
    locationService: LocationService = LocationService()

    @PostMapping("/<str:search>")
    def search(self, request, search: str):
        search = unquote(search)
        Logger.info(f"Fetching places for search: {search}")
        data = self.locationService.autoComplete(search, components="country:LK")
        Logger.info(
            f"{len(data.get('predictions', []))} places found for search: {search}"
        )
        return Return.ok(
            [
                dict(
                    placeId=prediction.get("place_id"),
                    name=prediction.get("description"),
                )
                for prediction in data.get("predictions", [])
            ]
        )

    @PostMapping("/airports/<str:search>")
    def searchAirports(self, request, search: str):
        search = unquote(search)
        Logger.info(f"Fetching airports for search: {search}")
        data = self.locationService.autoComplete(search, placeType="airport")
        Logger.info(
            f"{len(data.get('predictions', []))} airports found for search: {search}"
        )
        return Return.ok(
            [
                dict(
                    placeId=prediction.get("place_id"),
                    name=prediction.get("description"),
                )
                for prediction in data.get("predictions", [])
            ]
        )
