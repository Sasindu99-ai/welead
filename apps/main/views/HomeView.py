from datetime import datetime, timedelta
from typing import Any, Dict

from apps.settings.services import CountryService, SettingService
from apps.events.services import EventService, AudienceService
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
    eventService: EventService = EventService()
    audienceService: AudienceService = AudienceService()

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
        upcomingEvent = self.eventService.getUpcomingEvent()
        audiences = self.audienceService.getAll()

        context: Dict[str, Any] = dict(
            banners=banners,
            intro=dict(
                vision=vision,
                mission=mission
            ),
            upcomingEvent=upcomingEvent,
            audiences = audiences,
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
                faqs=[
                    dict(
                        question="What is Welead?",
                        answer="Welead is a platform that connects event organizers with their target audiences, "
                               "providing tools for event management, promotion, and engagement."
                    ),
                    dict(
                        question="How can I create an event?",
                        answer="To create an event, sign up for an account, navigate to the 'Create Event' section, "
                               "and fill out the necessary details about your event."
                    ),
                    dict(
                        question="How do I promote my event?",
                        answer="Welead offers various promotional tools including social media integration, email "
                               "marketing, and targeted advertising to help you reach a wider audience."
                    ),
                    dict(
                        question="Can I manage ticket sales through Welead?",
                        answer="Yes, Welead provides a comprehensive ticketing system that allows you to sell tickets, "
                               "track sales, and manage attendees all in one place."
                    ),
                    dict(
                        question="Is there a mobile app for Welead?",
                        answer="Yes, Welead has a mobile app available for both iOS and Android devices, allowing you to "
                               "manage your events on the go."
                    ),
                    dict(
                        question="How can I get support?",
                        answer="Our support team is available 24/7 to assist you with any questions or issues you may "
                               "have. You can reach us via email, phone, or live chat."
                    ),
                ]
            ),
        )
        return self.render(request, context=context, template_name="home")
