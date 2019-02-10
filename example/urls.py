from django.conf.urls import url, include
from news_sitemaps import register, NewsSitemap


class CommentSitemap(NewsSitemap):
    limit = 5000

    def items(self):
        return []

    def lastmod(self, obj):
        return obj.submit_date

    def genres(self, obj):
        return 'UserGenerated, Opinion'


register(comments=CommentSitemap)


urlpatterns = [
    url(r'^news-sitemaps/', include('news_sitemaps.urls')),
]

