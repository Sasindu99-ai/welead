from datetime import datetime, timedelta
from typing import Any, Dict

from apps.settings.services import CountryService, SettingService
from vvecon.zorion.views import GetMapping, Mapping, View
from ..settings import R

__all__ = ["HomeView"]


@Mapping("")
class HomeView(View):
    R = R()

    settingService: SettingService = SettingService()
    countryService: CountryService = CountryService()

    def basicConfig(self):
        self.R.data.navigator.enabled = True
        self.R.data.footer.enabled = True
        self.R.data.settings.mobileNumber = self.settingService.getByKey(
            "hotline", "general", None
        )
        self.R.data.settings.email = self.settingService.getByKey(
            "hotmail", "general", None
        )
        self.context = dict(
            countries=self.countryService.getAll(),
            heroSectionBackground=self.settingService.getByKey(
                "hero-section-background", "home", None
            ),
        )

    @GetMapping("")
    def home(self, request):
        self.basicConfig()

        self.R.data.settings.head = "Home"
        self.R.data.navigator.activeTab = "home"

        context: Dict[str, Any] = dict(
            hero=dict(
                background="/media/settings/home/hero-section-background.png",
                title="Hero Section Title Here",
                subtitle="Here is the subtitle for hero section. you can change this using admin panel. Please change "
                "this if you want to change this.  ",
                primaryButton=dict(
                    text="Learn More", classNames="btn-primary", link="#"
                ),
                secondaryButton=dict(
                    text="Join Now", classNames="btn-secondary", link="#"
                ),
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
