from vvecon.zorion.views import View, Mapping, GetMapping
from ..settings import R
from apps.settings.services import CountryService, SettingService

__all__ = ["ContactUsView"]


@Mapping("contact-us")
class ContactUsView(View):
    R = R()

    settingService: SettingService = SettingService()
    countryService: CountryService = CountryService()

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
    def contactUs(self, request):
        self.basicConfig()

        self.R.data.settings.head = "Contact Us"
        self.R.data.navigator.activeTab = "contact-us"

        context = dict()

        return self.render(request, context=context, template_name="contact-us")
