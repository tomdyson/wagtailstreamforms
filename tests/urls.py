from django.conf.urls import url, include
from django.contrib import admin

from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtailcore import urls as wagtail_urls
from wagtailstreamforms import urls as streamforms_urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^cms/', include(wagtailadmin_urls)),
    url(r'^forms/', include(streamforms_urls)),
    url(r'', include(wagtail_urls)),
]