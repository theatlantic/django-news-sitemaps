from django.conf.urls import url

from news_sitemaps import registry
import news_sitemaps.views


urlpatterns = [
    url(r'^index\.xml$',
        news_sitemaps.views.index,
        {'sitemaps': registry},
        name='news_sitemaps_index'),

    url(r'^(?P<section>.+)\.xml$',
        news_sitemaps.views.news_sitemap,
        {'sitemaps': registry},
        name='news_sitemaps_sitemap'),
]
