from apps.settings.services import PageService, SettingService
from vvecon.zorion.views import GetMapping, Mapping, View

from ..settings import R

__all__ = ["PageView"]


@Mapping("page")
class PageView(View):
    R = R()

    settingService = SettingService()
    pageService = PageService()

    def basicConfig(self):
        self.R.data.settings.mobileNumber = self.settingService.getByKey(
            "hotline", "general", None
        )

    @GetMapping("/<slug:slug>")
    def page(self, request, slug):
        self.basicConfig()

        page = self.pageService.getBySlug(slug)
        if not page:
            return self.__404__(request)

        self.R.data.settings.head = page.title
        self.R.data.navigator.enabled = page.nav
        self.R.data.aside.enabled = page.aside
        self.R.data.aside.activeTab = "home"
        self.R.data.footer.enabled = page.footer

        data = dict(slug=page.slug, content=page.content)

        return self.render(request, context=data, template_name="page")
