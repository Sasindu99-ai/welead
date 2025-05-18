from datetime import datetime, timedelta
from typing import Any, Dict

from apps.settings.services import CountryService, SettingService
from vvecon.zorion.views import GetMapping, Mapping, View
from ..enums import BannerPage
from ..services import BannerService
from ..settings import R

__all__ = ["HomeView"]


@Mapping("")
class HomeView(View):
    R = R()

    settingService: SettingService = SettingService()
    countryService: CountryService = CountryService()
    bannerService: BannerService = BannerService()

    def basicConfig(self):
        self.R.data.navigator.enabled = True
        self.R.data.footer.enabled = True
        mobileNumber, email = self.settingService.getByKeys(
            ["hotline", "hotmail"], "general", None
        )
        self.R.data.settings.mobileNumber, self.R.data.settings.email = mobileNumber, email
        self.context = dict(
            countries=self.countryService.getAll(),
        )

    @GetMapping("")
    def home(self, request):
        self.basicConfig()

        self.R.data.settings.head = "Home"
        self.R.data.navigator.activeTab = "home"

        banners = self.bannerService.search(dict(
            page=BannerPage.HOME,
            pagination=dict(
                sortBy=['order', 'created_at']
            )
        ))
        vision, mission = self.settingService.getByKeys(keys=['vision', 'mission'], tag='general')

        context: Dict[str, Any] = dict(
            banners=banners,
            intro=dict(
                vision=vision,
                mission=mission
            ),
            event=dict(
                background="/media/settings/home/event-section-background.png",
                title="EVENT NAME HERE",
                subtitle="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut"
                " labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco "
                "laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in "
                "voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat "
                "cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                startsAt=datetime.now() + timedelta(days=12),
                link="#",
            ),
            faq=dict(
                background="/media/settings/home/faq-section-background.png",
            ),
        )
        return self.render(request, context=context, template_name="home")
