from cms.urls import urlpatterns as cms_urlpatterns
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
]

# django-cms page routing requires the CMS urls to live inside i18n_patterns,
# otherwise /en/-prefixed URLs 404.
urlpatterns += i18n_patterns(*cms_urlpatterns)
