from django.contrib.sitemaps import Sitemap

from .models import Article


class BlogSitemap(Sitemap):
    changefreq = "never"  # значит что информация о статьях никогда не меняется
    priority = 0.5  #  от 0 до 1 по значению страницы

    def items(self):
        return (
            Article
            .objects
            .filter(published_at__isnull=False)  # через __ передаются такие фильтрации
            .order_by("-published_at")
        )

    def lastmod(self, obj: Article):
        return obj.published_at

