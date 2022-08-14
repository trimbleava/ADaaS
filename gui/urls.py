from django.urls import path, re_path
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.views.generic.base import TemplateView


from gui.views import HomeView

# CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)
print("in gui.urls..............")
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    # re_path(r'^contact/$', views.contact, name='contact'),
]

