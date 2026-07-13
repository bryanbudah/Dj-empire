from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    priority = 0.9
    changefreq = "weekly"

    def items(self):
        return [
            "home",
            "about",
            "services",
            "gallery",
            "contact",
            "booking",
            "mix_list",
            "events",
            "testimonials",
        ]

    def location(self, item):
        return reverse(item)