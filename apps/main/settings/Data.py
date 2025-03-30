from apps.settings.services import SettingService
from vvecon.zorion import utils

__all__ = ["Data"]


class Data(utils.Data):
    settingService: SettingService = SettingService()

    settings = utils.Settings(
        head="Welcome",
        app_name=" | WeLead",
        app_icon="img/common/img.png",
        site_name="https://we-lead.com",
        logo="img/common/logo.png",
    )

    meta = utils.Meta(
        description="VIP Travels: Your One-Stop Solution for Travel Services. From cab and car rentals to wedding car "
        "rentals, tours, transportation, and air tickets, we offer a comprehensive range of travel "
        "services. Our expert drivers and comfortable vehicles ensure a smooth and stress-free journey. "
        "Book with VIP Travels today and experience top-notch service!",
        keywords=[
            "Travel services",
            "cab rental",
            "car rental",
            "wedding car rental",
            "tours",
            "transportation",
            "air tickets",
            "luxury travel",
            "VIP Travels",
            "Hire taxi",
            "cab",
            "cab service",
            "colombo cab services",
            "in sri lanka cab service number taxi service sri lanka budget taxi booking nano cabs fair taxi Pick me "
            "Air port travel rent car wedding car vip car luxury cars rent vehicle vehicle fastest travel agency",
            "Cab service number,Cab service near me,Cab service Colombo",
            "Cab service in Sri Lanka",
            "Cab service packages",
            "Cab service Kandy",
            "Sri Lanka taxi service Colombo",
            "Taxi Sri Lanka Colombo",
            "Sri Lanka taxi price per km",
            "Taxi service in Colombo",
            "Pick Me taxi,Kangaroo Cabs",
            "Sri Lanka taxi app",
            "PIKMI",
            "taxiCab service packages",
            "Pick me price per KM in Sri Lanka",
            "What is the best taxi app in Sri Lanka?",
            "How much is a taxi in Sri Lanka?",
            "How do I book pick me?",
            "Sri Lanka taxi service Colombo",
            "Taxi services in Colombo",
            "Sri Lanka taxi price per km",
            "Taxi Sri Lanka Colombo",
            "Kangaroo Cabs",
            "Sri Lanka taxi app",
            "How much does it cost to tour Sri Lanka?",
            "How do I plan a trip to Sri Lanka?",
            "Sri Lanka Tour package for couple",
            "Sri Lanka tour packages from Pakistan",
            "International tour packages from Sri Lanka",
            "Sri Lanka tour package for family",
            "Sri Lanka tours 2021",
            "Sri Lanka Tours from Colombo",
            "Lanka Tours and Travels",
            "5 Days tour package Sri Lanka",
            "Tour operators in Sri Lanka",
            "Sri Lanka tour itinerary",
            "Blue Lanka Tours",
            "Taxi service in Colombo",
            "Pick me price per KM in Sri Lanka",
            "Pick me contact number",
            "Cab service near me",
            "What is the cheapest taxi app?",
            "Are taxis cheap in Sri Lanka?",
            "When tourism will start in Sri Lanka?",
            "Is Sri Lanka open for tourism?",
            "How much can you earn from PickMe?",
            "Sri Lanka airport taxi price",
            "Sri Lanka taxi service Colombo",
            "Taxi services in Colombo",
            "Cab service price",
            "Sri Lanka cab service",
            "BIA taxi price list",
            "Rent a cab Sri Lanka",
            "Taxi booking website",
            "Book a taxi online",
            "Taxi service in Sri Lanka",
            "What is online taxi booking?",
            "Which app is best for booking cab?",
            "How can I book my car online?",
            "Book a taxi near me",
            "Sri Lanka taxi price per km",
            "Kangaroo Cabs",
            "Sri Lanka taxi price per km",
            "Pick me price per KM in Sri Lanka",
            "Sri Lanka taxi app",
            "Pick me contact number",
            "Cab service number",
            "YOGO taxi contact number",
            "transport service",
            "transport service in sri lanka",
            "transport service colombo",
            "transport service near me",
            "transport service company",
            "transport service",
            "transport service piliyandala",
            "transport service in jaffna",
            "transport service kandy",
            "transport service gampaha",
            "budget taxi",
            "budget taxi sri lanka",
            "budget taxi service",
            "budget taxi contact number",
            "budget taxi number",
            "budget taxi colombo",
            "Budget Taxk iribathgoda",
            "budget taxi",
            "budget taxi kelaniya",
            "budget taxi phone number",
            "online budget taxi",
            "holiday trip srilanka",
            "travelling sri lanka alone",
            "travelling sri lanka with a baby",
            "travelling sri lanka alone",
            "female travelling to sri lanka",
            "travelling to sri lanka visa",
            "travelling places in sri lanka",
            "travelling jobs in sri lanka",
            "travelling companies in sri lanka",
            "travelling srilanka",
            "travelling sri lanka tours",
            "travelling sri lanka alone",
            "female travelling sri lanka on a budget",
            "travelling sri lanka 2 weeks",
            "travelling sri lanka as a couple",
            "travelling sri lanka in december",
            "travelling sri lanka in may",
            "countries around sri lanka",
            "travelling around sri lanka independently",
            "seaaround sri lanka",
            "backpacking around sri lanka",
            "trip around sri lanka",
            "weather around sri lanka",
            "driving around sri lanka",
            "tours colombo",
            "tours colombo service",
            "tours and travels",
            "tours and travels near me",
            "tours in sri lanka",
            "tours meaning",
            "van hire with driver",
            "van hire packages",
            "van hire sri lanka",
            "van hire near me",
            "van hire with drivernear me",
            "van hire in colombo",
            "van hire kandy",
            "Is it safe to visit Sri Lanka now?",
            "What is the best month to visit Sri Lanka?",
            "Is Sri Lanka expensive to visit?",
            "Is Sri Lanka opening?",
            "What is the best month to visit Sri Lanka?",
            "What is the main culture in Sri Lanka?",
            "What are some traditions in Sri Lanka?",
            "Did Buddha visit Sri Lanka?",
            "What should I avoid in Sri Lanka?",
            "How many days are enough for Sri Lanka?",
            "Sri Lanka honeymoon packages with Cruise",
            "Honeymoon packages in Colombo",
            "Sri Lanka honeymoon places",
            "Sri Lanka honeymoon destinations",
            "Sri Lanka honeymoon Packages from Delhi",
            "Sri Lanka tour package for family",
            "Honeymoon packages in Negombo",
            "Day Tours Belihuloya",
            "Day Tour",
            "Day Tour of Colombo",
            "Galle Day Tour",
            "Geoffrey Bawa Works in Sri Lanka",
            "Hot Air Ballooning Day Tour",
            "Kandy Day Tour",
            "Kithulgala White Water Rafting",
            "Little England Day Tour",
            "Sigiriya Dambulla Day Tour",
            "Udawalawe National Park Day Tour",
            "Wilpattu National Park Day Tour",
            "Yala National Park Day Tour",
            "Tailor Made Tours",
            "Discover Sri Lanka",
            "AYURVEDIC TOURS",
            "BEACH TOURS",
            "CULTURAL TOURS",
            "HILL COUNTRY TOURS",
            "HONEYMOON TOURS",
            "INCENTIVES TOURS",
            "LUXURY TOURS",
            "GOLF TOURS",
            "WILDLIFE & ADVENTURE TOURS",
            "BESPOKE TOURS",
            "MEDICAL TOURISM",
            "EXPLORE SRI LANKA",
            "MY DREAM HOLIDAY",
            "taxi driver",
            "taxi service",
            "taxi cab near me",
            "airport transfers",
            "airport taxi",
            "taxi booking",
            "cheap taxi near me",
            "local taxi near me",
            "pick me,cab fare calculator",
            " cab fare calculator",
            "calculate cab fare",
            "mini cab fare calculator",
            "uk taxi fare calculator",
            "taxi price calculator uk",
            "taxi fare calculator uk",
            "minicab fare calculator",
            "minicab cost calculator",
            "minicab price calculator",
            "taxi fare estimate",
            "cab fare estimator",
            "cab fare calculator",
            "cab fare calculator",
            "calculate cab fare",
            "vip taxi fare calculator",
            "cab fare estimator",
            "cab fare calculator",
            "cab fare estimate",
            "estimate cab fare",
            "calculate cab fare",
            "taxi fare estimate",
            "taxi fare estimator",
            "taxi price estimate",
            "taxi cost estimator",
            "estimated taxi fare",
            "book taxi online",
            "book a taxi",
            "book a taxi online",
            "taxi receipt book",
            "colombo airport taxi booking",
            "taxi price calculator",
            "taxi rate calculator",
            "vip taxi fare calculator",
            "uk taxi fare calculator",
            "how to calculate taxi fare",
            "pick me",
            "pick me pick me",
            "pick me up app",
            "what is a pick me",
            "pick me app",
            "taxi cost estimator",
            "cab cost estimator",
            "how much taxi cost",
            "minicab cost calculator",
            "book taxi online",
            "book a taxi online",
            "cab book online",
            "get a cab online",
            "online food delivery sri lanka",
            "hikkaduwa sri lanka map",
            "hotels in hikkaduwa sri lanka",
            "hikkaduwa sri lanka hotels",
            "sri lankan food delivery near me",
            "Sri Lankan near me",
            "sri lankan market near me",
            "sri lankan near me",
        ],
    )

    tracking = utils.Tracking(
        enabled=False,
        google="UA-XXXXX-X",
    )

    navigator = utils.Navigator()

    aside = utils.Aside()

    footer = utils.Footer()
